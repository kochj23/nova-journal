---
title: "🛡️ **Microsoft September 2026 Patch Tuesday — 964 CVEs, 104 Critical**"
date: 2026-09-08T17:21:56-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "tenable-blog-microsoft-s-september-2026-", "security"]
description: "BREAKING: Tenable Blog: Microsoft’s September 2026 Patch Tuesday addresses 964 CVEs (CVE-2026-81963, CVE-2026-"
cover:
  image: "/images/operations/2026-09-08-microsoft-september-2026-patch-tuesday-964-cves-104-critical.webp"
  alt: "**Microsoft September 2026 Patch Tuesday — 964 CVEs, 104 Critical**"
  relative: false
---

*Published Tuesday, September 08, 2026 at 05:21 PM PT*

![**Microsoft September 2026 Patch Tuesday — 964 CVEs, 104 Critical**](/images/operations/2026-09-08-microsoft-september-2026-patch-tuesday-964-cves-104-critical.webp)

BLUF: Microsoft released security patches addressing 964 vulnerabilities on September 2026 Patch Tuesday, including 104 Critical-severity issues (CVE-2026-81963, CVE-2026-85880, and others). Windows, .NET, and dependent services are affected. Patch and prioritize Critical CVEs immediately; deploy all updates within 30 days.

DETAILS:
- Microsoft's September 2026 Patch Tuesday covers 964 total CVEs: 104 rated Critical, 860 rated Important.
- Two CVEs confirmed in scope: CVE-2026-81963 and CVE-2026-85880; full advisory lists all identified vulnerabilities.
- .NET framework and associated Microsoft products confirmed affected; complete product/version mapping available in Microsoft Security Update Guidance.
- Patches available via Windows Update and Microsoft Update as of the September Patch Tuesday release.
- This represents a 2.4× increase from August 2026 (398 CVEs), continuing elevated disclosure volume in Microsoft's security posture.

IMPACT:
- All organizations running Windows systems, .NET applications, and Microsoft cloud services are potentially exposed.
- The 104 Critical-severity vulnerabilities present immediate exploitation risk in unpatched environments; proof-of-concept code typically appears within days of disclosure.
- Internet-facing services, remote access infrastructure, and cloud deployments relying on Microsoft components face highest risk of active exploitation.
- Delayed patching directly correlates with incident probability; Critical CVEs are prioritized by threat actors.

RECOMMENDED ACTIONS:
1. Inventory all Windows versions, .NET deployments, and Microsoft services in your environment immediately.
2. Apply all 104 Critical patches within 48 hours; use phased rollout for production systems requiring high availability.
3. Deploy Important-severity patches within 30 days, prioritizing those affecting internet-exposed or customer-facing systems.
4. Test patches in non-production first to identify compatibility issues before broad rollout.
5. Enable enhanced security event logging and EDR monitoring during patching to detect exploitation attempts.
6. Verify completeness: confirm all systems received patches and validate via security scanning tools.

SOURCES:
- Tenable Blog: "Microsoft's September 2026 Patch Tuesday Addresses 964 CVEs" (CVE-2026-81963, CVE-2026-85880)
- Microsoft Security Updates official advisory

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-08-breaking-alert-posture.webp)