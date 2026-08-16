---
title: "🛡️ **BREAKING: Salesforce and ServiceNow Portals Exposed 17 Months; Metabase 0-day Under Active Exploitation**"
date: 2026-08-16T04:23:02-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "help-net-security-week-in-review", "security"]
description: "BREAKING: Help Net Security: Week in review"
cover:
  image: "/images/operations/2026-08-16-breaking-salesforce-and-servicenow-portals-exposed-17-months.webp"
  alt: "**BREAKING: Salesforce and ServiceNow Portals Exposed 17 Months; Metabase 0-day Under Active Exploitation**"
  relative: false
---

*Published Sunday, August 16, 2026 at 04:23 AM PT*

![**BREAKING: Salesforce and ServiceNow Portals Exposed 17 Months; Metabase 0-day Under Active Exploitation**](/images/operations/2026-08-16-breaking-salesforce-and-servicenow-portals-exposed-17-months.webp)

**BLUF:** Salesforce and ServiceNow customer portals have been exposed for approximately 17 months and are believed to have been exploited; simultaneously, a Metabase 0-day vulnerability is actively exploited in the wild. Immediate action required if your organization uses these platforms, particularly Salesforce or ServiceNow portal deployments. Exposure window is substantial — assume compromise and initiate incident response if you have not patched/blocked Metabase instances.

**DETAILS**

- **Exposure duration:** Salesforce and ServiceNow portals were left exposed for ~17 months before discovery/remediation — an extended attack window affecting multiple Fortune 500 customer bases.
- **Metabase 0-day in active use:** An unpatched zero-day vulnerability in Metabase is confirmed exploited; no official patch details publicly available yet (availability of fix unconfirmed in source material).
- **GitHub Dependabot expanded:** Malware detection now covers eight package ecosystems — npm (active since March 2026), PyPI, Maven, RubyGems, NuGet, Go, crates.io, PHP. Detection scope has broadened significantly.
- **Scope incomplete:** Source material is truncated; full extent of Salesforce/ServiceNow exposure (data types, customer count, exfiltration confirmed vs. suspected) not yet detailed in available summary.

**IMPACT**

- **Salesforce orgs:** Any customer using Salesforce portals during the 17-month window should assume potential unauthorized access, data exfiltration, or account compromise. Portal accounts, API tokens, credential materials at elevated risk.
- **ServiceNow instances:** Customers with public-facing ServiceNow portals in the same timeframe face similar exposure — configuration data, user records, workflow definitions may have been accessed.
- **Metabase deployments:** All unpatched Metabase instances (regardless of where running — cloud, on-prem, internal dashboards) are vulnerable to the 0-day. Analytics, embedded credentials, upstream database access potentially compromised.
- **Supply chain:** Dependent packages pulled from the eight ecosystems now being scanned may carry injected malware; organizations relying on automatic dependency updates face elevated risk of trojanized components.

**RECOMMENDED ACTIONS**

- **Immediate:** Patch or isolate all Metabase instances; block external access until confirmed patched. Check logs for exploitation attempts (watch for unauthorized dashboard/query access, admin account changes).
- **Salesforce/ServiceNow:** Force password resets for all portal users. Audit access logs for the 17-month period. Review OAuth token grants and API keys for anomalous usage. If breach confirmed, notify affected customers and regulators per compliance obligations.
- **Dependency management:** If using npm, PyPI, Maven, RubyGems, NuGet, Go, crates.io, or Composer (PHP), review recent package pulls against GitHub Dependabot malware alerts and your own supply-chain scanning.
- **Incident response:** If running any of these platforms in production, escalate to security team for breach assumption and forensics.

**SOURCES**

Help Net Security week-in-review compilation (week of ~Aug 16, 2026). Full article details pending; source material truncated in summary provided.

---

**STATUS:** Developing — full technical details (Metabase CVE number, Salesforce/ServiceNow root cause, data classifications affected) not yet available. Monitor Help Net Security, vendor security advisories, and CISA for patches and forensic findings.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-08-16-breaking-alert-posture.webp)