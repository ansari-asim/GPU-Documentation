import psutil
import json
import time
import smtplib
import subprocess
import platform
import os
import requests
from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

# -------------------- LOAD ENV --------------------
load_dotenv()
ALERT_PASSWORD = os.getenv("ALERT_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
WEBHOOK_URL = os.getenv("GOOGLE_CHAT_WEBHOOK")

# -------------------- GLOBALS --------------------
CONFIG_FILE = "config.json"
last_status = {}
offline_since = {}

# -------------------- LOAD CONFIG --------------------
def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

# -------------------- ALERTS --------------------
def send_email(email_cfg, subject, message):
    if not email_cfg.get("enabled", False):
        return

    try:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = email_cfg["from_email"]
        msg["To"] = ", ".join(email_cfg["to_emails"])
        msg.set_content(message)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(email_cfg["from_email"], ALERT_PASSWORD)
            server.send_message(msg)

        print(f"[EMAIL SENT] {subject}")

    except Exception as e:
        print(f"[EMAIL ERROR] {e}")


def send_chat(enabled, message):
    if not enabled or not WEBHOOK_URL:
        return

    try:
        requests.post(WEBHOOK_URL, json={"text": message})
        print("[CHAT SENT]")
    except Exception as e:
        print("[CHAT ERROR]", e)

# -------------------- HELPERS --------------------
def format_duration(seconds):
    if seconds < 1:
        seconds = 1  # minimum 1 sec

    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h}h {m}m {s}s"

def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# -------------------- CHECK FUNCTIONS --------------------
def is_process_running(identifier):
    for proc in psutil.process_iter(attrs=["cmdline", "status", "memory_info"]):
        try:
            cmd = " ".join(proc.info.get("cmdline") or []).lower()
            if identifier.lower() in cmd:
                if proc.info["memory_info"].rss > 0 and proc.info["status"] not in (
                    psutil.STATUS_ZOMBIE,
                    psutil.STATUS_DEAD,
                    psutil.STATUS_STOPPED,
                ):
                    return True
        except:
            continue
    return False


def is_linux_service(service):
    if platform.system() != "Linux":
        return False
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True
        )
        return result.stdout.strip() == "active"
    except:
        return False


def is_iis(site):
    if platform.system() != "Windows":
        return False
    try:
        result = subprocess.run(
            ["powershell", "-Command", f"(Get-Website -Name '{site}').State"],
            capture_output=True,
            text=True
        )
        return result.stdout.strip().lower() == "started"
    except:
        return False

# -------------------- SERVICE CHECK --------------------
def check_service(entry, type_):
    name = entry["name"]

    if type_ in ["python", "dotnet"]:
        running = is_process_running(entry["process_name"])
    elif type_ == "linux":
        running = is_linux_service(entry["service_name"])
    elif type_ == "iis":
        running = is_iis(entry["site_name"])
    else:
        running = False

    return name, running

# -------------------- ALERT HANDLER --------------------
def handle_alert(name, key, running, config):
    email_cfg = config["email"]
    chat_enabled = config.get("google_chat_enabled", False)

    last_status.setdefault(key, True)
    offline_since.setdefault(key, None)

    prev = last_status[key]
    now = time.time()

    if prev != running:

        # 🔴 DOWN
        if not running:
            offline_since[key] = now

            msg_email = email_cfg.get(
                "body_down", "{service_name} is down."
            ).format(service_name=name)

            msg_chat = f"🔴 {name} DOWN\nTime: {current_time()}"

            send_email(email_cfg, email_cfg["subject_down"], msg_email)
            send_chat(chat_enabled, msg_chat)

        # 🟢 UP
        else:
            downtime = 0
            if offline_since[key]:
                downtime = now - offline_since[key]

            msg_email = email_cfg.get(
                "body_recovered", "{service_name} recovered."
            ).format(service_name=name)

            msg_chat = (
                f"🟢 {name} RECOVERED\n"
                f"Downtime: {format_duration(downtime)}\n"
                f"Time: {current_time()}"
            )

            send_email(email_cfg, email_cfg["subject_recovered"], msg_email)
            send_chat(chat_enabled, msg_chat)

            offline_since[key] = None

    last_status[key] = running

# -------------------- STATE FILE --------------------
def load_state_file(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return {}

def save_state_file(path, state):
    with open(path, "w") as f:
        json.dump(state, f, indent=2)

# -------------------- MAIN MONITOR --------------------
def monitor():
    config = load_config()
    state_file = config.get("state_file", "service_state.json")

    global last_status
    last_status = load_state_file(state_file)

    tasks = []

    for s in config.get("python_scripts", []):
        if s.get("enabled", True):
            tasks.append((s, "python", f"python::{s['name']}"))

    for s in config.get("dotnet_apps", []):
        if s.get("enabled", True):
            tasks.append((s, "dotnet", f"dotnet::{s['name']}"))

    for s in config.get("linux_services", []):
        if s.get("enabled", True):
            tasks.append((s, "linux", f"linux::{s['name']}"))

    for s in config.get("iis_sites", []):
        if s.get("enabled", True):
            tasks.append((s, "iis", f"iis::{s['name']}"))

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(lambda t: (t, check_service(t[0], t[1])), tasks))

    for (entry, type_, key), (name, running) in results:
        handle_alert(name, key, running, config)

    save_state_file(state_file, last_status)

    print(f"[{current_time()}] Service Status:")
    for k, v in last_status.items():
        print(f"{k}: {'Running' if v else 'Stopped'}")

# -------------------- LOOP --------------------
if __name__ == "__main__":
    print("🚀 Service Monitor Started...")
    while True:
        monitor()
        cfg = load_config()
        time.sleep(cfg.get("check_interval_seconds", 60))