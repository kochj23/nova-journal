---
title: "🛡️ **BREAKING: WP2Shell WordPress RCE Vulnerabilities Under Active Exploitation**"
date: 2026-07-20T02:44:02-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "news4hackers-wp2shell-wordpress-vulnerab", "security"]
description: "BREAKING: news4hackers: WP2Shell WordPress Vulnerabilities Exploited in the Wild"
cover:
  image: "/images/operations/2026-07-20-breaking-wp2shell-wordpress-rce-vulnerabilities-under-active.webp"
  alt: "**BREAKING: WP2Shell WordPress RCE Vulnerabilities Under Active Exploitation**"
  relative: false
---

*Published Monday, July 20, 2026 at 02:44 AM PT*

![**BREAKING: WP2Shell WordPress RCE Vulnerabilities Under Active Exploitation**](/images/operations/2026-07-20-breaking-wp2shell-wordpress-rce-vulnerabilities-under-active.webp)

**BLUF:** Two critical remote code execution vulnerabilities in WordPress Core (tracked as CVE-2026-*; specific CVE numbers not yet confirmed in available sources) are being actively exploited in the wild. WordPress site administrators should apply available patches immediately. Public exploits are circulating.

**DETAILS:**

- **Active exploitation confirmed:** Malicious activity targeting the vulnerabilities has been observed in operational environments shortly after disclosure.

- **RCE capability:** The flaws enable pre-authentication remote code execution, allowing attackers to execute arbitrary commands on affected WordPress installations without requiring valid credentials.

- **Public exploits available:** Exploit code has been released publicly, significantly lowering the barrier to attack and accelerating threat actor adoption.

- **Scope uncertain:** Sources reference "wp2shell" and "WP2Shell" designations inconsistently. The exact number of WordPress versions affected and whether this impacts WordPress Core or specific plugins requires clarification from official WordPress security advisories.

- **Related backdoor activity noted:** Separate reporting references WP-SHELLSTORM backdoor activity affecting thousands of WordPress sites, though direct connection to these CVE-2026 vulnerabilities is not yet established.

**IMPACT:**

- **Primary targets:** All WordPress site administrators running unpatched versions of affected Core releases.

- **Attack surface:** Pre-authentication RCE means attackers do not need valid site credentials or user accounts to compromise installations.

- **Scope:** Potentially widespread given WordPress's market dominance (~43% of all websites). Threat actors are actively scanning for and exploiting vulnerable instances.

**RECOMMENDED ACTIONS:**

1. **Immediate:** Apply WordPress Core security updates from wordpress.org/news/security/ if available for your version.

2. **Verify patch status:** Confirm your WordPress installation version and check official security advisories for applicable patches.

3. **Monitor:** Review access logs and file integrity for signs of compromise or shell uploads.

4. **If unpatched:** Consider taking affected sites offline or restricting access until patches are deployed.

**SOURCES:**

- BleepingComputer, SecurityWeek, SecurityAffairs, The Hacker News, Imperva, Help Net Security, news4hackers

**NOTE:** Specific CVE identifiers and affected version ranges require confirmation from official WordPress.org security channels. This alert will be updated as details are confirmed.