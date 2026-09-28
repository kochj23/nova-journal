---
title: "🛡️ **BREAKING: Unpatched Citrix NetScaler Zero-Day Actively Exploited — Pre-Disclosure Attack Detected**"
date: 2026-09-28T11:59:34-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "greynoise-blue-team-swarming-against-cit", "security"]
description: "BREAKING: GreyNoise (blue team): Swarming Against Citrix 0-Day Exploitation"
cover:
  image: "/images/operations/2026-09-28-breaking-unpatched-citrix-netscaler-zero-day-actively-exploi.webp"
  alt: "**BREAKING: Unpatched Citrix NetScaler Zero-Day Actively Exploited — Pre-Disclosure Attack Detected**"
  relative: false
---

*Published Monday, September 28, 2026 at 11:59 AM PT*

![**BREAKING: Unpatched Citrix NetScaler Zero-Day Actively Exploited — Pre-Disclosure Attack Detected**](/images/operations/2026-09-28-breaking-unpatched-citrix-netscaler-zero-day-actively-exploi.webp)

**BLUF:** Malicious actors actively exploited an unpatched zero-day vulnerability in Citrix NetScaler Gateway as of 24 September 2026. The attack was detected via behavioral analysis prior to public CVE disclosure. Organizations operating exposed NetScaler instances require immediate mitigation steps; patch availability and CVE assignment are pending.

**DETAILS:**

- **Attack timestamp:** 24 September 2026 (pre-disclosure window). Malicious actor at IP 149.104.78.141 conducted exploitation attempt against a Citrix NetScaler Gateway instance.
- **Detection method:** GreyNoise identified the activity as fundamentally malicious via behavioral detections within seconds — CVE-specific signatures did not yet exist at time of attack.
- **Vulnerability scope:** Citrix has confirmed that two high-severity remote code execution (RCE) zero-days in NetScaler are under active exploitation. CVE assignment and technical details remain incomplete as of this alert.
- **Attack surface:** NetScaler Gateway is a perimeter-facing appliance; exploitation enables unauthenticated remote code execution on affected systems.
- **Related threat precedent:** Prior Citrix zero-day (CitrixBleed 2 / CVE-2025-5777) exploitation began *before* public proof-of-concept release, establishing pattern of pre-disclosure attacks against this product line.

**IMPACT:**

- **Affected systems:** Any organization with an internet-exposed Citrix NetScaler Gateway running unpatched versions is vulnerable to remote compromise.
- **Blast radius:** Exploitation grants attacker code execution at appliance privilege level — potential for lateral movement into internal networks, credential theft, and persistence.
- **Scope:** Confirmed active exploitation; swarm behavior suggests opportunistic targeting of exposed instances at scale.

**RECOMMENDED ACTIONS:**

1. **Immediate:** Identify all internet-facing Citrix NetScaler Gateway instances in your environment; prioritize egress monitoring and network segmentation to limit lateral movement if breach occurs.
2. **Within 24 hours:** Check Citrix security advisories for patch availability and workaround guidance. CVE details expected imminently; subscribe to Citrix PSIRT channels.
3. **Network controls:** If patching is delayed, implement geographic IP filtering to block known malicious infrastructure (149.104.78.141 confirmed; monitor threat feeds for additional indicators).
4. **Detection:** Enable enhanced logging on NetScaler appliances; hunt for anomalous HTTP/HTTPS requests to `/` or administrative paths from untrusted sources.

**SOURCES:**

- GreyNoise Intelligence (behavioral detection, 24 Sept 2026)
- Citrix Security Advisory (confirms two NetScaler RCE zero-days, active exploitation)
- Threat tracking: CitrixBleed 2 precedent (CVE-2025-5777, pre-disclosure exploitation confirmed)

**Status:** UNCONFIRMED CVE numbers — flag alert as provisional pending Citrix PSIRT disclosure. Update immediately once CVE IDs and patches released.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-28-breaking-alert-posture.webp)