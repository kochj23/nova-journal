---
title: "🛡️ PRESIDENTIAL DAILY BRIEF — INFRASTRUCTURE & THREAT INTELLIGENCE"
date: 2026-06-23T09:01:19-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 23 Jun 2026"
cover:
  image: "/images/operations/2026-06-23-presidential-daily-brief-infrastructure-threat-intelligence.webp"
  alt: "PRESIDENTIAL DAILY BRIEF — INFRASTRUCTURE & THREAT INTELLIGENCE"
  relative: false
---

*Published Tuesday, June 23, 2026 at 09:01 AM PT*

![PRESIDENTIAL DAILY BRIEF — INFRASTRUCTURE & THREAT INTELLIGENCE](/images/operations/2026-06-23-presidential-daily-brief-infrastructure-threat-intelligence.webp)

23 JUN 2026 | FOR: SENIOR SRE/INFRASTRUCTURE ENGINEER | LOS ANGELES, CA

---

BLUF: Russian IAB "FortiBleed" campaign has captured 110M+ credentials via active Fortinet exploitation since Feb 2026; simultaneously, Miasma supply chain campaign now targets AI coding assistant session tokens — both represent direct risk to production credential stores and developer pipelines.

---

**CYBER**

- **FortiBleed Campaign [ACTIVE EXPLOITATION]:** Russian initial access broker deploying custom credential sniffer against Fortinet devices; 110M+ credentials captured since at least Feb 2026. Targets unpatched SSL-VPN and management interfaces. Patch status of any perimeter Fortinet gear requires immediate verification. [SecurityWeek] [HIGH CONFIDENCE]

- **Miasma Supply Chain Campaign:** Stolen session cookies used as initial access vector; campaign has escalated to persistence files targeting AI coding assistants — Claude Code, Cursor, Gemini CLI, VS Code. Developer credential underground market confirmed as downstream distribution channel. If any of these tools are in use in your pipeline, session token stores warrant audit. [Tenable] [HIGH CONFIDENCE]

- **Unpatched SharePoint RCE — Multi-Attacker Intrusion:** Microsoft post-incident analysis confirms two unrelated threat actors simultaneously operated inside a single victim network via unpatched SharePoint. Entry vector: known CVEs with available patches. Indicates opportunistic mass-scanning, not targeted ops. Inventory any internet-facing SharePoint instances. [CSO Online / Microsoft] [HIGH CONFIDENCE]

- **FFmpeg "PixelSmash" RCE:** Crafted media files trigger RCE in any application using FFmpeg's libavcodec. Scope: video players, media servers, NAS appliances. Plex (see LOCAL INFRASTRUCTURE below) is a confirmed libavcodec consumer. Patch status unknown pending upstream release. [SecurityWeek] [HIGH CONFIDENCE]

- **Drupal Core 10.5.5 — Error-Based SQL Injection:** Public PoC published Exploit-DB 23 JUN. Any Drupal instance at this version is now at elevated risk of automated exploitation. [Exploit-DB] [HIGH CONFIDENCE]

- **DPRK LNK + GitHub C2 Campaign:** North Korean-attributed actors using Windows LNK files with GitHub repositories as command-and-control infrastructure. Targets developer environments. Consistent with Miasma-era targeting of engineering workstations. [Fortinet FortiGuard] [MODERATE CONFIDENCE]

- **Five Eyes AI Threat Warning:** Alliance-level advisory states frontier AI model-enabled cyberattacks are "months away." No specific CVE or campaign attached. Noted for planning horizon. [Five Eyes / SecurityWeek] [MODERATE CONFIDENCE]

- **EO — Post-Quantum Cryptography:** Trump signed EO 23 JUN mandating federal agencies migrate high-value assets to PQC by end of 2030; high-impact systems by 2031. No immediate operational action required for private sector, but sets procurement and compliance trajectory. [SecurityWeek]

---

**MILITARY / GEOPOLITICAL**

- **US-Iran Ceasefire — Fragile:** Ceasefire announced following Switzerland talks. VP Vance describes progress as "very, very good." Iran publicly rebutted US characterization of terms. Cipher Brief analysis: agreement emerged despite narrow observable bargaining space; durability assessed as low without comprehensive settlement. [Cipher Brief / Just Security] [MODERATE CONFIDENCE]

- **Cuba SIGINT Array — CDAA Upgrade Complete:** CSIS confirmed 18 JUN that Cuba has completed replacement of older linear antenna grid with Circularly Disposed Antenna Array (CDAA) — a direction-finding system optimized for signals intelligence collection. Assessed as significant upgrade to coverage of US southeastern communications. [Cipher Brief / CSIS] [HIGH CONFIDENCE]

- **NATO Eastern Flank Hardening:** Estonia received first IRIS-T SLM medium-range air defense battery 22 JUN. Netherlands conducting 7,000-troop exercise incorporating Ukrainian-developed anti-drone tunnel doctrine. Both indicate accelerated NATO conventional deterrence posture. [Defence Blog] [HIGH CONFIDENCE]

- **US Pacific Force Posture — Okinawa:** Navy chartered four civilian roll-on/roll-off vessels for Okinawa amphibious operations. Marines in Okinawa simultaneously received NMESIS anti-ship and counter-drone systems. Consistent with sustained Indo-Pacific access-denial posture buildup. [Defence Blog / Task & Purpose] [HIGH CONFIDENCE]

- **Ukraine — Foreign Recruitment Licensing:** Ukraine Defense Minister Fedorov announced licensing of private military recruitment from global labor market to fill infantry shortfalls. Signals manpower pressure despite continued drone campaign effectiveness against Russian air defenses. [Defence Blog]

- **B-52 Crash — Test Community Impact:** USAF B-52 involved in fatal crash was on radar test sortie. Human and programmatic impact on B-52 modernization program noted. [The War Zone] — operational detail only, no threat vector.

---

**PHYSICAL / LOCAL (Los Angeles / SoCal)**

- **Deputy-Involved Shooting — Homeless Suspect:** LA County Sheriff's deputies fatally shot a knife-wielding homeless man following a stabbing incident. Suspect identified posthumously. No broader threat pattern indicated. [Local wire] NOSIG for infrastructure purposes.

- **Political Violence / Platform Narrative Risk:** Just Security analysis flags online platforms as infrastructure for escalating political violence narratives. Relevant to physical security planning for any public-facing facilities or events in the current domestic threat environment. [Just Security] [LOW CONFIDENCE — no specific SoCal nexus]

- No credible physical threats to Southern California critical infrastructure identified in last 24h. NOSIG.

---

**NUCLEAR / WMD**

- **Iran Nuclear Status — Ambiguous:** Trump stated publicly his red line was Iranian nuclear weapons capability; ceasefire framing centered on preventing nuclear breakout. No IAEA reporting of resumed enrichment activity in last 24h. Ceasefire fragility (see MILITARY) means this section warrants continued monitoring. [Cipher Brief] [MODERATE CONFIDENCE]

- No test activity, IAEA emergency reporting, or WMD-related SIGINT indicators in last 24h. Otherwise NOSIG.

---

**LOCAL INFRASTRUCTURE (YOUR ENVIRONMENT)**

- **[CRITICAL] Services Down — Plex, SearXNG, TinyChat:** Three services confirmed down. Plex is a direct exposure surface for FFmpeg PixelSmash RCE (see CYBER). Outage may be crash-related (20 crash_storm events in syslog) or indicative of resource exhaustion. Restore after confirming FFmpeg patch status or network isolation. Priority: do not restore Plex to internet-facing state until PixelSmash patch is applied or mitigated.

- **[WARNING] Possible Kernel-Level Rootkit — `pi`:** Wazuh flagged rootkit indicators on host `pi`. Threat score 11.0. Requires triage before this host is trusted for any sensitive operation. Recommended: offline forensic check, integrity verification against known-good baseline. Do not use `pi` as a jump host or credential store until cleared.

- **[WARNING] Correlated Security Events — `nuk`:** 5 correlated events, threat score 5.0. 6,204 SSH events on `nuk` in last 24h is anomalously high — warrants review of auth logs for brute-force or successful unauthorized access. Cross-reference with FortiBleed credential exposure (see CYBER).

- **`wazuh.manager` Threat Score 45.0:** Highest score in environment. Manager nodes accumulate score from aggregated detections, but this level warrants review to confirm score is detection-artifact vs. compromise of the SIEM itself. A compromised SIEM manager is a blind-spot generator.

- **`itunes` Threat Score 20.0:** Elevated. Source and nature of events not specified in feed. Flag for review — developer workstations are primary Miasma campaign targets.

- **Sensitive Access Events: 8 | IPS Events: 2 | Firewall Blocks: 2:** Low volume, but sensitive_access events require log review given active credential-harvesting campaigns in threat environment.

---

**KEY JUDGMENTS**

The convergence of the FortiBleed credential-harvesting campaign and the Miasma AI-assistant session-token attack represents a two-vector threat to developer pipeline integrity: perimeter credentials and local workstation tokens are being harvested simultaneously by separate, likely unrelated actors, indicating broad opportunistic targeting of engineering environments. The `pi` rootkit indicator and anomalous SSH volume on `nuk` are the highest-priority internal items and must be triaged before either host is used in any privileged capacity. The US-Iran ceasefire reduces near-term kinetic escalation risk to regional infrastructure but remains structurally fragile; the Cuba CDAA upgrade is a persistent, long-duration SIGINT threat to US communications with no immediate mitigation available at the operator level.