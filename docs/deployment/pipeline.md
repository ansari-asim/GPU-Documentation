---
title: Deployment Pipeline
description: Deployment automation and monitoring with daddy-ai and jtop.
tags:
  - deployment
  - automation
  - monitoring
---

# Deployment Pipeline

## daddy-ai Deployment Automation

`daddy-ai` is a deployment automation library that creates systemd-managed services for your Python applications with automatic restart scheduling.

### Installation { #daddy-ai-install }

```bash
pip install daddy-ai
```

### Import DeployMaster { #daddy-ai-import }

```python
from daddy_ai.deploy_master import DeployMaster
import os
```

### Initialize DeployMaster { #daddy-ai-init }

```python
deploy_master = DeployMaster(
    user=os.getenv("USER")
)
```

### Create a Bash Script { #daddy-ai-bash }

```python
script_file = deploy_master.create_bash(
    path="/path/to/your/app",
    command="python3 your_app.py",
    code_name="your_app_name"
)
```

### Generate Restart Code { #daddy-ai-restart }

```python
deploy_master.generate_restart_code(
    start_time="09:00:00",
    end_time="17:00:00",
    process_name="your_app.py",
    script_file=script_file
)
```

### Create a Service { #daddy-ai-service }

```python
deploy_master.create_service()
```

### File Locations { #daddy-ai-paths }

| File | Path |
|------|------|
| Bash scripts | `/home/{user}/daddy-ai/scripts/run_{code_name}.sh` |
| Restart scripts | `/home/{user}/daddy-ai/scripts/restart_{code_name}.py` |
| Service files | `/etc/systemd/system/daddy-ai-deploy-master-{code_name}.service` |

---

## jtop — Real-Time System Monitoring

`jtop` is a real-time system monitor for NVIDIA Jetson devices — part of the `jetson-stats` package.

### Key Features { #jtop-features }

| Feature | Description |
|---------|-------------|
| Real-time monitoring | CPU, GPU, and memory statistics |
| Temperature tracking | CPU, GPU, and critical component temps |
| Power consumption | Energy usage insights |
| Resource management | Identify bottlenecks |
| NVIDIA-specific metrics | Tensor core status, GPU load |

### Installation { #jtop-install }

```bash
sudo pip3 install -U jetson-stats
```

### Verify Installation { #jtop-verify }

```bash
jtop --version
```

### Running jtop { #jtop-run }

```bash
sudo jtop
```

!!! info "Dashboard layout"
    - **Top bar** — uptime, CPU usage, memory, temperature
    - **CPU section** — per-core load
    - **GPU section** — load and CUDA core status
    - **Memory** — RAM and swap usage
    - **Temperature** — per-component readings
    - **Power** — real-time draw

### Logging System Stats { #jtop-log }

```bash
sudo jtop --log <filename>
```

!!! tip "Additional features"
    - **Process Monitoring** — similar to `htop`
    - **Power Mode Adjustment** — change Jetson power mode directly from the interface
    - **Log Data** — capture stats for later analysis
