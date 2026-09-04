---
title: "🛡️ **CISCO NEXUS 9000 CRITICAL RCE — UNAUTHENTICATED REMOTE CODE EXECUTION AS ROOT**"
date: 2026-09-03T16:57:16-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "securityaffairs-cisco-fixed-critical-rce", "security"]
description: "BREAKING: securityaffairs: Cisco Fixed Critical RCE in Nexus 9000 Series Switches"
cover:
  image: "/images/operations/2026-09-03-cisco-nexus-9000-critical-rce-unauthenticated-remote-code-ex.webp"
  alt: "**CISCO NEXUS 9000 CRITICAL RCE — UNAUTHENTICATED REMOTE CODE EXECUTION AS ROOT**"
  relative: false
---

*Published Thursday, September 03, 2026 at 04:57 PM PT*

![**CISCO NEXUS 9000 CRITICAL RCE — UNAUTHENTICATED REMOTE CODE EXECUTION AS ROOT**](/images/operations/2026-09-03-cisco-nexus-9000-critical-rce-unauthenticated-remote-code-ex.webp)

**BLUF:** Cisco has released patches for a critical remote code execution vulnerability affecting Nexus 9000 Series switches that allows unauthenticated attackers to execute commands as root. Immediate patch deployment required for all affected Nexus 9000 devices exposed to untrusted networks.

**DETAILS:**
- Cisco Nexus 9000 Series switches contain a critical RCE flaw exploitable by unauthenticated remote attackers
- Successful exploitation grants root-level code execution on affected devices
- Patches have been released; specific CVE identifier and affected software versions not detailed in available materials
- No confirmed exploitation in the wild at publication, though related Cisco vulnerabilities (CVE-2026-20230, CVE-2026-20349, CVE-2026-20200) have seen active exploitation
- Cisco has concurrently patched multiple critical vulnerabilities in Crosswork, Secure Workload, SD-WAN, IOS XE, and FMC products, suggesting a broader advisory cycle

**IMPACT:**
- All Nexus 9000 Series switch deployments connected to untrusted networks (external-facing, MPLS edges, DCI fabric links)
- Compromise grants attacker full control of network device — configuration exfiltration, traffic interception, lateral movement to connected infrastructure
- Data center and enterprise networks with Nexus 9000 fabric are at highest risk

**RECOMMENDED ACTIONS:**
1. Identify all Nexus 9000 Series switches in your environment (running show version or DCNM inventory)
2. Cross-reference against Cisco advisory to determine affected OS versions — **URGENT if devices are internet-routable or accept untrusted BGP/OSPF**
3. Stage patches in non-production; test failover procedures (this will require device reload)
4. Prioritize patches for externally-exposed devices first
5. Monitor Cisco Security Advisory for CVE identifier, CVSS score, and affected versions (currently incomplete in public sources)

**SOURCES:**
- securityaffairs.com (patch confirmation)
- The Hacker News (unauthenticated RCE confirmation)
- SecurityWeek (related Cisco advisory cycle)

---

**STATUS: DEVELOPING — Full CVE details and affected version matrix pending from Cisco official advisory. Alert will update when specific identifiers and scope are published.**

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-03-breaking-alert-posture.webp)