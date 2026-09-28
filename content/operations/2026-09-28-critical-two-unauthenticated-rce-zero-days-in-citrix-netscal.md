---
title: "🛡️ **CRITICAL: Two Unauthenticated RCE Zero-Days in Citrix NetScaler ADC & Gateway — Active Exploitation — Patch Immediately**"
date: 2026-09-28T05:57:06-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "cso-online-netscaler-admins-told-to-patc", "security"]
description: "BREAKING: CSO Online: NetScaler admins told to patch critical zero-days in ADC and Gateway now"
cover:
  image: "/images/operations/2026-09-28-critical-two-unauthenticated-rce-zero-days-in-citrix-netscal.webp"
  alt: "**CRITICAL: Two Unauthenticated RCE Zero-Days in Citrix NetScaler ADC & Gateway — Active Exploitation — Patch Immediately**"
  relative: false
---

*Published Monday, September 28, 2026 at 05:57 AM PT*

![**CRITICAL: Two Unauthenticated RCE Zero-Days in Citrix NetScaler ADC & Gateway — Active Exploitation — Patch Immediately**](/images/operations/2026-09-28-critical-two-unauthenticated-rce-zero-days-in-citrix-netscal.webp)

Citrix NetScaler ADC and NetScaler Gateway deployments are under active, ongoing attack from two critical unauthenticated remote code execution (RCE) zero-day vulnerabilities (CVE-2026-88771, CVE-2026-88772). Patch deployment must begin today; deferred patching until Monday is confirmed too late. Citrix has released patches. CISA is amplifying the alert to federal agencies. Globally scoped exploitation.

**DETAILS**
- Two high-severity unauthenticated RCE flaws in NetScaler ADC and NetScaler Gateway confirmed by Citrix
- Both vulnerabilities exploited in active attacks for weeks; exploitation is widespread and ongoing
- Citrix patches now available; CSO Online reported weekend advisory urging immediate offline patching
- Watchtower CEO Benjamin Harris stated Monday patch deployment window is insufficient — attackers already in flight
- CISA alert amplifies urgency to federal agencies; global threat actors actively exploiting

**IMPACT**
- Directly affected: All NetScaler ADC and Gateway deployments exposed to the internet or untrusted networks
- Risk: Unauthenticated remote code execution as root/SYSTEM; complete infrastructure compromise
- Scope: Enterprise-wide on any organization running these appliances; government agencies explicitly named as priority targets by CISA
- No credentials, authentication bypass, or user interaction required for exploitation

**RECOMMENDED ACTIONS**
1. **Immediate (today):** Patch all NetScaler ADC and Gateway appliances with released updates from Citrix; consult vendor documentation for patch versions
2. **Interim (if patch deployment is delayed):** Isolate affected NetScaler instances from untrusted networks pending patching
3. **Investigation:** Check NetScaler logs and upstream firewall/IDS data for exploitation attempts (check last 2–3 weeks minimum)
4. **Verification:** Confirm patch deployment across all instances; do not assume automated systems caught all appliances

**SOURCES**
CSO Online, CISA Current Activity, Help Net Security, The Hacker News, Security Week, Security Affairs

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-28-breaking-alert-posture.webp)