---
title: "🛡️ **CISA, FBI Issue Third-Party ICS Risk Guidance to Critical Infrastructure Operators**"
date: 2026-09-24T05:35:44-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "industrial-cyber-cisa-fbi-warn-critical-", "security"]
description: "BREAKING: Industrial Cyber: CISA, FBI warn critical infrastructure operators of third-party ICS risks, urge le"
cover:
  image: "/images/operations/2026-09-24-cisa-fbi-issue-third-party-ics-risk-guidance-to-critical-inf.webp"
  alt: "**CISA, FBI Issue Third-Party ICS Risk Guidance to Critical Infrastructure Operators**"
  relative: false
---

*Published Thursday, September 24, 2026 at 05:35 AM PT*

![**CISA, FBI Issue Third-Party ICS Risk Guidance to Critical Infrastructure Operators**](/images/operations/2026-09-24-cisa-fbi-issue-third-party-ics-risk-guidance-to-critical-inf.webp)

**BLUF:** CISA and FBI issued formal guidance to critical infrastructure operators on managing risks from third-party Industrial Control Systems integrations. Key recommendations: enforce least-privilege access and restrict remote access capabilities for all third-party connections to ICS environments.

**DETAILS**

- CISA and FBI jointly issued guidance directed at operators of critical infrastructure protecting industrial control systems.
- Primary focus: risks inherent in third-party ICS components and remote vendor access arrangements.
- Recommended controls: least-privilege access policies for all third-party vendor interactions with ICS networks; strict limits on remote access capabilities and connectivity.
- Guidance aligns with broader CISA hardening campaign; related advisories address insider threats, internet exposure reduction, and router security in critical infrastructure contexts.
- Full advisory text truncated in available material; core message and recommendations confirmed.

**IMPACT**

- **Scope:** All U.S. critical infrastructure sectors relying on third-party ICS vendors (energy, water, transportation, communications, manufacturing).
- **Threat Context:** Third-party supply chain is proven high-risk attack vector. Nation-state and advanced persistent threat actors routinely target vendor relationships to gain ICS access; remote access tools (RDP, VPN, SSH) provide persistence and lateral movement once inside.
- **Specificity:** No active attack or zero-day is identified in the material; this is defensive guidance, likely preemptive response to known threat actor tradecraft.

**RECOMMENDED ACTIONS**

- **Immediate (24–48 hours):**
  - Audit all active third-party vendor accounts with access to ICS networks.
  - Identify which vendors have remote access capabilities enabled; document privilege levels.
  - Flag any vendor with unnecessary administrative or production-level permissions.

- **Near-term (1–2 weeks):**
  - Enforce least-privilege principle: remove overprivileged third-party accounts; require vendor justification for elevated access.
  - Implement or tighten remote access policies: require VPN, MFA, geofencing, session recording, and connection time windows where operationally feasible.
  - Require vendors to provide access justification and attend security reviews.

- **Ongoing:**
  - Quarterly audit of third-party access rights.
  - Incident response plan for vendor compromise scenarios.

**SOURCES**

- CISA and FBI guidance (title and core recommendations confirmed; full text pending).

---

**Status:** Advisory confirmed as issued; full text not yet in hand. Alert will be updated when complete guidance is available.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-24-breaking-alert-posture.webp)