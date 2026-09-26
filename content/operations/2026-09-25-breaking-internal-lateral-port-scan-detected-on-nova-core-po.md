---
title: "🛡️ **BREAKING: Internal Lateral Port Scan Detected on nova-core — Potential Active Reconnaissance**"
date: 2026-09-25T22:45:10-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "ips-lateral-scan-192-168-1-9-hit-5-ports", "security"]
description: "BREAKING: IPS: Lateral scan: 192.168.1.9 hit 5 ports on 192.168.1.138 in 60s"
cover:
  image: "/images/operations/2026-09-25-breaking-internal-lateral-port-scan-detected-on-nova-core-po.webp"
  alt: "**BREAKING: Internal Lateral Port Scan Detected on nova-core — Potential Active Reconnaissance**"
  relative: false
---

*Published Friday, September 25, 2026 at 10:45 PM PT*

![**BREAKING: Internal Lateral Port Scan Detected on nova-core — Potential Active Reconnaissance**](/images/operations/2026-09-25-breaking-internal-lateral-port-scan-detected-on-nova-core-po.webp)

**BLUF:** IPS detected lateral movement from internal host 192.168.1.9 probing 5 ports on 192.168.1.138 within 60 seconds. Direction: internal. System: nova-core. Specific ports and target identity not confirmed; requires immediate investigation to determine if host is compromised or network baseline violation.

**DETAILS:**
- IPS signature triggered on lateral_movement at 2026-09-25; source 192.168.1.9, destination 192.168.1.138, 5 ports scanned in 60-second window
- Scan pattern consistent with reconnaissance (port enumeration across single target in short burst)
- Previous lateral movement alert noted 192.168.1.86 probing same target (192.168.1.138); unclear if related or repeated activity by different source
- CVE exploit activity is tracked in Nova's threat database (CVE-2023-22515 CVSS 10.0, CVE-2022-40684 CVSS 9.8, CVE-2026-29000 CVSS 9.3) — context indicates known scanning infrastructure
- Specific ports hit and target host identity not provided in alert payload

**IMPACT:**
- nova-core network integrity: potential compromise of 192.168.1.9 or unauthorized network device
- 192.168.1.138 exposure: identity of target host and services unknown; cannot assess if ports align with known vulnerabilities
- Scope: internal network only; no external-facing traffic detected

**RECOMMENDED ACTIONS (immediate):**
1. Identify both hosts — WHOIS/ARP 192.168.1.9 and 192.168.1.138; confirm ownership, assigned user, OS
2. Isolate 192.168.1.9 if unauthorized or ownership cannot be confirmed; block at core switch pending investigation
3. Retrieve full IPS log for this event — exact ports, TCP flags, any payload data, full packet times
4. Check 192.168.1.138 for signs of compromise (unusual processes, listening ports, outbound connections)
5. Correlate with previous 192.168.1.86 lateral scan — same attacker/device drifting IP, or independent event
6. Review network segmentation policy for nova-core; enforce zero-trust between subnets if not deployed

**SOURCES:**
- IPS lateral_movement signature (2026-09-25)
- Nova threat memory: CVE exploit tracking, previous lateral movement alert (192.168.1.86)

**Status:** ACTIVE — investigation required.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-25-breaking-alert-posture.webp)