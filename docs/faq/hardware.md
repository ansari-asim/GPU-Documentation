---
title: FAQ Hardware Questions
description: Frequently asked questions about hardware compatibility and specifications.
tags:
  - faq
  - hardware
---

# FAQ — Hardware Questions

## GPU & Device Compatibility

**What is the standard lead time for GPU orders?**

The typical lead time is **2 weeks** from the date of the purchase order (PO).

---

## Camera Configuration

**What should be the ideal camera resolution?**

A 2MP camera is generally sufficient for most AI-based applications. Higher resolutions can improve detection accuracy and detail for demanding analytics tasks.

**What camera configurations are suitable for AI?**

Any camera with a resolution **above 2MP** is recommended for AI solutions — it provides the clarity and data density needed for accurate analysis.

**What types of cameras does your solution support?**

| Camera Type | Supported |
|-------------|-----------|
| Dome | ✅ |
| Bullet | ✅ |
| Unifocal | ✅ |
| Bifocal | ✅ |
| PTZ (Pan-Tilt-Zoom) | ✅ |

**What is the effective AI detection range?**

The solution is effective up to **75% of the camera's focal distance**.

---

## Networking & Connectivity

**How do you connect a GPU with an NVR/DVR or cameras?**

Both the GPU and NVR/DVR must be on the **same local network**, typically bridged via a **network switch**.

**Can cameras be accessed directly through an NVR or DVR?**

Yes — but a **network switch** is required to connect the GPU and the NVR/DVR together.

**Can an IP camera be directly connected to the GPU?**

Yes — IP cameras can connect directly to the GPU, but a **network switch** is needed for the connection.

---

## Bandwidth & Performance

**What is the minimum required internet bandwidth?**

| Cameras | Minimum Upload Speed |
|---------|---------------------|
| 5 cameras | 10 Mbps |
| Each additional camera | +0.35 Mbps |

Download speed should consistently be **10 Mbps or higher** for optimal performance.

**What are the camera bandwidth requirements for streaming?**

A bandwidth of **4 Mbps** is required to access a single camera when using **multi-stream mode**.

**Can all devices be connected wirelessly?**

!!! warning "Wired connections recommended"
    While wireless connections are possible, **wired connections are strongly recommended** due to enhanced security and better, more stable performance.
    Wireless connections may pose security risks and result in reduced throughput.
