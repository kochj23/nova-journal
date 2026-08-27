---
title: "🛡️ **ACTIVE ZERO-DAY IN PAPERCUT NG/MF — IMMEDIATE NETWORK ISOLATION REQUIRED**"
date: 2026-08-27T10:48:13-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "bleepingcomputer-papercut-warns-of-ng-mf", "security"]
description: "BREAKING: BleepingComputer: PaperCut warns of NG, MF flaw exploited in zero-day attacks"
cover:
  image: "/images/operations/2026-08-27-active-zero-day-in-papercut-ng-mf-immediate-network-isolatio.webp"
  alt: "**ACTIVE ZERO-DAY IN PAPERCUT NG/MF — IMMEDIATE NETWORK ISOLATION REQUIRED**"
  relative: false
---

*Published Thursday, August 27, 2026 at 10:48 AM PT*

![**ACTIVE ZERO-DAY IN PAPERCUT NG/MF — IMMEDIATE NETWORK ISOLATION REQUIRED**](/images/operations/2026-08-27-active-zero-day-in-papercut-ng-mf-immediate-network-isolatio.webp)

**BLUF:** PaperCut NG and MF print management software are under active remote exploitation via an unpatched zero-day affecting all currently supported versions. Australian vendor released emergency patches 28 August 2026 after confirming exploitation in customer environments. All organizations with internet-facing PaperCut servers must restrict network access to trusted IPs immediately; patching alone is insufficient as initial access vector remains unmitigated.

**DETAILS**

- **Confirmed active exploitation:** PaperCut's security team verified the flaw is being abused in the wild after a university customer's forensics team surfaced attack evidence. Emergency out-of-cycle builds released same day (v25 and v26 for Windows/Linux/macOS; v24 patch in progress).

- **All supported versions vulnerable:** No version number provides protection. Exposure is binary—either the server is isolated from the internet or it is at risk.

- **Remote access capability:** The urgency of the emergency response and same-day patch cycle indicates a remote code execution or equivalent critical path. Technical details remain under investigation and undisclosed.

- **No CVE assigned yet:** As of publication (28 August 2026), no formal CVE identifier has been registered. Attackers already have working exploits.

- **Prior history:** PaperCut suffered CVE-2023-27351 (auth bypass) in 2023, exploited by ransomware operators. That flaw appeared in CISA's Known Exploited Vulnerabilities catalog as recently as early 2026, signaling continued interest from threat actors.

**IMPACT**

- **Scope:** Every organization running internet-accessible PaperCut NG or MF in production (global user base includes enterprises, universities, government).
- **Attack surface:** Internet-facing Application Servers are primary targets; internal servers behind restrictive firewalls are lower-risk unless network segmentation is absent.
- **Post-exploitation risk:** Confirmed indicators include suspicious `pc-app.exe` process behavior, truncated/deleted `server.log` files, and specific database-related error strings. Absence of these artifacts does not confirm safety.

**RECOMMENDED ACTIONS**

1. **Immediate (next 2 hours):** All PaperCut NG/MF customers with public-internet-facing servers must enforce firewall rules restricting Application Server access to trusted internal IP ranges only. Do not wait for patches or incident detection.

2. **Urgent (today):** Upgrade to latest emergency builds (v25/v26 for supported versions). v24 customers should begin preparation for migration or standby for v24 patch.

3. **Investigation:** Search logs for indicators of compromise: pc-app.exe anomalies, missing server.log entries, "ERROR No suitable driver found for jdbc:no:x" or "ERROR DatabaseUtils Database error looking up cardID: VALUES CAST" messages. Escalate any findings immediately.

4. **Monitoring:** PaperCut plans to publish validated IOC indicators as investigation matures. Monitor for updates and maintain heightened detection sensitivity.

**SOURCES**

- PaperCut security bulletin (28 August 2026)
- CybersecurityNews / BleepingComputer reporting
- University customer incident forensics (initial discovery)

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-08-27-breaking-alert-posture.webp)