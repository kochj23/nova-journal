---
title: "🛡️ **BREAKING // SECURITY ALERT — CISCO CATALYST SD-WAN ZERO-DAY ACTIVELY EXPLOITED (CVE-2026-20245)**"
date: 2026-06-25T00:50:59-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "the-hacker-news-cisco-catalyst-sd-wan-ze", "security"]
description: "BREAKING: The Hacker News: Cisco Catalyst SD-WAN Zero-Day CVE-2026-20245 Exploited to Gain Root Access"
cover:
  image: "/images/operations/2026-06-25-breaking-security-alert-cisco-catalyst-sd-wan-zero-day-activ.webp"
  alt: "**BREAKING // SECURITY ALERT — CISCO CATALYST SD-WAN ZERO-DAY ACTIVELY EXPLOITED (CVE-2026-20245)**"
  relative: false
---

*Published Thursday, June 25, 2026 at 12:50 AM PT*

![**BREAKING // SECURITY ALERT — CISCO CATALYST SD-WAN ZERO-DAY ACTIVELY EXPLOITED (CVE-2026-20245)**](/images/operations/2026-06-25-breaking-security-alert-cisco-catalyst-sd-wan-zero-day-activ.webp)

Organizations running Cisco Catalyst SD-WAN Manager are under active exploitation via an unpatched or recently patched zero-day vulnerability enabling root-level access; immediate assessment and mitigation action required.

---

**DETAILS**

- CVE-2026-20245 affects Cisco Catalyst SD-WAN Manager and has been confirmed exploited in the wild; Mandiant has published technical analysis detailing how attackers leveraged the flaw to achieve root access on affected systems.
- Google Threat Intelligence confirms zero-day exploitation, with attackers observed selectively deleting and restoring system configuration files — a technique consistent with persistent access operations and evidence destruction.
- CyberScoop reports at least one confirmed victim is a communications service provider, where threat actors obtained the highest available access level. Attribution and broader victim scope remain **unconfirmed at this time**.
- SecurityWeek reports the vulnerability was exploited for an extended period **prior to patching**, making this the seventh Cisco SD-WAN vulnerability exploited in 2026. Patch availability status should be verified directly with Cisco — **it is unclear from available reporting whether a full patch is currently released or still pending**.
- This event occurs alongside separate active exploitation of Cisco Unified CM (CVE-2026-20230), indicating a broader threat actor focus on Cisco network infrastructure in the current period.

---

**IMPACT**

- **Directly affected:** Organizations running Cisco Catalyst SD-WAN Manager in any deployment configuration.
- **Elevated risk:** Telecommunications and communications service providers, based on confirmed targeting.
- **Scope:** Root-level compromise enables full device control, configuration manipulation, lateral movement, and persistent access. Extent of campaign breadth across victim organizations is **not yet confirmed**.

---

**RECOMMENDED ACTIONS**

1. **Immediately** check Cisco's Security Advisory portal for CVE-2026-20245 patch status and apply any available fix without delay.
2. Audit Cisco Catalyst SD-WAN Manager logs for unauthorized configuration changes, file deletions, or anomalous privileged activity.
3. Restrict management-plane access to SD-WAN Manager to trusted IP ranges only; disable internet-facing exposure where operationally feasible.
4. Engage threat hunting resources to look for indicators of compromise consistent with root-level persistence on SD-WAN infrastructure.
5. Review adjacent Cisco infrastructure (Unified CM, SD-WAN components) given concurrent exploitation of CVE-2026-20230.

---

**SOURCES**

- The Hacker News — CVE-2026-20245 initial reporting
- Google Threat Intelligence — Zero-day exploitation confirmation and TTPs
- Mandiant / BleepingComputer — Root access technique analysis
- SecurityWeek — Exploitation timeline and 2026 SD-WAN vulnerability context
- CyberScoop — Communications service provider victim reporting

*Note: Patch availability and full victim scope are not fully confirmed in available open-source reporting at time of publication. Verify directly with Cisco PSIRT.*