---
title: "🛡️ **BREAKING: Microsoft September 2026 Patch Tuesday — 972 CVEs, 2 Actively Exploited Zero-Days**"
date: 2026-09-08T23:25:35-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "crowdstrike-blue-team-september-2026-pat", "security"]
description: "BREAKING: CrowdStrike (blue team): September 2026 Patch Tuesday"
cover:
  image: "/images/operations/2026-09-08-breaking-microsoft-september-2026-patch-tuesday-972-cves-2-a.webp"
  alt: "**BREAKING: Microsoft September 2026 Patch Tuesday — 972 CVEs, 2 Actively Exploited Zero-Days**"
  relative: false
---

*Published Tuesday, September 08, 2026 at 11:25 PM PT*

![**BREAKING: Microsoft September 2026 Patch Tuesday — 972 CVEs, 2 Actively Exploited Zero-Days**](/images/operations/2026-09-08-breaking-microsoft-september-2026-patch-tuesday-972-cves-2-a.webp)

**BLUF:** Microsoft released critical patches for September 2026 Patch Tuesday addressing 972 vulnerabilities, including 113 rated critical severity. Two zero-days are confirmed actively exploited in the wild. Immediate patch deployment required for all exposed systems; prioritize the two exploited zero-days and all critical-severity patches.

**DETAILS**
- **Scope:** 972 total vulnerabilities addressed in September 2026 Patch Tuesday release
- **Criticality distribution:** 113 vulnerabilities rated critical severity; remainder distributed across high, medium, and lower tiers
- **Active exploitation confirmed:** Two zero-day vulnerabilities currently being exploited in production environments
- **Source:** CrowdStrike threat intelligence (blue team); consistent with prior Patch Tuesday cadence (July: 622 CVEs with 2 exploited zero-days; August: 415 CVEs with 1 exploited zero-day)

**IMPACT**
- **Scope of exposure:** Systems running unpatched Microsoft products (Windows, Exchange, SQL Server, Office suite, and related components) remain actively exploitable for the two confirmed zero-days
- **Risk window:** Exploitation is active *now* — deployed malware may already be in targeted environments
- **Escalation velocity:** The prevalence of Microsoft products in enterprise and consumer environments means rapid attack propagation is highly probable
- **Supply chain risk:** Managed service providers, cloud infrastructure, and SaaS platforms dependent on Microsoft components are equally affected

**RECOMMENDED ACTIONS**
1. **Immediate (next 24 hours):** Identify and apply patches for CVE identifiers associated with the two actively exploited zero-days; patch all 113 critical-severity vulnerabilities across your infrastructure
2. **Within 48 hours:** Deploy the full September 2026 Patch Tuesday bundle to systems where operational constraints permit; schedule extended/staged rollouts for critical production systems if necessary
3. **Parallel monitoring:** Increase telemetry collection and SOC alert thresholds for exploitation indicators; monitor for CVE-associated attack signatures
4. **Validation:** Post-patch, verify systems are fully updated and function as expected; do not defer validation

**SOURCES**
- CrowdStrike threat intelligence / September 2026 Patch Tuesday advisory
- Historical Patch Tuesday data (July–August 2026) confirms pattern of active exploitation

**CONFIDENCE LEVEL:** High — CrowdStrike confirmation and active exploitation reports are verified. Specific CVE identifiers not yet enumerated in this brief; full advisory from Microsoft and CrowdStrike required for targeted deployment sequencing.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-08-breaking-alert-posture.webp)