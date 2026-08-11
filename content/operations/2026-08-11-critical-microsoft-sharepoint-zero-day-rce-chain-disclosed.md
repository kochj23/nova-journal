---
title: "🛡️ **CRITICAL: Microsoft SharePoint Zero-Day RCE Chain Disclosed**"
date: 2026-08-11T10:28:50-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "rapid7", "security"]
description: "BREAKING: rapid7: : "
cover:
  image: "/images/operations/2026-08-11-critical-microsoft-sharepoint-zero-day-rce-chain-disclosed.webp"
  alt: "**CRITICAL: Microsoft SharePoint Zero-Day RCE Chain Disclosed**"
  relative: false
---

*Published Tuesday, August 11, 2026 at 10:28 AM PT*

![**CRITICAL: Microsoft SharePoint Zero-Day RCE Chain Disclosed**](/images/operations/2026-08-11-critical-microsoft-sharepoint-zero-day-rce-chain-disclosed.webp)

**BLUF:** Rapid7 and Microsoft today disclosed CVE-2026-63520 (remote code execution), the second vulnerability in a two-bug chain affecting Microsoft SharePoint. When chained with CVE-2026-55040, attackers can achieve unauthenticated RCE on vulnerable instances. **Immediate action:** Identify all SharePoint deployments; obtain patch status from Microsoft immediately; isolation/network segmentation for production instances pending patches.

---

**DETAILS**

- Rapid7 Labs zero-day research identified two SharePoint vulnerabilities that chain to achieve unauthenticated remote code execution. First CVE (CVE-2026-55040) disclosed previously by Rapid7 and Microsoft; second CVE (CVE-2026-63520) disclosed today concurrent with this alert.
- Attack chain does not require prior authentication; no valid user account needed to trigger RCE.
- Vulnerability affects Microsoft SharePoint (specific versions not yet detailed in available disclosures).
- Exploitation risk is elevated: Rapid7 has functional research code demonstrating the chain.
- **UNCONFIRMED:** Active in-the-wild exploitation; patch availability and timeline; affected SharePoint product versions (on-premises vs. online).

---

**IMPACT**

- **Affected:** All organizations running vulnerable Microsoft SharePoint instances (on-premises deployments presumed highest risk; Online status unclear pending Microsoft advisory).
- **Scope:** Internet-exposed or internal SharePoint servers accessible to any network-positioned attacker.
- **Risk:** Unauthenticated remote code execution as the SharePoint service account, leading to data theft, lateral movement, ransomware deployment.

---

**RECOMMENDED ACTIONS**

1. **Immediate (next 4 hours):** Inventory all Microsoft SharePoint deployments. Contact Microsoft Support for patch ETA and workaround guidance.
2. **Today:** Obtain Microsoft's official security advisory (CVE-2026-63520); confirm which versions are vulnerable.
3. **This week:** Apply patches as released by Microsoft. Pending patches, consider network segmentation (firewall rules restricting access to SharePoint), disable external access, or temporary shutdown of non-critical instances.
4. **Ongoing:** Monitor Microsoft Security Response Center (MSRC), Rapid7 Labs, and your SIEM for exploitation attempts (watch for unusual SharePoint service activity, code execution via OWSSVR.DLL or related processes).

---

**SOURCES**

- Rapid7 Labs disclosure (date: 2026-08-11)
- Microsoft (joint disclosure, same date)
- CVE-2026-63520 (RCE)
- CVE-2026-55040 (prior vulnerability in chain)

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-08-11-breaking-alert-posture.webp)