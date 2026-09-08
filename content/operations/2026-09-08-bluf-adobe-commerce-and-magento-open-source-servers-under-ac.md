---
title: "🛡️ **BLUF: Adobe Commerce and Magento Open Source servers under active exploitation — unauthenticated remote code execution via zero-day StyleSmuggler attack. Immediate patching required; monitor for indicators of compromise.**"
date: 2026-09-08T05:17:43-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "cso-online-adobe-commerce-max-severity-b", "security"]
description: "BREAKING: CSO Online: Adobe Commerce max-severity bug comes under active attack"
cover:
  image: "/images/operations/2026-09-08-bluf-adobe-commerce-and-magento-open-source-servers-under-ac.webp"
  alt: "**BLUF: Adobe Commerce and Magento Open Source servers under active exploitation — unauthenticated remote code execution via zero-day StyleSmuggler attack. Immediate patching required; monitor for indicators of compromise.**"
  relative: false
---

*Published Tuesday, September 08, 2026 at 05:17 AM PT*

![**BLUF: Adobe Commerce and Magento Open Source servers under active exploitation — unauthenticated remote code execution via zero-day StyleSmuggler attack. Immediate patching required; monitor for indicators of compromise.**](/images/operations/2026-09-08-bluf-adobe-commerce-and-magento-open-source-servers-under-ac.webp)

---

**DETAILS**

- **Vulnerability:** Adobe Commerce and Magento Open Source are affected by a maximum-severity zero-day flaw (CVE-2026-71362) that allows unauthenticated attackers to execute arbitrary code on vulnerable servers.

- **Attack vector:** Threat actors abuse Magento's Style properties to inject malicious code, bypassing existing input validation safeguards. The attack has been nicknamed "StyleSmuggler" by security firm Sansec.

- **Active exploitation confirmed:** Multiple security firms (Sansec, SecurityWeek, securityaffairs) report exploitation attempts and active attacks in the wild. Exploitation began immediately or very shortly after public disclosure.

- **Scope:** All online stores and web properties running Adobe Commerce or Magento Open Source without patches are at risk. No authentication required for the attack to succeed.

- **Patch status:** Unknown from provided material whether Adobe has released a patch; only exploitation and discovery are confirmed.

---

**IMPACT**

Online retailers and merchant platforms running Adobe Commerce or Magento Open Source face immediate risk of data theft (customer payment cards, PII), ransomware deployment, malware injection, or complete site compromise. The low barrier to entry (no authentication required) and active exploitation in the wild significantly increase attack probability.

---

**RECOMMENDED ACTIONS**

1. **Immediate:** Check whether your organization runs Adobe Commerce or Magento Open Source. If yes, classify as critical priority.

2. **Monitor:** Search web-accessible logs, WAF logs, and intrusion detection systems for suspicious HTTP requests containing Style property payloads or unusual code execution patterns.

3. **Patch:** Obtain and deploy available patches from Adobe as soon as confirmed. If none are yet available, consider temporary WAF rules to block suspicious Style-based requests or disable Style properties if operationally feasible.

4. **Assess:** Review recent access logs and database activity for signs of unauthorized code execution or data exfiltration.

---

**SOURCES**

- CSO Online (Adobe Commerce max-severity bug comes under active attack)
- SecurityWeek (Adobe Commerce Bug Targeted Immediately After Disclosure; CVE-2026-71362)
- Sansec (StyleSmuggler threat identification)
- securityaffairs (CVE-2026-71362 active exploitation reports)
- BleepingComputer (SAP Commerce Cloud related CVE tracking)

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-08-breaking-alert-posture.webp)