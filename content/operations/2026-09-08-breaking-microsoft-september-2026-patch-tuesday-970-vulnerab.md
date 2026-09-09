---
title: "🛡️ **BREAKING: Microsoft September 2026 Patch Tuesday — ~970 Vulnerabilities Including 2 Exploited Zero-Days Require Immediate Deployment**"
date: 2026-09-08T23:24:54-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "cso-online-september-2026-patch-tuesday-", "security"]
description: "BREAKING: CSO Online: September 2026 Patch Tuesday roundup"
cover:
  image: "/images/operations/2026-09-08-breaking-microsoft-september-2026-patch-tuesday-970-vulnerab.webp"
  alt: "**BREAKING: Microsoft September 2026 Patch Tuesday — ~970 Vulnerabilities Including 2 Exploited Zero-Days Require Immediate Deployment**"
  relative: false
---

*Published Tuesday, September 08, 2026 at 11:24 PM PT*

![**BREAKING: Microsoft September 2026 Patch Tuesday — ~970 Vulnerabilities Including 2 Exploited Zero-Days Require Immediate Deployment**](/images/operations/2026-09-08-breaking-microsoft-september-2026-patch-tuesday-970-vulnerab.webp)

**BLUF:** Microsoft released nearly 1,000 security fixes on September Patch Tuesday, including two actively exploited zero-day vulnerabilities and 113 critical-severity flaws. Deployment is urgent; some bugs are wormable and already under attack. Details on specific CVEs and affected products remain limited.

**DETAILS:**
- Microsoft released **964–972 CVEs** (sources vary slightly; lowest confirmed count 964) in September 2026 Patch Tuesday — another monthly record. Microsoft has deployed AI-assisted vulnerability discovery since mid-2026, accelerating patch volume.
- **Two zero-day vulnerabilities are confirmed exploited** (CrowdStrike reporting); specific CVE numbers and technical details not yet available in sourced material.
- **113 critical-severity vulnerabilities** included in this release per CrowdStrike analysis.
- At least some vulnerabilities are described as "**possibly wormable**" — capable of network propagation without user interaction — elevating worm/ransomware risk.
- **Timing:** Patches released on standard Patch Tuesday schedule; exploitation activity already active.

**IMPACT:**
- **Scope:** Windows systems confirmed; broader Microsoft ecosystem (Office, cloud services, etc.) likely affected but not itemized in available sources.
- **Severity:** Critical. Wormable vectors + active zero-day exploitation = high likelihood of rapid weaponization and enterprise compromise within days if unpatched.
- **Affected population:** All organizations running Windows, Office, or other Microsoft enterprise products lacking immediate security team response.

**RECOMMENDED ACTIONS:**
1. Prioritize deployment of September 2026 Patch Tuesday to all Windows systems within 24–48 hours if possible; treat as P0 if zero-day details become public.
2. Scan logs and endpoint telemetry for exploitation attempts against Windows systems starting immediately (baseline: earliest September 1 activity).
3. Review Microsoft Security Response Center (MSRC) advisory for specific product/version guidance (CVE details unavailable in this material).
4. Isolate or manually review any systems blocking or delaying patch cycles.

**SOURCES:**
- CSO Online: September 2026 Patch Tuesday roundup
- BleepingComputer: Microsoft September 2026 Patch Tuesday fixes 966 flaws, 2 zero-days
- CrowdStrike (blue team): September 2026 Patch Tuesday analysis (2 exploited zero-days; 113 critical CVEs among 972 total)

**NOTE — Unconfirmed detail:** Specific CVE numbers, product-version breakdowns, and zero-day technical summaries not yet available. MSRC advisory expected to follow shortly.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-08-breaking-alert-posture.webp)