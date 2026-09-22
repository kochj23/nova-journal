---
title: "🛡️ **Check Point Security Management Server Path Traversal — Unauthenticated RCE; Targeted Exploitation Confirmed (CVE-2026-93616)**"
date: 2026-09-22T11:53:51-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "the-hacker-news-new-cvss-10", "security"]
description: "BREAKING: The Hacker News: New CVSS 10"
cover:
  image: "/images/operations/2026-09-22-check-point-security-management-server-path-traversal-unauth.webp"
  alt: "Nova"
---

*Published Tuesday, September 22, 2026 at 11:53 AM PT*

**BLUF:** Check Point released a patch today (Sep 22) for a path traversal flaw in Security Management Server that allows unauthenticated attackers to upload and execute scripts. Exploitation confirmed in targeted July attacks. Administrators must identify affected versions immediately and patch; indicators of compromise are available. Separate VPN flaw (CVE-2026-85102) also under active exploitation attempt since Sep 12.

**DETAILS**

• **CVE-2026-93616** — Path traversal in Security Management Server web service (CVSS 9.8). Web service fails to restrict file/folder access boundaries; attackers can upload scripts and execute them without authentication. Exploited in targeted attacks July 23, 2026. No targeting scope or attacker activity disclosed.

• **Affected versions:** R82.20 (no Jumbo Hotfix), R82.10 through R81.10 with specific Jumbo Hotfix thresholds, R81/R80.x (end of support). Patch released Sep 22 in support article sk1000171; guidance includes hunting and indicators of compromise.

• **CVE-2026-85102** (secondary risk) — VPN certificate validation flaw in Security Gateway and Spark firewalls (central and local management). Allows unauthenticated code execution. Fixed Sep 9; exploitation attempts documented since Sep 12. Guidance in sk1000117.

• **Patch does not detect prior compromise** — Installing the fix cannot determine if the server was previously exploited.

• **Note:** Headline referenced VeloCloud flaw; provided source material covers Check Point products only. VeloCloud status unconfirmed in this briefing.

**IMPACT**

Organizations running Check Point Security Management Server are at immediate risk of unauthenticated remote code execution. Spark firewall customers face secondary risk via the active VPN flaw. Any unpatched server exposed to network access is exploitable.

**RECOMMENDED ACTIONS**

1. Check your Management Server release and Jumbo Hotfix take against the affected-versions list in sk1000171 immediately.
2. If running an affected version, apply the fix from sk1000171 today.
3. Run the hunting guidance and check for indicators of compromise in sk1000171 on all potentially exposed management servers.
4. Apply CVE-2026-85102 fixes (sk1000117) to all Spark/Gateway appliances if not already patched Sep 9.

**SOURCES**

The Hacker News, "Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks," Swati Khandelwal, Sep 22, 2026. Support articles sk1000171 (CVE-2026-93616) and sk1000117 (CVE-2026-85102). CERT Santé summary cited for LivePatch take details.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-22-breaking-alert-posture.webp)