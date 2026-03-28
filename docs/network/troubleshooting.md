---
title: Network Troubleshooting & VPN
description: VPN setup and network troubleshooting guides for secure remote access.
tags:
  - network
  - vpn
  - troubleshooting
---

# Network Troubleshooting & VPN

## VPN

### Tunnel VPN

A Tunnel VPN creates an encrypted channel between your device and a VPN server — all traffic is protected from interception and tampering.

=== "Key Features"

    | Feature | Description |
    |---------|-------------|
    | **Encryption** | End-to-end encrypted — unreadable if intercepted |
    | **Authentication** | Only authorized users can establish a tunnel |
    | **Data Integrity** | Ensures data is not tampered with in transit |

=== "Common Use Cases"

    | Use Case | Details |
    |----------|---------|
    | Public Wi-Fi security | Encrypts traffic on untrusted networks |
    | Remote access | Access internal AI infrastructure from outside |
    | Sensitive data protection | Shields GPU telemetry and model data in transit |

### Configuring FortiClient Tunnel VPN

**Step 1 — Download and Install FortiClient**

- Visit the [Fortinet website](https://www.fortinet.com/support/product-downloads).
- Download the version for your OS (Windows / macOS / Linux).
- Run the installer and follow on-screen instructions.

**Step 2 — Configure VPN Settings**

- Launch **FortiClient** → go to **Remote Access** tab.
- Click **Configure VPN** → choose **SSL-VPN** or **IPsec VPN**.

| Field | Value |
|-------|-------|
| Connection Name | e.g. `Work VPN` |
| Remote Gateway | IP or hostname of your VPN server |
| Port | Default, or as given by your network admin |
| Username / Password | Your VPN credentials |

- Click **Save**.

**Step 3 — Connect**

- In FortiClient → **Remote Access** → select your connection → click **Connect**.
- Enter credentials and complete any 2FA steps.

!!! success "Connected"
    FortiClient will show status as **Connected**.
    You can now access remote resources as if on-site.

**Step 4 — Disconnect**

- Return to FortiClient → click **Disconnect** on the Remote Access tab.

!!! tip "Best practice"
    Disconnect VPN when not in use to avoid unnecessary bandwidth usage
    and maintain optimal GPU node network performance.
