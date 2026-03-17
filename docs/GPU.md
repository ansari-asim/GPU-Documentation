---
title: GPU
description: Jetson device flashing, dGPU Ubuntu dual-boot, and OS transfer guides.
tags:
  - gpu
  - jetson
  - cuda
  - ubuntu
  - flashing
---

# 🖥️ GPU

Complete guide for flashing Jetson devices with BSP packages, setting up dGPU Ubuntu environments, and transferring the OS to SSD/SD card.

---

## Jetson Device { #jetson }

### Avermedia — Nano { #avermedia-nano }

!!! info "Prerequisites"
    - Jetson Nano device
    - Avermedia EN715 board
    - USB cable (for recovery mode)
    - Host PC running Ubuntu 18.04 or 20.04

**Step 1 — Download the BSP File**

Download the BSP (Board Support Package) for the Avermedia EN715 Nano board:

[⬇ Download BSP File](https://s3.us-west-2.amazonaws.com/storage.avermedia.com/web_release_www/EN715/BSP/BSP-Nano/2021-12-20/EN715-R1.0.20.4.6.tar.gz){ .md-button }

**Step 2 — Extract the BSP File**

```bash
sudo tar xzvf EN715-R1.0.20.4.6.tar.gz
```

**Step 3 — Put Jetson Nano into Recovery Mode**

1. Connect the Jetson Nano to your host PC via micro-USB.
2. Press and hold the **Recovery** button.
3. While holding Recovery, press the **Power** button.
4. Release the Recovery button.

**Step 4 — Run Flashing Commands**

Navigate to the extracted directory:

```bash
cd JetPack_4.6_Linux_JETSON_NANO_TARGETS/Linux_for_Tegra
```

Run the setup script:

```bash
sudo ./setup.sh
```

!!! note "When prompted"
    Select ***Raspberry_Pi_v2*** by entering `7`.

Run the flash:

```bash
sudo ./install.sh
```

---

### Avermedia — NX { #avermedia-nx }

!!! info "Prerequisites"
    - Jetson NX device
    - Avermedia EN715 board
    - USB cable (for recovery mode)
    - Host PC running Ubuntu 18.04 or 20.04

**Step 1 — Download the BSP File**

[⬇ Download BSP File](https://avermedia.sharepoint.com/:u:/s/AVer.AI/EZVNof1ngB1AjENIYrIr5HEBwscp22NZcgk6IzAc1NVVuQ?e=O5TVlm){ .md-button }

**Step 2 — Extract the BSP File**

```bash
sudo tar zxf EN715-NX-R1.0.22.4.6.tar.gz
```

**Step 3 — Put Jetson NX into Recovery Mode**

1. Connect Jetson NX to your host PC via micro-USB.
2. Press and hold the **Recovery** button.
3. While holding Recovery, press the **Power** button.
4. Release the Recovery button.

**Step 4 — Run Flashing Commands**

```bash
cd JetPack_4.6_Linux_JETSON_XAVIER_NX_TARGETS/Linux_for_Tegra
```

```bash
sudo ./setup.sh
```

!!! note "When prompted"
    Select ***Raspberry_Pi_v2*** by entering `7`.

```bash
sudo ./install.sh
```

---

### Avermedia — TX2NX { #avermedia-tx2nx }

!!! info "Prerequisites"
    - Jetson TX2NX device
    - Avermedia EN715 board
    - USB cable (for recovery mode)
    - Host PC running Ubuntu 18.04 or 20.04

**Step 1 — Download the BSP File**

[⬇ Download BSP File](https://s3.us-west-2.amazonaws.com/storage.avermedia.com/web_release_www/EN715/BSP/BSP-TX2+NX/EN715-TX2-NX-R1.0.4.4.6.tar.gz){ .md-button }

**Step 2 — Extract the BSP File**

```bash
sudo tar zxf EN715-TX2-NX-R1.0.4.4.6.tar.gz
```

**Step 3 — Put Jetson TX2NX into Recovery Mode**

1. Connect Jetson TX2NX to your host PC via micro-USB.
2. Press and hold the **Recovery** button.
3. While holding Recovery, press the **Power** button.
4. Release the Recovery button.

**Step 4 — Run Flashing Commands**

```bash
cd JetPack_4.6_Linux_JETSON_TX2_TARGETS/Linux_for_Tegra
```

```bash
sudo ./setup.sh
```

!!! note "When prompted"
    Select ***Raspberry_Pi_v2*** by entering `7`.

```bash
sudo ./install.sh
```

---

### Eagletech-101 { #eagletech }

!!! info "Preloaded OS"
    | Field | Value |
    |-------|-------|
    | OS | Preloaded with BSP |
    | Username | `nvidia` |
    | Password | `nvidia` |

!!! info "Prerequisites"
    - Eagle-101 with Jetson Nano Module
    - Host PC running Ubuntu 18.04

**Step 1 — Download Required Files**

From the [NVIDIA Developer Portal](https://developer.nvidia.com/embedded/linux-tegra-r3272), download:

- `Jetson-210_Linux_R32.7.2_aarch64.tbz2`
- `Tegra_Linux_Sample-Root-Filesystem_R32.7.2_aarch64.tbz2`

**Step 2 — Decompress Image File on Host PC**

Decompress the Jetson Linux archive:

```bash
tar xf jetson-210_Linux_R32.7.2_aarch64.tbz2
```

Navigate to the rootfs directory:

```bash
cd Linux_for_Tegra/rootfs/
```

Decompress the root filesystem (replace `/path/to/` with actual path):

```bash
sudo tar xpf /path/to/Tegra_Linux_Sample-Root-Filesystem_R32.7.2_aarch64.tbz2
```

Return to the parent directory and apply binaries:

```bash
cd ..
sudo ./apply_binaries.sh
```

**Step 3 — Copy Device Tree File**

[⬇ Download DTB File](https://drive.google.com/file/d/1bXZB38e7l73AnbYmQjp5-Xd215msaowh/view?usp=sharing){ .md-button }

```bash
cp tegra210-p3448-0002-p3449-0000-b00.dtb \
   Linux_for_Tegra/kernel/dtb/
```

**Step 4 — Flash Image and Boot**

Put the Jetson Nano into Force Recovery Mode:

- On the Eagle-101 board, short the **3-pin (FC REC)** and **4-pin (GND)**.
- Connect the Micro USB to your host PC.

Flash the image from the `Linux_for_Tegra/` directory:

```bash
sudo ./flash.sh jetson-nano-emmc mmcblk0p1
```

---

### Developer Kit { #developer-kit }

!!! info "Hardware required"
    - Jetson Nano Developer Kit
    - MicroSD card (32 GB minimum)
    - 5V/4A power supply
    - HDMI or DisplayPort monitor
    - USB keyboard and mouse

**Step 1 — Flash the OS**

- Download and install [Etcher](https://etcher.balena.io/).
- Download the [Jetson Nano SD Card Image](https://developer.nvidia.com/jetson-nano-sd-card-image).
- In Etcher: **Select image** → choose the downloaded `.zip` → **Flash!**
- Wait 10–15 minutes for Etcher to write and validate.
- Eject the SD card when complete.

**Step 2 — First Boot Setup**

1. Insert the microSD card into the Jetson Nano.
2. Plug in the power supply to boot.
3. The system boots into NVIDIA JetPack OS (Ubuntu 18.04).
4. Follow on-screen instructions:
    - Create username and password (default for tutorials: `nvidia` / `nvidia`).
    - Configure network access via Ethernet or USB Wi-Fi dongle.

---

### Tacodi { #tacodi }

!!! info "Prerequisites"
    - Host PC: Ubuntu 18.04
    - NVIDIA SDK Manager installed
    - USB-to-USB cable
    - JetPack 4.6.5

**Step 1 — Install NVIDIA SDK Manager**

```bash
sudo apt install ./sdkmanager_*.deb
```

!!! note
    Replace `sdkmanager_*.deb` with the actual filename. Download from the [NVIDIA Developer website](https://developer.nvidia.com/sdk-manager).

**Step 2 — Download JetPack via SDK Manager**

1. Open SDK Manager and log in with your NVIDIA Developer account.
2. Under JetPack, select **JetPack 4.6**.
3. Choose target hardware: **Jetson Nano**.
4. Click **Download and Install**.

**Step 3 — Connect the Tacodi Board**

1. Connect Tacodi to host PC via USB-to-USB cable.
2. Connect the jumper to enable **force recovery mode**.
3. Power on the Tacodi board.

**Step 4 — Flash the Device**

1. In SDK Manager, go to the **Flash** section.
2. Select your device from the connected devices list.
3. Click **Flash**.
4. Enter your host system password when prompted.
5. Set the Jetson username and password (default: `nvidia` / `nvidia`).

---

### OS Transfer to SSD / SD Card { #os-transfer }

When flashing a Jetson SOM, the OS is initially on eMMC. Use these steps to transfer it to an SSD or SD card.

**Format the target drive**

```bash
sudo mkfs -t ext4 /dev/nvme0n1
sudo fdisk /dev/nvme0n1
sudo mkfs -t ext4 /dev/nvme0n1p1
```

**Download the transfer scripts**

[⬇ Download ZIP (scripts)](https://drive.google.com/file/d/16R8RoCx-6oYDGRgITnLtxrTqIMEmVE_h/view?usp=sharing){ .md-button }

Extract the ZIP — you will find two shell scripts:

- `copy-rootfs-ssd.sh`
- `setup-service.sh`

**Run the scripts**

1. Run `copy-rootfs-ssd.sh` to copy the root filesystem to the SSD/SD card.
2. Run `setup-service.sh` to configure boot services.

**Reboot and verify**

```bash
df -h
```

!!! success "Transfer confirmed"
    If the OS transferred successfully, you will see the SSD or SD card listed as the root filesystem mount point.

---

## dGPU { #dgpu }

### Ubuntu 20.04 — Dual Boot { #ubuntu-2004 }

!!! info "Prerequisites"
    - USB drive (8 GB or larger)
    - [Ubuntu 20.04 LTS ISO](https://releases.ubuntu.com/focal/ubuntu-20.04.6-desktop-amd64.iso)
    - [Rufus](https://github.com/pbatard/rufus/releases/download/v4.5/rufus-4.5.exe) (bootable USB tool)

**Step 1 — Create a Bootable USB**

- Open Rufus → select your USB drive.
- Choose the Ubuntu 20.04 ISO.
- Set **Partition Scheme** to `GPT` and **Target System** to `UEFI`.
- Click **Start**.

**Step 2 — Free Disk Space in Windows**

- Open **Disk Management**.
- Right-click your main Windows partition (`C:`) → **Shrink Volume**.
- Shrink by at least **25 GB** for Ubuntu.

**Step 3 — Boot from USB**

- Reboot → enter **BIOS/UEFI** (`F2`, `F10`, `DEL`, or `Esc`).
- **Disable Secure Boot**.
- Set boot order to boot from **USB drive**.
- Save and exit.

**Step 4 — Install Ubuntu 20.04**

During installation:

- Select **Install Ubuntu alongside Windows Boot Manager**.
- Allocate the free space for Ubuntu — create at minimum a root partition `/` with `ext4` (25 GB+).
- Set timezone, language, keyboard layout, and user account.
- Click **Install Now** and confirm partition changes.

**Step 5 — Post-Installation**

- Remove the USB drive and restart.
- The **GRUB bootloader** will appear, letting you choose between Ubuntu and Windows.

---

### Ubuntu 22.04 — Dual Boot { #ubuntu-2204 }

!!! info "Prerequisites"
    - USB drive (8 GB or larger)
    - [Ubuntu 22.04 LTS ISO](https://releases.ubuntu.com/jammy/ubuntu-22.04.5-desktop-amd64.iso)
    - [Rufus](https://github.com/pbatard/rufus/releases/download/v4.5/rufus-4.5.exe)

**Step 1 — Create a Bootable USB**

- Open Rufus → select your USB drive.
- Choose the Ubuntu 22.04 ISO.
- Set **Partition Scheme** to `GPT` and **Target System** to `UEFI`.
- Click **Start**.

**Step 2 — Free Disk Space in Windows**

- Open **Disk Management**.
- Right-click your main Windows partition (`C:`) → **Shrink Volume**.
- Shrink by at least **25 GB**.

**Step 3 — Boot from USB**

- Reboot → enter **BIOS/UEFI** (`F2`, `F10`, `DEL`, or `Esc`).
- **Disable Secure Boot**.
- Set boot order to boot from **USB drive**.
- Save and exit.

**Step 4 — Install Ubuntu 22.04**

- Select **Install Ubuntu alongside Windows Boot Manager**.
- Allocate the free space — root partition `/` with `ext4` (25 GB+).
- Set timezone, language, keyboard layout, and user account.
- Click **Install Now**.

**Step 5 — Post-Installation**

- Remove the USB drive and restart.
- **GRUB bootloader** will appear on startup — choose Ubuntu or Windows.