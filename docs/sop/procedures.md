---
title: SOP Procedures
description: Standard procedures for GPU installation, setup, and maintenance.
tags:
  - sop
  - procedures
  - installation
---

# SOP Procedures

## Environment Setup

### Designated Area

- Ensure the GPU and device are placed in a **clean, dust-free environment**.
- If such an environment is unavailable, install a **rack system**.

### Rack Requirements

| Device Type | Rack Size |
|-------------|-----------|
| Jetson Devices | 2U rack |
| RTX GPUs | 12U rack |

Racks must be **water-resistant and dust-proof**.

### Power Requirements

| Device Type | Socket Required |
|-------------|----------------|
| Jetson Devices | 5 Amp socket |
| RTX GPUs | 16 Amp socket |

---

## GPU Installation

### Step 1 — Power Down and Open Case

1. Shut down the computer and **unplug it** from the wall.
2. Press the power button for a few seconds to **discharge remaining electricity**.
3. Open the case by unscrewing or releasing the side panel.

### Step 2 — Identify PCIe Slot

- Locate the **primary PCIe x16 slot** — usually the top slot closest to the CPU.

### Step 3 — Prepare the Case

- Remove the **expansion slot covers** on the case corresponding to the GPU size.

### Step 4 — Insert the GPU

1. Line up the GPU's PCIe connector with the slot.
2. Gently press down until you hear a **click** from the retention clip.
3. Secure the GPU bracket to the case using screws.

### Step 5 — Connect Power Cables

- Connect **PCIe power cables** from the PSU to the GPU (6-pin, 8-pin, or both — depending on GPU model).
- Ensure all connections are firm and secure.

### Step 6 — Close and Power Up

1. Replace the side panel and screw it back into place.
2. Plug the system back in and power it on.

---

## Servicing & Maintenance

### Service Frequency

!!! warning "Mandatory service interval"
    All devices must be serviced **every 3 months** to ensure optimal performance and longevity.

### Servicing Steps

**1. Cabinet Cleaning**

- Use a soft fabric or tissue to clean the **cabinet exterior and interior**.
- Remove accumulated dust and dirt.

**2. Dust Removal**

- Use a **blower** to thoroughly clean the machine, including all visible and hidden areas.

**3. RAM Cleaning**

- Carefully remove the RAM modules.
- Inspect for **carbon deposits** or residue on the contacts.
- If carbon is present, clean contacts gently with a **rubber eraser**.

**4. GPU Cleaning**

- Carefully detach the GPU from the motherboard.
- Check GPU contacts for **carbon deposits**.
- Clean contacts gently with a **rubber eraser**.

**5. Fan Cleaning**

- Use a blower to clean fans thoroughly.
- Ensure no dust or debris remains.

**6. Fan Net Cleaning**

- Clean fan nets using a combination of **blower and soft fabric**.
- Ensure nets are free of blockages.

### Additional Checks

!!! note "During every service visit"
    - Inspect power sockets and connectors for wear and tear.
    - Ensure all screws and rack fittings are securely fastened.
    - Verify fans are running smoothly without noise or obstruction.

!!! danger "Handling precaution"
    Always handle components with care to avoid **electrostatic discharge (ESD)** damage.
    Ensure proper ventilation during installation and servicing to prevent overheating.
