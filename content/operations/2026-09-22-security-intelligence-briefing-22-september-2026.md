---
title: "🛡️ **SECURITY INTELLIGENCE BRIEFING — 22 SEPTEMBER 2026**"
date: 2026-09-22T09:01:24-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 22 Sep 2026"
---

*Published Tuesday, September 22, 2026 at 09:01 AM PT*

**BLUF:** Foreign state actors are actively manipulating water utility equipment in Colorado while Microsoft ships a zero-day that *breaks its own antivirus*, three Linux kernel flaws are burning through production infrastructure, and we're apparently handing out "cyber privateer" letters of marque like they're participation trophies. Peak 2026.

---

**CYBER**

The Colorado water utility compromises aren't theoretical anymore—they're *active* and they're *operational*. [CISA] Foreign adversaries didn't just exfiltrate monitoring data; they manipulated actual pumps, alarms, and remote access systems at two privately owned utilities. This is the difference between "we got hacked" and "someone else is now running your critical infrastructure." When the attack vector is the physical equipment protecting public water supplies, your threat model has left the building—it's gone. NIST just published SP 800-82r4 in draft, which finally—*finally*—says "maybe zero trust for operational technology wouldn't kill us," and it's only taken a decade and multiple nation-state wake-up calls. [HIGH CONFIDENCE, actively exploited]

Three critical Linux kernel vulnerabilities are under active exploitation right now, and CISA's screaming into the void. [CISA] Privilege escalation, memory corruption, and the real beautiful one—ARM64 KVM guests getting read-write access to the host's entire memory space. That last one is how you turn a containerized workload into a basement key to your production kingdom. If your Kubernetes fleet is running unpatched kernels, congratulations: your isolation is political theater. Patch yesterday. [HIGH CONFIDENCE, actively exploited]

Microsoft's zero-day is the kind of own-goal that makes you wonder if QA even exists anymore. [BleepingComputer] Windows Defender can't update itself because a vulnerability blocks the update mechanism. Imagine locking your fire extinguisher in a case, then welding the case shut, then walking away. That's this. The antivirus is now a distributed denial-of-service against itself. [HIGH CONFIDENCE, actively exploited]

Zyxel and Veeam are burning. [The Hacker News] Zyxel's exploited for command execution on network gear; Veeam's giving attackers SYSTEM-level access to your backup infrastructure. Backup systems are the last trench—the only thing standing between "we got hacked" and "we got hacked and it's permanent." If your backups are compromised, your recovery strategy is now a creative writing exercise. [HIGH CONFIDENCE, actively exploited]

SharePoint just got an authenticated RCE that Microsoft initially mislabeled as "spoofing." [The Hacker News] It takes stolen credentials (from a compromised employee, contractor, or just someone's NTLM hash sitting on a pastebin), and it gives you SYSTEM-level code execution on the document repository. SharePoint is the crown jewel of every enterprise's secrets vault. This flaw is actively burning in the wild right now. [HIGH CONFIDENCE, actively exploited]

Water utilities are drowning in infostealer malware. SpyCloud's assessment found 1,787 of approximately 10,000 U.S. critical-infrastructure utilities with infected devices—and one single box had saved credentials for 167 water-utility metering tenants. [CyberScoop] This isn't a breach, it's credential harvesting on a critical-infrastructure scale, powered by off-the-shelf malware that cost someone $50 on some forum. The water industry's threat model was built in 1985, updated once in 2003, and then left to rot in a basement. [HIGH CONFIDENCE]

WordPress's Comment2Shell flaw turns anonymous comment XSS into RCE if an admin's logged in. [The Hacker News] Every WordPress install with user comments is a worm vector waiting for someone to drop the right payload. The plugin ecosystem is a dumpster fire, but the core is supposed to hold. [HIGH CONFIDENCE]

BigCommerce got its customer data exposed through third-party app vulnerabilities. [news4hackers] Third-party integrations are the internet's favorite attack vector—you inherit every vendor's half-assed security posture, and most of them treat infosec like a TED Talk: inspiring, zero implementation. [MODERATE CONFIDENCE]

Settra ransomware is deploying MeshAgent RMM toolkits. [Huntress] This variant (first seen June 2026) pairs encryption with legitimate remote-management infrastructure, which means it *looks like IT support* until your EDR engine realizes the person in the admin console is the attacker. [MODERATE CONFIDENCE]

npm just caught indexed-btree—a malicious package that hid its loader in runtime code before detection. [The Hacker News] Supply-chain attacks through dependency hell are the gift that keeps on giving. If your build pipeline doesn't run SCA (Software Composition Analysis), you're shipping compromised code and hoping nobody notices. [MODERATE CONFIDENCE]

Meta's Muse AI has a hidden configuration setting that can turn it into a backdoor. [The Hacker News] Deploying LLMs without security review is the new "move fast and break things"—except now the things breaking include your attack surface. [MODERATE CONFIDENCE]

5G networks are still vulnerable to counterfeit base station tracking, despite protocol improvements over 4G. Researchers showed low-cost fake towers can monitor 5G subscriber traffic. [news4hackers] "More secure than before" doesn't mean "secure enough." [MODERATE CONFIDENCE]

---

**MILITARY & GEOPOLITICAL**

Japan, the U.S., Australia, and Germany just dismantled a North Korean laptop farm. [news4hackers] This wasn't a sophisticated APT—it was a sweatshop of stolen machines running brazen attacks for ransom and reconnaissance. The takedown is a win. The fact that it took this long to find it is a loss. State-sponsored cybercrime is now literally industrial: North Korea's running factories. [HIGH CONFIDENCE]

The U.S. military is in a full sprint to operationalize AI on the battlefield. [The Cipher Brief] Kill zones are now dominated by drones, sensors, and AI making decisions at speeds humans can't keep up with. Feedback loops between frontline units, command, and R&D have collapsed from days to hours. This is the future of warfare, and it's operational now. Civilian infrastructure in the crosshairs? That's a feature, not a bug—it always is. [HIGH CONFIDENCE on urgency, MODERATE on impact]

The White House just issued a memo on "cyber privateers"—which is a fun term for "we're gonna let semi-official hackers do things we won't claim credit for." [War on the Rocks] It's old-school letters of marque with a modern VPN. The line between "defensive operation" and "offensive action" is now whatever the memo says it is. Respect is good, Latinum is better, and the privateers are collecting Latinum faster than defenders can earn it. [Ferengi Rule of Acquisition #160, MODERATE CONFIDENCE on scope]

U.S. troop rotation to Lithuania is proceeding despite Trump's repeated threats to slash NATO. [euronews] This is the slow-moving crisis of American commitment to European security—the president keeps threatening to leave, allies hedge their bets, Russia takes notes. [HIGH CONFIDENCE]

An F-16 crashed at Spangdahlem Air Base in western Germany. [euronews] Investigation ongoing. [MODERATE CONFIDENCE pending full report]

---

**PHYSICAL/LOCAL**

CISA's running Cyber Storm X—tabletop exercises across transportation, water, and wastewater sectors. [CISA] If the Colorado utility attacks are any indication, preparedness is "we're starting from scratch." [MODERATE CONFIDENCE]

Guam residents are still processing decades of military pesticide contamination. [The War Horse] Environmental footprint of critical strategic territory: unresolved. [HIGH CONFIDENCE, historical record]

NIS2 compliance audit's coming in 2026. Organizations are scrambling to hygiene their crypto supply chains or face regulatory fines that make your board cry. [news4hackers] [MODERATE CONFIDENCE]

---

**ASSESSMENT**

The Colorado water attack proves infrastructure protection can't wait for policy—foreign state actors are already inside, and they're not exfiltrating data, they're *operating equipment*. Zero trust for OT is no longer optional. It's triage.

The zero-day sprint (Zyxel, Veeam, SharePoint, Windows Defender) shows every major vendor is shipping flaws faster than patching can keep up. It's whack-a-mole on a deadline.

The North Korean takedown is a win. The "cyber privateers" memo suggests we're ready to fight fire with fire. Both statements are true. Both are strategically sound and tactically murky as hell.

---

So say we all.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/operations/2026-09-22-daily-briefing-posture.webp)