
**Dependencies**

```

sudo apt install smartmontools ifstat -y

sudo apt install python3-pip

pip3 install psutil pytz watchdog

sudo apt-get install lm-sensors

```

## **Network Monitoring**

This script logs network usage periodically by executing the ifstat command every 30 seconds and saving the output to a rotating log file named network.log. It uses Python's subprocess module to run shell commands, pytz for timezone handling, and logging for capturing and rotating logs efficiently.

```
import subprocess
import datetime
import pytz
import logging
from logging.handlers import RotatingFileHandler
import time

ist = pytz.timezone('Asia/Kolkata')  

# Set up logging
def setup_logging(log_filename):
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_filename, maxBytes=10 * 1024 * 1024, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Log network monitoring data
def log_network_usage(net_logger):
    while True:
        try:
            timestamp = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")  
            result = subprocess.run(['ifstat', '30', '1'], capture_output=True, text=True)
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

## **Temperature Monitoring**

This script monitors system metrics, including CPU and GPU temperatures, CPU utilization, and RAM usage, logging the data every 30 seconds into a rotating log file named temperature.log. It leverages subprocess for executing shell commands and logging for efficient log management.


```
import subprocess
import datetime
import pytz
import psutil
import logging
from logging.handlers import RotatingFileHandler
import time

ist = pytz.timezone('Asia/Kolkata') 

# Set up logging
def setup_logging(log_filename):
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_filename, maxBytes=10 * 1024 * 1024, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Log temperatures and system utilization
def log_temperatures(temp_logger):
    while True:
        try:
            try:
                cpu_temp_output = subprocess.check_output(["sensors"], text=True).strip()
            except FileNotFoundError:
                cpu_temp_output = "sensors command not found"

            # Check for the NVIDIA GPU temperature
            try:
                gpu_temp_output = subprocess.check_output(
                    ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"], text=True
                ).strip()
            except FileNotFoundError:
                gpu_temp_output = "nvidia-smi command not found"

            cpu_utilization = psutil.cpu_percent(interval=1)
            ram_utilization = psutil.virtual_memory().percent
            timestamp = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S IST")

            temp_logger.info(
                f"Timestamp IST: {timestamp}, CPU Temp: {cpu_temp_output}, GPU Temp: {gpu_temp_output}, "
                f"CPU Utilization: {cpu_utilization}%, RAM Utilization: {ram_utilization}%"
            )
        except Exception as e:
            temp_logger.error(f"Unexpected error: {e}")
        time.sleep(30)

if __name__ == "__main__":
    temp_logger = setup_logging('temperature.log')
    log_temperatures(temp_logger)

```

## **Disk Monitoring**

This Python script monitors disk usage on the system every 5 minutes, logging both the total and free disk space for each partition. If disk usage exceeds a specified threshold (default 90%), it generates a warning in the log file

```
import psutil
import time
import logging
from logging.handlers import RotatingFileHandler

# Log disk usage
def monitor_disk_usage(disk_logger, threshold=90):
    while True:
        for part in psutil.disk_partitions():
            usage = psutil.disk_usage(part.mountpoint)
            total_gb = usage.total / (1024 ** 3)
            free_gb = usage.free / (1024 ** 3)
            used_gb = total_gb - free_gb
            disk_logger.info(f"Disk usage on {part.mountpoint}: {usage.percent}% used, {used_gb:.2f} GB used, {free_gb:.2f} GB remaining out of {total_gb:.2f} GB total")
            if usage.percent >= threshold:
                disk_logger.warning(f"Disk usage alert on {part.mountpoint}: {usage.percent}% used, {used_gb:.2f} GB used, {free_gb:.2f} GB remaining out of {total_gb:.2f} GB total")
        time.sleep(300)  

# Setup logging function
def setup_logging(log_filename):
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_filename, maxBytes=10 * 1024 * 1024, backupCount=10)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == "__main__":
    # Setup disk usage logger
    disk_logger = setup_logging('disk_usage.log')

    # Start disk usage monitoring
    monitor_disk_usage(disk_logger)


```

## **Cache Monitoring**

This Python script monitors and logs the cache memory usage of the system every 5 Minutes, saving the data in a rotating log file. If an error occurs while fetching the memory status, it logs the error message in the same file.

```

import psutil
import time
import logging
from logging.handlers import RotatingFileHandler

# Log config
LOG_MAX_SIZE = 10 * 1024 * 1024  # 10 MB for general monitoring logs
LOG_BACKUP_COUNT = 10

# Setup logging function
def setup_logging(log_filename):
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_filename, maxBytes=LOG_MAX_SIZE, backupCount=LOG_BACKUP_COUNT)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Log cache memory status
def log_cache_memory_status(cache_logger):
    while True:
        try:
            mem_info = psutil.virtual_memory()
            cache_logger.info(f"Cache memory: {mem_info.cached / 1024 / 1024} MB")
        except Exception as e:
            cache_logger.error(f"Error fetching cache memory status: {e}")
        time.sleep(300)

if __name__ == "__main__":
    # Setup logger for cache memory monitoring
    cache_logger = setup_logging('cache_memory.log')

    # Start cache memory monitoring
    log_cache_memory_status(cache_logger)

```

## **SSD Monitoring**

This script leverages smartctl (a command-line utility for monitoring storage devices) to check the health of an NVMe SSD. The output from the smartctl command is parsed to extract relevant health metrics, including temperature, available spare, usage percentage, read/write data, and more. This information is essential for ensuring the SSD is in good condition and to detect potential issues before they affect performance.


```
import psutil
import subprocess
import time
import datetime
import pytz
import logging
from logging.handlers import RotatingFileHandler

# Log config
LOG_MAX_SIZE = 10 * 1024 * 1024  # 10 MB for general monitoring logs
LOG_BACKUP_COUNT = 10

# Set the timezone to UTC
IST = pytz.timezone('Asia/Kolkata')

# Setup logging function
def setup_logging(log_filename):
    logger = logging.getLogger(log_filename)
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler(log_filename, maxBytes=LOG_MAX_SIZE, backupCount=LOG_BACKUP_COUNT)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Auto-detect SSD and run smartctl
def detect_ssd_and_log_smartctl(smartctl_logger):
    while True:
        ssd_path = None
        for disk in psutil.disk_partitions(all=False):
            if 'nvme' in disk.device or 'sd' in disk.device:
                ssd_path = disk.device.replace('/dev/', '')
                break

        if ssd_path:
            try:
                timestamp = datetime.datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S IST")
                result = subprocess.run(['sudo','smartctl', '-a', f'/dev/{ssd_path}'], capture_output=True, text=True)
                
                if result.returncode == 0:
                    smartctl_logger.info(f"Timestamp: {timestamp}\n{result.stdout}")
                    print(f"Logged smartctl data for {ssd_path} at {timestamp}")
                else:
                    error_message = f"Error running smartctl for {ssd_path}: {result.stderr}"
                    smartctl_logger.error(error_message)
                    print(error_message)

            except Exception as e:
                error_message = f"Exception occurred while running smartctl for {ssd_path}: {e}"
                smartctl_logger.error(error_message)
                print(error_message)
        else:
            smartctl_logger.warning("No SSD detected.")
            print("No SSD detected.")
        time.sleep(300)  

if __name__ == "__main__":
    # Setup SSD health monitoring logger
    smartctl_logger = setup_logging('smartctl.log')

    # Start SSD health monitoring
    detect_ssd_and_log_smartctl(smartctl_logger)

```