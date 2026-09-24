---
title: "🛡️ **CRITICAL: Check Point Security Gateway & Management Server Actively Exploited**"
date: 2026-09-23T23:33:37-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "cso-online-check-point-hacked", "security"]
description: "BREAKING: CSO Online: Check Point hacked"
cover:
  image: "/images/operations/2026-09-23-critical-check-point-security-gateway-management-server-acti.webp"
  alt: "**CRITICAL: Check Point Security Gateway & Management Server Actively Exploited**"
  relative: false
---

*Published Wednesday, September 23, 2026 at 11:33 PM PT*

![**CRITICAL: Check Point Security Gateway & Management Server Actively Exploited**](/images/operations/2026-09-23-critical-check-point-security-gateway-management-server-acti.webp)

Check Point Security Gateway and Security Management products are under active exploitation. Multiple critical vulnerabilities—including unauthenticated remote code execution and full admin privilege escalation in SmartConsole—are being exploited in the wild. Affected organizations must patch immediately or implement strict network access controls on management interfaces until patches are available.

**DETAILS:**

• Check Point has disclosed active exploitation of multiple vulnerabilities in Security Gateway and Security Management products; attackers are gaining unauthorized access to critical perimeter infrastructure

• At minimum two distinct critical flaws confirmed: (1) 9.8-severity VPN Certificate vulnerabilities enabling unauthenticated remote code execution, and (2) SmartConsole admin privilege escalation accessible to unauthenticated attackers  

• CVE-2026-93616 (Management Server Zero-Day) confirmed actively exploited in targeted attacks

• These products serve as primary firewall and perimeter defense for enterprises—compromise grants attackers direct control over network ingress/egress and management plane

**IMPACT:**

Organizations running Check Point Security Gateway or Security Management infrastructure face immediate risk. Successful exploitation grants attackers:
- Remote code execution on security gateways (firewall bypass)
- Unauthenticated full administrative access to SmartConsole management
- Ability to modify firewall rules, disable protections, or pivot into internal networks
- Complete visibility and control over network traffic

Active exploitation indicates real-world attacks are occurring now against public and private sector enterprises.

**RECOMMENDED ACTIONS:**

1. **IMMEDIATE:** Apply patches for Security Gateway and Security Management when available from Check Point. Monitor Check Point advisories and CISA for patch release status and CVE details.

2. Review Security Gateway and Management Server access logs for indicators of compromise: unauthenticated admin logins, unusual rule modifications, or atypical management traffic.

3. Verify firewall rule integrity and check for unauthorized changes.

4. **If patching is delayed:** Implement strict network access controls limiting management interfaces (SmartConsole, management API ports) to trusted administrator IPs only. Segment management infrastructure from production networks if possible.

5. Monitor for additional CVE disclosures; Check Point has indicated multiple vulnerabilities are involved.

**SOURCES:**

- CSO Online — "Check Point hacked: The security software protecting your network has become a prime attack target"
- SOC Prime — "CVE-2026-93616: Check Point Management Server Zero-Day Exploited in Targeted Attacks"
- The Hacker News — "Check Point Warns of Management Server Zero-Day Exploited in Targeted Attacks"

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-09-23-breaking-alert-posture.webp)