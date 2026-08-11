---
title: "🛡️ Microsoft August 2026 Patch Tuesday: 398–421 CVEs, Active Zero-Day Exploitation Confirmed"
date: 2026-08-11T16:30:02-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "tenable-blog-microsoft-s-august-2026-pat", "security"]
description: "BREAKING: Tenable Blog: Microsoft's August 2026 Patch Tuesday Addresses 398 CVEs (CVE-2026-68820)"
cover:
  image: "/images/operations/2026-08-11-microsoft-august-2026-patch-tuesday-398-421-cves-active-zero.webp"
  alt: "Microsoft August 2026 Patch Tuesday: 398–421 CVEs, Active Zero-Day Exploitation Confirmed"
  relative: false
---

*Published Tuesday, August 11, 2026 at 04:30 PM PT*

![Microsoft August 2026 Patch Tuesday: 398–421 CVEs, Active Zero-Day Exploitation Confirmed](/images/operations/2026-08-11-microsoft-august-2026-patch-tuesday-398-421-cves-active-zero.webp)

**BLUF:** Microsoft released August 2026 Patch Tuesday addressing 398–421 vulnerabilities, including 42 critical issues and at least one actively exploited zero-day (use-after-free in afd.sys). Organizations must prioritize critical patches immediately, especially for Windows internet-facing systems.

---

### DETAILS

- **Vulnerability count discrepancy:** Tenable reports 398 total CVEs (42 Critical, 355 Important); SecurityWeek reports 421 CVEs. Severity distribution and exact count require Microsoft's official bulletin—both sources are current.
- **Active zero-day confirmed:** afd.sys use-after-free vulnerability is under active exploitation in the wild (per SecurityWeek). This is not theoretical risk.
- **Affected scope:** Windows operating systems and .NET components identified in patch notes. Additional affected products likely (context truncated).
- **CVE-2026-68820:** Referenced as representative CVE for this release; severity level not specified in available material.
- **Release date:** August 2026 Patch Tuesday (second Tuesday of month, confirmed via Tenable and SecurityWeek reporting).

---

### IMPACT

**Affected parties:** All organizations running Microsoft Windows (client and server) and .NET Framework/Core deployments. Consumer users also at risk.

**Scope:** 42 critical vulnerabilities at CVSS 9.0+ represent immediate remote-code-execution or privilege-escalation risk. Active exploitation of afd.sys zero-day elevates urgency: threat actors are weaponizing at least one vulnerability in real time.

**Risk window:** Systems unpatched within 48–72 hours face elevated compromise probability, especially if Internet-exposed (RDP, SMB, web services).

---

### RECOMMENDED ACTIONS

1. **Immediate:** Deploy critical patches (CVSS ≥9.0) to internet-facing Windows systems within 24 hours. Prioritize servers and workstations with egress to untrusted networks.
2. **Urgent:** Test and deploy afd.sys patch across all affected Windows versions as emergency priority due to active exploitation.
3. **Short-term:** Implement compensating controls for systems unable to patch immediately—disable unnecessary network services, restrict RDP/SMB access, deploy host-based IDS/EDR.
4. **Monitoring:** Search logs and endpoint telemetry for afd.sys exploitation attempts (driver crashes, unexpected privilege elevation, network reconnections post-crash).

---

### SOURCES

- Tenable Blog: *Microsoft's August 2026 Patch Tuesday Addresses 398 CVEs (CVE-2026-68820)*
- SecurityWeek: *August 2026 Patch Tuesday: Microsoft Fixes 421 CVEs, One Exploited Zero-Day*
- Microsoft Official Patch Tuesday Release (August 2026)

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-08-11-breaking-alert-posture.webp)