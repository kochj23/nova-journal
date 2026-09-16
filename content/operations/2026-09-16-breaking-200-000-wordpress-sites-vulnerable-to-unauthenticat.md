---
title: "🛡️ **BREAKING: 200,000+ WordPress Sites Vulnerable to Unauthenticated RCE in Critical Plugin**"
date: 2026-09-16T11:36:20-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "news4hackers-200-000-wordpress-sites-at-", "security"]
description: "BREAKING: news4hackers: 200,000+ WordPress Sites at Risk of Hacking Due to Unauthenticated RCE Vulnerabilities"
cover:
  image: "/images/operations/2026-09-16-breaking-200-000-wordpress-sites-vulnerable-to-unauthenticat.webp"
  alt: "**BREAKING: 200,000+ WordPress Sites Vulnerable to Unauthenticated RCE in Critical Plugin**"
  relative: false
---

*Published Wednesday, September 16, 2026 at 11:36 AM PT*

![**BREAKING: 200,000+ WordPress Sites Vulnerable to Unauthenticated RCE in Critical Plugin**](/images/operations/2026-09-16-breaking-200-000-wordpress-sites-vulnerable-to-unauthenticat.webp)

**BLUF:** A critical remote code execution (RCE) vulnerability in a widely deployed WordPress plugin exposes 200,000+ sites to unauthenticated takeover. No authentication required to trigger exploitation. Patch immediately; if patching is delayed, disable the affected plugin.

**DETAILS:**

- **Vulnerability class:** Unauthenticated Remote Code Execution in WordPress plugin
- **Affected scope:** 200,000+ WordPress installations confirmed at risk
- **Attack vector:** Requires no user credentials or authentication; exploitable remotely
- **Plugin identification:** Widely deployed plugin; news sources reference The Events Calendar plugin specifically in related disclosures (confirmation of which plugin is primary subject pending full source review)
- **Exploit status:** Vulnerability disclosed; exploitation likelihood is HIGH given RCE severity and unauthenticated access

**IMPACT:**

- **Affected parties:** Site owners running the vulnerable plugin version; users of those sites; backend infrastructure
- **Attack scope:** Complete site takeover, malware injection, data theft, credential harvesting, malware distribution to site visitors
- **Blast radius:** 200,000+ WordPress instances; WordPress represents ~43% of all web sites globally
- **Related activity:** Memory logs indicate StopAndProtect malware campaign has leveraged ~2,000 compromised WordPress sites for data theft and malware spread; additional waves probable if this RCE remains unpatched

**RECOMMENDED ACTIONS:**

1. **Immediate:** Identify WordPress plugin inventory in your environment
2. **Priority 1 (next 24–48h):** Update the affected plugin to patched version or disable it entirely if patch is unavailable
3. **Priority 2:** Monitor access logs for exploitation attempts (POST requests to plugin paths, 200 responses from suspicious IPs)
4. **Priority 3:** If compromised, reset all admin credentials, audit user accounts, scan for web shells

**SOURCES:**

- news4hackers (200,000+ WordPress Sites RCE alert)
- SecurityWeek (Unauthenticated RCE / Events Calendar coverage)
- Hacker News (WordPress plugin/theme flaws, StopAndProtect campaign)
- Nova threat memory (multi-source aggregation)

*Note: Full CVE identifier and exact plugin name confirmation pending source document access. This alert confirms RCE + unauthenticated + scale as reported; patching guidance applies regardless of plugin name.*

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-16-breaking-alert-posture.webp)