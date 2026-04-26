# Windows 11 (Pro)-Like Environment on macOS and Android

## Purpose

This document surveys every **legitimate** path to running or experiencing a Windows 11
Pro-like environment when the host device is a macOS machine or an Android device.
It covers virtual machines, cloud desktops, and UI-theme approaches, and it explicitly
documents the legal and technical constraints around Windows image distribution.

---

## 1. Legal and Distribution Constraints

Before choosing an approach, understand what you are and are not allowed to do:

| Action | Permitted? | Notes |
|---|---|---|
| Download a Windows 11 ISO from Microsoft | ✅ Yes | Free from [microsoft.com/software-download/windows11](https://www.microsoft.com/software-download/windows11) |
| Install Windows 11 in a VM for personal use | ✅ Yes | Requires a valid license key for activation |
| Share or redistribute a pre-installed Windows VM disk image | ❌ No | Violates Microsoft's EULA regardless of activation status |
| Publish a "pre-activated" or "pre-configured" Windows image to GitHub | ❌ No | Also violates GitHub's Terms of Service |
| Use Windows 365 / Azure Virtual Desktop | ✅ Yes | Microsoft hosts it; you connect remotely |

**Key takeaway:** You can freely build your own configured Windows 11 VM; you cannot
legally distribute one or download one from a third-party repository.

---

## 2. Option A — Virtual Machine on macOS (Full Windows 11)

Running a genuine Windows 11 VM locally on a Mac is the most capable option.
You get the full Win32 application stack, GPU-accelerated graphics, and offline access.

### 2a. Apple Silicon (M1 / M2 / M3 / M4) — Recommended: Parallels Desktop

Windows 11 ARM runs natively and is officially supported by Microsoft for Arm-based
hardware.

**What you need:**

1. **Parallels Desktop 19+** — <https://www.parallels.com/products/desktop/>  
   (commercial; free 14-day trial available)
2. **Windows 11 ARM ISO** — obtained automatically by Parallels during setup,
   or downloaded from [Microsoft's Insider / MSDN channels](https://www.microsoft.com/en-us/software-download/windowsinsiderpreviewARM64).
3. A **Windows 11 Pro product key** (purchase via [Microsoft Store](https://www.microsoft.com/en-us/store/b/windows)).

**Setup steps:**

```
1. Install Parallels Desktop.
2. Open Parallels → "+" → "Install Windows".
3. Parallels fetches the ARM ISO automatically — or point it at your own ISO.
4. Follow the on-screen wizard (RAM ≥ 8 GB, Disk ≥ 64 GB recommended).
5. Boot the VM and enter your product key during or after installation.
6. Install Parallels Tools inside the VM for clipboard sharing and folder mounting.
```

**Alternative for Apple Silicon (free/open-source): UTM**

- <https://mac.getutm.app/>  
- Uses QEMU under the hood; slower than Parallels but completely free.
- UTM gallery has a one-click Windows 11 ARM template:
  <https://mac.getutm.app/gallery/>

---

### 2b. Intel Mac — Options: VMware Fusion / VirtualBox

Both run x86-64 Windows 11 natively.

| Tool | Cost | URL |
|---|---|---|
| VMware Fusion Pro | Free for personal use (since 2024) | <https://www.vmware.com/products/desktop-hypervisor.html> |
| VirtualBox | Free, open-source | <https://www.virtualbox.org/> |

**Windows 11 ISO source (official):**  
<https://www.microsoft.com/software-download/windows11>

**Setup steps (VMware Fusion example):**

```
1. Download and install VMware Fusion.
2. File → New → drag your Windows 11 ISO into the dialog.
3. Choose "UEFI" firmware and enable TPM (required by Windows 11).
4. Allocate ≥ 4 GB RAM and ≥ 64 GB disk.
5. Complete installation; activate with your product key.
```

> **TPM workaround on older hardware:** Windows 11 requires TPM 2.0.
> VMware Fusion can expose a virtual TPM. In VirtualBox you may need to apply
> the registry bypass documented by Microsoft for unsupported hardware:
> <https://support.microsoft.com/en-us/windows/ways-to-install-windows-11-e0edbbfb-cfc5-4011-868b-2ce77ac7c70e>

---

## 3. Option B — Cloud Windows 11 (Access from macOS or Android)

If you do not want to run Windows locally, or you are on an Android device,
a cloud-hosted Windows desktop is the most practical path.

### 3a. Windows 365 Cloud PC (Microsoft)

- **What it is:** A full Windows 11 Pro desktop hosted in Microsoft Azure;
  you stream it via a browser or the Remote Desktop app.
- **Supported clients:** macOS, Android, iOS, Windows, web browser.
- **Cost:** Subscription starting at ~$20–$41 USD/month depending on vCPU/RAM.
- **URL:** <https://www.microsoft.com/en-us/windows-365>

**Access from macOS:**

```
1. Subscribe to Windows 365 at windows365.microsoft.com.
2. Open a browser and go to windows365.microsoft.com — click "Open in browser".
   OR install Microsoft Remote Desktop: https://aka.ms/rdmac
3. Sign in with your Microsoft / Entra ID account.
```

**Access from Android:**

```
1. Install "Microsoft Remote Desktop" from Google Play:
   https://play.google.com/store/apps/details?id=com.microsoft.rdc.androidx
2. Add a "Windows 365" workspace with your Microsoft account.
3. Connect — you get a full Windows 11 desktop with touch/keyboard support.
```

---

### 3b. Azure Virtual Desktop (AVD)

- More configurable than Windows 365; suited for power users and developers.
- Requires an Azure subscription.
- **URL:** <https://azure.microsoft.com/en-us/products/virtual-desktop>
- Same Remote Desktop apps as Windows 365 are used to connect.

---

### 3c. Third-party cloud Windows providers

Several providers offer pre-provisioned Windows 11 VMs billed by the hour:

| Provider | URL | Notes |
|---|---|---|
| Shadow PC | <https://shadow.tech> | Consumer-focused; GPU included |
| Paperspace | <https://www.paperspace.com> | Developer-friendly; hourly billing |
| Boosteroid | <https://boosteroid.com> | Gaming-oriented cloud Windows |

---

## 4. Option C — Windows-Like UI Themes (No Windows License Required)

If the goal is **UI familiarity rather than running Windows apps**, desktop
themes that replicate the Windows 11 look are available for Linux (and
indirectly for macOS via customisation tools).

> **Note:** These are cosmetic only. They do not run `.exe` files or
> Windows-specific services.

### macOS — Windhawk + custom themes

- **Windhawk** is a Windows mod manager; there is no direct macOS equivalent
  for system-wide theming.
- The closest macOS approach is using a custom dock replacement and icon pack:
  - **uBar** (dock replacement): <https://brawsoftware.com/products/ubar>
  - **Windows 11 icon pack for macOS** (community): search `windows 11 icons macos`
    on sites like [macosicons.com](https://macosicons.com).

### Android — Windows 11 Launchers

Several Android launchers replicate the Windows 11 Start menu and taskbar:

| App | Google Play Link | Notes |
|---|---|---|
| Computer Launcher | <https://play.google.com/store/apps/details?id=com.computer.launcher> | Windows 11-style home screen |
| Win 11 Launcher | Search Google Play for "Win 11 Launcher" | Multiple variants available |

---

## 5. Automation and Provisioning Scripts (Advanced)

For users who need a **repeatable, scripted Windows 11 VM build** (e.g., a
developer environment reset to a known state), the following open-source
tools can automate the installation:

| Tool | URL | What it does |
|---|---|---|
| **Packer** (HashiCorp) | <https://developer.hashicorp.com/packer> | Builds VM disk images automatically from an ISO |
| **Vagrant** | <https://www.vagrantup.com> | Manages and provisions VMs via a `Vagrantfile` |
| **Ansible** | <https://www.ansible.com> | Configures a running Windows VM over WinRM |
| **Chocolatey** | <https://chocolatey.org> | Windows package manager for automated app installs |
| **WinGet** | <https://github.com/microsoft/winget-cli> | Microsoft's official Windows package manager |

**Example Packer + Ansible workflow:**

```
1. Write a Packer template that:
   - Points at your locally downloaded Windows 11 ISO
   - Boots the VM, applies an autounattend.xml for unattended install
   - Waits for WinRM to become available
2. Write an Ansible playbook that installs your required software via Chocolatey.
3. Run: packer build windows11.pkr.hcl
4. The output is a fully configured VM disk image — for your own use only.
```

> ⚠️ The resulting VM image contains Windows and must **not** be redistributed.

---

## 6. Summary Decision Table

| Goal | Host OS | Recommended Path |
|---|---|---|
| Run Windows apps natively | macOS (Apple Silicon) | Parallels Desktop + Windows 11 ARM |
| Run Windows apps natively | macOS (Intel) | VMware Fusion (free) + Windows 11 x64 |
| Run Windows apps natively | macOS (any, free/OSS) | UTM |
| Access Windows from anywhere | macOS or Android | Windows 365 Cloud PC |
| GPU-accelerated cloud Windows | macOS or Android | Shadow PC |
| Windows 11 UI feel only | Android | Computer Launcher |
| Scripted/repeatable dev environment | macOS | Packer + Vagrant + Ansible |

---

## 7. References and Further Reading

- Microsoft Windows 11 download page: <https://www.microsoft.com/software-download/windows11>
- Microsoft Windows 11 on Arm FAQ: <https://support.microsoft.com/en-us/windows/windows-11-on-arm-faq>
- Parallels Desktop documentation: <https://kb.parallels.com/en/125375>
- UTM documentation: <https://docs.getutm.app>
- VMware Fusion user guide: <https://docs.vmware.com/en/VMware-Fusion/>
- VirtualBox manual: <https://www.virtualbox.org/manual/>
- Windows 365 documentation: <https://learn.microsoft.com/en-us/windows-365/>
- Microsoft Remote Desktop for Android: <https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-android>
- HashiCorp Packer Windows examples: <https://github.com/StefanScherer/packer-windows>
- WinGet CLI repository: <https://github.com/microsoft/winget-cli>
