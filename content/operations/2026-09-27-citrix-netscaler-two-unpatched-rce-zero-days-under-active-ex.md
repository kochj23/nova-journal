---
title: "🛡️ **CITRIX NetScaler: Two Unpatched RCE Zero-Days Under Active Exploitation**"
date: 2026-09-27T11:53:10-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "bleepingcomputer-citrix-confirms-two-net", "security"]
description: "BREAKING: BleepingComputer: Citrix confirms two NetScaler RCE zero-days exploited in attacks"
cover:
  image: "/images/operations/2026-09-27-citrix-netscaler-two-unpatched-rce-zero-days-under-active-ex.webp"
  alt: "**CITRIX NetScaler: Two Unpatched RCE Zero-Days Under Active Exploitation**"
  relative: false
---

*Published Sunday, September 27, 2026 at 11:53 AM PT*

![**CITRIX NetScaler: Two Unpatched RCE Zero-Days Under Active Exploitation**](/images/operations/2026-09-27-citrix-netscaler-two-unpatched-rce-zero-days-under-active-ex.webp)

---

**BLUF:** Citrix has confirmed two remote code execution (RCE) zero-days in NetScaler are actively exploited in ongoing attacks. No patches are available. Organizations running affected NetScaler instances should assume compromise and implement network segmentation immediately.

**DETAILS:**

- Citrix officially confirmed two separate RCE zero-day flaws in NetScaler products are being exploited in the wild by threat actors.
- Both vulnerabilities remain unpatched as of publication; Citrix has not released remediation code.
- Attacks are confirmed active and ongoing—this is not theoretical or in-the-wild proof-of-concept stage.
- Multiple independent security research outlets (BleepingComputer, The Hacker News, Security Affairs) have independently corroborated the findings.
- The flaws permit unauthenticated or low-privilege remote code execution on vulnerable NetScaler appliances.

**IMPACT:**

- **Primary target:** Organizations relying on Citrix NetScaler for edge access control, load balancing, or VPN services.
- **Scope:** Any NetScaler deployment exposed to untrusted networks (internet-facing gateways, remote access controllers).
- **Severity:** Critical. RCE with no patch means defenders cannot eliminate the vulnerability short of removing/replacing the appliance.
- **Risk:** Lateral movement into internal networks post-compromise; data exfiltration; persistent backdoors.

**RECOMMENDED ACTIONS:**

1. **Immediate:** Identify all NetScaler appliances in your environment and network topology; isolate internet-facing instances if feasible.
2. **Urgent:** Implement detection signatures for exploitation attempts on NetScaler log streams; monitor for anomalous admin creation, authentication bypass, or unexpected code execution.
3. **Tactical:** Segment NetScaler administrative interfaces behind additional authentication layers; restrict outbound network access from affected appliances.
4. **Strategic:** Contact Citrix support for patch availability timeline; prepare contingency plan (failover, appliance replacement, network redesign).
5. **Investigation:** Check NetScaler logs, firewall logs, and endpoint telemetry for signs of compromise dating back to before this disclosure.

**SOURCES:**

BleepingComputer, The Hacker News, Security Affairs, securityaffairs.com

---

**STATUS:** Confirmed. Updates will follow as patches become available.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-27-breaking-alert-posture.webp)