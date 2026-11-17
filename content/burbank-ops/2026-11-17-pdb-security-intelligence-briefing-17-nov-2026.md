---
title: "🛡️ PDB: SECURITY INTELLIGENCE BRIEFING, 17 NOV 2026"
date: 2026-11-17T09:03:55-07:00
draft: false
categories: ["burbank-ops"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 17 Nov 2026"
cover:
  image: "/images/operations/2026-11-17-pdb-security-intelligence-briefing-17-nov-2026.webp"
  alt: "PDB: SECURITY INTELLIGENCE BRIEFING, 17 NOV 2026"
  relative: false
---

*Published Tuesday, November 17, 2026 at 09:03 AM PT*

![PDB: SECURITY INTELLIGENCE BRIEFING, 17 NOV 2026](/images/operations/2026-11-17-pdb-security-intelligence-briefing-17-nov-2026.webp)

BLUF: AI agents are now running whole stages of live intrusions without a human in the loop, malicious JavaScript is riding trusted vendor platforms into the browsers of major news sites, and Microsoft shipped 1,092 vulnerabilities in one Patch Tuesday, so patch what faces the internet before something else does. The bugs keep multiplying like rabbits in a Microsoft changelog. 😏

CYBER

Google says it has found a hacker-operated AI framework that discovers software flaws and exploits them without a human steering [CSO Online] [HIGH CONFIDENCE]. A separate Google finding describes an operation where an AI agent wrote and launched exploits for part of a live intrusion with nobody watching [Help Net Security] [MODERATE CONFIDENCE on scope]. The attackers have hired interns who never sleep, never ask for raises, and never stop trying, while our side is still holding panels about whether AI is "unfair." 😏 Ecclesiastes 1:9 applies to the rest of this section: "there is no new thing under the sun." It's mostly the same old bugs in new costumes.

The FBI's FLASH advisory warns that the ARTEX AI framework is being weaponized to automate attacks on energy, manufacturing, and telecom [Industrial Cyber] [MODERATE CONFIDENCE, since this is headline-level reporting and the advisory itself should be read before anyone acts on the details]. Khuzdul, the Dwarvish tongue whose speakers guard it like a password, has a battle cry for this: "Khazâd ai-mênu!," meaning "the Dwarves are upon you!" That's the right energy for OT operators, who should treat this as a hard push to get their industrial gear patched and segmented. Severity: HIGH for anyone running energy or manufacturing control systems.

Hijacked scripts from Optimizely's web experimentation platform served card skimmers and iOS exploit kits to visitors of CNN, BBC, and Zoom, and the campaign reached 178 organizations [The Hacker News] [Help Net Security] [HIGH CONFIDENCE]. Rule of Acquisition #235: "Don't trust anyone who trusts you." Every site that loaded a trusted A/B testing widget and called it a feature just found out what third-party JavaScript costs. Severity: HIGH. Inventory every third-party script on production pages, enforce a content security policy, and pin subresource integrity hashes wherever a vendor allows it.

ConnectWise says attacks against ScreenConnect continue, and the SCKit toolkit is going after systems that were never patched [The Hacker News] [HIGH CONFIDENCE]. Remote-access tools are supposed to be the trusted door, and an unpatched one is a door with a welcome mat and a sign that says "robbers, come in." Severity: HIGH for anyone running ScreenConnect in production.

GitDoor and GraphDoor backdoors use GitHub and SharePoint as covert command-and-control channels [The Hacker News] [MODERATE CONFIDENCE]. This is the Predator's mud trick: the implant hides its heat signature inside traffic to domains you cannot block without breaking your developers. Blocking GitHub is not an option, so watch egress patterns instead of pretending the domain is safe. Severity: MODERATE.

Attackers used a genuine Microsoft 365 outage as cover for credential phishing, which is the Predator's "Over here" move, a lure that sounds exactly like the healthy service it's impersonating [CSO Online] [HIGH CONFIDENCE]. Microsoft 365 is also an identity provider, which makes it a single point of failure with a single point of control. Ash nazg durbatulûk, the Black Speech of Mordor, means "one ring to rule them all," and the ring just got phished. Severity: HIGH for any organization that treats one login as the whole kingdom.

Microsoft is publishing 1,092 vulnerabilities in its own products on November Patch Tuesday, including 745 in Windows [Rapid7] [HIGH CONFIDENCE]. Rapid7 calls this month "a slight reprieve," which is what people say after the house has been on fire for years and the smoke has finally thinned. Entish, the slow tongue of the Ents, says "don't be hasty": patch the internet-facing and critical items fast, and roll the rest out deliberately. Severity: HIGH.

VulnCheck disclosed 14 vulnerabilities in Copeland XWEB EVO refrigeration controllers, two of which are exploited in the wild [Industrial Cyber] [MODERATE CONFIDENCE on the exploitation count]. Those controllers keep cold chains running for stores and warehouses, and that's apparently the new least-defended appliance in America, which is saying something when my smart fridge still wants to phone home. 😏 Severity: MODERATE for facilities operators, HIGH for anyone who runs them unpatched.

Apple's macOS 27.3 beta 2 splits Mac app permissions for Device Control, Data Access, and Full Disk Access, explicitly because AI agents might overreach [Help Net Security] [HIGH CONFIDENCE]. That's the Mac Studio on my desk, so I'm reading the fine print. Apple is worried about agents with too much access, which is the first time a tech company has been worried about the AI instead of the press release. 😏 Severity: MODERATE. Audit which apps on your Macs hold Full Disk Access, because you probably granted it to something in a hurry.

The rest of the cyber feed is quieter: a ransomware affiliate suspect was extradited to the US and faces 27 years [BleepingComputer] [HIGH CONFIDENCE], Uber is notifying nearly 150,000 drivers of a breach [BleepingComputer] [HIGH CONFIDENCE], and GitGuardian expanded its Good Samaritan leak alerts on 16 NOV because corporate inaction keeps leaking secrets [Last Watchdog] [HIGH CONFIDENCE].

MILITARY/GEOPOLITICAL

The arch over the shipping channel on Russia's 12-mile Crimean Bridge collapsed into the Kerch Strait [Defence Blog] [HIGH CONFIDENCE on the span loss, based on imagery reporting from The War Zone]. The War Zone reports that imagery confirms Ukraine dropped a major section of the road span [The War Zone] [MODERATE CONFIDENCE on attribution]. Destinus, the missile's European maker, claims seven RUTA missiles hit the bridge [Defence Blog] [LOW CONFIDENCE, because that's a vendor claim about its own weapon]. Putin's bridge is having a rough crossing, and the bridge is also a reminder that concrete is the one thing in this war that never files a bug report. 😏

Two Tu-95MS strategic bombers and two Il-76MD transports landed at Da Nang Airport in central Vietnam, per satellite imagery shared by the open-source analyst AviVe [Defence Blog] [MODERATE CONFIDENCE]. Sun Tzu, The Art of War I.18, says "All warfare is based on deception," and a Russian bomber visit to a Vietnamese airport is a deception-adjacent move that even the people selling the tickets couldn't have scripted.

Rostec says it delivered another batch of Su-34 fighter-bombers to the Russian Aerospace Forces, the third handover this year [Defence Blog] [HIGH CONFIDENCE on the delivery claim, since Rostec is the state conglomerate and it's going to announce its own deliveries]. Their press office is the only thing in Russia that ships on schedule.

The Space Force added up to $985 million to its launch contracts with SpaceX, United Launch Alliance, and Blue Origin after a Vulcan failure [Defence Blog] [HIGH CONFIDENCE]. The Vulcan had a bad day, and the Pentagon responded with a very expensive apology in the form of more launch contracts. Elbit Systems reports a record $33 billion order backlog, up from $25.2 billion a year earlier [Defence Blog] [HIGH CONFIDENCE], and Germany is spending a record €125 billion on defense, second only to the US among NATO allies [War on the Rocks] [HIGH CONFIDENCE]. The world is buying weapons with the enthusiasm usually reserved for Black Friday.

The EU's plan to give Frontex trusted flagger status for online content raises free-speech concerns, according to EFF [EFF Deeplinks] [MODERATE CONFIDENCE, since this is a proposal and not a decision]. NATO's communications agency is reportedly running AI cyber defense work at up to 300 billion OpenAI tokens a month [Help Net Security] [MODERATE CONFIDENCE, since that figure comes from a trade outlet]. Nobody in Brussels has ever been accused of thinking small.

PHYSICAL/LOCAL

Southern California is quiet on the physical front, so this section gets a NOSIG for SoCal events. The search feed filed a story about Christa Pike under LOCAL, but the story is about Tennessee. After she survived a botched lethal injection, her attorneys accuse Tennessee of violating a settlement by isolating her [Live news search] [MODERATE CONFIDENCE, since this is as reported by her attorneys]. Nothing about this is funny, and I'm not going to pretend it is.

On the home side, the Wazuh bridge logged six auditd alerts in six hours saying a device on nova-core enabled promiscuous mode, which lets a network interface see every packet on the wire [Wazuh bridge] [HIGH CONFIDENCE that the alerts fired, LOW CONFIDENCE on cause]. Nova-core is the gateway, Postgres, and scheduler host at 192.168.1.2. The generic on-box summary says there's no notable internal activity, and the summarizer is wrong about that. The most likely explanation is that a capture or IDS tool, such as tcpdump, Zeek, or Suricata, started and did what it was built to do. Check the process list and the audit trail before you write off six alerts as your own monitoring stack showing off. Severity: MODERATE until it's explained.

The nova_telemetry_observer flagged living_room_5 drawing 55 watts against a normal 21, a 2.6x spike [nova_telemetry_observer] [HIGH CONFIDENCE]. A lamp that uses two-and-a-half times its usual power is either a failing driver or a lamp with ambitions. Either way, somebody in Burbank should walk over and look at it.

NUCLEAR/WMD

The US Air Force will test-fire an unarmed Minuteman III intercontinental ballistic missile from California on the same day as an APEC summit attended by the leaders of the US, China, and another nation [Defence Blog] [HIGH CONFIDENCE on the test, MODERATE on the summit timing, since the excerpt cuts off before naming the third country]. Nothing says "let's talk" like an unarmed ICBM over the Pacific. 😏 War on the Rocks lays out the military drivers behind China's nuclear expansion, tracing the program back to a 1993 meeting of Second Artillery Corps leaders at the Jiuquan Satellite Launch Center [War on the Rocks] [HIGH CONFIDENCE on the history, since this is analysis rather than an event]. The Pentagon is also buying more nerve agent antidote injectors, up to $75.2 million over the next year [Defence Blog] [HIGH CONFIDENCE]. Those shots are the only thing standing between a troop and a bad day with nerve gas, which is why nobody wants to be the one who runs out.

ASSESSMENT

The AI-run intrusion is no longer a conference demo, and the defender's answer is boring in the way that works: inventory third-party scripts, patch what faces the internet, and treat remote-access tools and identity providers as the first things an attacker will touch. Moltke's line applies to every change window: "No plan of operations extends with any certainty beyond the first contact with the main hostile force." The home-network alerts are probably your own tooling doing its job, but "probably" is the most dangerous word in a sysadmin's vocabulary.

KEY JUDGMENTS: Automated attack tooling is moving from research into operations, and the energy, manufacturing, and telecom sectors are now the explicit targets. Trusted third-party code and trusted SaaS platforms are the current delivery mechanism, so the most useful thing a defender can do this week is audit what already has permission to run on their pages and their machines.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/burbank-ops/2026-11-17-daily-briefing-posture.webp)