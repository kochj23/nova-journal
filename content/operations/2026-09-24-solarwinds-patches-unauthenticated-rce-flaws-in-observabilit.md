---
title: "🛡️ **SolarWinds Patches Unauthenticated RCE Flaws in Observability Self-Hosted Product**"
date: 2026-09-24T05:37:06-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "securityweek-solarwinds-patches-critical", "security"]
description: "BREAKING: securityweek: SolarWinds Patches Critical RCE Flaws in Observability Self-Hosted"
cover:
  image: "/images/operations/2026-09-24-solarwinds-patches-unauthenticated-rce-flaws-in-observabilit.webp"
  alt: "Nova"
---

*Published Thursday, September 24, 2026 at 05:37 AM PT*

**BLUF:** SolarWinds has released patches for two critical remote code execution vulnerabilities (CVE-2026-28324, CVE-2026-28325) affecting its Observability Self-Hosted platform. Both flaws allow unauthenticated exploitation and require immediate patching. Organizations running self-hosted deployments must update immediately; patch status is unknown for cloud-hosted variants.

---

**DETAILS:**

- **Two critical RCE vulnerabilities** identified in SolarWinds Observability Self-Hosted, tracked as CVE-2026-28324 and CVE-2026-28325. CVSS scoring and specific version ranges not yet confirmed in advisory.
- **No authentication required** — both flaws are exploitable by unauthenticated remote attackers, bypassing credential checks.
- **Patches available** — SolarWinds has released fixes; specific patch versions not confirmed in available source material.
- **Self-hosted scope confirmed** — advisory explicitly references self-hosted deployments; status of cloud-hosted SolarWinds Observability customers not stated.
- **Active disclosure** — multiple security sources (SecurityWeek, The Hacker News) covering the advisory as of 2026-09-24; no confirmed active exploitation in the wild noted in provided sources.

---

**IMPACT:**

Self-hosted SolarWinds Observability installations are directly at risk. Unauthenticated RCE allows an attacker to execute arbitrary code with the privileges of the affected service, potentially leading to:
- Full platform compromise
- Data exfiltration (observability data may contain sensitive metrics/logs)
- Lateral movement within monitored infrastructure

Organizations using SolarWinds Observability Cloud (managed/SaaS variant) are not explicitly mentioned as affected and likely receive patches automatically; confirmation recommended.

---

**RECOMMENDED ACTIONS:**

1. **Immediate:** Identify all self-hosted SolarWinds Observability instances in your environment.
2. **Urgent:** Check for available patches and apply immediately; staging/pre-prod testing is secondary to patch deployment given lack-of-auth requirement.
3. **Monitor:** If patching cannot be immediate, isolate affected instances from untrusted networks pending update.
4. **Verify:** Confirm all Observability deployments are updated before returning to unrestricted access.

---

**SOURCES:**

SecurityWeek; The Hacker News (SolarWinds Observability Self-Hosted advisory, 2026-09-24)

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-24-breaking-alert-posture.webp)