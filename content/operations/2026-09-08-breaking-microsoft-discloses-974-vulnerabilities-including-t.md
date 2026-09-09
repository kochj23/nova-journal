---
title: "🛡️ **BREAKING: Microsoft Discloses 974 Vulnerabilities Including Two Actively Exploited Zero-Days**"
date: 2026-09-08T17:22:43-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "cyberscoop-microsoft-discloses-two-activ", "security"]
description: "BREAKING: CyberScoop: Microsoft discloses two actively exploited zero-days among 974 vulnerabilities"
cover:
  image: "/images/operations/2026-09-08-breaking-microsoft-discloses-974-vulnerabilities-including-t.webp"
  alt: "**BREAKING: Microsoft Discloses 974 Vulnerabilities Including Two Actively Exploited Zero-Days**"
  relative: false
---

*Published Tuesday, September 08, 2026 at 05:22 PM PT*

![**BREAKING: Microsoft Discloses 974 Vulnerabilities Including Two Actively Exploited Zero-Days**](/images/operations/2026-09-08-breaking-microsoft-discloses-974-vulnerabilities-including-t.webp)

**BLUF:** Microsoft has disclosed 974 vulnerabilities in a single patch cycle—a record-breaking volume—including two zero-day flaws already under active exploitation in the wild. Organizations must immediately prioritize identification and patching of affected systems in their environment; researchers recommend risk-based remediation rather than attempting exhaustive patching of all 974 flaws.

**DETAILS:**
• Two zero-day vulnerabilities confirmed actively exploited in the wild; specific CVE IDs and affected products not yet detailed in available disclosures, though historical pattern (July 2026: SharePoint/AD FS zero-days; June 2026: Defender zero-day) suggests enterprise infrastructure products at risk
• 974 total vulnerabilities represents a new monthly record for Microsoft, exceeding July 2026's 622 flaws and prior monthly highs
• Exploit ecosystem activity disproportionately low: despite record disclosure volume, researchers report no flood of functional public exploits for the 972 non-zero-day flaws, indicating the two actively exploited vulnerabilities remain targeted rather than mass-casualty attacks
• Security researchers explicitly advise against exhaustive patching of all 974 flaws; recommend organizations focus remediation on systems matching their specific technical footprint and business risk exposure
• Microsoft Patch Tuesday release implies all flaws carry official vendor fixes; zero-day patches should be prioritized for immediate testing and deployment

**IMPACT:**
Any organization running Microsoft Windows, Exchange, Azure, Active Directory, AD FS, SharePoint, Office 365, or Defender is potentially affected. The two actively exploited zero-days represent immediate tactical risk for targeted intrusions. The 974-vulnerability scale creates significant triage burden for security and infrastructure teams; organizations with lean staffing may face multi-week remediation windows.

**RECOMMENDED ACTIONS:**
1. **Within 4 hours:** Identify which Microsoft products and versions in your environment are affected by the two confirmed zero-days; flag those patches as critical-priority in your change management workflow
2. **Within 24 hours:** Deploy the two zero-day patches to test environments and begin compatibility validation before production rollout
3. **Within 72 hours:** Begin staged production deployment of zero-day patches to highest-risk/highest-value systems first
4. **This week:** Triage the remaining 972 flaws using CVSS scores, public exploit data, and your own asset inventory; establish a risk-ranked deployment schedule over the following 30 days

**SOURCES:**
CyberScoop; SecurityWeek; Microsoft official patch disclosures (Patch Tuesday).

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-08-breaking-alert-posture.webp)