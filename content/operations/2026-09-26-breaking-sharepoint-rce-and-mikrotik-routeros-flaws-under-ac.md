---
title: "🛡️ BREAKING: SharePoint RCE and MikroTik RouterOS Flaws Under Active Exploitation"
date: 2026-09-26T05:47:39-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "the-hacker-news-sharepoint-rce-and-mikro", "security"]
description: "BREAKING: The Hacker News: SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild"
cover:
  image: "/images/operations/2026-09-26-breaking-sharepoint-rce-and-mikrotik-routeros-flaws-under-ac.webp"
  alt: "BREAKING: SharePoint RCE and MikroTik RouterOS Flaws Under Active Exploitation"
  relative: false
---

*Published Saturday, September 26, 2026 at 05:47 AM PT*

![BREAKING: SharePoint RCE and MikroTik RouterOS Flaws Under Active Exploitation](/images/operations/2026-09-26-breaking-sharepoint-rce-and-mikrotik-routeros-flaws-under-ac.webp)

**BLUF:** Microsoft SharePoint and MikroTik RouterOS critical remote code execution flaws are actively exploited in the wild. Two SharePoint CVEs (CVE-2026-45659, CVE-2026-50522) enable authenticated RCE with machine key theft; MikroTik CVE-2026-67276 SSH zero-day enables unauthenticated router takeover. Both are now tracked in CISA's Known Exploited Vulnerabilities catalog. Organizations running either product must patch immediately; public proof-of-concept code is available.

---

## DETAILS

- **SharePoint RCE (CVE-2026-45659, CVE-2026-50522):** Authenticated remote code execution flaws in Microsoft SharePoint initially misclassified as spoofing issues. Active exploitation confirmed; attackers stealing machine keys and achieving code execution. Public PoC published, triggering rapid CISA KEV addition.

- **MikroTik RouterOS SSH Zero-Day (CVE-2026-67276):** Unauthenticated SSH vulnerability in MikroTik RouterOS enabling complete router compromise. Attackers actively exploiting to hijack routers and gain network infrastructure control. Multiple new flaws in RouterOS being exploited concurrently.

- **CISA Tracked:** Both SharePoint and MikroTik flaws formally added to CISA's Known Exploited Vulnerabilities catalog, confirming government-level threat assessment and active in-the-wild exploitation.

- **Attack Surface:** SharePoint impact limited to authenticated users but grants kernel-level code execution and credential theft; MikroTik impact universal across exposed router interfaces (potentially WAN-facing).

---

## IMPACT

**Organizations affected:**
- All Microsoft SharePoint deployments (on-premises and hybrid)
- All MikroTik RouterOS deployments (RouterOS 7.x, 6.x currently reported)
- Supply chain: network infrastructure operators and ISPs managing MikroTik devices

**Scope:** Active exploitation by multiple threat actors; no attribution to single group. Likely rapid adoption across threat landscape given public PoC and CISA advisory.

---

## RECOMMENDED ACTIONS

1. **Immediate (next 24h):**
   - SharePoint: Audit authentication logs for suspicious authenticated sessions; isolate machines with exported machine keys
   - MikroTik: Restrict SSH to authenticated/VPN-only access; isolate WAN-exposed RouterOS devices pending patch

2. **Within 72h:**
   - Deploy latest Microsoft SharePoint security updates (patch KB numbers TBD in advisory)
   - Apply MikroTik RouterOS patch (v7.x / v6.x critical releases) or disable SSH if patching delayed

3. **Ongoing:**
   - Monitor CISA KEV catalog for additional MikroTik flaws; assume multi-vulnerability exploitation chain
   - Hunt for machine key export artifacts in SharePoint logs and file systems

---

## SOURCES

- The Hacker News: "SharePoint RCE and MikroTik RouterOS Flaws Actively Exploited in the Wild"
- CISA Known Exploited Vulnerabilities Catalog (SharePoint CVE-2026-45659, CVE-2026-50522; MikroTik CVE-2026-67276)
- BleepingComputer: "Critical SharePoint RCE flaw exploited to steal machine keys"
- Multiple vendor advisories: MikroTik Security Advisories; Microsoft Security Update Guides

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-26-breaking-alert-posture.webp)