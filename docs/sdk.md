---
title: SDK
description: DeepStream, CUDA, TensorRT, and Docker setup for Jetson and dGPU devices.
tags:
  - sdk
  - deepstream
  - cuda
  - tensorrt
  - docker
---

# 🧰 SDK { #sdk }

Complete setup guide for DeepStream, CUDA, TensorRT, and Python bindings on Jetson and dGPU platforms.

---

!!! tip "Quick Start checklist"
    Use this page as an execution checklist for your target platform.

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

### DeepStream 6.0 — Jetson { #deepstream-60-jetson }

**Download DeepStream 6.0**

```bash
sudo gdown 1RnLnqyooOM9CU7KA8BJ7_uteARUzsJJG
```

**Install DeepStream 6.0**

```bash
sudo apt-get install -y \
  ./deepstream-6.0_6.0.0-1_arm64.deb
```

#### Python Apps { #ds60-python-apps }

**Navigate to DeepStream sources**

```bash
cd /opt/nvidia/deepstream/deepstream/sources/
```

**Clone the Python apps repository**

```bash
sudo git clone \
  https://github.com/NVIDIA-AI-IOT/deepstream_python_apps.git && \
cd deepstream_python_apps/
```

**Checkout the DeepStream 6.0 version**

```bash
sudo git checkout \
  20c6b13671e81cf73ca98fa795f84cab7dd6fc67
```

**Initialize git submodules**

```bash
cd bindings/ && \
sudo git submodule update --init
```

**Create build directory**

```bash
sudo mkdir build && cd build
```

**Run CMake**

```bash
sudo cmake .. \
  -DPYTHON_MAJOR_VERSION=3 \
  -DPYTHON_MINOR_VERSION=6 \
  -DPIP_PLATFORM=linux_aarch64 \
  -DDS_PATH=/opt/nvidia/deepstream/deepstream
```

**Build Python bindings**

```bash
sudo make -j$(nproc)
```

**Copy wheel to export directory**

```bash
sudo cp pyds-*.whl /export_pyds
```

**Install wheel package**

```bash
sudo python3 -m pip install --upgrade pip && \
sudo pip3 install ./pyds-1.1.0-py3-none*.whl
```

**Run DeepStream analytics sample**

```bash
cd /opt/nvidia/deepstream/deepstream-6.2/sources/ \
  deepstream_python_apps/apps/deepstream-nvdsanalytics/ && \
sudo python3 deepstream_nvdsanalytics.py \
  file:/opt/nvidia/deepstream/deepstream/samples/streams/sample_1080p_h264.mp4
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

---

### DeepStream 6.2 { #deepstream-62 }

**Download and install**

```bash
sudo gdown 1UHGdU5utMwAvwTa4_0a2U6ArH9tgTRub && \
sudo apt-get install -y \
  ./deepstream-6.2_6.2.0-1_amd64.deb
```

#### Python Apps { #ds62-python-apps }

**Clone repository**

```bash
cd /opt/nvidia/deepstream/deepstream-6.2/sources && \
git clone -b v1.1.6 \
  https://github.com/NVIDIA-AI-IOT/deepstream_python_apps.git
```

**Install Python development packages**

```bash
sudo apt install -y \
  python3-gi \
  python3-dev \
  python3-gst-1.0 \
  python-gi-dev \
  python3 \
  python3-pip \
  python3.8-dev \
  cmake \
  g++ \
  build-essential \
  libglib2.0-dev \
  libglib2.0-dev-bin \
  libgstreamer1.0-dev \
  libtool \
  m4 \
  autoconf \
  automake \
  libgirepository1.0-dev \
  libcairo2-dev
```

**Initialize submodules**

```bash
cd /opt/nvidia/deepstream/deepstream/sources/deepstream_python_apps/ && \
git submodule update --init
```

**Install Gst-python certificates**

```bash
sudo apt-get install -y apt-transport-https ca-certificates && \
sudo update-ca-certificates
```

**Build and install GStreamer Python bindings**

```bash
cd 3rdparty/gst-python/ && \
./autogen.sh && \
make -j$(nproc) && \
sudo make install
```

**Build and install pyds bindings**

```bash
cd ../../bindings && \
sudo mkdir build && \
cd build && \
sudo cmake .. && \
sudo make -j$(nproc) && \
sudo pip3 install pyds-1.1.6-py3-none-linux_x86_64.whl
```

**Run analytics sample**

```bash
cd /opt/nvidia/deepstream/deepstream-6.2/sources/ \
  deepstream_python_apps/apps/deepstream-nvdsanalytics/ && \
sudo python3 deepstream_nvdsanalytics.py \
  file:/opt/nvidia/deepstream/deepstream/samples/streams/sample_1080p_h264.mp4
```

---

### CUDA 12.2 { #cuda-122 }

!!! info "Prerequisites"
    | Component | Version |
    |-----------|---------|
    | Ubuntu | 22.04 |
    | GStreamer | 1.20.3 |
    | CUDA | 12.2 |
    | TensorRT | 8.6.1.6 |
    | NVIDIA Driver | 560.35.03 (RTX GPUs) |

**Remove previous DeepStream installations**

```bash
sudo rm -rf \
  /usr/local/deepstream \
  /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libgstnv* \
  /usr/bin/deepstream* \
  /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libnvdsgst* \
  /usr/lib/x86_64-linux-gnu/gstreamer-1.0/deepstream* \
  /opt/nvidia/deepstream/deepstream* && \
sudo rm -rf \
  /usr/lib/x86_64-linux-gnu/libv41/plugins/libcuvidv4l2_plugin.so
```

**Migrate glib to newer version**

```bash
pip3 install meson ninja
```

```bash
git clone https://github.com/GNOME/glib.git && \
cd glib && \
git checkout <glib-version-branch> && \
meson build --prefix=/usr && \
ninja -C build/ && \
cd build/ && \
ninja install
```

**Verify glib version**

```bash
pkg-config --modversion glib-2.0
```

**Install dependencies**

```bash
sudo apt install \
  libssl3 \
  libssl-dev \
  libgles2-mesa-dev \
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

**Add CUDA 12.2 repository and install**

```bash
sudo apt-key adv \
  --fetch-keys \
  https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub && \
sudo add-apt-repository \
  "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /" && \
sudo apt-get update && \
sudo apt-get install cuda-toolkit-12-2
```

---

### TensorRT 8.6.1.6 { #tensorrt-8616 }

```bash
sudo apt-get install --no-install-recommends \
  libnvinfer-lean8=8.6.1.6-1+cuda12.0 \
  libnvinfer-vc-plugin8=8.6.1.6-1+cuda12.0 \
  libnvinfer-headers-dev=8.6.1.6-1+cuda12.0 \
  libnvinfer-dev=8.6.1.6-1+cuda12.0 \
  libnvinfer-headers-plugin-dev=8.6.1.6-1+cuda12.0 \
  libnvinfer-plugin-dev=8.6.1.6-1+cuda12.0 \
  libnvonnxparsers-dev=8.6.1.6-1+cuda12.0 \
  libnvinfer-lean-dev=8.6.1.6-1+cuda12.0 \
  libnvparsers-dev=8.6.1.6-1+cuda12.0 \
  python3-libnvinfer-lean=8.6.1.6-1+cuda12.0 \
  python3-libnvinfer-dispatch=8.6.1.6-1+cuda12.0 \
  uff-converter-tf=8.6.1.6-1+cuda12.0 \
  onnx-graphsurgeon=8.6.1.6-1+cuda12.0 \
  libnvinfer-bin=8.6.1.6-1+cuda12.0 \
  libnvinfer-dispatch-dev=8.6.1.6-1+cuda12.0 \
  libnvinfer-dispatch8=8.6.1.6-1+cuda12.0 \
  libnvonnxparsers8=8.6.1.6-1+cuda12.0 \
  libnvinfer-vc-plugin-dev=8.6.1.6-1+cuda12.0 \
  libnvinfer-samples=8.6.1.6-1+cuda12.0
```

---

### DeepStream 7.0 { #deepstream-70 }

**Download and install**

```bash
sudo gdown 1p7jUJmSVXmayGZNPQt8tQW6USHq9oORG && \
sudo apt-get install -y \
  ./deepstream-7.0_7.0.0-1_amd64.deb
```

#### Python Apps { #ds70-python-apps }

**Clone repository**

```bash
cd /opt/nvidia/deepstream/deepstream-7.0/sources && \
git clone -b v1.1.11 \
  https://github.com/NVIDIA-AI-IOT/deepstream_python_apps.git
```

**Base dependencies**

```bash
apt install \
  python3-gi \
  python3-dev \
  python3-gst-1.0 \
  python-gi-dev \
  git \
  meson \
  python3 \
  python3-pip \
  python3.10-dev \
  cmake \
  g++ \
  build-essential \
  libglib2.0-dev \
  libglib2.0-dev-bin \
  libgstreamer1.0-dev \
  libtool \
  m4 \
  autoconf \
  automake \
  libgirepository1.0-dev \
  libcairo2-dev
```

**Initialize submodules**

```bash
cd /opt/nvidia/deepstream/deepstream/sources/deepstream_python_apps/ && \
git submodule update --init
```

**Install Gst-python**

```bash
sudo apt-get install -y apt-transport-https ca-certificates && \
sudo update-ca-certificates
```

**Build gst-python**

```bash
cd 3rdparty/gstreamer/subprojects/gst-python/ && \
meson setup build && \
cd build && \
ninja && \
ninja install
```

**Compile bindings**

```bash
cd deepstream_python_apps/bindings && \
mkdir build && \
cd build && \
cmake .. && \
make -j$(nproc)
```

**Install bindings wheel**

```bash
pip3 install ./pyds-1.1.11-py3-none*.whl
```

??? tip "Wheel install fails?"
    Upgrade pip first, then retry:
    ```bash
    python3 -m pip install --upgrade pip
    ```

**Install cuda-python**

```bash
sudo pip3 install cuda-python
```

---

### DeepStream 8.0 { #deepstream-80 }

!!! info "Prerequisites"
    | Component | Version |
    |-----------|---------|
    | Ubuntu | 24.04 |
    | GStreamer | 1.24.2 |
    | NVIDIA Driver | 570.133.20 |
    | CUDA | 12.8 |
    | TensorRT | 10.9.0.34 |

**Install prerequisite packages**

```bash
sudo apt install \
  libssl3 \
  libssl-dev \
  libgles2-mesa-dev \
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
  libmosquitto1 \
  gcc \
  make \
  git \
  python3
```

!!! note "RTSP EOS issue"
    If the application gets stuck at EOS with RTSP streams, run `update_rtpmanager.sh` located at `/opt/nvidia/deepstream/deepstream/` after installing dependencies.
    On Docker, run `user_additional_install.sh` instead.

**Install CUDA Toolkit 12.8**

```bash
sudo apt-key adv \
  --fetch-keys \
  https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/3bf863cc.pub && \
sudo add-apt-repository \
  "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/ /" && \
sudo apt-get update && \
sudo apt-get install cuda-toolkit-12-8
```

**Install TensorRT 10.9.0.34**

```bash
version="10.9.0.34-1+cuda12.8" && \
sudo apt-get install \
  libnvinfer-dev=${version} \
  libnvinfer-dispatch-dev=${version} \
  libnvinfer-dispatch10=${version} \
  libnvinfer-headers-dev=${version} \
  libnvinfer-headers-plugin-dev=${version} \
  libnvinfer-lean-dev=${version} \
  libnvinfer-lean10=${version} \
  libnvinfer-plugin-dev=${version} \
  libnvinfer-plugin10=${version} \
  libnvinfer-vc-plugin-dev=${version} \
  libnvinfer-vc-plugin10=${version} \
  libnvinfer10=${version} \
  libnvonnxparsers-dev=${version} \
  libnvonnxparsers10=${version} \
  tensorrt-dev=${version}
```

**Download and install DeepStream 8.0**

```bash
sudo gdown 1p7jUJmSVXmayGZNPQt8tQW6USHq9oORG && \
sudo apt-get install ./deepstream-8.0_8.0.0-1_amd64.deb
```

---

### Uninstalling { #uninstall }

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

### Docker Setup { #docker }

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