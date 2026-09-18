---
title: "🛡️ **URGENT — Cisco Identity Services Engine: Maximum-Severity Zero-Day Actively Exploited**"
date: 2026-09-17T17:35:22-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "cyberscoop-cisco-alerts-customers-to-sec", "security"]
description: "BREAKING: CyberScoop: Cisco alerts customers to second actively exploited zero-day in as many days"
cover:
  image: "/images/operations/2026-09-17-urgent-cisco-identity-services-engine-maximum-severity-zero-.webp"
  alt: "**URGENT — Cisco Identity Services Engine: Maximum-Severity Zero-Day Actively Exploited**"
  relative: false
---

*Published Thursday, September 17, 2026 at 05:35 PM PT*

![**URGENT — Cisco Identity Services Engine: Maximum-Severity Zero-Day Actively Exploited**](/images/operations/2026-09-17-urgent-cisco-identity-services-engine-maximum-severity-zero-.webp)

BLUF: Cisco has confirmed a second actively exploited zero-day within 24 hours, this time affecting Cisco Identity Services Engine (ISE) with maximum-severity rating. Active exploitation in the wild is confirmed. ISE deployments require immediate mitigation. Concurrent active exploitation of Cisco Secure Email Gateway (CVE-2026-76461) continues.

DETAILS:
- **Dual zero-day disclosure:** Cisco disclosed two actively exploited zero-days within a single day; the latest targets Cisco Identity Services Engine with maximum-severity CVSS rating (10.0 confirmed via corroborating sources).
- **ISE attack pattern:** Identity Services Engine has been targeted by three separate actively exploited vulnerabilities since June 2025, indicating sustained and escalating attacker targeting of this critical access-control product.
- **Authentication bypass mechanism:** The ISE zero-day is an authentication bypass, allowing unauthenticated attackers to compromise access controls and bypass identity verification.
- **Active exploitation confirmed:** Multiple sources confirm malicious actors are actively exploiting the ISE vulnerability in production environments.
- **Email gateway RCE ongoing:** Cisco Secure Email Gateway zero-day (CVE-2026-76461) with remote code execution capability remains under active attack.

IMPACT:
- **Direct risk:** All organizations running Cisco ISE or Cisco Secure Email Gateway are targeted.
- **Lateral movement vector:** ISE compromise enables attackers to bypass identity controls, move laterally, exfiltrate data, and establish persistence across dependent systems.
- **Operational risk:** ISE manages authentication for enterprise infrastructure; exploitation can cascade into widespread access compromise.

RECOMMENDED ACTIONS:
- **Immediate:** Retrieve Cisco Security Advisory for ISE; apply patches if available or implement network isolation pending patch availability.
- **Urgent:** Enable verbose authentication and administrative logging on ISE; review logs for failed/anomalous authentication and unauthorized admin access over past 7 days.
- **Monitor:** Isolate or restrict egress from ISE appliances; flag outbound connections to unexpected destinations.
- **Escalate:** Engage Cisco TAC; prepare contingency user-authentication procedures if ISE unavailability is necessary.

SOURCES:
CyberScoop (trigger); BleepingComputer, The Hacker News, The Register, Help Net Security, SecurityAffairs (corroboration).

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-17-breaking-alert-posture.webp)