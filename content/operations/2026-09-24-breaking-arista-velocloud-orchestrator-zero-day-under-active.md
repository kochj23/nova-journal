---
title: "🛡️ **BREAKING: Arista VeloCloud Orchestrator Zero-Day Under Active Attack — Maximum Severity**"
date: 2026-09-24T11:38:03-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "cso-online-on-prem-velocloud-orchestrato", "security"]
description: "BREAKING: CSO Online: On-prem VeloCloud Orchestrator under attack, only some versions patched"
cover:
  image: "/images/operations/2026-09-24-breaking-arista-velocloud-orchestrator-zero-day-under-active.webp"
  alt: "**BREAKING: Arista VeloCloud Orchestrator Zero-Day Under Active Attack — Maximum Severity**"
  relative: false
---

*Published Thursday, September 24, 2026 at 11:38 AM PT*

![**BREAKING: Arista VeloCloud Orchestrator Zero-Day Under Active Attack — Maximum Severity**](/images/operations/2026-09-24-breaking-arista-velocloud-orchestrator-zero-day-under-active.webp)

**BLUF:** Arista Networks' on-premises VeloCloud Orchestrator is actively being exploited via a CVSS 10.0 zero-day vulnerability affecting SD-WAN management deployments. Patches exist but not all vulnerable versions have been updated. Organizations running unpatched on-premises VCO must apply fixes immediately.

**DETAILS**

- **Vulnerability:** Maximum-severity (CVSS 10.0) flaw in on-premises VeloCloud Orchestrator enables remote attackers to gain unauthorized access to the SD-WAN management platform and its controlled edge devices.
- **Exploitability:** Active in-the-wild exploitation confirmed; certificate-based VCO configurations confirmed as attack vector.
- **Affected scope:** On-premises VCO deployments only; cloud-hosted instances status not explicitly confirmed in available material, though Arista's advisory applies to on-premises.
- **Patch status:** Arista has issued patches, but as of advisory, not all vulnerable versions have been remediated — deployment versions vary across customer installations.
- **Access implications:** Successful exploitation grants attackers direct access to the platform that orchestrates SD-WAN subscriptions and controls all connected edge appliances.

**IMPACT**

- Any organization operating unpatched on-premises VeloCloud Orchestrator deployments (version specifics not fully enumerated in public guidance to date).
- Compromised Orchestrator = control of SD-WAN network management and edge device fleet.
- Risk tier: Infrastructure-critical (SD-WAN is perimeter routing).

**RECOMMENDED ACTIONS**

- Identify which VeloCloud Orchestrator version(s) run in your environment immediately.
- Determine which versions are covered by Arista's published patches (consult Arista security advisory for version matrix).
- Apply patches to all on-premises VCO deployments without delay.
- Monitor VCO access logs and management console for unauthorized logins or configuration changes.
- If certificate-based authentication is configured, verify certificate integrity and audit revocation status.

**SOURCES**

CSO Online, The Hacker News, news4hackers, securityweek; Arista Networks security advisories.

---

*Alert status: CONFIRMED. Exploitation and patch availability confirmed across multiple reliable sources. Vulnerable version details remain incomplete in public disclosures; check Arista's advisory for your specific deployment version.*

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-24-breaking-alert-posture.webp)