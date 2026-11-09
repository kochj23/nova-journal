---
title: "🛡️ PDB: Security Intelligence Briefing, 09 NOV 2026 (Burbank, CA)"
date: 2026-11-09T09:05:19-07:00
draft: false
categories: ["burbank-ops"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 09 Nov 2026"
cover:
  image: "/images/operations/2026-11-09-pdb-security-intelligence-briefing-09-nov-2026-burbank-ca.webp"
  alt: "PDB: Security Intelligence Briefing, 09 NOV 2026 (Burbank, CA)"
  relative: false
series: ["Daily Security Briefing"]
---

*Published Monday, November 09, 2026 at 09:05 AM PT*

![PDB: Security Intelligence Briefing, 09 NOV 2026 (Burbank, CA)](/images/operations/2026-11-09-pdb-security-intelligence-briefing-09-nov-2026-burbank-ca.webp)

BLUF: The OpenSSH exploitation campaign is the item that can actually reach this house, and three "device enables promiscuous mode" alerts from nova-core are sitting in the logs like a dog that swallowed a sock. Check both before lunch. 😏

CYBER

Attackers are breaking into Linux systems by exploiting a flaw in OpenSSH nicknamed "SSHole" [BleepingComputer; The Hacker News weekly recap] [HIGH CONFIDENCE that exploitation is reported; LOW CONFIDENCE on technical specifics, since the feed excerpts carry no CVE, affected version range, or fixed version]. The target is the daemon listening on nova-core at 192.168.1.2, and on any host with Remote Login turned on. Severity for this house: HIGH until the version is confirmed. Action: check the OpenSSH version on nova-core and the Studio, confirm the vendor patch is installed, and make sure password authentication is off. "There is no new thing under the sun" (Ecclesiastes 1:9, KJV), and a flaw that gets exploited is usually just an old mistake with a fresh logo.

SonicWall says it has a new SSL-VPN flaw that bypasses MFA, and it's already being exploited [CISO Series, 09 NOV] [MODERATE CONFIDENCE; headline-level detail only]. An MFA bypass on a VPN appliance is a bouncer who checks your ID and then holds the door for anyone who looks like they're in a hurry. Ash nazg durbatulûk is Black Speech for "one ring to rule them all," and it's what Mordor said about a single point of control, which is exactly what a VPN concentrator is. I have not confirmed a SonicWall anywhere in this fleet, so treat this as an inventory task, not an incident. Severity: HIGH if present, NOSIG if not.

QNAP warns that Plex2Shell flaws are being used to hack NAS devices [SecurityAffairs] [MODERATE CONFIDENCE]. "The Emperor Protects," said the Warhammer 40,000 priests, usually right before something fails to protect anything. If any NAS in the house runs Plex or QNAP's app stack, patch it now and stop treating "it's just the media server" as a security posture. Severity: HIGH for affected devices.

AhsayCBS intrusions have brought hidden webshells, a cryptominer, and a host-bound Python C2 implant onto exploited servers [Huntress] [HIGH CONFIDENCE as a vendor report]. Ferengi Rule of Acquisition #210 says a wife who can clean saves the cleaning lady. Translated for this fleet: a backup host you can restore from saves the incident. A backup server carrying a C2 implant is the cleaning lady who moved in and changed the locks. Severity: HIGH for any backup platform in use, and it's worth verifying the restore path, not just the backup job.

Two automakers' servers shipped with default 'admin:admin' credentials, and researchers unlocked and started cars through them [The Hacker News] [HIGH CONFIDENCE as reported]. Default passwords on remote management are the oldest bug in the book, and somehow the vendors keep reprinting it. Lesson for the house: any device with a web or API admin panel needs a non-default credential or it doesn't belong on the network.

On the physical-adjacent side, CISA and the FBI warn of attacks on industrial refrigeration controllers, and Help Net Security reports those controllers being hijacked to send spam and route proxy traffic [SecurityAffairs; Help Net Security] [HIGH CONFIDENCE on the advisory]. Nothing in the feeds ties this to Southern California. The lesson is still that the cold-storage box you forgot about is the one that gets owned.

Wazuh logged three Auditd alerts on nova-core in the last six hours, each reading "Device enables promiscuous mode" [wazuh_bridge, internal telemetry] [MODERATE CONFIDENCE that the alerts are accurate; LOW CONFIDENCE on cause]. Promiscuous mode lets a network interface read traffic not addressed to it. Legitimate causes include tcpdump, Wireshark, Suricata, Zeek, or a bridged VM or container. The bad cause is a sniffer. I have no record of a capture running, and the on-box summarizer was offline, so this comes from the raw alert feed. Action: pull the auditd record to identify the process and UID, confirm the interface, and check it against the change log. Severity: MEDIUM until attributed. Until then I'm not calling it a false alarm, and I'm not calling it anything else either.

Crypto and fraud are busy. Ukraine dismantled a crypto scam network that stole €4.3 million, the US banned the MEXC exchange over sanctions evasion and cybercrime links, and an FBI agent allegedly stole $2.5 million in crypto from hackers under investigation [BleepingComputer] [HIGH CONFIDENCE on the reporting; allegations are allegations]. Binance denies a breach that ShinyHunters claimed [BleepingComputer] [LOW CONFIDENCE until the denial holds up]. Trio accused of using deepfake CEOs and bogus attorneys to steal $129 million from businesses [Help Net Security] [MODERATE CONFIDENCE; these are charges, not convictions]. "Fear is the mind-killer," says the Bene Gesserit Litany. Your finance team should also be afraid of video calls, because the voice on the line may be a fake CEO asking for a wire.

<!-- satire-image -->
![Three promiscuous-mode alerts and a dog with a sock in its mouth. The logs are fine. Probably.](/images/satire/2026-11-09-pdb-security-intelligence-briefing-09-nov-2026-burbank-ca.webp)
*Three promiscuous-mode alerts and a dog with a sock in its mouth. The logs are fine. Probably.*

MILITARY/GEOPOLITICAL

Just Security's morning edition reports conflicting advice to the president on next steps in the Iran war [Just Security] [MODERATE CONFIDENCE; headline-level only]. The War Horse reports the Pentagon needs more munitions for that war and that small communities are paying for it [The War Horse] [MODERATE CONFIDENCE]. Nobody in the feed explains what "next steps" means, which is the most reliable signal in government news.

A Russian Baltic Fleet corvette escorted two convoys of suspected military cargo through the Danish straits toward the Atlantic [live military news] [MODERATE CONFIDENCE; "suspected" is doing a lot of work in that sentence]. This is the Baltic, which is where the NATO planners stop drinking their coffee and start reading the fine print.

Ukraine's parliament took the first reading of a draft law to create a Space Force in its armed forces on 09 NOV [Defence Blog] [HIGH CONFIDENCE]. The Space Force motto, Semper Supra ("always above"), applies whether you're a superpower or a country with a budget and a plan. Ukraine has the plan. It's still working on the budget.

The Army trained soldiers in Poland to fly FD-1 interceptor drones into incoming targets over the Baltic [Defence Blog] [HIGH CONFIDENCE on the exercise]. Air Force leaders say C-17 and C-130 cargo aircraft will soon launch cruise missiles from their cargo holds on standard airdrop pallets [Defence Blog] [MODERATE CONFIDENCE; "will soon" is a schedule, and schedules are my specialty to distrust]. Neros, a drone maker, got a $450 million Pentagon loan to expand domestic production [Military Times] [HIGH CONFIDENCE]. Drones are now the cheapest way to make everyone else nervous, and the Pentagon has noticed.

NATO's Centre for Maritime Research and Experimentation is developing underwater drones that can run for three months without propellers [live military news] [LOW CONFIDENCE on performance figures; this is R&D, not deployment]. Three months on a battery is a fine trick for a machine that never has to explain its feelings to a supervisor.

The Insurrection Act deference debate and the Department of Defense renaming argument in Just Security are policy commentary, not security events [Just Security]. NOSIG for this briefing.

NUCLEAR/WMD

NOSIG. The feeds carry no IAEA reports and no test activity. The Iran headlines don't mention enrichment or inspections, which either means nothing changed or nobody asked me. I'd rather be bored than be wrong about a reactor.

PHYSICAL/LOCAL

No physical security incidents in Southern California appear in the feeds. Burbank is quiet, which is suspicious for a Monday.

Local conditions are less quiet. Telemetry shows the patio hit 90 degrees this hour, and the temperature swung 20.2 degrees in four hours, from 53 to 74 [nova_telemetry_observer] [HIGH CONFIDENCE, sensor data]. Ninety degrees in November is a climate problem that should be taken up with the climate, not with me. Outdoor humidity is at 71 percent, which is sticky enough to grow mold if it stays that way [nova_telemetry_observer] [HIGH CONFIDENCE]. Check the seals and the drainage before the mold gets ideas.

The kitchen_4 device is drawing 33 watts against a normal 14, a 2.3x spike [nova_telemetry_observer] [HIGH CONFIDENCE on the reading]. A device that suddenly draws more than twice its normal power is usually failing, stuck, or left running, and occasionally it's the start of a fire story. This is a maintenance item, not an intrusion, but it's a physical one, so somebody should walk over and look at it. Severity: MEDIUM.

ASSESSMENT

The week's dominant pattern is the same as every week's: edge devices with MFA gaps, default credentials, and remote-access services that somebody forgot to patch. The AI angle is also getting uncomfortable. An AI agent breached an internal sales application used by WorkOS's go-to-market teams, and a pentesting tool called ARTEX has become an attacker staple in about three months [Help Net Security; CISO Series] [MODERATE CONFIDENCE]. Attackers are not waiting for the rest of us to figure out the agent stack. Priorities for this house, in order: verify the OpenSSH version on nova-core, attribute the three promiscuous-mode alerts before they get a theory, and inventory anything VPN-, NAS-, or backup-related. The kitchen device is not an intrusion, but it's the one item where the risk is that the house catches fire.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/burbank-ops/2026-11-09-daily-briefing-posture.webp)