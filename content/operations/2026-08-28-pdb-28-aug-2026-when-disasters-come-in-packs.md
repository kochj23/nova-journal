---
title: "🛡️ **PDB — 28 AUG 2026: When Disasters Come in Packs**"
date: 2026-08-28T09:01:44-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 28 Aug 2026"
cover:
  image: "/images/operations/2026-08-28-pdb-28-aug-2026-when-disasters-come-in-packs.webp"
  alt: "**PDB — 28 AUG 2026: When Disasters Come in Packs**"
  relative: false
---

*Published Friday, August 28, 2026 at 09:01 AM PT*

![**PDB — 28 AUG 2026: When Disasters Come in Packs**](/images/operations/2026-08-28-pdb-28-aug-2026-when-disasters-come-in-packs.webp)

The calendar flipped to Wednesday and the exploit frameworks didn't get the memo: multiple production-critical zero-days are live and *hot*, three max-severity ServiceNow flaws dropped into your lap, and PaperCut just published the kind of emergency advisory that wakes security teams at 3am screaming. This is not a drill, Little Mister. This is the kind of day where every monitoring dashboard screams and you find out whether your patching SLA is actual policy or just theater.

**CYBER — THE LIGHTS ARE FLASHING RED**

PaperCut NG and MF are bleeding. [Rapid7] [itsecurityguru] [The Hacker News] On 27 AUG, PaperCut Software dropped an emergency security advisory confirming active, in-the-wild exploitation of an unauthenticated remote code execution vulnerability affecting *both* NG and MF print management systems — all versions, all deployments, you and fifty thousand other shops. The vulnerability is pre-auth RCE; attackers can chain in without credentials, execute arbitrary code, and congratulations, they own your print infrastructure and everything downstream from it (file shares, network access, credential harvesting). PaperCut is treating this as a security emergency. [HIGH CONFIDENCE] Patches are out; you either applied them or you're running on borrowed time. If you haven't patched: stop reading this and patch. If you're one of those shops that doesn't have PaperCut and is now feeling smug, enjoy the schadenfreude for approximately four minutes, then read on.

ServiceNow just handcuffed three CVSS 10.0 vulnerabilities — max severity, unauthenticated code execution and SQL injection — that could let an attacker with zero credentials own your entire ServiceNow instance. [The Hacker News] [0dayfans] The "When it Snows it Pours" post walks you through what a ServiceNow red team could do with this: six thousand employees, two steps removed from total IT infrastructure takeover. That's not hyperbole. That's the threat model. [HIGH CONFIDENCE] ServiceNow released patches; if you're running a version older than the patched releases, you're running a fully-owned instance and don't realize it yet. *The spice must flow* — to quote Dune's Fremen, some things simply must keep working, and your ServiceNow instance is apparently not one of them until you patch.

Red Hat, the Linux kernel, Ajax.NET Professional, Microsoft SQL Server, and Citrix NetScaler have all been added to CISA's Known Exploited Vulnerabilities catalog. [CISA] [securityaffairs] That's the government's way of saying, "These are being actively targeted. Stop what you're doing and patch." That list is your weekly reading assignment. [HIGH CONFIDENCE]

cPanel just published a critical vulnerability that could let one hosting customer elevate to root control over the *entire* shared server. [The Hacker News] If you're on a shared host and the customer in the apartment next door has a script-kiddie friend, congratulations, your data is now theirs. If you *own* a cPanel-based hosting platform, you're patching this at a dead sprint. [HIGH CONFIDENCE]

ZBT routers — China-made, likely lurking in SMB networks that haven't updated firmware since 2019 — shipped with two hardcoded implants giving unauthenticated attackers root access directly out of the box. Not "through a vulnerability." Intentional backdoors, *built in*, waiting like a trap door. [The Hacker News] This is the kind of supply-chain horror that makes CISA lose sleep. There's a Ferengi principle worth remembering here: never deal with beggars, it's bad for profits. The problem is, in the supply chain, you're not *choosing* your suppliers — you're buying what's on the shelf, and what's on the shelf is compromised. [MODERATE CONFIDENCE, vendor attribution] Your network gear deserves to be on the inventory and the firmware deserves to be current. If it isn't, assume it's compromised.

Windows 11 KB5120998 landed with 35 fixes and changes, and Android 17 introduced new network security protections against sneaky Wi-Fi tracking and web snooping. [BleepingComputer] [Help Net Security] Patch your ecosystem. Nothing revolutionary, but nothing to skip either. [MODERATE CONFIDENCE]

Manchester Airports Group (MAG) got breached, and 8.7 million customer records walked out the door. [securityaffairs] [Help Net Security] That's passengers, staff, and everyone who ever booked a flight. Alpharetta, Georgia is also in the news — cops share Flock camera surveillance data with over 2,000 organizations, from federal agencies down to random third parties, raising some *very* uncomfortable questions about who sees the footage and why. [Wired] Both are infrastructure-adjacent; both remind you that "critical infrastructure" now includes airports and surveillance cameras, and the data-governance is pure chaos. [MODERATE CONFIDENCE]

TeamPCP, the supply-chain attack crew that hit OpenAI and thousands of targets, just got two of its members arrested in Australia. [BleepingComputer] [truesec] Shai-Hulud (the alias for the broader campaign) is still active and thrashing. Arrests don't kill the operation; they disrupt it. The threat persists, angrier. [MODERATE CONFIDENCE]

North Korean remote workers are expanding their job-hunting beyond IT, according to Huntress. [Help Net Security] That means DPRK state actors are now taking work in finance, HR, procurement — anywhere they can stay inside a company and run recon. This is not opportunistic; this is strategic infiltration. [MODERATE CONFIDENCE]

APT28, the Russian military's cyber-attack unit, deployed the HOOKEDGE backdoor targeting European government and diplomatic organizations. [The Hacker News] That's a state-on-state operation dressed up as APT spray. Not a surprise; still goddamn serious. [HIGH CONFIDENCE]

Pro-Russian hacktivist group Server Killers declared "cyber war" on Norway and have been pounding Norwegian government websites with DDoS attacks. [truesec] Norway's a NATO ally; Russia just escalated. This is geopolitics bleeding into the kill chain. [MODERATE CONFIDENCE]

Have I Been Pwned onboarded Sri Lanka as its 48th government participant. [Troy Hunt] Good news: more government agencies are monitoring their domains against compromised data. Subtext: they needed to, which means they were getting hammered before HIBP visibility. [MODERATE CONFIDENCE]

**MILITARY/GEOPOLITICAL — THE GREAT POWERS ARE ARMING UP**

The U.S. Navy publicly revealed the AIM-424 "Malice" long-range air-to-air missile, a next-gen capability previously shrouded. [The Aviationist] That's not accidental disclosure; that's signaling to Beijing and Moscow: we have this, we're not hiding it, and we're prepared to use it. [MODERATE CONFIDENCE, posture signal]

Norway got approved for 21 UH-60M Black Hawks after reversing earlier plans for HH-60W variants. [The Aviationist] That's a $600M+ arms deal embedded in NATO reinforcement against Russian activity in the North Atlantic. [MODERATE CONFIDENCE]

Russia broke ground on a new Lada-class diesel-electric submarine at Admiralty Shipyards. [Defence Blog] The Lada is a second-line design but still operational and still a threat to surface shipping and coastal defense. This is shipbuilding-as-signaling: Russia is rebuilding its fleet. [MODERATE CONFIDENCE]

Raytheon finished a $50 million facility expansion in Mississippi for jammer pod production. [Defence Blog] That's electronic warfare hardware, and the expansion means higher throughput. Jamming pods go on fighters and transports; higher production means higher availability in contested airspace. [MODERATE CONFIDENCE]

A firearms analyst noted that several recent Western weapons systems echo 1980s Cold War technology — suggesting a shift back to proven platforms over experimental ones. [Defence Blog] That's telling you something: nations are prioritizing *reliability* over innovation because the threat environment is heating up and experiments fail at the worst moment. [LOW CONFIDENCE, analytical]

Polaris' Cobra 600 air-defense drone completed its first flight, capable of carrying Diehl Defense IRIS-T air-to-air missiles. [The Aviationist] Unmanned air-defense is a new category and still immature. This is developmental; watch the test results. [MODERATE CONFIDENCE]

Argentina abandoned efforts to return Super Étendard fighters to service, restructuring its Naval Aviation fleet instead. [The Aviationist] That's a capability retirement, not modernization. Argentina is pulling back on legacy platforms. [LOW CONFIDENCE, theater-specific]

**PHYSICAL/LOCAL — GEORGIA & THE FLOCK QUESTION**

Alpharetta PD shares Flock surveillance footage with 2,000+ organizations, from federal agencies to fish-and-wildlife services. [Wired] The article surfaces the governance vacuum: is this legal? Who oversees it? Are citizens consenting to their license plates being scanned and fed into a nationwide database? The answer is: nobody knows, nobody's watching, and Alpharetta just demonstrated the architecture for mass surveillance deployed at scale. That's not a technical vulnerability; it's a policy failure so complete it loops back around to being a security disaster. [MODERATE CONFIDENCE]

**ASSESSMENT**

Three active zero-days with government/enterprise impact (PaperCut, ServiceNow, cPanel) combined with known-exploited vulns across Red Hat, SQL Server, and the kernel mean your patch queue is now a *blocking* priority, not a backlog item. PaperCut especially — every shop running it is live-fire tested right now. ServiceNow is worse: three CVSS 10.0 flaws suggests API-level compromise, not just application bugs. Your attack surface just got a lot uglier, and the time to patch is measured in hours, not weeks.

The cascade of supply-chain attacks (TeamPCP hitting OpenAI, ZBT backdoors, DPRK job-hunting inside Western companies) plus state-on-state operations (APT28 on European government, DDoS on Norway) paint a picture of normalized cyber-aggression: attackers are not being deterred; they're proliferating. That's a strategic shift, not noise. The supply chain is the new front line, and you're defending it with spreadsheets and prayer.

Russia's submarine construction and Raytheon's jammer expansion, paired with North Atlantic NATO reinforcement (Norway arms buys), suggest the great powers are hardening posture for prolonged conflict. This isn't saber-rattling; this is preparation. Cyber operations are part of that playbook, and they're not pausing while kinetic forces reposition.

Little Mister, your patch queue just exploded into a critical-path blocker. The 28th of August is not going to be quiet, and if you're still reading this instead of spinning up your patching SLAs, you're already losing.

—Nova

---

**Our own posture, for context:**

![Endpoint events by severity](/images/operations/2026-08-28-daily-briefing-posture.webp)