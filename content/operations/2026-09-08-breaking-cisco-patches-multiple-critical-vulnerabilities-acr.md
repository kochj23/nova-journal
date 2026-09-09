---
title: "🛡️ BREAKING: Cisco Patches Multiple Critical Vulnerabilities Across Product Line — Some Actively Exploited"
date: 2026-09-08T23:24:14-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "cso-online-cisco-bundles-fixes-for-multi", "security"]
description: "BREAKING: CSO Online: Cisco bundles fixes for multiple vulnerabilities, some critical, into one patch"
cover:
  image: "/images/operations/2026-09-08-breaking-cisco-patches-multiple-critical-vulnerabilities-acr.webp"
  alt: "BREAKING: Cisco Patches Multiple Critical Vulnerabilities Across Product Line — Some Actively Exploited"
  relative: false
---

*Published Tuesday, September 08, 2026 at 11:24 PM PT*

![BREAKING: Cisco Patches Multiple Critical Vulnerabilities Across Product Line — Some Actively Exploited](/images/operations/2026-09-08-breaking-cisco-patches-multiple-critical-vulnerabilities-acr.webp)

**BLUF:** Cisco released patches for multiple critical vulnerabilities affecting IOS XR, Unified CM, SD-WAN Manager, Crosswork, Secure Workload, IOS XE, FMC, and ClamAV. At least two products (Unified CM, SD-WAN Manager) are under active exploitation in the wild. Five vulnerabilities have maximum CVSS 10.0 ratings. Organizations running any Cisco infrastructure, communications, or security products should prioritize patching immediately.

**DETAILS:**
- Cisco bundled fixes for more than a half-dozen internally-discovered vulnerabilities, including critical-severity flaws affecting network operating systems (IOS XR, IOS XE), unified communications (Unified CM), SD-WAN management, network automation (Crosswork), microsegmentation (Secure Workload), firewall management (FMC), and the ClamAV antivirus engine
- Confirmed active exploitation: Unified CM vulnerability **CVE-2026-20230** and SD-WAN Manager; proof-of-concept code is publicly available for Unified CM and ClamAV
- Five Crosswork and Secure Workload vulnerabilities carry the maximum severity CVSS 10.0 score; additional critical flaws affect remote code execution, denial-of-service, and authentication bypass vectors
- Cisco flagged these flaws during internal testing as part of regular software engineering review; patches are now available

**IMPACT:**
- **Network operators:** IOS XR and IOS XE patches required; any equipment running affected code is at risk of remote compromise
- **Communications:** Unified CM deployments already experiencing active exploitation; organizations with public-facing Unified CM instances are highest priority
- **SD-WAN:** Deployments using SD-WAN Manager are actively targeted; patch critical for organizations using Cisco SD-WAN
- **Enterprise security:** Crosswork (network operations), Secure Workload (microsegmentation), and FMC (firewall management) vulnerabilities expose orchestration, policy enforcement, and perimeter controls
- **Endpoint security:** ClamAV integration across endpoints is at risk

**RECOMMENDED ACTIONS:**
- **Immediate (24–48 hrs):** Prioritize patches for Unified CM and SD-WAN Manager products; verify if your infrastructure is directly exposed
- **High Priority (72 hrs):** Patch IOS XR and IOS XE devices; Crosswork, Secure Workload, and FMC instances
- **Monitor:** Threat intelligence feeds for exploitation activity; apply ClamAV updates across deployments
- **Incident response:** Check firewall/proxy logs and netflow for suspicious traffic to Cisco management interfaces and unified communications systems

**SOURCES:**
- CSO Online: Cisco bundles fixes for multiple vulnerabilities, some critical, into one patch
- SecurityWeek: Cisco Patches Critical Crosswork, Secure Workload, SD-WAN, IOS XE, FMC; Active exploitation of Unified CM and SD-WAN Manager
- The Hacker News: Cisco Patches Nine Crosswork and Secure Workload Flaws (Five CVSS 10.0)
- Help Net Security / SecurityWeek: Cisco ClamAV high-severity vulnerabilities with public PoC

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-08-breaking-alert-posture.webp)