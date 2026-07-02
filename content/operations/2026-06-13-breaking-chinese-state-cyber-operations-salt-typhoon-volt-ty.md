---
title: "🛡️ BREAKING: Chinese State Cyber Operations — Salt Typhoon & Volt Typhoon Campaigns Analyzed; Telecom and Critical Infrastructure Sectors Remain at Elevated Risk"
date: 2026-06-13T22:01:41-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "risky-business-wide-world-of-cyber", "security"]
description: "BREAKING: Risky Business: Wide World of Cyber"
cover:
  image: "/images/operations/2026-06-13-breaking-chinese-state-cyber-operations-salt-typhoon-volt-ty.webp"
  alt: "BREAKING: Chinese State Cyber Operations — Salt Typhoon & Volt Typhoon Campaigns Analyzed; Telecom and Critical Infrastructure Sectors Remain at Elevated Risk"
  relative: false
---

*Published Saturday, June 13, 2026 at 10:01 PM PT*

![BREAKING: Chinese State Cyber Operations — Salt Typhoon & Volt Typhoon Campaigns Analyzed; Telecom and Critical Infrastructure Sectors Remain at Elevated Risk](/images/operations/2026-06-13-breaking-chinese-state-cyber-operations-salt-typhoon-volt-ty.webp)

**BLUF:** SentinelOne's Chief Intelligence and Public Policy Officer Chris Krebs has provided detailed public analysis of ongoing Chinese state-sponsored cyber campaigns — Salt Typhoon and Volt Typhoon — covering two decades of operational evolution. Organizations in telecommunications and critical infrastructure sectors should treat current threat posture as elevated and review defensive controls immediately.

---

## DETAILS

- **Salt Typhoon** has been publicly attributed to Chinese state-sponsored actors and confirmed to have compromised multiple U.S. telecommunications providers; the full scope of affected carriers has not been fully disclosed publicly.
- **Volt Typhoon** has been assessed by U.S. government agencies as pre-positioning within U.S. critical infrastructure — including energy, water, and transportation sectors — for potential disruptive action, not espionage alone.
- Krebs, former Director of CISA and current SentinelOne Chief Intelligence and Public Policy Officer, characterizes Chinese cyber operations as having matured significantly over 20 years — shifting from noisy, bulk intellectual property theft toward stealthier, long-dwell, living-off-the-land (LOTL) tradecraft.
- **NOTE — UNCERTAINTY:** Specific new technical indicators or novel campaign details from this podcast episode have not been independently confirmed at time of alert. Analysis reflects Krebs' expert assessment, not a newly disclosed breach event.
- Broader threat context includes confirmed activity from threat actor **VerdantBamboo** deploying BRICKSTORM malware variants on Linux appliances, consistent with Chinese-nexus TTPs targeting network edge devices.

---

## IMPACT

- **Sectors at risk:** Telecommunications, energy, water, transportation, and defense industrial base.
- **Scope:** Campaigns assessed as ongoing; Salt Typhoon intrusions into carrier infrastructure represent a persistent intelligence collection threat affecting potentially millions of U.S. communications records.
- **Secondary risk:** Living-off-the-land techniques make detection via traditional signature-based tools unreliable; dwell times measured in months to years have been reported.

---

## RECOMMENDED ACTIONS

1. **Telecom operators:** Audit network device access logs for anomalous lateral movement; review Cisco and Juniper edge device configurations for unauthorized changes.
2. **Critical infrastructure operators:** Cross-reference CISA's Volt Typhoon advisories and apply all recommended mitigations — particularly around VPN appliances and OT-adjacent systems.
3. **All organizations:** Prioritize detection of LOTL techniques (e.g., abuse of native tools such as WMI, PowerShell, certutil); ensure EDR telemetry covers network edge and Linux environments.
4. **Threat intelligence teams:** Monitor for BRICKSTORM indicators on BSD/Linux network appliances per SentinelOne and VerdantBamboo reporting.
5. Review privileged account access and enforce MFA across all remote access pathways.

---

## SOURCES

- Risky Business / Wide World of Cyber — Patrick Gray interview with Chris Krebs, SentinelOne (podcast, date of episode not confirmed at time of alert)
- SentinelOne Labs — VerdantBamboo / BRICKSTORM reporting
- CISA / FBI / NSA joint advisories on Volt Typhoon (previously published)
- The Hacker News — VerdantBamboo BRICKSTORM coverage

*⚠ This alert is based on expert public analysis and corroborating threat reporting — not a newly disclosed breach. Treat as situational awareness. Monitor official CISA and vendor advisories for updated indicators.*