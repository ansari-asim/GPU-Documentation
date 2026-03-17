---
title: Monitoring
description: Network, temperature, disk, cache, and SSD health monitoring scripts for AI hardware nodes.
tags:
  - monitoring
  - telemetry
  - logging
  - python
---

# 📊 Monitoring { #monitoring }

Python-based monitoring scripts for AI hardware nodes — covering network usage, GPU/CPU temperature, disk health, cache memory, and SSD diagnostics. All scripts use rotating log files capped at 10 MB.

---

## Dependencies { #dependencies }

```bash
sudo apt install smartmontools ifstat -y && \
sudo apt install python3-pip -y && \
pip3 install psutil pytz watchdog && \
sudo apt-get install lm-sensors -y
```

---

## Network Monitoring { #network }

Logs network usage every 30 seconds using `ifstat`, with rotating log output to `network.log`.

```python title="network_monitor.py"
import subprocess
import datetime
import pytz
import logging
from logging.handlers import RotatingFileHandler
import time

ist = pytz.timezone('Asia/Kolkata')

def setup_logging(log_filename):
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(
        log_filename,
        maxBytes=10 * 1024 * 1024,
        backupCount=10
    )
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def log_network_usage(net_logger):
    while True:
        try:
            timestamp = datetime.datetime.now(ist).strftime(
                "%Y-%m-%d %H:%M:%S IST"
            )
            result = subprocess.run(
                ['ifstat', '30', '1'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                net_logger.info(f"[{timestamp}] {result.stdout.strip()}")
            else:
                net_logger.error(f"Error: {result.stderr}")
        except Exception as e:
            net_logger.error(f"Exception occurred: {e}")
        time.sleep(30)

if __name__ == "__main__":
    net_logger = setup_logging('network.log')
    log_network_usage(net_logger)
```

---

## Temperature Monitoring { #temperature }

Logs CPU/GPU temperature, CPU utilization, and RAM usage every 30 seconds to `temperature.log`.

```python title="temperature_monitor.py"
import subprocess
import datetime
import pytz
import psutil
import logging
from logging.handlers import RotatingFileHandler
import time

ist = pytz.timezone('Asia/Kolkata')

def setup_logging(log_filename):
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(
        log_filename,
        maxBytes=10 * 1024 * 1024,
        backupCount=10
    )
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def log_temperatures(temp_logger):
    while True:
        try:
            try:
                cpu_temp_output = subprocess.check_output(
                    ["sensors"], text=True
                ).strip()
            except FileNotFoundError:
                cpu_temp_output = "sensors command not found"

            try:
                gpu_temp_output = subprocess.check_output(
                    [
                        "nvidia-smi",
                        "--query-gpu=temperature.gpu",
                        "--format=csv,noheader,nounits"
                    ],
                    text=True
                ).strip()
            except FileNotFoundError:
                gpu_temp_output = "nvidia-smi command not found"

            cpu_utilization = psutil.cpu_percent(interval=1)
            ram_utilization = psutil.virtual_memory().percent
            timestamp = datetime.datetime.now(ist).strftime(
                "%Y-%m-%d %H:%M:%S IST"
            )

            temp_logger.info(
                f"Timestamp IST: {timestamp}, "
                f"CPU Temp: {cpu_temp_output}, "
                f"GPU Temp: {gpu_temp_output}, "
                f"CPU Utilization: {cpu_utilization}%, "
                f"RAM Utilization: {ram_utilization}%"
            )
        except Exception as e:
            temp_logger.error(f"Unexpected error: {e}")
        time.sleep(30)

if __name__ == "__main__":
    temp_logger = setup_logging('temperature.log')
    log_temperatures(temp_logger)
```

---

## Disk Monitoring { #disk }

Monitors disk usage every 5 minutes across all partitions. Logs a warning if usage exceeds 90%.

```python title="disk_monitor.py"
import psutil
import time
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_filename):
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(
        log_filename,
        maxBytes=10 * 1024 * 1024,
        backupCount=10
    )
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def monitor_disk_usage(disk_logger, threshold=90):
    while True:
        for part in psutil.disk_partitions():
            usage = psutil.disk_usage(part.mountpoint)
            total_gb = usage.total / (1024 ** 3)
            free_gb  = usage.free  / (1024 ** 3)
            used_gb  = total_gb - free_gb

            disk_logger.info(
                f"Disk usage on {part.mountpoint}: "
                f"{usage.percent}% used, "
                f"{used_gb:.2f} GB used, "
                f"{free_gb:.2f} GB remaining "
                f"out of {total_gb:.2f} GB total"
            )

            if usage.percent >= threshold:
                disk_logger.warning(
                    f"⚠ Disk alert on {part.mountpoint}: "
                    f"{usage.percent}% used — "
                    f"{free_gb:.2f} GB remaining"
                )
        time.sleep(300)

if __name__ == "__main__":
    disk_logger = setup_logging('disk_usage.log')
    monitor_disk_usage(disk_logger)
```

---

## Cache Monitoring { #cache }

Logs cache memory usage every 5 minutes to `cache_memory.log`.

```python title="cache_monitor.py"
import psutil
import time
import logging
from logging.handlers import RotatingFileHandler

LOG_MAX_SIZE    = 10 * 1024 * 1024   # 10 MB
LOG_BACKUP_COUNT = 10

def setup_logging(log_filename):
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(
        log_filename,
        maxBytes=LOG_MAX_SIZE,
        backupCount=LOG_BACKUP_COUNT
    )
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def log_cache_memory_status(cache_logger):
    while True:
        try:
            mem_info = psutil.virtual_memory()
            cache_logger.info(
                f"Cache memory: "
                f"{mem_info.cached / 1024 / 1024:.2f} MB"
            )
        except Exception as e:
            cache_logger.error(
                f"Error fetching cache memory status: {e}"
            )
        time.sleep(300)

if __name__ == "__main__":
    cache_logger = setup_logging('cache_memory.log')
    log_cache_memory_status(cache_logger)
```

---

## SSD Monitoring { #ssd }

Uses `smartctl` to monitor NVMe SSD health — temperature, available spare, read/write data, and more. Logs to `smartctl.log` every 5 minutes.

!!! info "What is monitored"
    `smartctl -a` returns comprehensive health data including:
    temperature, available spare capacity, percentage used, data units read/written, and power-on hours.

```python title="ssd_monitor.py"
import psutil
import subprocess
import time
import datetime
import pytz
import logging
from logging.handlers import RotatingFileHandler

LOG_MAX_SIZE     = 10 * 1024 * 1024
LOG_BACKUP_COUNT = 10
IST = pytz.timezone('Asia/Kolkata')

def setup_logging(log_filename):
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(
        log_filename,
        maxBytes=LOG_MAX_SIZE,
        backupCount=LOG_BACKUP_COUNT
    )
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def detect_ssd_and_log_smartctl(smartctl_logger):
    while True:
        ssd_path = None
        for disk in psutil.disk_partitions(all=False):
            if 'nvme' in disk.device or 'sd' in disk.device:
                ssd_path = disk.device.replace('/dev/', '')
                break

        if ssd_path:
            try:
                timestamp = datetime.datetime.now(IST).strftime(
                    "%Y-%m-%d %H:%M:%S IST"
                )
                result = subprocess.run(
                    ['sudo', 'smartctl', '-a', f'/dev/{ssd_path}'],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    smartctl_logger.info(
                        f"Timestamp: {timestamp}\n{result.stdout}"
                    )
                else:
                    smartctl_logger.error(
                        f"Error running smartctl "
                        f"for {ssd_path}: {result.stderr}"
                    )
            except Exception as e:
                smartctl_logger.error(
                    f"Exception for {ssd_path}: {e}"
                )
        else:
            smartctl_logger.warning("No SSD detected.")

        time.sleep(300)

if __name__ == "__main__":
    smartctl_logger = setup_logging('smartctl.log')
    detect_ssd_and_log_smartctl(smartctl_logger)
```