---
title: "🛡️ **DEVELOPING — Multiple Critical Flaws in macOS, SharePoint, vCenter, and Microsoft IKE Under Active Exploitation**"
date: 2026-08-19T10:39:51-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "the-hacker-news-critical-macos-sharepoin", "security"]
description: "BREAKING: The Hacker News: Critical macOS, SharePoint, vCenter, and Microsoft IKE Flaws Under Active Exploitat"
cover:
  image: "/images/operations/2026-08-19-developing-multiple-critical-flaws-in-macos-sharepoint-vcent.webp"
  alt: "**DEVELOPING — Multiple Critical Flaws in macOS, SharePoint, vCenter, and Microsoft IKE Under Active Exploitation**"
  relative: false
---

*Published Wednesday, August 19, 2026 at 10:39 AM PT*

![**DEVELOPING — Multiple Critical Flaws in macOS, SharePoint, vCenter, and Microsoft IKE Under Active Exploitation**](/images/operations/2026-08-19-developing-multiple-critical-flaws-in-macos-sharepoint-vcent.webp)

---

**BLUF:** Four critical vulnerabilities spanning Apple macOS, Microsoft SharePoint, Broadcom VMware vCenter, and Microsoft IKE protocols are confirmed under active exploitation. CISA has added all four to its Known Exploited Vulnerabilities catalog. Immediate patching and network segmentation required; internet-exposed systems already targeted.

---

**DETAILS**

- **macOS Screen Sharing flaw** — attackers exploiting a Screen Sharing vulnerability to gain root access on internet-exposed Macs; crypto miners (Monero) and malware observed deployed post-compromise
- **SharePoint RCE (CVE-2026-50522)** — remote code execution flaw confirmed under active exploitation; public proof-of-concept available
- **VMware vCenter vulnerability** — active exploitation observed; attackers achieving persistent remote access
- **Microsoft IKE protocol flaws** — multiple IKE vulnerabilities added to CISA's Known Exploited list; specific exploitation vector unconfirmed in available reporting
- **CISA advisory status** — all four flaws formally added to the Known Exploited Vulnerabilities catalog, triggering federal contractor reporting requirements

---

**IMPACT**

- **Scope:** macOS endpoints with Screen Sharing enabled, SharePoint on-premises and cloud deployments, VMware vCenter infrastructure, and organizations relying on IKE (VPN/IPsec)
- **Risk:** Root access on macOS systems; RCE on SharePoint; VPN/remote access compromise via IKE; crypto-miner deployment and data theft observed in the wild
- **Who:** All sectors; DPRK-linked malvertising campaigns and unattributed threat actors confirmed active

---

**RECOMMENDED ACTIONS**

1. **Immediate:** Disable internet-facing Screen Sharing on macOS; require VPN or firewall rules if needed
2. **SharePoint:** Apply CVE-2026-50522 patches immediately; monitor audit logs for exploitation indicators
3. **vCenter:** Isolate from untrusted networks; apply vendor patches without delay
4. **IKE/VPN:** Audit IKE implementations; work with Cisco/Fortinet/other vendors on affected versions; rotate VPN credentials
5. **Detection:** Monitor for Monero miner traffic, unexpected root-level SSH, and suspicious vCenter API activity

---

**SOURCES**

- The Hacker News (breaking coverage, multiple reports)
- U.S. CISA Known Exploited Vulnerabilities catalog
- SecurityWeek, SecurityAffairs, Help Net Security, News4Hackers (corroborating reports)

**NOTE:** This alert synthesizes public headlines and CISA tracking data only. Specific technical indicators, affected product versions, and full exploit chains are not yet detailed in available public reporting. Status will update as details emerge.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-08-19-breaking-alert-posture.webp)