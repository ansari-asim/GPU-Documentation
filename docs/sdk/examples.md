---
title: Docker Setup
description: Sample code, Docker setup, and advanced deployment examples.
tags:
  - sdk
  - examples
  - docker
---

# Docker Setup

## Uninstalling

**Remove all DeepStream and CUDA libraries**

```bash
sudo rm -rf \
  /usr/local/deepstream \
  /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libgstnv* \
  /usr/bin/deepstream* \
  /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libnvdsgst* \
  /usr/lib/x86_64-linux-gnu/gstreamer-1.0/deepstream* \
  /opt/nvidia/deepstream/deepstream* && \
sudo rm -rf \
  /usr/lib/x86_64-linux-gnu/libv41/plugins/libcuvidv4l2_plugin.so && \
sudo apt-get remove -y cuda* libnvinfer* && \
sudo apt update -y
```

---

## Docker Setup { #docker }

**Add Docker GPG key and repository**

```bash
sudo apt-get update && \
sudo apt-get install ca-certificates curl && \
sudo install -m 0755 -d /etc/apt/keyrings && \
sudo curl -fsSL \
  https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc && \
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

**Add Docker apt source**

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) \
  signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" \
  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null && \
sudo apt-get update
```

**Install Docker packages**

```bash
sudo apt-get install \
  docker-ce \
  docker-ce-cli \
  containerd.io \
  docker-buildx-plugin \
  docker-compose-plugin
```

**Verify Docker installation**

```bash
sudo docker run hello-world
```

**Install NVIDIA Container Toolkit**

```bash
sudo apt-get install -y nvidia-container-toolkit && \
sudo nvidia-ctk runtime configure --runtime=docker && \
sudo systemctl restart docker
```

**Download Docker image**

!!! warning "Use a screen session"
    This download can take a long time. Start a `screen` session before running:
    ```bash
    screen -S docker-pull
    ```

**Upgrade gdown and download the image**

```bash
sudo pip3 install \
  --upgrade \
  --no-cache-dir \
  gdown && \
gdown --id 1oWvWU7ft50TzbYCzhx_RcdoTZuLF8vhl
```

**Load Docker image**

```bash
sudo docker load -i rajesh-ds-py.tar
```

*Additional examples are coming soon.*
