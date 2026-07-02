---
title: "🛡️ PRESIDENTIAL DAILY BRIEF — INFRASTRUCTURE SECURITY INTELLIGENCE"
date: 2026-06-25T09:01:17-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 25 Jun 2026"
cover:
  image: "/images/operations/2026-06-25-presidential-daily-brief-infrastructure-security-intelligenc.webp"
  alt: "PRESIDENTIAL DAILY BRIEF — INFRASTRUCTURE SECURITY INTELLIGENCE"
  relative: false
---

*Published Thursday, June 25, 2026 at 09:01 AM PT*

![PRESIDENTIAL DAILY BRIEF — INFRASTRUCTURE SECURITY INTELLIGENCE](/images/operations/2026-06-25-presidential-daily-brief-infrastructure-security-intelligenc.webp)

25 JUN 2026 | FOR: SENIOR SRE/INFRASTRUCTURE ENGINEER | LOS ANGELES, CA

─────────────────────────────────────────────────────────────────────────────

BLUF: Patch Chrome 149 and GitLab now; Akira ransomware affiliate active via novel exfiltration channel; device code phishing ecosystem (Kali365) at scale; Cal Water incident warrants Southern California water infrastructure awareness; internal host anomalies require immediate triage.

─────────────────────────────────────────────────────────────────────────────

CYBER

• Chrome 149 released with 18 vulnerability patches; majority are use-after-free defects with RCE potential. No confirmed in-the-wild exploitation reported as of 25 JUN, but use-after-free class historically weaponized within days of disclosure. Patch priority: HIGH. [SecurityWeek] [HIGH CONFIDENCE]

• GitLab CE/EE patched 13 vulnerabilities including 3 high-severity code execution and information disclosure flaws. Any self-hosted GitLab instance in CI/CD pipeline is an immediate patching target. [SecurityWeek] [HIGH CONFIDENCE]

• Akira ransomware affiliate observed using LimeWire-owned infrastructure as data exfiltration staging point — novel channel likely bypassing domain-blocklist-based DLP controls. Huntress investigation confirmed active campaign. Review egress logs for connections to LimeWire domains. [Huntress] [HIGH CONFIDENCE]

• Kali365 device code phishing ecosystem documented at scale. Threat actors abuse OAuth device code flow to harvest tokens without credential entry — bypasses MFA on M365, Azure AD. Huntress reports 8 million phishing emails in single campaign wave. Conditional Access policies blocking legacy auth and device code flows are the primary mitigation. [Huntress] [HIGH CONFIDENCE]

• ClickFix attack chain delivering Potemkin Loader + RMMProject RAT confirmed active. Post-compromise behavior includes browser credential theft, hidden RDP session establishment, lateral movement across 11+ hosts per incident. Entry vector: fake browser update / CAPTCHA prompt. [Huntress] [HIGH CONFIDENCE]

• Mistic backdoor linked to KongTuke threat cluster observed in ClickFix and ModeloRAT campaigns. Attribution to financially motivated actor; TTPs overlap with prior Eastern European cybercrime groups. [The Hacker News] [MODERATE CONFIDENCE]

• Gaslight macOS malware uses prompt injection to corrupt AI-assisted security analysis output — specifically targets LLM-based triage tools. Novel evasion technique; low immediate operational risk unless AI-assisted SOC tooling is in use. [The Hacker News] [MODERATE CONFIDENCE]

• Curl patched for 25-year-old vulnerability (medium/low severity) alongside 17 additional flaws. Not assessed as immediately critical but curl is near-universal in infrastructure tooling; update in next maintenance window. [SecurityWeek] [HIGH CONFIDENCE]

• Cockpit CMS version 359 RCE exploit published to Exploit-DB. If Cockpit is running anywhere in the environment, treat as actively exploitable. [Exploit-DB] [HIGH CONFIDENCE]

• Lantronix serial-to-IP converter CVE-2025-67038 (BRIDGE:BREAK research family) confirmed exploited in the wild against OT environments. Relevant if any serial-to-IP conversion devices exist on network edge or OT-adjacent segments. [SecurityWeek] [HIGH CONFIDENCE]

• CyberScoop reports 6-week undetected VPN dwell time in recent breach investigation — reinforces that patching alone does not remediate already-compromised endpoints. Relevant to current internal host anomaly investigation (see PHYSICAL/LOCAL). [CyberScoop] [HIGH CONFIDENCE]

• Zero Trust policy gap identified: AI agents operating under user-delegated tokens inherit full user permissions and are not captured by standard ZT policy enforcement. Relevant if any agentic AI tooling is deployed in production. [Netskope] [MODERATE CONFIDENCE]

─────────────────────────────────────────────────────────────────────────────

MILITARY / GEOPOLITICAL

• US awards Lockheed Martin $35B contract to quadruple THAAD interceptor production. Signals sustained elevated threat assessment for ballistic missile attack on CONUS and allied territory. [Defence Blog] [HIGH CONFIDENCE]

• UK successfully test-fired three low-cost deep-strike One Way Effectors (OWE) intended for Ukraine transfer; ground-launched, 500km+ range. Incremental escalation in Western long-range strike capability provision. [The Aviationist] [HIGH CONFIDENCE]

• Trump-Iran MOU under pressure within first week of 60-day negotiation window; Long War Journal analysis indicates concessions accumulating without reciprocal Iranian commitments. Diplomatic track fragility elevates risk of rapid posture change in CENTCOM AOR. [Long War Journal] [MODERATE CONFIDENCE]

• First US warship visit to Egypt's Berenice Naval Base on Red Sea recorded by CENTCOM. Signals US intent to expand Red Sea basing options amid continued Houthi maritime threat. [USCENTCOM] [HIGH CONFIDENCE]

• Ukraine sinks 3 Russian explosive drone boats via Bayraktar TB2 strikes, 23 JUN. Black Sea maritime corridor pressure continues; no direct CONUS infrastructure implication. [Defence Blog] [HIGH CONFIDENCE]

• EU Security & Defence Committee advancing hybrid warfare protection framework for critical infrastructure — 497 amendments under review 25 JUN. Relevant to allied posture alignment. [EU Security & Defence Committee] [HIGH CONFIDENCE]

• War on the Rocks analysis flags US Navy subsea rare earth supply chain vulnerability affecting Columbia-class SSBN production. Strategic-level risk; no immediate operational infrastructure impact. [War on the Rocks] [LOW CONFIDENCE — long-horizon risk]

─────────────────────────────────────────────────────────────────────────────

PHYSICAL / LOCAL (Southern California)

• Cal Water (California Water Service) confirmed cyberattack; threat actors claimed capability to disrupt water supply OT systems. Mandiant investigation found no evidence of OT system access or operational impact as of 25 JUN. Incident remains under investigation. [SecurityWeek] [HIGH CONFIDENCE]

• ASSESSMENT: Cal Water serves portions of Los Angeles County. No confirmed OT compromise, but the claim itself and the confirmed IT-layer breach indicate a threat actor with water utility targeting intent operating in the Southern California region. Awareness posture warranted.

• Internal perimeter: Elevated scanning activity blocked at perimeter. Internal host showing repeated port changes and high-severity behavioral alerts — pattern consistent with post-compromise lateral movement or active C2 beacon behavior. Requires immediate triage; do not assume this is noise. [ON-BOX POSTURE SUMMARY] [HIGH CONFIDENCE — anomaly confirmed, attribution TBD]

• Venezuela earthquakes (back-to-back, 25 JUN) — casualties reported. No California seismic correlation. NOSIG for local infrastructure. [Just Security]

─────────────────────────────────────────────────────────────────────────────

NUCLEAR / WMD

NOSIG. No IAEA reporting, test activity, or credible threat intelligence in current feed cycle.

─────────────────────────────────────────────────────────────────────────────

ASSESSMENT

The most operationally urgent items for this environment are: (1) the internal host anomaly — repeated port changes plus high-severity behavioral alerts in the context of an active ClickFix/RMMProject RAT campaign and documented 6-week VPN dwell times constitutes a credible active intrusion hypothesis until disproven; (2) Chrome 149 and GitLab patches, which should be treated as same-day given the RCE-class severity and historical weaponization timelines for use-after-free bugs; and (3) M365 device code phishing exposure — if Conditional Access is not blocking device code flow, the Kali365 ecosystem represents a near-term token-harvest risk at scale.

The Cal Water incident is the most significant regional development: no OT compromise confirmed, but a threat actor with demonstrated water utility targeting intent is operating in Southern California, and the IT breach vector remains uncharacterized. Monitor for CISA advisories specific to water sector ICS/SCADA in the coming 72 hours.

The Iran MOU fragility and THAAD production surge together indicate the US government's own threat calculus has not de-escalated despite diplomatic activity — infrastructure operators should maintain current resilience posture without relaxation.

─────────────────────────────────────────────────────────────────────────────

END OF BRIEF — 25 JUN 2026