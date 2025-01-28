# GPU


## **Jetson Device**

### **Avermedia** (Nano)

**Before proceeding, ensure you have the following:**

   - Jetson Nano device
   - Avermedia EN715 board
   - USB cable for putting the device into recovery mod
   - Require Host PC Ubuntu 18.04 or Ubuntu 20.04

**Step 1: Download the BSP File**

Download the required BSP (Board Support Package) file for the Avermedia EN715 board from the following link :

[Download BSP File](https://s3.us-west-2.amazonaws.com/storage.avermedia.com/web_release_www/EN715/BSP/BSP-Nano/2021-12-20/EN715-R1.0.20.4.6.tar.gz)

**Step 2: Extract the BSP File**

Once the BSP file has been downloaded, open a terminal on your host machine and navigate to the directory where the file is located.

Run the following command to extract the BSP file:

```
sudo tar xzvf EN715-R1.0.20.4.6.tar.gz
```
**Step 3: Put Jetson Nano into Recovery Mode**

To flash the BSP file onto the Jetson Nano, you need to put the device into recovery mode.

**Steps to enter Recovery Mode:**

  - Connect the Jetson Nano to your host PC using a micro-USB cable.
  - Press and hold the Recovery button.
  - While holding the Recovery button, press the Power button.
  - Release the Recovery button.

**Step 4: Run Flashing Commands**

  - Navigate to the directory

```
cd JetPack_4.6_Linux_JETSON_NANO_TARGETS/Linux_for_Tegra
```
  - Run the setup script

```
sudo ./setup.sh 
```
 
  - When prompted, select ***Raspberry_Pi_v2*** by entering **7**.
 
  - Run the flashing command
 
```
sudo ./install.sh
```

### **Avermedia** (NX)

*Before proceeding, ensure you have the following:**

   - Jetson NX device
   - Avermedia EN715 board
   - USB cable for putting the device into recovery mod
   - Require Host PC Ubuntu 18.04 or Ubuntu 20.04

**Step 1: Download the BSP File**

Download the required BSP (Board Support Package) file for the Avermedia EN715 board from the following link :

[Download BSP File](https://avermedia.sharepoint.com/:u:/s/AVer.AI/EZVNof1ngB1AjENIYrIr5HEBwscp22NZcgk6IzAc1NVVuQ?e=O5TVlm)

**Step 2: Extract the BSP File**

Once the BSP file has been downloaded, open a terminal on your host machine and navigate to the directory where the file is located.

Run the following command to extract the BSP file:

```
sudo tar zxf EN715-NX-R1.0.22.4.6.tar.gz
```
**Step 3: Put Jetson NX into Recovery Mode**

To flash the BSP file onto the Jetson NX, you need to put the device into recovery mode.

**Steps to enter Recovery Mode:**

  - Connect the Jetson NX to your host PC using a micro-USB cable.
  - Press and hold the Recovery button. 
  - While holding the Recovery button, press the Power button.
  - Release the Recovery button.

**Step 4: Run Flashing Commands**

  - Navigate to the directory

```
cd JetPack_4.6_Linux_JETSON_XAVIER_NX_TARGETS/Linux_for_Tegra
```
  - Run the setup script

```
sudo ./setup.sh 
```
 
  - When prompted, select ***Raspberry_Pi_v2*** by entering **7**.
 
  - Run the flashing command
 
```
sudo ./install.sh
```
### **Avermedia** (TX2NX)

*Before proceeding, ensure you have the following:**

   - Jetson TX2NX device
   - Avermedia EN715 board
   - USB cable for putting the device into recovery mod
   - Require Host PC Ubuntu 18.04 or Ubuntu 20.04

**Step 1: Download the BSP File**

Download the required BSP (Board Support Package) file for the Avermedia EN715 board from the following link :

[Download BSP File](https://s3.us-west-2.amazonaws.com/storage.avermedia.com/web_release_www/EN715/BSP/BSP-TX2+NX/EN715-TX2-NX-R1.0.4.4.6.tar.gz)

**Step 2: Extract the BSP File**

Once the BSP file has been downloaded, open a terminal on your host machine and navigate to the directory where the file is located.

Run the following command to extract the BSP file:

```
sudo tar zxf EN715-TX2-NX-R1.0.4.4.6.tar.gz
```
**Step 3: Put Jetson NX into Recovery Mode**

To flash the BSP file onto the Jetson TX2NX, you need to put the device into recovery mode.

**Steps to enter Recovery Mode:**

  - Connect the Jetson TX2NX to your host PC using a micro-USB cable.
  - Press and hold the Recovery button. 
  - While holding the Recovery button, press the Power button.
  - Release the Recovery button.

**Step 4: Run Flashing Commands**

  - Navigate to the directory

```
cd JetPack_4.6_Linux_JETSON_TX2_TARGETS/Linux_for_Tegra
```
  - Run the setup script

```
sudo ./setup.sh 
```
 
  - When prompted, select ***Raspberry_Pi_v2*** by entering **7**.
 
  - Run the flashing command
 
```
sudo ./install.sh
```

### **Eagletech-101**

**Preloaded OS Information**
  
  - **OS:** Preloaded with BSP
  - **Username:** ***nvidia***
  - **Password:** ***nvidia***

**Prerequisites**

  - Eagle-101 with Jetson Nano Module
  - Require Host PC Ubuntu 18.04

**Step 1: Download Required Files**

Download the following two files from the [NVIDIA Developer Portal](https://developer.nvidia.com/embedded/linux-tegra-r3272)

 - Jetson-210_Linux_R32.7.2_aarch64.tbz2
 - Tegra_Linux_Sample-Root-Filesystem_R32.7.2_aarch64.tbz2

 **Step 2: Decompress Image File on Host PC**

  - Open a terminal on your host PC (Ubuntu 18.04).
  - Decompress the Jetson Linux file:
```
tar xf jetson-210_Linux_R32.7.2_aarch64.tbz2
```
  - Navigate to the root filesystem directory:
```
cd Linux_for_Tegra/rootfs/
```
  - Decompress the root filesystem into the ***rootfs/*** directory:
```
sudo tar xpf /path/to/Tegra_Linux_Sample-Root-Filesystem_R32.7.2_aarch64.tbz2
```
- Replace ***/path/to/*** with the actual path to the downloaded file.

- Move back to the ***Linux_for_Tegra/*** directory:
```
cd ..
```
- Apply Binaries
```
sudo ./apply_binaries.sh
```

**Step 3: Copy Device Tree File**

[Download dtb File](https://drive.google.com/file/d/1bXZB38e7l73AnbYmQjp5-Xd215msaowh/view?usp=sharing)

Copy the necessary device tree file to the appropriate directory:

```
cp tegra210-p3448-0002-p3449-0000-b00.dtb Linux_for_Tegra/kernel/dtb/
```
**Step 4: Flash Image and Boot the Device**

- Put the Jetson Nano into Force Recovery Mode:
    - On the Eagle-101 board, short the 3-pin (FC REC) and 4-pin (GND)
    - Connect the Micro USB to your host PC.
- Run the flash command in the ***Linux_for_Tegra/*** directory:

```
sudo ./flash.sh jetson-nano-emmc mmcblk0p1
```

### **Developer-Kit**

**Hardware Setup**

- Jetson Nano Developer Kit: Comes with the board, heat sink, and ports pre-mounted.
- MicroSD Card (minimum 32 GB recommended): For OS and application storage.
- 5V/4A Power Supply: Required for powering the board. Optionally, you can use micro-USB power for low-power projects.
- HDMI or DisplayPort Monitor: For display output.
- USB Keyboard and Mouse: For input.

**Flashing the OS**

 - Download, install, and launch [Etcher](https://etcher.balena.io/)

 - Download the [Jetson Nano Developer Kit SD Card Image](https://developer.nvidia.com/jetson-nano-sd-card-image), and note where it was saved on the computer.
 
 - Click “Select image” and choose the zipped image file downloaded earlier.

 - Click “Flash!” Your OS may prompt for your username and password before it allows Etcher to proceed.

 - It will take Etcher 10-15 minutes to write and validate the image if your microSD card is connected via USB 3.0

 - After Etcher finishes, eject the SD Card using Files application

 - Physically remove microSD card from the computer.

 **3. First Boot Setup**

  - Insert the microSD card into the Jetson Nano.

  - Power on the Jetson Nano by plugging in the power supply.
  
  - The system will boot into the NVIDIA JetPack OS, which is based on Ubuntu 18.04.

  - Follow the on-screen instructions to set up the system, including:

     - Username and password creation (default for tutorials: ***nvidia/nvidia***).
      - Setting up network access (Wi-Fi via USB dongle or Ethernet).

### **Tacodi**

**Prerequisites**

 - Host PC: Ubuntu 18.04
 - NVIDIA SDK Manager: Installed on the host PC
 - USB-to-USB Cable: To connect the Tacodi board to the host PC
 - JetPack 4.6.5: Downloaded and installed via SDK Manager

**Step 1: Install NVIDIA SDK Manager**
 
 -  Download the NVIDIA SDK Manager from the official [NVIDIA Developer website](https://developer.nvidia.com/sdk-manager)
 
 - Open a terminal and install the SDK Manager:
```
sudo apt install ./sdkmanager_*.deb
``` 
 - Replace **sdkmanager_*.deb** with the actual filename of the SDK Manager installer.

 - Launch the SDK Manager:

**Step 2: Download JetPack**

 - Open the SDK Manager and log in using your NVIDIA Developer account.
 - Under JetPack in the SDK Manager, select JetPack 4.6 from the available options.
 - Choose the target hardware as Jetson Nano .
 - Click Download and Install to download the necessary JetPack components and flash tools.

**Step 3: Connect the Tacodi Board**

 - Connect the Tacodi board to your host PC using a USB-to-USB cable.
 - Connect the jumper to put board into force recovery mode
 - Power on the Tacodi board.

**Step 4: Flash the Device**

 - In the SDK Manager, navigate to the Flash section.
 - Select your device from the list of connected devices.
 - Click Flash to begin the process
 - Enter the host system password 
 - Enter the Jetson username and password which you want to set (By default is ***nvidia/nvidia***)  

### **OS Transfer**

When flashing the Jetson SOM (System on Module), the operating system is initially installed on the eMMC. If you need to transfer the OS to an SSD or SD card, follow these steps

**Format the SSD or sd card**

```
sudo mkfs -t ext4 /dev/nvme0n1
sudo fdisk /dev/nvme0n1
sudo mkfs -t ext4 /dev/nvme0n1p1
```

**Download and Extract Required Files**

[Download](https://drive.google.com/file/d/16R8RoCx-6oYDGRgITnLtxrTqIMEmVE_h/view?usp=sharing) the provided ZIP file. After extracting it, you will find two important shell scripts:

 - ```copy-rootfs-ssd.sh```
 - ```setup-service.sh```

**Run the Scripts**

 - Run the copy-rootfs-ssd.sh script to copy the root filesystem to the SSD or SD card.

 - After that, run the setup-service.sh script to configure the necessary services for booting from the SSD or SD card.

**Reboot Device**

Once the scripts have been executed successfully, restart the system.

**Verify the Transfer**

After rebooting, run the following command to check if the operating system is now running from the SSD or SD card:

```
df -h
```

## **dGPU**

### **Ubuntu 20.04**

**Dual Boot Setup: Installing Ubuntu 20.04 Alongside Windows**

**Prerequisites**

- USB Drive (8 GB or larger): To create a bootable Ubuntu 20.04 installation media.
- Ubuntu 20.04 ISO File: Download the [Ubuntu 20.04 LTS ISO](https://releases.ubuntu.com/focal/ubuntu-20.04.6-desktop-amd64.iso).
- [Rufus](https://github.com/pbatard/rufus/releases/download/v4.5/rufus-4.5.exe) : For creating a bootable USB drive.

**Step 1: Create a Bootable USB**

- Download and install Rufus 
- Insert the USB drive into your system and open Rufus:
    - Select your USB drive.
    - Choose the downloaded Ubuntu 20.04 ISO as the image.
    - Ensure Partition Scheme is set to GPT and Target System to UEFI.
- Click Start and wait for the bootable USB to be created.

**Step 2: Prepare Windows for Dual Boot**

- Free Up Disk Space for Ubuntu
  - Go to Disk Management
  - Right-click on your main Windows partition (usually ***C:***) and select Shrink Volume.
  - Shrink the partition by the amount of space you want to allocate for Ubuntu (minimum 25 GB recommended)

**Step 3: Boot from the USB Drive**

- Reboot your system and enter the **BIOS/UEFI** settings by pressing a specific key (usually **F2**, **F10**, **DEL**, or **Esc**) during startup.
- Disable the **Secure boot** 
- Change the boot order to boot from the **USB drive**.
- Save and exit BIOS/UEFI settings. 

The system will now boot from the Ubuntu installation USB.

**Step 4: Install Ubuntu 20.04**

- Once the system boots from the USB, you will be prompted with the **Ubuntu installation screen**. Select **Install Ubuntu** to begin the installation process.

**During Installation**

 - **Select Your Language** and click **Continue**.

- On the **Keyboard Layout** screen, select your preferred layout and continue.

- **Updates and Software**: Choose whether to install third-party software for graphics, Wi-Fi hardware, and additional media formats.

- In the **Installation Type** screen, select **Install Ubuntu alongside Windows Boot Manager** (this option should appear if Windows is detected).

    - If this option doesn’t appear, choose **Something else** and manually allocate partitions (refer to the advanced guide below).

- Allocate Space for Ubuntu:

    - Allocate the free space you created earlier for Ubuntu installation.
    - Ensure you create at least:
        - A root partition **(/)** with ext4 file system (25 GB+ recommended).

- **Time Zone**: Select your location for the correct time zone and click **Continue**
- **Create User Account**: Enter your name, computer name, username, and password.
- Click **Install Now** to begin the installation. Confirm the partition changes when prompted

**Step 5: Post-Installation Setup**

- After installation completes, remove the USB drive and restart the computer.

- The **GRUB Bootloader** menu will appear at startup, allowing you to choose between **Ubuntu** and **Windows**.


### **Ubuntu 22.04**

**Dual Boot Setup: Installing Ubuntu 22.04 Alongside Windows**

**Prerequisites**

- USB Drive (8 GB or larger): To create a bootable Ubuntu 22.04 installation media.
- Ubuntu 22.04 ISO File: Download the [Ubuntu 22.04 LTS ISO](https://releases.ubuntu.com/jammy/ubuntu-22.04.5-desktop-amd64.iso).
- [Rufus](https://github.com/pbatard/rufus/releases/download/v4.5/rufus-4.5.exe) : For creating a bootable USB drive.

**Step 1: Create a Bootable USB**

- Download and install Rufus 
- Insert the USB drive into your system and open Rufus:
    - Select your USB drive.
    - Choose the downloaded Ubuntu 22.04 ISO as the image.
    - Ensure Partition Scheme is set to GPT and Target System to UEFI.
- Click Start and wait for the bootable USB to be created.

**Step 2: Prepare Windows for Dual Boot**

- Free Up Disk Space for Ubuntu
  - Go to Disk Management
  - Right-click on your main Windows partition (usually ***C:***) and select Shrink Volume.
  - Shrink the partition by the amount of space you want to allocate for Ubuntu (minimum 25 GB recommended)

**Step 3: Boot from the USB Drive**

- Reboot your system and enter the **BIOS/UEFI** settings by pressing a specific key (usually **F2**, **F10**, **DEL**, or **Esc**) during startup.
- Disable the **Secure boot** 
- Change the boot order to boot from the **USB drive**.
- Save and exit BIOS/UEFI settings. 

The system will now boot from the Ubuntu installation USB.

**Step 4: Install Ubuntu 22.04**

- Once the system boots from the USB, you will be prompted with the **Ubuntu installation screen**. Select **Install Ubuntu** to begin the installation process.

**During Installation**

 - **Select Your Language** and click **Continue**.

- On the **Keyboard Layout** screen, select your preferred layout and continue.

- **Updates and Software**: Choose whether to install third-party software for graphics, Wi-Fi hardware, and additional media formats.

- In the **Installation Type** screen, select **Install Ubuntu alongside Windows Boot Manager** (this option should appear if Windows is detected).

    - If this option doesn’t appear, choose **Something else** and manually allocate partitions (refer to the advanced guide below).

- Allocate Space for Ubuntu:

    - Allocate the free space you created earlier for Ubuntu installation.
    - Ensure you create at least:
        - A root partition **(/)** with ext4 file system (25 GB+ recommended).

- **Time Zone**: Select your location for the correct time zone and click **Continue**
- **Create User Account**: Enter your name, computer name, username, and password.
- Click **Install Now** to begin the installation. Confirm the partition changes when prompted

**Step 5: Post-Installation Setup**

- After installation completes, remove the USB drive and restart the computer.

- The **GRUB Bootloader** menu will appear at startup, allowing you to choose between **Ubuntu** and **Windows**.