---
title: Home
description: AI Hardware Documentation — Networking, GPU, SDK, Deployment, Monitoring, SOP, FAQ
hide:
  - navigation
  - toc
---

<div class="hero-wrap">
<div class="hero-inner">

<div class="hero-chip">AI Hardware Documentation</div>

<h1 class="hero-title">Engineering Intelligence,<br>At Silicon Speed</h1>

<p class="hero-sub">
  A unified reference for building, deploying, and operating AI hardware infrastructure —
  from bare-metal GPU racks to production-grade SDK integrations.
</p>

<div class="hero-actions">
  <a href="network/" class="btn-primary">Get Started →</a>
  <a href="https://github.com/ansari-asim" class="btn-ghost">GitHub ↗</a>
  <a href="https://ansari-asim.github.io/asim-portfolio/" class="btn-ghost">Portfolio ↗</a>
</div>

<div class="hero-stats">
  <div class="stat-item">
    <span class="stat-num">7</span>
    <span class="stat-label">Sections</span>
  </div>
  <div class="stat-item">
    <span class="stat-num">GPU</span>
    <span class="stat-label">Compute</span>
  </div>
  <div class="stat-item">
    <span class="stat-num">SDK</span>
    <span class="stat-label">Integration</span>
  </div>
  <div class="stat-item">
    <span class="stat-num">VPN</span>
    <span class="stat-label">Secured</span>
  </div>
</div>

</div>
</div>

<div class="author-wrap">
  <div class="author-avi">
    <img src="assets/profile.jpg" alt="Asim Ansari profile photo">
  </div>
  <div class="author-body">
    <span class="author-name">Asim Ansari</span>
    <div class="author-role">AI Infrastructure Engineer · Hardware Systems · SDK Integration</div>
    <div class="author-links">
      <a href="https://github.com/ansari-asim" class="author-link gh">⌥ GitHub</a>
      <a href="https://ansari-asim.github.io/asim-portfolio/" class="author-link pf">◈ Portfolio</a>
      <a href="https://linkedin.com/in/asim-ansari-19b383151" class="author-link li">in LinkedIn</a>
    </div>
  </div>
</div>

<p class="nav-section-title">Documentation</p>

<div class="cards-grid">

<a href="network/" class="doc-card">
  <div class="card-icon">🌐</div>
  <div class="card-title">Network</div>
  <div class="card-desc">Static IP setup, dual-network config, CCTV integration, and FortiClient VPN tunneling.</div>
  <div class="card-cta">Explore →</div>
</a>

<a href="GPU/" class="doc-card">
  <div class="card-icon">🖥️</div>
  <div class="card-title">GPU</div>
  <div class="card-desc">Jetson flashing, BSP setup, dGPU dual-boot, Ubuntu installation, and OS transfer to SSD.</div>
  <div class="card-cta">Explore →</div>
</a>

<a href="sdk/" class="doc-card">
  <div class="card-icon">🧰</div>
  <div class="card-title">SDK</div>
  <div class="card-desc">DeepStream 6–8, CUDA 11/12, TensorRT, Python bindings, and Docker setup.</div>
  <div class="card-cta">Explore →</div>
</a>

<a href="deployment/" class="doc-card">
  <div class="card-icon">🚀</div>
  <div class="card-title">Deployment</div>
  <div class="card-desc">daddy-ai deploy master, jtop monitoring, and all system dependency installation.</div>
  <div class="card-cta">Explore →</div>
</a>

<a href="monitoring/" class="doc-card">
  <div class="card-icon">📊</div>
  <div class="card-title">Monitoring</div>
  <div class="card-desc">Network, temperature, disk, cache, and SSD health monitoring with rotating log files.</div>
  <div class="card-cta">Explore →</div>
</a>

<a href="SOP/" class="doc-card">
  <div class="card-icon">📋</div>
  <div class="card-title">SOP</div>
  <div class="card-desc">GPU installation procedures, rack requirements, servicing schedule, and maintenance SOPs.</div>
  <div class="card-cta">Explore →</div>
</a>

<a href="FAQ/" class="doc-card">
  <div class="card-icon">❓</div>
  <div class="card-title">FAQ</div>
  <div class="card-desc">Camera config, bandwidth requirements, GPU connectivity, and security certifications.</div>
  <div class="card-cta">Explore →</div>
</a>

</div>

---

## Stack Overview

=== "Infrastructure"

    | Layer | Technology |
    |-------|-----------|
    | Networking | Ethernet / InfiniBand / DVR |
    | Compute | NVIDIA Jetson / RTX GPU |
    | OS | Ubuntu 20.04 / 22.04 / 24.04 |
    | Container | Docker + NVIDIA Container Toolkit |

=== "Software"

    | Layer | Technology |
    |-------|-----------|
    | Inference | DeepStream 6.0 / 6.2 / 7.0 / 8.0 |
    | CUDA | 11.8 / 12.2 / 12.8 |
    | TensorRT | 8.5 / 8.6 / 10.9 |
    | Monitoring | psutil · jtop · smartctl |

=== "Operations"

    | Process | Tooling |
    |---------|---------|
    | Deployment | daddy-ai DeployMaster |
    | Log Management | RotatingFileHandler |
    | VPN | FortiClient SSL/IPsec |
    | Maintenance | 3-month SOP cycle |

---

!!! tip "New here? Start with this path"
    **[Network](network/)** → connectivity &nbsp;·&nbsp;
    **[GPU](GPU/)** → flash & install &nbsp;·&nbsp;
    **[SDK](sdk/)** → DeepStream & CUDA &nbsp;·&nbsp;
    **[Deployment](deployment/)** → run in production