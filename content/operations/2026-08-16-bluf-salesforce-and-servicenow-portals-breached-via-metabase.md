---
title: "🛡️ **BLUF: Salesforce and ServiceNow Portals Breached via Metabase Zero-Day — 17-Month Exposure, Ongoing Exploitation**"
date: 2026-08-16T04:22:21-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "news4hackers-salesforce-servicenow-porta", "security"]
description: "BREAKING: news4hackers: Salesforce ServiceNow Portals Exposed 17 Months Metabase 0-Day Exploit"
cover:
  image: "/images/operations/2026-08-16-bluf-salesforce-and-servicenow-portals-breached-via-metabase.webp"
  alt: "**BLUF: Salesforce and ServiceNow Portals Breached via Metabase Zero-Day — 17-Month Exposure, Ongoing Exploitation**"
  relative: false
---

*Published Sunday, August 16, 2026 at 04:22 AM PT*

![**BLUF: Salesforce and ServiceNow Portals Breached via Metabase Zero-Day — 17-Month Exposure, Ongoing Exploitation**](/images/operations/2026-08-16-bluf-salesforce-and-servicenow-portals-breached-via-metabase.webp)

Attackers exploited a Metabase authentication bypass vulnerability to gain unauthenticated admin access to Salesforce and ServiceNow customer portals, exfiltrating sensitive data for at least 17 months before discovery. Exploitation is active in the wild. Organizations using Metabase or relying on Salesforce/ServiceNow integrations should audit access logs and update immediately.

---

**DETAILS**

- **Exposure window:** Salesforce and ServiceNow portals were accessible to unauthorized users for approximately 17 months prior to public disclosure. Most affected organizations remain unaware of the breach.
- **Attack vector:** Metabase zero-day vulnerability allows unauthenticated remote attackers to bypass authentication and gain full administrator-level access without credentials.
- **Active exploitation:** The vulnerability is being exploited in the wild by attackers using a custom toolset tracked as "City-Forum." At least one confirmed victim (Framework, San Francisco-based company) had customer data accessed via this path.
- **Data exfiltration:** Attackers gained access to admin panels and sensitive customer data across multiple organizations operating Salesforce, ServiceNow, or integrated Metabase instances.
- **Global scope:** The exposure affected organizations worldwide; the attack pattern suggests systematic reconnaissance and targeting rather than opportunistic compromise.

---

**IMPACT**

- Salesforce and ServiceNow users leveraging Metabase for analytics or reporting face admin-level compromise of their instances.
- Customer PII, transaction data, and proprietary business intelligence stored in these platforms is at risk.
- Affected organizations include enterprise customers across multiple verticals. Actual victim count is likely significantly higher than publicly confirmed cases due to the 17-month silence.
- Attackers have had extended access to sensitive data and may have installed persistence mechanisms.

---

**RECOMMENDED ACTIONS**

1. **Immediate:** Update Metabase to the latest patched version. Do not delay; active exploitation is ongoing.
2. **Audit:** Review authentication logs, admin account activity, and API access logs for the past 17 months. Flag anomalous logins, data exports, or configuration changes.
3. **Assume breach:** If your Metabase instance was exposed or internet-facing during this period, assume admin access was compromised. Rotate all admin credentials and API keys.
4. **Notify:** Alert customers and compliance teams if personal data or customer records were accessible via the affected portals.
5. **Segment:** Restrict Metabase network access to internal IPs or VPN; do not expose to the internet unless absolutely required.

---

**SOURCES**

- news4hackers; Help Net Security; SecurityWeek; SecurityAffairs
- Confirmed cases: Framework (San Francisco, design/manufacturing)
- Attack attribution: "City-Forum" custom toolset used in Salesforce/ServiceNow targeting campaigns

---

**STATUS:** CONFIRMED — patches available, exploitation active.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-08-16-breaking-alert-posture.webp)