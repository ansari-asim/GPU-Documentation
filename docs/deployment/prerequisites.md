---
title: Deployment Prerequisites
description: System requirements and dependency installation for deployment.
tags:
  - deployment
  - prerequisites
  - dependencies
---

# Deployment Prerequisites

## System Dependencies

Full system dependency installation for AI hardware nodes.

### System Update { #deps-update }

```bash
sudo apt update -y && \
sudo apt upgrade -y
```

### Python and Dev Tools { #deps-python }

```bash
sudo apt install python3-pip -y && \
sudo apt-get install \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential -y
```

### MySQL { #deps-mysql }

```bash
sudo apt-get install mysql-server -y
```

```bash
sudo pip3 uninstall mysql-connector -y && \
sudo pip3 install mysql-connector && \
sudo pip3 install \
    mysql-connector-python \
    mysqlclient
```

### AWS SDK — Boto3 { #deps-boto3 }

```bash
sudo pip3 install \
    boto3 \
    botocore \
    awscli \
    --ignore-installed
```

### psutil — System Monitoring { #deps-psutil }

```bash
sudo pip3 install psutil
```

### GStreamer and Multimedia Plugins { #deps-gstreamer }

```bash
sudo apt install \
    libssl1.0.0 \
    libgstreamer1.0-0 \
    gstreamer1.0-tools \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    libgstrtspserver-1.0-0 \
    "libjansson4=2.11-1" -y
```

### nano Text Editor { #deps-nano }

```bash
sudo apt install nano -y
```

### gdown — Google Drive Downloads { #deps-gdown }

```bash
sudo pip3 install gdown
```
