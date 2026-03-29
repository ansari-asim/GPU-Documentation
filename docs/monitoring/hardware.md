---
title: Hardware Utilization Monitoring
description: CPU, RAM, disk, and GPU utilization monitoring and alerting.
tags:
  - monitoring
  - hardware
  - gpu
---

# Hardware Utilization Monitoring

Monitors CPU, RAM, disk, and GPU utilization on hardware nodes. Sends 🔴 threshold-exceeded alerts with cooldown to prevent spam. Logs all metrics to a daily CSV.

[:material-download: Download `hardware_monitor.py`](../scripts/hardware_monitor.py){ .md-button download="hardware_monitor.py" }

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
    4. Set `"enabled": true` in `config.json` under `google_chat`

---

## How It Works

Hardware metrics are collected every poll cycle. Thresholds are checked and compared:

**CPU** — System CPU percentage. Alert fires when usage exceeds threshold (filtered by CPU name if specified).

**RAM** — Total RAM used (GB). Alert fires when usage exceeds threshold.

**Disk** — Total disk used (GB). Alert fires when usage exceeds threshold.

**GPU Utilization** — Per-GPU compute utilization (%). Alert fires when usage exceeds threshold. Filtered by GPU name if specified.

**GPU VRAM** — Per-GPU memory used (GB). Alert fires when usage exceeds threshold.

All metrics are checked in parallel. Alerts have a cooldown window (`alert_cooldown_minutes`) to prevent duplicate notifications of the same condition.

---

## Project Structure

```
hardware_monitor/
├── hardware_monitor.py
├── config.json
├── .env
└── logs/
    └── hardware_YYYY-MM-DD.csv
```

---

## Configuration

```json title="config.json"
{
  "interval_seconds": 60,
  "csv_file": "logs/hardware_YYYY-MM-DD.csv",
  "thresholds": {
    "cpu_percent": 80,
    "ram_gb": 60,
    "disk_gb": 300,
    "gpu_util_percent": 85,
    "vram_gb": 20
  },
  "filters": {
    "cpu_name_contains": "Intel",
    "gpu_names": ["RTX", "A100"]
  },
  "google_chat": {
    "enabled": true,
    "webhook_url": "https://chat.googleapis.com/v1/spaces/..."
  },
  "alert_cooldown_minutes": 5
}
```

| Key | Type | Default | Description |
|---|---|---|---|
| `interval_seconds` | int | `60` | Poll frequency in seconds |
| `csv_file` | string | — | CSV file path; supports `YYYY-MM-DD` date template |
| `thresholds.cpu_percent` | int | `80` | CPU usage threshold (%) to trigger alert |
| `thresholds.ram_gb` | int | `60` | RAM usage threshold (GB) to trigger alert |
| `thresholds.disk_gb` | int | `300` | Disk usage threshold (GB) to trigger alert |
| `thresholds.gpu_util_percent` | int | `85` | GPU utilization threshold (%) to trigger alert |
| `thresholds.vram_gb` | int | `20` | GPU VRAM usage threshold (GB) to trigger alert |
| `filters.cpu_name_contains` | string | `""` | Optional filter — only alert if CPU name contains this string |
| `filters.gpu_names` | list | `[]` | Optional list of GPU name fragments — only monitor matching GPUs |
| `google_chat.enabled` | bool | `true` | Enable Google Chat alerts |
| `alert_cooldown_minutes` | int | `5` | Minutes to wait before re-alerting on the same condition |

---

## Log Output

```
date,time,cpu_name,cpu_percent,ram_used_gb,ram_total_gb,disk_used_gb,disk_total_gb,gpu_id,gpu_name,gpu_util_percent,vram_used_gb,vram_total_gb
2024-01-15,14:30:45,Intel Core i9,35.2,45.6,128.0,250.3,500.0,0,NVIDIA RTX 4090,72.5,18.3,24.0
2024-01-15,14:31:45,Intel Core i9,38.1,46.2,128.0,250.4,500.0,0,NVIDIA RTX 4090,78.9,19.1,24.0
```

| Column | Description |
|---|---|
| `date`, `time` | Timestamp of metric capture |
| `cpu_name` | Processor model |
| `cpu_percent` | System CPU usage (%) |
| `ram_used_gb`, `ram_total_gb` | RAM usage and capacity |
| `disk_used_gb`, `disk_total_gb` | Disk usage and capacity |
| `gpu_id` | GPU device ID |
| `gpu_name` | GPU model name |
| `gpu_util_percent` | GPU compute utilization (%) |
| `vram_used_gb`, `vram_total_gb` | VRAM usage and capacity |

---

## Running

```bash
python3 hardware_monitor.py
```
