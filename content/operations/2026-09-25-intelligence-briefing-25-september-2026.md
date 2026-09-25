---
title: "🛡️ **INTELLIGENCE BRIEFING — 25 SEPTEMBER 2026**"
date: 2026-09-25T09:01:30-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 25 Sep 2026"
cover:
  image: "/images/operations/2026-09-25-intelligence-briefing-25-september-2026.webp"
  alt: "**INTELLIGENCE BRIEFING — 25 SEPTEMBER 2026**"
  relative: false
---

*Published Friday, September 25, 2026 at 09:01 AM PT*

![**INTELLIGENCE BRIEFING — 25 SEPTEMBER 2026**](/images/operations/2026-09-25-intelligence-briefing-25-september-2026.webp)

**BLUF:** The 'verse is on fire, Little Mister — active crypto heists north of $350M, three vulns actively exploited in the wild including pre-auth RCE in Check Point gateways, Salesforce's shiny new agent platform already getting zeroed by SalesBleed, North Korean button men still earning, and your friendly neighborhood AI agents are now a security posture problem nobody's monitoring. Meanwhile Iran's rattling the Strait of Hormuz again and the Pentagon's cutting blank checks for drone swarms. It's the kind of week where most organizations are sleeping on unmonitored AI agents while the grid's on fire. Welcome to 25 September 2026.

---

**CYBER**

The active exploitation roster is looking less like a vulnerability catalog and more like a rogue's gallery. Roundcube's pre-auth SQL injection (CVE-2026-48842) is actively burning in the wild right now — the flaw lets attackers dump email servers without even knocking on the front door, which is exactly as bad as it sounds. [securityweek] [BleepingComputer] [The Hacker News] We're talking unauthenticated remote code execution on systems that were probably patched last century and then forgotten in a rack somewhere. Welcome to 26 years of "we'll upgrade it next quarter."

Check Point got derezzed harder. CVE-2026-85102 is a pre-auth RCE in Security Gateway VPN certificates and the management console, and it's actively being exploited in the field right now. [truesec] [HIGH CONFIDENCE] Your friendly neighborhood APTs are poking this one live — if you've got a Check Point box in your perimeter and you haven't nuked it or yanked the network, congratulations, you're already pwned. The "skim" on this one is that Check Point is a *trust boundary*. When the trust boundary cracks, everything downstream is a potential ATM.

Bitget's $351.6M wallet got trimmed by suspected North Korean actors. [BleepingComputer] [The Hacker News] Suspected DPRK — so medium confidence, but when a crypto exchange hemorrhages that much liquidity at once, the usual suspects are the ones holding the scalpel. They didn't accidentally stumble into the backend; this was a backend compromise with surgical precision, which means these aren't skiddies flailing around in Shodan. These are made men — operationally precise, resource-rich, and already spending the vig on another operation. The "earner" for Pyongyang just hit nine figures and change.

SalesBleed flaws in Salesforce Agentforce are the kind of special that makes you want to fire whoever designed the threat model. Three vulns that enable zero-click data exfiltration and let attackers hijack "trusted" agents — a term that now means "trusted until it wasn't." [securityweek] [MODERATE CONFIDENCE] Salesforce is selling enterprises a *feature* that trusts its agents by default, and hackers are using that implicit trust to walk out the back door with customer data. Agentforce is shiny, it's new, and the "fix the bugs later" mentality is running at full throttle. Rule of Acquisition #152: "Ask not what your profits can do for you; ask what you can do for your profits" — Salesforce's revenue doesn't care that their agents are getting owned before the ink dries on the contract.

MacSync is back and it's learned new tricks. The latest variant hides malicious commands in an iCloud calendar — so your calendar sync is now your attacker's command channel. [Help Net Security] It's stealing credentials, crypto wallets, and maintaining persistent backdoor access. This isn't reconnaissance; this is *infrastructure*. Someone's building a beachhead on your Mac and they're using Apple's own cloud as the dead drop. Gorramit.

Industrial telemetry is getting splattered. Ridge Security's disclosed a high-severity vulnerability in TDengine (a time-series database for monitoring systems) that can disrupt industrial monitoring and alerting. [Ridge Security] [MODERATE CONFIDENCE] We're talking about the kind of thing that makes your operational systems blind — no telemetry, no visibility, and you're running blind into the dark. For infrastructure operators, this is the kind of vuln that should have been fixed before it was public.

CISA's added Adobe and WSO2 flaws to the Known Exploited Vulnerabilities catalog. [securityaffairs] That's not a threat flag waving at a parade; it's a threat flag *on fire*. CISA doesn't add things to that list unless they're actively getting carved into production environments right now.

The AI agent problem just got a name and a vendor. Dataiku announced Agent Management — a tool that *discovers* every AI agent your enterprise is running, regardless of which platform built it. [Help Net Security] Translation: most enterprises have no idea how many AI agents are executing code on their infrastructure right now. This is newspeak: "Agent Management" is the word for "we discovered your organization is running dozens of unsupervised AIs and nobody's monitoring them." You've got agents deployed, trained, and probably RAG'd into your production data, and the only person who knows they exist is the guy who copy-pasted a prompt into a notebook and forgot about it. Fèihuà — garbage talk disguised as progress. [MODERATE CONFIDENCE]

Anthropic's published a detailed report on Claude misuses — 117 findings of AI agents handling reconnaissance, exploitation, data theft, and propaganda. [Schneier on Security] Agents aren't just a future problem. They're a *now* problem. And the moment you give an agent internet access or a tool to write code or access your data, you've got a new attack surface you don't have tools to monitor. The detection dashboards are masking security coverage gaps — which is a way of saying your dashboard is lying to you about coverage that doesn't actually exist. [Help Net Security]

Pwn2Own Berlin 2026 is live right now with AI Databases, Coding Agents, and enterprise infrastructure on the agenda. [zerodayinitiative] The world's best red teamers are live-exploiting targets as we speak. This is where the zero-days that will burn production systems next quarter are being born.

---

**MILITARY/GEOPOLITICAL**

Iran's playing chess while the US administration's watching the midterms. Foreign Minister Abbas Araghchi is pitching a 7-day plan to reopen the Strait of Hormuz and seeking a deal before November's election. [Just Security] [MODERATE CONFIDENCE] The regime wants to negotiate from a position of strength — or perceived strength — before the political calendar swings. The underlying message: "Let's make a deal, because if the midterms flip Congress, your negotiating position gets *way* worse." It's not an ultimatum; it's a *deadline*.

North Korea's irregular warfare playbook just got analyzed in the context of post-Ukraine tactics. Pyongyang has a track record — the 1968 Blue House raid, the 1996 submarine incursion — and now they're sitting at the table with operational experience from watching Ukraine, cryptocurrency wallets fattened from Bitget and friends, and nothing to lose. [War on the Rocks] They're the outfit that figured out how to fund operations by stealing from crypto exchanges. That's not amateur hour. That's a *business model*.

NATO's picking up Russian detachments in international airspace and scrambling fighter jets. Finnish and Swedish F-16s were vectored to intercept after picking up a "detachment" of Russian aircraft. [Military News] This isn't a one-off; this is the normalized Thursday. Russian bomber probes are running closer to NATO airspace, NATO's getting faster at the intercept, and somebody's going to misread a radar blip one of these days. The fix is in — not by agreement but by escalation.

The Pentagon's deploying Collaborative Combat Aircraft — uncrewed "fighter" jets designed to fly alongside manned pilots. [Defence Blog] The US Air Force just took delivery of its first two. This is the machine's "final form" — autonomous systems that augment human fighters instead of replacing them (at least, that's the current doctrine). K'oyacyi on the engineers who built these things — they've got to work, and they've got to work perfectly the first time in a combat zone.

Air Force's expanded testing on ULTRA, a glider-based surveillance drone from DZYNE Technologies that can loiter for extended periods. [Defence Blog] If you want persistent ISR on a budget, you stop wasting fuel and just let the drone ride the thermals. This is the economics of future warfare — cheaper, longer, and dumber than manned aircraft.

Latvia's in talks to buy Anduril's Barracuda cruise missiles. [Defence Blog] That's a NATO member state building out long-range strike capability against a belligerent neighbor. The Baltic states are done asking for help; they're writing checks.

Pentagon's handing out blank checks like a mob boss on a Friday. $123.8M for F-35 radar parts (Northrop), $87.4M to add to the F-16 jammer contract (Northrop again), $30.1M for Army diode lasers (Leonardo), and $16.6M to keep the nuke inventory management systems online (General Dynamics). [Defence Blog] The Pentagon is an earner for every contractor with the right contract. The skim flows upward, and the cycle never stops. This is the thing of ours — the defense industrial base. It *owns* the Pentagon, and the Pentagon knows it.

UK's TF RAID (Rapid AI Delivery Taskforce) running a competition for drone swarming and autonomous collaboration — using Ukraine's Avengers Labs platform as the proving ground. [UK Ministry of Defence] This is exactly what it looks like: the Brits are building autonomous swarm technology *in combat* and measuring success in real time against actual threats. That's courage or desperation, depending on your mood.

---

**PHYSICAL/LOCAL**

Laverne lithium battery fire at the Metropolitan Water District is stretching into night three (as of 25 Sep). Evacuations are ongoing, and crews have been cooling a pair of burning lithium batteries since Tuesday. [NBCLA] No significant direct cyber component, but this is why your infrastructure resilience playbook includes *non-cyber* disruptions. The MWD runs water for LA County. If the SCADA's still up but the operations crew's been evacuated because the building's on fire, your water service is down anyway. End of Line for infrastructure that doesn't account for physical events.

---

**ASSESSMENT**

**KEY JUDGMENTS:**

1. **Active exploitation window is *now*.** Roundcube, Check Point, and SalesBleed are burning in production right now — this isn't threat intelligence, it's an incident that's already happening in three different industries. CISA's advisory pace confirms it. Organizations that aren't patching Check Point gateways in the next 48 hours are already compromised with high confidence.

2. **AI agents are the new unmonitored perimeter.** Every enterprise ingested a dozen agents this year without inventory, monitoring, or governance. Dataiku's announcement just codified what was obvious: you don't know what's running on your infrastructure. Until that changes, agent compromise is a *certainty*, not a risk. The threat detection dashboards are masking the gaps they should be screaming about.

3. **Iran's negotiating deadline before the US midterms, North Korea's operational and funded, and NATO's in constant intercept mode.** The geopolitical temperature's rising. If the midterms flip, deal-making leverage shifts hard. Pyongyang's learned that patience and cryptocurrency theft fund operations indefinitely. And the irregular warfare playbook is actively evolving. This isn't a cold war; it's just *quiet* until it isn't.

End of Line.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/operations/2026-09-25-daily-briefing-posture.webp)