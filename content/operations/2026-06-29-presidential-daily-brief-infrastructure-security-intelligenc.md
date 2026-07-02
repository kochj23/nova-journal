---
title: "🛡️ PRESIDENTIAL DAILY BRIEF — INFRASTRUCTURE & SECURITY INTELLIGENCE"
date: 2026-06-29T09:01:01-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 29 Jun 2026"
cover:
  image: "/images/operations/2026-06-29-presidential-daily-brief-infrastructure-security-intelligenc.webp"
  alt: "PRESIDENTIAL DAILY BRIEF — INFRASTRUCTURE & SECURITY INTELLIGENCE"
  relative: false
---

*Published Monday, June 29, 2026 at 09:01 AM PT*

![PRESIDENTIAL DAILY BRIEF — INFRASTRUCTURE & SECURITY INTELLIGENCE](/images/operations/2026-06-29-presidential-daily-brief-infrastructure-security-intelligenc.webp)

29 JUN 2026 | FOR: SENIOR SRE/INFRASTRUCTURE ENGINEER | LOS ANGELES, CA

BLUF: Oracle PeopleSoft zero-day exploitation is active and widening; patch or isolate all PeopleSoft and Oracle E-Business Suite instances immediately.

---

CYBER

- Oracle PeopleSoft zero-day actively exploited. NAIC (National Association of Insurance Commissioners) confirmed breach; ShinyHunters claims 3.1 TB exfiltrated. Nissan separately confirmed payroll records and SSNs exposed via same attack vector. Two confirmed victims in 24h window suggests broad scanning campaign underway. [SecurityWeek, The Register] [HIGH CONFIDENCE]

- Oracle E-Business Suite critical flaw now under active exploitation. Distinct from PeopleSoft vector; CISA added to KEV catalog. Any internet-exposed Oracle EBS instance should be treated as compromised pending patch verification. [BleepingComputer, CISA]

- CISA added three vulnerabilities to KEV catalog 28-29 JUN. Specific CVEs not fully enumerated in feed; check catalog directly. Remediation deadline applies to federal agencies under BOD 22-01; treat as priority signal for production systems. [CISA]

- DirtyClone Linux kernel LPE disclosed. Variant of DirtyFrag; unprivileged local users can manipulate page cache to gain root. Affects production Linux hosts. Patch status unclear; assess kernel versions across fleet. [SecurityWeek] [HIGH CONFIDENCE]

- CVE-2026-55200 (libssh2) public PoC released. Client-side SSH flaw; exploitation now within reach of low-sophistication actors. Any service or automation using libssh2 for outbound SSH connections is exposed. [The Hacker News]

- FortiBleed campaign active per ACSC advisory. Australian Cyber Security Centre flagging active exploitation of Fortinet firewall/VPN gateways. Campaign name suggests credential/memory exposure. Relevant to any Fortinet edge devices in stack. [ACSC] [HIGH CONFIDENCE]

- Supply chain: hijacked npm and Go packages deploying Python infostealer via VS Code Tasks. Attack vector targets developer workstations. Audit recent dependency updates; review VS Code task configurations in CI/CD pipelines. [The Hacker News]

- 119 malicious Microsoft Edge extensions removed. Malware concealed in images and fonts. If Edge is in use on any managed endpoints, audit extension inventory. [The Hacker News]

- Ransomware actors exploiting unpatched SimpleHelp RMM to compromise utility billing software provider. CISA advisory. If SimpleHelp is in environment, patch immediately; CVE is KEV-listed. [CISA Alerts]

- P2Pinfect targeting misconfigured Kubernetes clusters. Fortinet analysis describes enroll-and-dormant pattern — compromised nodes may not exhibit immediate malicious behavior. Audit K8s RBAC and exposed API surfaces. [Fortinet FortiGuard]

- CI/CD-to-Redshift attack chain documented ("Shai Hulud"). Persistence established in CI/CD pipeline leads to cloud data store exfiltration. Relevant to any AWS Redshift-backed analytics infrastructure. [Fortinet FortiGuard]

---

MILITARY / GEOPOLITICAL

- US-Iran ceasefire holding after second exchange of strikes. US struck Iranian coastal targets following attack on commercial vessel; both sides agreed to stand down and continue negotiations. Iranian government claims billions in frozen assets to be unfrozen. Strait of Hormuz shipping risk reduced short-term; situation remains fragile. [The Aviationist, live news] [MODERATE CONFIDENCE on durability]

- Pentagon reviewing all US military forces in Europe. SecDef Hegseth has initiated formal review; Tomahawk missile contracts already cancelled per reporting. Timing 8 days before NATO Ankara Summit is significant. Trump's 5% GDP defense spending demand creating alliance fracture risk. [War on the Rocks, live news]

- China-Russia joint air incursion into South Korean ADIZ, 27 JUN. Approximately 10 combined aircraft entered and exited Korean Air Defense Identification Zone. Seoul scrambled fighters. Pattern consistent with probing and normalization of joint operations. [Defence Blog] [HIGH CONFIDENCE]

- Armed Russian LNG carrier operating in Baltic near NATO waters. Vessel previously docked Rotterdam; now fitted with heavy machine guns. Potential hybrid warfare asset; relevant to undersea cable and energy infrastructure threat picture. [live news]

- Russia "passportization" campaign in occupied Ukraine assessed as hybrid warfare tool. Systematic citizenship manipulation used to manufacture legal pretexts and embed personnel. [Just Security]

- France arrested four alleged Chinese intelligence operatives living in a rural village. Suggests deep-cover network, not diplomatic-adjacent. Ongoing European CI sweep. [intelNews]

- Hegseth purge of senior US military officers: 24+ officers removed, representing 900+ combined years of experience. Just Security analysis draws parallel to Red Army purges of 1937. Institutional readiness degradation risk. [Just Security] [MODERATE CONFIDENCE on operational impact timeline]

---

PHYSICAL / LOCAL (LOS ANGELES / SOCAL)

- FIFA World Cup matches ongoing with LA as host city. US DOJ seized hundreds of illegal streaming domains in enforcement action. Elevated crowd density at SoFi Stadium and surrounding infrastructure on match days. Expect traffic, transit, and cellular congestion. [BleepingComputer, live news]

- Venezuela 4.8-magnitude earthquake, offshore. No SoCal seismic relevance. NOSIG for local infrastructure.

- No credible physical threat reporting for Southern California in this cycle. NOSIG.

---

NUCLEAR / WMD

- NOSIG. No IAEA reporting, test activity, or credible WMD threat signals in this cycle.

---

ASSESSMENT

**KEY JUDGMENTS:**

The Oracle PeopleSoft/E-Business Suite exploitation cluster represents the highest-priority patching action this cycle — two confirmed high-profile victims in under 24 hours indicates an active, opportunistic campaign likely scanning for all exposed instances, not targeted operations; any internet-reachable Oracle application tier should be treated as a priority remediation target before end of business 29 JUN. The DirtyClone LPE combined with the libssh2 public PoC creates a viable local-to-root-to-lateral-movement chain on Linux hosts, particularly dangerous in containerized or shared-tenant environments where the threat model assumes kernel isolation. The NATO Ankara Summit (approx. 07 JUL) and the fragile US-Iran ceasefire are the two geopolitical tripwires most likely to generate rapid cyber or infrastructure escalation within the next 10 days; monitor for retaliatory Iranian cyber activity against US financial and energy sectors if negotiations collapse.

---

*Classification: UNCLASSIFIED // FOR INTERNAL USE // 29 JUN 2026 0600Z*