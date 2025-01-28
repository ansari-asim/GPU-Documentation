## **Jetson Device**

### **Avermedia & Tacodi**

**Update and Install JetPack Dependencies**

```
sudo apt update && apt depends nvidia-jetpack | awk '{print $2}' | uniq | xargs -I {} bash -c "sudo apt clean ; sudo apt install -y {}"
```
**Explanation:**

 - **apt depends nvidia-jetpack:** Lists all the dependencies required by the nvidia-jetpack package.
 - **awk '{print $2}':** Extracts only the package names
 - **uniq:** Removes duplicate entries from the package list.
 - **xargs -I {} bash -c "sudo apt clean ; sudo apt install -y {}":**
    - **apt clean:** Clears the package cache to free up space before the installation.
    - **apt install -y {}:** Installs each package found in the dependency list without asking for confirmation.

**Purpose:** This command updates your system and ensures all necessary JetPack dependencies are freshly installed.

**Remove Unnecessary or Old Packages**
```
sudo apt autoremove --purge libnvidia-container0 libnvidia-container-tools nvidia-container-csv-cuda nvidia-container-csv-cudnn nvidia-container-csv-tensorrt nvidia-container-csv-visionworks nvidia-container-runtime nvidia-container-toolkit nvidia-docker2 cuda-toolkit-10-2 libcudnn8 libcudnn8-dev libcudnn8-samples libopencv libopencv-dev libopencv-python libopencv-samples opencv-licenses graphsurgeon-tf libnvinfer8 libnvinfer-bin libnvinfer-dev libnvinfer-doc libnvinfer-plugin8 libnvinfer-plugin-dev libnvinfer-samples libnvonnxparsers8 libnvonnxparsers-dev libnvparsers8 libnvparsers-dev python3-libnvinfer python3-libnvinfer-dev tensorrt uff-converter-tf libvisionworks libvisionworks-dev libvisionworks-samples libvisionworks-sfm libvisionworks-sfm-dev libvisionworks-tracking libvisionworks-tracking-dev libnvvpi1 vpi1-dev vpi1-samples vpi1-demos nvidia-l4t-jetson-multimedia-api -y
```

**Explanation:**

 - **sudo apt autoremove:** Automatically removes packages that were installed as dependencies but are no longer required.
 - **--purge:** Ensures that not only are the packages removed but also their associated configuration files.
 - The list of packages includes various older or unnecessary libraries and tools (like CUDA 10.2, cuDNN, TensorRT, OpenCV, VisionWorks, etc.) that are specific to Jetson development.
 - **-y:** Runs the command without prompting for confirmation.

**Purpose:** This step clears out any outdated or unneeded packages and configurations, ensuring that only necessary software remains on the device.

**Reinstall JetPack Dependencies**
```
sudo apt update && apt depends nvidia-jetpack | awk '{print $2}' | uniq | xargs -I {} bash -c "sudo apt clean ; sudo apt install -y {}"
```

**Explanation:**

This command repeats the process of the first command:

  - Updates the system package list.
  - Re-fetches the dependencies for **nvidia-jetpack**.
  - Clears cached files (**apt clean**).
  - Reinstalls the necessary packages with **apt install**.

**Purpose:** After purging old or unnecessary packages in the second step, this step ensures that the Jetson device is updated with all the required JetPack dependencies, ensuring a clean and functional setup.


**Note:** 
 
 - The above documentation applies to **Nano, NX,** and **TX2NX** devices using **Avermedia** and  **Tacodi** carrier boards. 
 
 - For **Eagletech** boards, please refer to the next documentation. 


### **Eagletech**

**Update and Install JetPack Dependencies**

```
sudo apt update && apt depends nvidia-jetpack | awk '{print $2}' | uniq | xargs -I {} bash -c "sudo apt clean ; sudo apt install -y {}"
```
**Explanation:**

 - Updates the package list and installs the necessary JetPack dependencies.
 - Cleans up the package cache to free space during installation.

**Reboot The GPU**

```
sudo reboot
```

**Update the System:**
```
sudo apt update -y
```

**Install python , gdown and nano**
```
sudo apt install python3-pip -y
sudo pip3 install gdown
sudo apt install nano -y
```

**Source ***.bashrc*** and Change Directory to Home**
 
 - Source the **.bashrc** to apply any environment changes and move to the home directory.
```
source ~/.bashrc
echo "Changing directory to home"
cd ~
```
**Install Additional Dependencies**

 - Install various system libraries and GStreamer plugins required for DeepStream.
```
sudo apt install \
libssl1.0.0 \
libgstreamer1.0-0 \
gstreamer1.0-tools \
gstreamer1.0-plugins-good \
gstreamer1.0-plugins-bad \
gstreamer1.0-plugins-ugly \
gstreamer1.0-libav \
libgstrtspserver-1.0-0 \
libjansson4=2.11-1 -y
```

**Create Directory for DeepStream 6.0**

 - Create a directory for DeepStream 6.0 and copy necessary libraries.
```
sudo mkdir -p /opt/nvidia/deepstream/deepstream-6.0/lib
sudo cp /usr/local/lib/librdkafka* /opt/nvidia/deepstream/deepstream-6.0/lib
```
**Reboot The GPU**

```
sudo reboot
```

### **Deepstream 6.0**

**Downloading DeepStream 6.0**
```
sudo gdown 1RnLnqyooOM9CU7KA8BJ7_uteARUzsJJG
```
**Installing DeepStream 6.0**
```
sudo apt-get install -y ./deepstream-6.0_6.0.0-1_arm64.deb
```

###### **Python-apps**

**Navigate to DeepStream Sources Directory**
```
cd /opt/nvidia/deepstream/deepstream/sources/
```
**Clone the deepstream_python_apps Repository**
```
sudo git clone https://github.com/NVIDIA-AI-IOT/deepstream_python_apps.git
cd deepstream_python_apps/
```
**Checkout the Specific Version for DeepStream 6.0**
```
sudo git checkout 20c6b13671e81cf73ca98fa795f84cab7dd6fc67
```
**Initialize Git Submodules**
```
cd bindings/
sudo git submodule update --init
```
**Create and Navigate to Build Directory**
```
sudo mkdir build && cd build
```

**Run CMake with Specific Options**
```
sudo cmake .. -DPYTHON_MAJOR_VERSION=3 -DPYTHON_MINOR_VERSION=6 -DPIP_PLATFORM=linux_aarch64 -DDS_PATH=/opt/nvidia/deepstream/deepstream
```

**Build the Python Bindings**
```
sudo make -j$(nproc)
```
**Copy the Python Wheel File to Export Directory**
```
sudo cp pyds-*.whl /export_pyds
```

**Install the Python Wheel Package**
```
sudo python3 -m pip install --upgrade pip
sudo pip3 install ./pyds-1.1.0-py3-none*.whl
```
**Running DeepStream Analytics Application**
```
cd /opt/nvidia/deepstream/deepstream-6.2/sources/deepstream_python_apps/apps/deepstream-nvdsanalytics/
sudo python3 deepstream_nvdsanalytics.py file:/opt/nvidia/deepstream/deepstream/samples/streams/sample_1080p_h264.mp4
```
## **dGPU**

### **CUDA 11.8**

**Select NVIDIA Driver 535**
  
  - Open **Ubuntu Software → Additional Drivers**.

  - Select **NVIDIA driver 535** from the list and apply the changes.

  - Restart your system for the changes to take effect.

**Installing Dependencies**
```
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

**Explanation**

 - Installs required libraries and packages for DeepStream and GStreamer (used for media   handling in DeepStream).
 - Development tools like gcc, make, and git are included for compilation and building purposes.

 **Setting up CUDA 11.8 Repository**

```
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
sudo add-apt-repository -y "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
sudo apt-get update -y
```
**Explanation**

 - Adds the official NVIDIA CUDA 11.8 repository for Ubuntu 20.04.
 - Fetches the GPG key for secure installation of CUDA packages.

**Installing CUDA Toolkit 11.8**
```
sudo apt-get install -y cuda-toolkit-11-8
```
**Explanation**

 - Installs CUDA toolkit version 11.8, which provides the necessary GPU libraries and tools.

### **TensorRT 8.5.1**

**Installing NVIDIA TensorRT and Related Libraries**

```
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

**Explanation**

 - Installs TensorRT libraries (libnvinfer, libnvparsers, libcudnn) for optimizing deep learning inference, particularly on NVIDIA hardware.
 - Specific version 8.5.1 of TensorRT is installed with CUDA 11.8 compatibility.

**Install Python gdown Tool**

```
sudo apt-get install python3-pip
sudo pip3 install gdown 
```

### **Deepstream 6.2**

**Downloading DeepStream 6.2**

```
sudo gdown 1UHGdU5utMwAvwTa4_0a2U6ArH9tgTRub 
```

**Installing DeepStream 6.2**

```
sudo apt-get install -y ./deepstream-6.2_6.2.0-1_amd64.deb
```

#### **Python-apps**

**Cloning DeepStream Python Applications Repository**

```
cd /opt/nvidia/deepstream/deepstream-6.2/sources
git clone -b v1.1.6 https://github.com/NVIDIA-AI-IOT/deepstream_python_apps.git
```

**Installing Python Development Packages**
```
sudo apt install -y python3-gi python3-dev python3-gst-1.0 python-gi-dev \
    python3 python3-pip python3.8-dev cmake g++ build-essential \
    libglib2.0-dev libglib2.0-dev-bin libgstreamer1.0-dev libtool m4 \
    autoconf automake libgirepository1.0-dev libcairo2-dev
```
**Explanation**

 - Installs essential Python and GStreamer libraries for Python bindings, including libgirepository, glib, and gstreamer components.


**Initialization of submodules**

This will create the following directory:

```
<DeepStream 6.2 ROOT>/sources/deepstream_python_apps
```

The repository utilizes gst-python and pybind11 submodules. To initializes them, run the following command:

```
cd /opt/nvidia/deepstream/deepstream/sources/deepstream_python_apps/
git submodule update --init
```

**Installing Gst-python**

```
sudo apt-get install -y apt-transport-https ca-certificates -y
sudo update-ca-certificates
```

**Building and Installing DeepStream Python Bindings**
```
cd 3rdparty/gst-python/
./autogen.sh
make -j$(nproc)
sudo make install
```

**Explanation**

 - Builds and installs the GStreamer Python bindings for DeepStream.

```
cd ../../bindings
sudo mkdir build
cd build
sudo cmake ..
sudo make -j$(nproc)
sudo pip3 install pyds-1.1.6-py3-none-linux_x86_64.whl
```

**Explanation**

 - Builds and installs the Python bindings for DeepStream **(pyds)**.

**Running DeepStream Analytics Application**

```
cd /opt/nvidia/deepstream/deepstream-6.2/sources/deepstream_python_apps/apps/deepstream-nvdsanalytics/
sudo python3 deepstream_nvdsanalytics.py file:/opt/nvidia/deepstream/deepstream/samples/streams/sample_1080p_h264.mp4
```

### **CUDA 12.2**

**Prerequisites**

Install the following components:

 - Ubuntu 22.04

 - GStreamer 1.20.3

 - CUDA 12.2

 - TensorRT  8.6.1.6

**NVIDIA Driver:**

 - 560.35.03 (for RTX GPUs)

**Remove Previous DeepStream Installations**

```
sudo rm -rf /usr/local/deepstream /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libgstnv* /usr/bin/deepstream* \
/usr/lib/x86_64-linux-gnu/gstreamer-1.0/libnvdsgst* /usr/lib/x86_64-linux-gnu/gstreamer-1.0/deepstream* \
/opt/nvidia/deepstream/deepstream*
```

```
sudo rm -rf /usr/lib/x86_64-linux-gnu/libv41/plugins/libcuvidv4l2_plugin.so
```

**Migrate glib to a Newer Version**

Run the following commands:

```
pip3 install meson
pip3 install ninja
```

***Compilation and Installation Steps***

```
git clone https://github.com/GNOME/glib.git
cd glib
git checkout <glib-version-branch>  # e.g., 2.76.6
meson build --prefix=/usr
ninja -C build/
cd build/
ninja install
```

***Verify the newly installed glib version:***

```
pkg-config --modversion glib-2.0
```

**Install Dependencies**

Run the following commands:

```
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


```
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub
```

```
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"
```

```
sudo apt-get update
```

```
sudo apt-get install cuda-toolkit-12-2
```


### **TensorRT 8.6.1.6**

```
sudo apt-get install --no-install-recommends libnvinfer-lean8=8.6.1.6-1+cuda12.0 libnvinfer-vc-plugin8=8.6.1.6-1+cuda12.0 \
libnvinfer-headers-dev=8.6.1.6-1+cuda12.0 libnvinfer-dev=8.6.1.6-1+cuda12.0 libnvinfer-headers-plugin-dev=8.6.1.6-1+cuda12.0 \
libnvinfer-plugin-dev=8.6.1.6-1+cuda12.0 libnvonnxparsers-dev=8.6.1.6-1+cuda12.0 libnvinfer-lean-dev=8.6.1.6-1+cuda12.0 \
libnvparsers-dev=8.6.1.6-1+cuda12.0 python3-libnvinfer-lean=8.6.1.6-1+cuda12.0 python3-libnvinfer-dispatch=8.6.1.6-1+cuda12.0 \
uff-converter-tf=8.6.1.6-1+cuda12.0 onnx-graphsurgeon=8.6.1.6-1+cuda12.0 libnvinfer-bin=8.6.1.6-1+cuda12.0 \
libnvinfer-dispatch-dev=8.6.1.6-1+cuda12.0 libnvinfer-dispatch8=8.6.1.6-1+cuda12.0 libnvonnxparsers-dev=8.6.1.6-1+cuda12.0 \
libnvonnxparsers8=8.6.1.6-1+cuda12.0 libnvinfer-vc-plugin-dev=8.6.1.6-1+cuda12.0 libnvinfer-samples=8.6.1.6-1+cuda12.0
```

### **Deepstream 7.0**

**Downloading DeepStream 6.2**

```
sudo gdown 1p7jUJmSVXmayGZNPQt8tQW6USHq9oORG
```

**Installing DeepStream 6.2**

```
sudo apt-get install -y ./deepstream-7.0_7.0.0-1_amd64.deb
```

#### **Python-apps**

```
cd /opt/nvidia/deepstream/deepstream-7.0/sources
git clone -b v1.1.11 https://github.com/NVIDIA-AI-IOT/deepstream_python_apps.git
```

**Base dependencies**

```
apt install python3-gi python3-dev python3-gst-1.0 python-gi-dev git meson \
    python3 python3-pip python3.10-dev cmake g++ build-essential libglib2.0-dev \
    libglib2.0-dev-bin libgstreamer1.0-dev libtool m4 autoconf automake libgirepository1.0-dev libcairo2-dev
```

**Initialization of submodules**

```
cd /opt/nvidia/deepstream/deepstream/sources/deepstream_python_apps/
git submodule update --init
```

**Installing Gst-python**

```
sudo apt-get install -y apt-transport-https ca-certificates -y
sudo update-ca-certificates
```

**Build and install gst-python:**

```
cd 3rdparty/gstreamer/subprojects/gst-python/
meson setup build
cd build
ninja
ninja install
```

**Compiling the bindings**

```
cd deepstream_python_apps/bindings
mkdir build
cd build
cmake ..
make -j$(nproc)
```

**Installing the bindings**

```
pip3 install ./pyds-1.1.11-py3-none*.whl
```

**pip wheel troubleshooting**

If the wheel installation fails, upgrade the pip using the following command:

```
python3 -m pip install --upgrade pip
```

**Cuda-python**

```
sudo pip3 install cuda-python
```
### **Uninstalling**

**Uninstalling Previous DeepStream and CUDA Libraries**

```
sudo rm -rf /usr/local/deepstream /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libgstnv* /usr/bin/deepstream* /usr/lib/x86_64-linux-gnu/gstreamer-1.0/libnvdsgst* /usr/lib/x86_64-linux-gnu/gstreamer-1.0/deepstream*  /opt/nvidia/deepstream/deepstream*
sudo rm -rf /usr/lib/x86_64-linux-gnu/libv41/plugins/libcuvidv4l2_plugin.so
sudo apt-get remove cuda* libnvinfer* -y 
sudo apt update -y
```

**Explanation:**

 - Removes all existing DeepStream components, CUDA, TensorRT libraries, and plugins to ensure a clean environment.
 - apt-get remove cuda* libnvinfer* uninstalls any existing CUDA and TensorRT installations.

### **Docker Setup**

Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker repository. Afterward, you can install and update Docker from the repository.

**Add Docker's official GPG key:**

```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

**Add the repository to Apt sources:**
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

**Install the Docker packages.**

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
**Verify that the Docker Engine installation is successful by running the hello-world image.**
```
sudo docker run hello-world
```
**Install NVIDIA Container Toolkit:**

```
sudo apt-get install -y nvidia-container-toolkit
```
**Configure the NVIDIA runtime for Docker:**
```
sudo nvidia-ctk runtime configure --runtime=docker
```

**Restart Docker service:**
```
sudo systemctl restart docker
```

**Download the docker image**

**Note:** Please use a screen session for this downloading , because it takes a lot of time to download

**Upgrade and install gdown**

```
sudo pip3 install --upgrade --no-cache-dir gdown
```

**Download file from Google Drive using its ID:**

```
gdown --id 1oWvWU7ft50TzbYCzhx_RcdoTZuLF8vhl 
```

**Load a Docker image from a tar file:**

```
sudo docker load -i rajesh-ds-py.tar

```