---
title: "🛡️ **CISCO IDENTITY SERVICES ENGINE (ISE) — MAX-SEVERITY AUTHENTICATION BYPASS, ACTIVELY EXPLOITED — PATCH IMMEDIATELY**"
date: 2026-09-17T17:34:37-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "cso-online-cisco-patches-max-severity-is", "security"]
description: "BREAKING: CSO Online: Cisco patches max-severity ISE flaw, the second critical zero-day this week"
cover:
  image: "/images/operations/2026-09-17-cisco-identity-services-engine-ise-max-severity-authenticati.webp"
  alt: "**CISCO IDENTITY SERVICES ENGINE (ISE) — MAX-SEVERITY AUTHENTICATION BYPASS, ACTIVELY EXPLOITED — PATCH IMMEDIATELY**"
  relative: false
---

*Published Thursday, September 17, 2026 at 05:34 PM PT*

![**CISCO IDENTITY SERVICES ENGINE (ISE) — MAX-SEVERITY AUTHENTICATION BYPASS, ACTIVELY EXPLOITED — PATCH IMMEDIATELY**](/images/operations/2026-09-17-cisco-identity-services-engine-ise-max-severity-authenticati.webp)

---

**BLUF:** Cisco has released emergency patches for an actively exploited authentication bypass vulnerability (CVSS 10.0) affecting Cisco Identity Services Engine (ISE), used for enterprise network access control and policy enforcement. This is the second critical zero-day Cisco has patched in one week. Enterprises running ISE must apply patches without delay; this vulnerability is being exploited in the wild against production systems.

---

**DETAILS**

• **CVE-2026-76460** — Cisco ISE authentication bypass with CVSS 10.0 severity; enables attackers to bypass network access controls on enterprise IAM systems in active exploitation.

• **Active Exploitation Confirmed** — Multiple security researchers and vendors confirm malicious actors are weaponizing this flaw against production ISE deployments; attack rate and sophistication unknown but trending upward.

• **Second Zero-Day in One Week** — Cisco also patched CVE-2026-76461 (Cisco Secure Email Gateway root RCE) earlier this week, signaling an unusual attack surface spike against Cisco network infrastructure.

• **ISE Scope** — Cisco ISE is mission-critical for enterprise network access control (NAC), policy enforcement, and authentication. Compromise allows attackers to assume authenticated user/device status and move laterally within the network.

• **Patches Released** — Cisco has released patches; specific patch version and affected platforms not yet detailed in available sources. Check Cisco security advisory for your platform/version.

---

**IMPACT**

Enterprises running Cisco ISE face immediate network compromise risk. Successful exploitation allows:
- Bypass of network admission policies
- Lateral movement as trusted network endpoints
- Potential for insider-like persistence and data exfiltration

**Scope:** Any organization with ISE deployed for network access control (common in Fortune 500, healthcare, financial services, government, telecommunications).

**Attack Pattern:** Exploitation is active and untargeted; no evidence of selective targeting. Expect broad scanning and probing for vulnerable ISE instances reachable from the internet or compromised VPNs.

---

**RECOMMENDED ACTIONS**

1. **Immediate:** Identify all Cisco ISE instances (on-premises and cloud-hosted); cross-reference with Cisco's affected version list (advisory TBD).
2. **Within 24 Hours:** Apply Cisco's released patch to all ISE systems. If patch unavailable for your version, engage Cisco TAC for timeline and interim mitigations (network segmentation, access restrictions).
3. **Monitoring:** Enable ISE authentication logging; search for anomalous login patterns, unexpected privilege escalation, or failed-then-succeeded auth sequences.
4. **Escalate:** Notify CISO and infrastructure teams; this requires mandatory out-of-cycle patching.

---

**SOURCES**

- CSO Online, The Hacker News, BleepingComputer, CyberScoop, SOC Prime, Help Net Security, news4hackers — all reporting active Cisco ISE CVE-2026-76460 exploitation and CVE-2026-76461 email gateway RCE.

---

**STATUS:** CONFIRMED / ACTIVE EXPLOITATION — Watch Cisco security advisories for patch release details and affected platform/version matrix.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-17-breaking-alert-posture.webp)