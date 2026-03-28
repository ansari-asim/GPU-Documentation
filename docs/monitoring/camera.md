---
title: Camera Monitoring
description: RTSP camera stream monitoring for connectivity and health checks.
tags:
  - monitoring
  - camera
  - rtsp
---

# Camera Monitoring

Monitors RTSP camera streams for connectivity, latency, and offline events. Sends 🔴 Disconnect and 🟢 Reconnect alerts, and logs all events to a daily CSV.

[:material-download: Download `camera_monitor.py`](../../scripts/camera_monitor.py){ .md-button download="camera_monitor.py" }

---

## Dependencies

Install all monitoring dependencies:

```bash
sudo apt install python3-pip ffmpeg -y && \
pip3 install psutil GPUtil requests python-dotenv
```

| Package | Used By | Purpose |
|---|---|---|
| `psutil` | Solution, Hardware | Process scanning, CPU/RAM/disk metrics |
| `GPUtil` | Hardware | GPU utilization and VRAM metrics |
| `requests` | Camera, Solution, Hardware | Sends Google Chat webhook alerts |
| `python-dotenv` | Camera, Solution | Loads credentials from `.env` |
| `ffmpeg` | Camera | Captures JPEG snapshots from RTSP streams |

---

## Alert Setup

All scripts that support alerts read from a `.env` file in the same directory.

```bash title=".env"
# Google Chat — required if google_chat_enabled = true
GOOGLE_CHAT_WEBHOOK=https://chat.googleapis.com/v1/spaces/...

# Email — required if email alerts are enabled
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
ALERT_PASSWORD=your_app_password
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

### Google Chat Webhook

!!! tip "Getting a Webhook URL"
    1. Open your Google Chat space → click the space name → **Manage webhooks**
    2. Click **Add webhook**, give it a name, copy the URL
    3. Paste it into `.env` as `GOOGLE_CHAT_WEBHOOK`
    4. Set `"google_chat_enabled": true` in `config.json`

### Email (Gmail App Password)

!!! warning "Use an App Password — not your Gmail password"
    1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
    2. Select **Mail**, copy the 16-character password generated
    3. Paste it as `ALERT_PASSWORD` or `EMAIL_PASSWORD` in `.env`
    4. Enable email alerts in `config.json`

---

## How It Works

Each camera is pinged on every cycle. Three states are tracked:

**Connected** — ping OK, latency within threshold. Row written to CSV.

**High Latency** — ping OK but RTT exceeds `latency_threshold_ms`. A JPEG snapshot is captured via `ffmpeg` for diagnostics.

**Not Connected** — ping fails for longer than `offline_confirm_seconds` continuously. A 🔴 alert fires on confirmed offline; a 🟢 alert with downtime duration fires on recovery. The confirm window prevents false alerts from a single dropped packet.

All cameras are checked in parallel (up to 10 threads).

---

## Project Structure

```
camera_monitor/
├── camera_monitor.py
├── config.json
├── .env
└── logs/
    ├── log_YYYY-MM-DD.csv
    └── frames/
        └── Cam_2_20240101_120000.jpg
```

---

## Configuration

```json title="config.json"
{
  "cameras": [
    { "name": "Cam_2", "url": "rtsp://<user>:<pass>@<ip>:<port>/<path>" },
    { "name": "Cam_4", "url": "rtsp://<user>:<pass>@<ip>:<port>/<path>" }
  ],
  "log_directory": "logs",
  "check_interval_seconds": 5,
  "offline_confirm_seconds": 5,
  "latency_threshold_ms": 100,
  "save_csv": true,
  "save_frame": true,
  "ping_check_enabled": true,
  "ping_timeout_seconds": 5,
  "google_chat_enabled": true,
  "email_alerts_enabled": false,
  "email_settings": {
    "sender": "your_email@gmail.com",
    "receiver": ["receiver@example.com"],
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587
  }
}
```

| Key | Default | Description |
|---|---|---|
| `cameras` | — | List of cameras with `name` and RTSP `url` |
| `check_interval_seconds` | `5` | Poll frequency in seconds |
| `offline_confirm_seconds` | `5` | Consecutive fail time before marking offline |
| `latency_threshold_ms` | `100` | RTT above which status becomes High Latency |
| `save_csv` | `true` | Write status to daily CSV |
| `save_frame` | `true` | Capture JPEG on high-latency events |
| `ping_timeout_seconds` | `5` | Max wait per ping |
| `google_chat_enabled` | `true` | Enable Google Chat alerts |
| `email_alerts_enabled` | `false` | Enable email alerts |

---

## Log Output

| File | Description |
|---|---|
| `logs/log_YYYY-MM-DD.csv` | One row per camera per cycle — Time, Camera, IP, Status, Latency |
| `logs/frames/` | JPEG snapshots on high-latency events |

| Status | Meaning |
|---|---|
| `Connected` | Ping OK, latency within threshold |
| `High Latency` | Ping OK, RTT exceeds threshold |
| `Not Connected` | Ping failed beyond confirm window |

---

## Running

```bash
python3 camera_monitor.py
```
