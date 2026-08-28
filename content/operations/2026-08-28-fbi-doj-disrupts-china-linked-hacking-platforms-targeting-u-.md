---
title: "🛡️ **FBI/DOJ Disrupts China-Linked Hacking Platforms Targeting U.S. Critical Infrastructure**"
date: 2026-08-28T16:57:42-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "r-hacking-justice-department-and-fbi-sei", "security"]
description: "BREAKING: r/hacking: Justice Department and FBI Seize Platforms Operated and Used by China State-Sponsored Hac"
cover:
  image: "/images/operations/2026-08-28-fbi-doj-disrupts-china-linked-hacking-platforms-targeting-u-.webp"
  alt: "**FBI/DOJ Disrupts China-Linked Hacking Platforms Targeting U.S. Critical Infrastructure**"
  relative: false
---

*Published Friday, August 28, 2026 at 04:57 PM PT*

![**FBI/DOJ Disrupts China-Linked Hacking Platforms Targeting U.S. Critical Infrastructure**](/images/operations/2026-08-28-fbi-doj-disrupts-china-linked-hacking-platforms-targeting-u-.webp)

**BLUF:** U.S. federal law enforcement has seized multiple hacking platforms (QScan, QTRouter, QTFY) operated by China-linked state-sponsored actors who conducted sustained intrusions against NASA, DOE, U.S. Senate, and critical infrastructure. Organizations should immediately audit network logs and IoT/infrastructure devices for indicators of these tools' presence and remediate any detected foothold.

**DETAILS**

- FBI and Department of Justice coordinated seizure of Chinese state-sponsored hacking infrastructure used for persistent access to U.S. federal agencies and critical infrastructure operators.

- Confirmed compromised entities include NASA, Department of Energy, U.S. Senate, U.S. military networks, and unnamed critical infrastructure sectors—scope of compromise remains under investigation.

- Primary attack platforms identified as QScan and QTRouter (proxy/scanning tools for reconnaissance and lateral movement); a related infrastructure suite designated QTFY also disrupted.

- The platforms were used for initial network access, enumeration, persistence, and data exfiltration; operational timeline spans multiple years.

- FBI action includes platform seizure and public attribution to China-linked state-sponsored threat actors—court authorization obtained; infrastructure dismantled or neutralized.

**IMPACT**

- **Federal agencies:** Immediate risk to NASA, DOE, Senate networks from persistent backdoors; additional agencies likely affected but not yet disclosed.

- **Critical infrastructure:** Energy, communications, and other CISA-designated sectors exposed; unknown which organizations remain compromised.

- **Data breach scope:** Confirmed exfiltration of classified and sensitive data; full contents and recipients not yet public—assume adversary retained copies.

- **Ongoing operations:** Seizure disrupts current C2 traffic but does not guarantee removal of implants already deployed; affected orgs may have dormant backdoors.

**RECOMMENDED ACTIONS**

1. **Immediate (today):** Check network logs from 2024–present for connections to QScan/QTRouter domains and IP ranges (full IOC list expected from CISA/FBI within 24–48 hours).

2. **IoT/infrastructure scan:** Audit routers, industrial control systems, and appliances for unauthorized remote access tools or unusual process execution—these platforms target less-patched edge devices.

3. **Incident investigation:** If your org supplies DOE, NASA, energy, or Senate infrastructure, contact FBI's IC3 or your sector's ISAC immediately to determine if you are on the affected customer list.

4. **Credential reset:** Assume some administrative credentials for affected systems are compromised; rotate all high-privilege account passwords on affected networks.

**SOURCES**

- r/hacking (post, 2026-08-28)
- Multiple confirmed outlets: The Register, Help Net Security, SecurityAffairs, Wired, CyberScoop, SecurityWeek, The Hacker News
- Attribution: China-linked state-sponsored threat actors (DOJ/FBI official statement)
- Status: **Active disruption; agencies expected to release full indicators within 48 hours.**

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-08-28-breaking-alert-posture.webp)