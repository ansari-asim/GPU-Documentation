---
title: SDK Installation Guide
description: CUDA, TensorRT, and DeepStream setup for Jetson and dGPU devices.
tags:
  - sdk
  - installation
  - cuda
  - tensorrt
  - deepstream
---

# SDK Installation Guide

## Quick Start Checklist

=== "Jetson Path"

    - [ ] Verify internet and package mirrors
    - [ ] Clean old CUDA / TensorRT artifacts
    - [ ] Reinstall JetPack dependencies
    - [ ] Install DeepStream and Python bindings

=== "dGPU Path"

    - [ ] Install NVIDIA driver and CUDA toolkit
    - [ ] Install TensorRT matching CUDA version
    - [ ] Install DeepStream and Python dependencies
    - [ ] Validate sample pipeline execution

??? info "Before you run commands"
    - Use the copy button on each code block to avoid typos.
    - Open a fresh terminal with ++ctrl+shift+t++ before starting.
    - Replace placeholders like ==interface names== and ==IP values== with your actual values.

!!! warning "Version consistency"
    CUDA, TensorRT, and DeepStream versions must stay aligned.
    A version mismatch will cause package install failures or missing runtime libraries.

---

## Jetson Device { #jetson }

### Avermedia & Tacodi { #avermedia-tacodi }

**Update and install JetPack dependencies**

```bash
sudo apt update && \
apt depends nvidia-jetpack \
  | awk '{print $2}' \
  | uniq \
  | xargs -I {} bash -c \
      "sudo apt clean ; sudo apt install -y {}"
```

??? note "Command breakdown"
    - `apt depends nvidia-jetpack` — lists all packages required by nvidia-jetpack
    - `awk '{print $2}'` — extracts package names only
    - `uniq` — removes duplicate entries
    - `sudo apt clean` — clears cache before each install
    - `apt install -y {}` — installs each package without confirmation

**Remove old and unnecessary packages**

```bash
sudo apt autoremove --purge -y \
  libnvidia-container0 \
  libnvidia-container-tools \
  nvidia-container-csv-cuda \
  nvidia-container-csv-cudnn \
  nvidia-container-csv-tensorrt \
  nvidia-container-csv-visionworks \
  nvidia-container-runtime \
  nvidia-container-toolkit \
  nvidia-docker2 \
  cuda-toolkit-10-2 \
  libcudnn8 \
  libcudnn8-dev \
  libcudnn8-samples \
  libopencv \
  libopencv-dev \
  libopencv-python \
  libopencv-samples \
  opencv-licenses \
  graphsurgeon-tf \
  libnvinfer8 \
  libnvinfer-bin \
  libnvinfer-dev \
  libnvinfer-doc \
  libnvinfer-plugin8 \
  libnvinfer-plugin-dev \
  libnvinfer-samples \
  libnvonnxparsers8 \
  libnvonnxparsers-dev \
  libnvparsers8 \
  libnvparsers-dev \
  python3-libnvinfer \
  python3-libnvinfer-dev \
  tensorrt \
  uff-converter-tf \
  libvisionworks \
  libvisionworks-dev \
  libvisionworks-samples \
  libvisionworks-sfm \
  libvisionworks-sfm-dev \
  libvisionworks-tracking \
  libvisionworks-tracking-dev \
  libnvvpi1 \
  vpi1-dev \
  vpi1-samples \
  vpi1-demos \
  nvidia-l4t-jetson-multimedia-api
```

**Reinstall JetPack dependencies**

```bash
sudo apt update && \
apt depends nvidia-jetpack \
  | awk '{print $2}' \
  | uniq \
  | xargs -I {} bash -c \
      "sudo apt clean ; sudo apt install -y {}"
```

!!! note "Applies to"
    **Nano, NX, and TX2NX** devices on **Avermedia** and **Tacodi** carrier boards.
    For Eagletech boards, see the section below.

---

### Eagletech { #eagletech }

**Update and install JetPack dependencies**

```bash
sudo apt update && \
apt depends nvidia-jetpack \
  | awk '{print $2}' \
  | uniq \
  | xargs -I {} bash -c \
      "sudo apt clean ; sudo apt install -y {}"
```

**Reboot**

```bash
sudo reboot
```

**System update**

```bash
sudo apt update -y
```

**Install Python, gdown, and nano**

```bash
sudo apt install python3-pip -y && \
sudo pip3 install gdown && \
sudo apt install nano -y
```

**Source `.bashrc` and return home**

```bash
source ~/.bashrc
echo "Changing directory to home"
cd ~
```

**Install GStreamer and system libraries**

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

**Create DeepStream 6.0 directory and copy libraries**

```bash
sudo mkdir -p \
  /opt/nvidia/deepstream/deepstream-6.0/lib && \
sudo cp \
  /usr/local/lib/librdkafka* \
  /opt/nvidia/deepstream/deepstream-6.0/lib
```

**Reboot**

```bash
sudo reboot
```

---

## dGPU { #dgpu }

### CUDA 11.8 { #cuda-118 }

!!! info "Prerequisites"
    - Open **Ubuntu Software → Additional Drivers**
    - Select **NVIDIA driver 535** and apply changes
    - Restart the system

**Install dependencies**

```bash
sudo apt install -y \
  libssl1.1 \
  libgstreamer1.0-0 \
  gstreamer1.0-tools \
  gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-bad \
  gstreamer1.0-plugins-ugly \
  gstreamer1.0-libav \
  libgstreamer-plugins-base1.0-dev \
  libgstrtspserver-1.0-0 \
  libjansson4 \
  libyaml-cpp-dev \
  libjsoncpp-dev \
  protobuf-compiler \
  gcc \
  make \
  git \
  python3
```

**Add CUDA 11.8 repository**

```bash
sudo apt-key adv \
  --fetch-keys \
  https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub && \
sudo add-apt-repository -y \
  "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /" && \
sudo apt-get update -y
```

**Install CUDA Toolkit 11.8**

```bash
sudo apt-get install -y cuda-toolkit-11-8
```

---

### TensorRT 8.5.1 { #tensorrt-851 }

**Install TensorRT 8.5.1 libraries**

```bash
sudo apt-get install -y \
  libnvinfer8=8.5.1-1+cuda11.8 \
  libnvinfer-plugin8=8.5.1-1+cuda11.8 \
  libnvparsers8=8.5.1-1+cuda11.8 \
  libnvonnxparsers8=8.5.1-1+cuda11.8 \
  libnvinfer-bin=8.5.1-1+cuda11.8 \
  libnvinfer-dev=8.5.1-1+cuda11.8 \
  libnvinfer-plugin-dev=8.5.1-1+cuda11.8 \
  libnvparsers-dev=8.5.1-1+cuda11.8 \
  libnvonnxparsers-dev=8.5.1-1+cuda11.8 \
  libnvinfer-samples=8.5.1-1+cuda11.8 \
  libcudnn8=8.6.0.163-1+cuda11.8 \
  libcudnn8-dev=8.6.0.163-1+cuda11.8 \
  python3-libnvinfer=8.5.1-1+cuda11.8 \
  python3-libnvinfer-dev=8.5.1-1+cuda11.8
```

**Install gdown**

```bash
sudo apt-get install python3-pip && \
sudo pip3 install gdown
```
