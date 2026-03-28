import psutil
import GPUtil
import time
import json
import csv
import requests
from datetime import datetime, timedelta
import os
import platform

# Load config
with open("config.json") as f:
    config = json.load(f)

INTERVAL = config["interval_seconds"]
CSV_FILE = config["csv_file"]
THRESHOLDS = config["thresholds"]
CHAT_CONFIG = config["google_chat"]
COOLDOWN_MINUTES = config["alert_cooldown_minutes"]
FILTERS = config["filters"]

last_alert_time = {}

# ---------------- UTIL ----------------
def now():
    return datetime.now()

def bytes_to_gb(b):
    return round(b / (1024 ** 3), 2)

def get_cpu_name():
    name = platform.processor()
    if not name:
        # fallback for Linux
        try:
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if "model name" in line:
                        return line.split(":")[1].strip()
        except:
            return "Unknown CPU"
    return name

# ---------------- COOLDOWN ----------------
def should_alert(key):
    if key not in last_alert_time:
        return True
    return (now() - last_alert_time[key]) > timedelta(minutes=COOLDOWN_MINUTES)

def update_alert_time(key):
    last_alert_time[key] = now()

# ---------------- CSV ----------------
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date",
                "time",
                "cpu_name",
                "cpu_percent",
                "ram_used_gb",
                "ram_total_gb",
                "disk_used_gb",
                "disk_total_gb",
                "gpu_id",
                "gpu_name",
                "gpu_util_percent",
                "vram_used_gb",
                "vram_total_gb"
            ])

# ---------------- METRICS ----------------
def get_system_metrics():
    vm = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        "cpu": psutil.cpu_percent(),
        "ram_used": bytes_to_gb(vm.used),
        "ram_total": bytes_to_gb(vm.total),
        "disk_used": bytes_to_gb(disk.used),
        "disk_total": bytes_to_gb(disk.total)
    }

def get_gpu_metrics():
    gpu_list = []
    allowed_names = FILTERS["gpu_names"]

    for gpu in GPUtil.getGPUs():
        name = gpu.name

        # Apply GPU name filter
        if allowed_names:
            if not any(n.lower() in name.lower() for n in allowed_names):
                continue

        gpu_list.append({
            "id": gpu.id,
            "name": name,
            "util": round(gpu.load * 100, 2),
            "vram_used": round(gpu.memoryUsed / 1024, 2),
            "vram_total": round(gpu.memoryTotal / 1024, 2)
        })

    return gpu_list

# ---------------- CSV LOG ----------------
def log_to_csv(date_str, time_str, cpu_name, sys, gpus):
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not gpus:
            writer.writerow([
                date_str, time_str,
                cpu_name, sys["cpu"],
                sys["ram_used"], sys["ram_total"],
                sys["disk_used"], sys["disk_total"],
                "NA", "NA", 0, 0, 0
            ])
        else:
            for g in gpus:
                writer.writerow([
                    date_str, time_str,
                    cpu_name, sys["cpu"],
                    sys["ram_used"], sys["ram_total"],
                    sys["disk_used"], sys["disk_total"],
                    g["id"], g["name"],
                    g["util"],
                    g["vram_used"], g["vram_total"]
                ])

# ---------------- ALERT ----------------
def send_alert(msg):
    if not CHAT_CONFIG["enabled"]:
        return
    try:
        requests.post(CHAT_CONFIG["webhook_url"], json={"text": msg})
    except Exception as e:
        print("Alert failed:", e)

# ---------------- CHECK ----------------
def check_thresholds(cpu_name, sys, gpus):
    alerts = []

    cpu_filter = FILTERS["cpu_name_contains"]

    # CPU check (only if matches filter)
    if cpu_filter.lower() in cpu_name.lower():
        if sys["cpu"] > THRESHOLDS["cpu_percent"]:
            key = "cpu"
            if should_alert(key):
                alerts.append(f"CPU ({cpu_name}): {sys['cpu']}% used")
                update_alert_time(key)

    # RAM
    if sys["ram_used"] > THRESHOLDS["ram_gb"]:
        key = "ram"
        if should_alert(key):
            alerts.append(f"RAM: {sys['ram_used']} GB / {sys['ram_total']} GB used")
            update_alert_time(key)

    # Disk
    if sys["disk_used"] > THRESHOLDS["disk_gb"]:
        key = "disk"
        if should_alert(key):
            alerts.append(f"Disk: {sys['disk_used']} GB / {sys['disk_total']} GB used")
            update_alert_time(key)

    # GPUs
    for g in gpus:
        gpu_short = g["name"].replace("NVIDIA GeForce ", "").strip()

        # GPU utilization
        util_key = f"gpu_util_{g['id']}"
        if g["util"] > THRESHOLDS["gpu_util_percent"]:
            if should_alert(util_key):
                alerts.append(
                    f"GPU {g['id']} Memory ({gpu_short}): {g['util']}%"
                )
                update_alert_time(util_key)

        # GPU VRAM
        vram_key = f"gpu_vram_{g['id']}"
        if g["vram_used"] > THRESHOLDS["vram_gb"]:
            if should_alert(vram_key):
                alerts.append(
                    f"GPU {g['id']} VRAM ({gpu_short}): {g['vram_used']} GB / {g['vram_total']} GB used"
                )
                update_alert_time(vram_key)

    if alerts:
        send_alert("\n".join(alerts))
# ---------------- MAIN ----------------
def main():
    print("Monitoring started...")
    init_csv()

    while True:
        current = now()
        date_str = current.strftime("%Y-%m-%d")
        time_str = current.strftime("%H:%M:%S")

        cpu_name = get_cpu_name()
        sys_metrics = get_system_metrics()
        gpu_metrics = get_gpu_metrics()

        log_to_csv(date_str, time_str, cpu_name, sys_metrics, gpu_metrics)
        check_thresholds(cpu_name, sys_metrics, gpu_metrics)

        #print(f"{ts} | CPU:{sys_metrics['cpu']}% RAM:{sys_metrics['ram_used']}GB GPUs:{len(gpu_metrics)}")
        print(f"{date_str} {time_str} | CPU:{sys_metrics['cpu']}% RAM:{sys_metrics['ram_used']}GB GPUs:{len(gpu_metrics)}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()