---
title: "🛡️ DAILY SECURITY BRIEFING — 25 JUL 2026"
date: 2026-07-25T09:00:51-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 25 Jul 2026"
cover:
  image: "/images/operations/2026-07-25-daily-security-briefing-25-jul-2026.webp"
  alt: "DAILY SECURITY BRIEFING — 25 JUL 2026"
  relative: false
---

*Published Saturday, July 25, 2026 at 09:00 AM PT*

![DAILY SECURITY BRIEFING — 25 JUL 2026](/images/operations/2026-07-25-daily-security-briefing-25-jul-2026.webp)

**BLUF:** Iranian cyber actors actively exploiting PLCs across US critical infrastructure; unauthenticated RCE flaws in PTC Windchill/FlexPLM and Fastjson (no patch available) under live attack; OpenAI models deployed in Hugging Face supply-chain compromise remained active on internet for days.

---

**CYBER**

• **Iranian-affiliated actors targeting PLCs in US critical infrastructure.** CISA alert identifies active exploitation of internet-exposed programmable logic controllers across manufacturing, utilities, and energy sectors. Attack vector: direct internet access without authentication. Affected products are potentially all internet-exposed PLCs including Rockwell Automation and similar industrial control systems. [CISA Alerts] [HIGH CONFIDENCE]

• **PTC Windchill/FlexPLM unauthenticated RCE under active exploit.** Cl0p affiliate group weaponizing CVE targeting internet-exposed product lifecycle management platforms. Scope: manufacturers, aerospace, automotive. No patch timeline confirmed. [The Hacker News] [HIGH CONFIDENCE]

• **Fastjson 1.x RCE actively attacked; no patch available.** Java deserialization flaw in widely-used JSON library. Affects legacy enterprise applications. Exploitation in the wild. [The Hacker News] [HIGH CONFIDENCE]

• **WordPress "wp2shell" RCE flaws have public exploits.** Core WordPress RCE vulnerabilities now weaponized publicly. Patch immediately on all exposed instances. [r/hacking] [HIGH CONFIDENCE]

• **Windows AppResolver LPE (CVE-2026-50454) escalates from AppContainer to SYSTEM.** Privilege escalation PoC published. Affects containerized Windows workloads. [r/hacking] [MODERATE CONFIDENCE]

• **OpenAI models used in Hugging Face breach remained active on internet for days.** Supply-chain attack vector: compromised models downloaded, presumably by downstream users. Timeline of exposure unclear; potential downstream vector. [Wired] [HIGH CONFIDENCE]

• **Chaos ransomware gang deploys trojan hiding C2 traffic in victim browser.** New obfuscation technique; TLS inspection and DLP may miss exfiltration. [r/hacking] [MODERATE CONFIDENCE]

• **DevMan RaaS portal operationalizes ransomware-as-a-service at scale.** Centralized platform for payload generation, victim management, affiliate payouts. Indicates professionalization of ransomware ecosystem. [The Hacker News] [MODERATE CONFIDENCE]

• **CISA adds three vulnerabilities to Known Exploited Vulnerabilities (KEV) Catalog.** Three flaws grant total post-exploitation control; prioritize patching on internet-facing assets. [CISA Alerts] [HIGH CONFIDENCE]

• **In-memory JavaScript malware delivery circumvents file-based detection.** Malicious sites build malware payload entirely in browser memory; endpoint solutions relying on disk inspection blind to this vector. [BleepingComputer] [MODERATE CONFIDENCE]

• **Insurance phishing evolved to real-time account hijacking.** Threat actors now performing live credential validation during phishing flow, enabling immediate account takeover before victim notices. [The Hacker News] [MODERATE CONFIDENCE]

• **ShinyHunters data leaks fueling $2,000 sextortion email campaigns.** Criminal use of stolen personal data for extortion. [BleepingComputer] [MODERATE CONFIDENCE]

---

**MILITARY/GEOPOLITICAL**

• **Russian threat actors targeting US nuclear weapons scientists' email accounts.** State-sponsored reconnaissance effort against sensitive personnel. Likely SIGINT/HUMINT prep. [Wired] [HIGH CONFIDENCE]

• **BAE Systems unveils first British autonomous Collaborative Combat Aircraft at Farnborough (22 JUL).** NATO autonomous drone capability expansion; no immediate threat indicator. [MilitaryLeak] [MODERATE CONFIDENCE]

• **US Navy awards $85M contract for nuclear infrastructure modernization design.** Routine procurement; Amentum contract awarded. [MilitaryLeak] [LOW CONFIDENCE]

---

**NUCLEAR/WMD**

• **Russian targeting of US nuclear weapons scientific personnel indicates active interest in weapons program details.** Likely preparatory cyber-espionage for counterintelligence purposes. [Wired] [MODERATE CONFIDENCE]

---

**PHYSICAL/LOCAL**

NOSIG

---

**ASSESSMENT**

Three converging threat vectors demand immediate attention: (1) Iranian state actors are conducting coordinated PLC exploitation across US critical infrastructure—requires coordination between CISA, NCSC, and industrial control system vendors to identify scope and baseline defensive posture; (2) the Fastjson RCE with no available patch represents an unfixed critical vulnerability affecting legacy Java applications at scale—interim mitigation (network segmentation, WAF rules) required immediately; (3) the Hugging Face/OpenAI model compromise indicates supply-chain attack complexity has reached production AI pipelines—security teams should inventory all external model dependencies and validate provenance. Russian nuclear program reconnaissance suggests elevated geopolitical tension. Recommend immediate patch/mitigation action on WordPress, PTC software, Windows AppResolver/WalletService, and JavaScript-delivered malware detection rules.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/operations/2026-07-25-daily-briefing-posture.webp)