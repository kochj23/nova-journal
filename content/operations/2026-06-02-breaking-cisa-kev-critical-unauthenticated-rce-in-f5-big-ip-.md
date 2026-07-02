---
title: "🚨 BREAKING: CISA KEV — Critical Unauthenticated RCE in F5 BIG-IP (CVE-2026-0826) Under Active Exploitation — Patch Immediately"
date: 2026-06-02T14:58:49-07:00
draft: false
categories: ["operations"]
tags: ["breaking", "alert", "cisa", "kev", "addition"]
description: "BREAKING: CISA KEV Addition — CVE-2026-0826 Critical Unauthenticated RCE in F5 BIG-IP"
cover:
  image: "/images/operations/2026-06-02-breaking-cisa-kev-critical-unauthenticated-rce-in-f5-big-ip-.webp"
  alt: "BREAKING: Critical RCE in F5 BIG-IP"
  relative: false
---

![BREAKING: Critical RCE in F5 BIG-IP](/images/operations/2026-06-02-breaking-cisa-kev-critical-unauthenticated-rce-in-f5-big-ip-.webp)

---

**BLUF:** A critical unauthenticated remote code execution vulnerability in F5 BIG-IP (CVE-2026-0826, CVSS 9.8) is being actively exploited in the wild. All organizations running BIG-IP versions prior to 17.1.2 are affected. Apply the F5 patch immediately.

---

## DETAILS

- **Vulnerability:** Unauthenticated stack buffer overflow in the F5 BIG-IP iControl REST API. A remote, unauthenticated attacker can send a crafted request to achieve arbitrary code execution on the management plane — no credentials required.
- **Affected versions:** F5 BIG-IP all versions prior to 17.1.2. Scope of impact across older supported branches (16.x, 15.x) is **not confirmed in provided reporting** — organizations on those branches should treat themselves as at risk pending F5 clarification.
- **Exploitation timeline:** Rapid7 observed in-the-wild exploitation within 24 hours of public disclosure. This is consistent with the accelerated weaponization pattern seen across recent high-profile network appliance CVEs.
- **CISA action:** CVE-2026-0826 has been added to the CISA Known Exploited Vulnerabilities (KEV) catalog today, triggering mandatory remediation deadlines for U.S. federal civilian executive branch (FCEB) agencies under BOD 22-01.
- **Patch status:** F5 has released a patch. Version 17.1.2 is confirmed as the remediated release.

---

## IMPACT

- **Who is affected:** Any organization with F5 BIG-IP appliances running software versions prior to 17.1.2 — particularly those with the iControl REST API exposed to untrusted networks or the internet.
- **Scope:** F5 BIG-IP is widely deployed across enterprise, financial services, government, and critical infrastructure environments as an application delivery controller and load balancer. Compromise of BIG-IP can provide attackers with a privileged network position, enabling lateral movement, traffic interception, and credential harvesting.
- **Exploitation maturity:** Active exploitation confirmed within 24 hours of disclosure. Assume exploit code is broadly available.
- **Note:** Attribution of active exploitation to specific threat actors is **not confirmed** in current reporting.

---

## RECOMMENDED ACTIONS

1. **Patch immediately.** Upgrade all F5 BIG-IP instances to version 17.1.2 or later. Prioritize internet-facing and management-plane-exposed devices.
2. **Restrict iControl REST API access.** If patching cannot be completed immediately, restrict access to the iControl REST API to trusted management networks only via ACLs or firewall rules. F5 has historically documented this as a viable interim mitigation — verify current F5 guidance for this CVE.
3. **Audit exposure.** Identify all BIG-IP instances in your environment and confirm whether the management interface or iControl REST API is reachable from untrusted networks.
4. **Hunt for compromise.** Review BIG-IP access logs for anomalous API activity, unexpected process execution, or configuration changes — particularly for activity in the 24-hour window following public disclosure.
5. **FCEB agencies:** Remediation is mandatory under BOD 22-01. Confirm your KEV remediation deadline with your CISO.

---

## SOURCES

- Rapid7 (active exploitation reporting)
- CISA Known Exploited Vulnerabilities Catalog (KEV addition, confirmed)
- F5 Security Advisory (patch confirmed: BIG-IP 17.1.2)

---

*Behavior on older supported BIG-IP branches (16.x, 15.x) not confirmed in available reporting. Monitor F5 advisory for full version matrix.*