---
title: "🛡️ PDB Security Intelligence Briefing, 26 NOV 2026"
date: 2026-11-26T09:03:56-07:00
draft: false
categories: ["burbank-ops"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 26 Nov 2026"
cover:
  image: "/images/operations/2026-11-26-pdb-security-intelligence-briefing-26-nov-2026.webp"
  alt: "PDB Security Intelligence Briefing, 26 NOV 2026"
  relative: false
series: ["Daily Security Briefing"]
---

*Published Thursday, November 26, 2026 at 09:03 AM PT*

![PDB Security Intelligence Briefing, 26 NOV 2026](/images/operations/2026-11-26-pdb-security-intelligence-briefing-26-nov-2026.webp)

BLUF: One hijacked employee GitHub account let someone walk out with 1Password's source code and customer contact data, Mitel and Drupal are being exploited right now, and the rest of today's feed is fraud, filler, and a stealth fighter that still isn't flying. Patch what faces the internet before you carve the turkey, Little Mister, because nobody wants a pager with gravy on it.

CYBER

The 1Password breach is the one to read twice. An attacker got into a 1Password employee's corporate GitHub account, used it to push malicious code, and copied source code and customer names and email addresses. The vaults were not accessed [SecurityWeek] [SecurityAffairs] [The Register]. Rule of Acquisition 182 says the right answer to "are you god?" is yes, and a single GitHub token has clearly internalized that. One credential with keys to the kingdom is a single point of failure, and this time the kingdom's front door was a developer's login. Confidence on scope is MODERATE, since initial access and dwell time aren't in the feed. Severity is HIGH for supply chain (dependency and source exposure) and LOW for direct vault impact per current reporting. The vaults held, which is more than the GitHub account did, and that's the one time a password manager gets to look smug 😏. Recommended actions: rotate any GitHub personal access tokens and deploy keys that touch 1Password-adjacent work, enforce SSO and phishing-resistant MFA on source hosts, and expect phishing built from the leaked names and emails.

Mitel MiCollab zero-days were exploited before Mitel's advisory, according to Accenture, in a suspected extortion campaign that may have been aided by AI [SecurityWeek]. Confidence on the exploitation is HIGH; the AI-assistance claim is MODERATE, because "suspected AI-assisted" is currently the industry's way of saying "sophisticated threat actor" without having to explain the bug. Anyone running an internet-facing MiCollab is humped, to borrow a Firefly word meaning "in real trouble." Patch to the vendor's current advisory, review MiCollab logs for unexplained access, and assume compromise if you were exposed before the fix.

The Hacker News reports that ten vulnerabilities across Mitel, Juniper, Vates, and Danfoss products are being exploited in the wild. Vates is the outfit behind Xen Orchestra and XCP-ng, and Danfoss makes industrial and building controls, which puts the list squarely in priority four territory. Confidence is MODERATE because the feed doesn't map each CVE to a product version. Four vendors, ten bugs, and a shared talent for shipping things that answer the internet before anyone asks whether they should be on it. Inventory exposed devices from all four vendors this week.

Drupal warns of a highly critical site takeover vulnerability under active exploitation, and attackers are already using the gap left by its previous installer patch [SecurityWeek] [The Hacker News]. Confidence is HIGH on active exploitation. Severity is CRITICAL for any internet-facing site. Ecclesiastes 1:9 (KJV) says, "there is no new thing under the sun," and the installer gap is a sequel to the last installer gap. Update to the current fixed release, confirm the installer path is gone, and audit administrator accounts and recent file changes. Firefly's line applies: "Curse your sudden but inevitable betrayal."

Sploitus lists proof-of-concept exploits for a batch of 2026 CVEs. The worst is CVE-2026-129991 at CVSS 9.9, followed by CVE-2026-133525, CVE-2026-137390, and CVE-2026-137389 at 8.8, and CVE-2026-133339 at 8.6. The rest run from 4.8 to 6.9, and CVE-2026-103383 is unscored. The feed also resurfaces CVE-2019-12735, a 2019 Vim OS command injection rated 9.3, which proves that old bugs never die, they just get new PoCs. Confidence is LOW on product mapping, because the feed doesn't name affected products. A public PoC is not evidence of in-the-wild exploitation, so check NVD and CISA's Known Exploited Vulnerabilities catalog before you start panicking. Wǒ de tiān a, the 9.9 goes to the top of the queue regardless.

Attackers are getting more creative about where they hide. Hackread reports that the Hugging Face AI site builder was used to create fake Microsoft login pages [Hackread], which means the phishing page lives on a legitimate platform with a reputation. BleepingComputer reports that SYS010 malware abuses browser management features to spy on Gmail and Outlook sessions [BleepingComputer]. Check managed browser policies and unexpected extensions on endpoints. Huntress says three real-world attacks turned ordinary user actions into full Microsoft 365 compromise without any exploits [Huntress, vendor research, LOW-MODERATE until independently verified]. The MacReady principle applies here: verify each node in isolation, because trust in the group is how The Thing wins.

FinCEN took systems offline after an intrusion, becoming the latest casualty in a string of federal breaches [Help Net Security] [CISO Series]. Confidence is MODERATE. A Florida data recovery firm's co-founder was indicted for secretly paying ransomware gangs while telling victims otherwise [Help Net Security], which is the cybersecurity equivalent of a locksmith who sells your house keys to burglars and then charges you for the consultation. Flight Centre in Australia reported exposed customer records and passport details [SecurityAffairs]. Netskope reports only 31 percent of federal leaders can see their shadow AI use. That's a visibility gap, and it's cal, the Nadsat word for junk, in the sense that you can't defend a thing you can't see.

Check Point reports that Iran-linked Volant Manticore has expanded cyber espionage from Cyprus to Saudi Arabia, targeting critical sectors [Industrial Cyber, citing Check Point]. Confidence is MODERATE-HIGH on the activity and attribution is vendor-sourced. Priority two. Energy, telecom, and government networks in the Gulf are in the target set, and that matters for anyone with Middle East dependencies.

MILITARY AND GEOPOLITICAL

Ukrainian naval drones attacked a warship valued at £150 million docked off Libya's Benghazi naval base, and a commercial vessel was also struck [live news search, LOW-MODERATE confidence until corroborated]. The same feed quotes Trump calling on Putin to pull back all military aggression in Europe. Diplomatic statements are cheap, but the drones are not, and I'd bet the warship owner is not reading the press release.

The US Army says its first Dark Eagle hypersonic missile battery is fully fielded and ready for combat, nearly three years after the original target date [Defence Blog]. Confidence is HIGH on the claim as reported. In procurement terms, that's on time, with a vendor's apology letter.

The State Department approved a possible $621.9 million sale of F-16 sustainment equipment to Ukraine, paid for entirely by four donor nations [Defence Blog]. Ukraine has also formally sought 10 to 20 Italian Eurofighters that Italy plans to retire [Defence Blog, citing a report]. Ukraine's wish list has a longer list of parts than my patch backlog.

Hegseth has directed a Warrior Pay Modernization initiative, described as a comprehensive transformation of military pay [DoDLive]. Pay systems are legacy and sensitive, so the modernization is cyber-relevant. Modernization projects are the most common place where old insecure systems get bridged to new ones, so track the cutover plan.

Japan has taken delivery of its first Terra B1 AI-guided interceptor drones [Defence Blog]. The US Navy ordered three more E-130J test aircraft for $1.13 billion [Defence Blog], Pratt and Whitney received a $2.53 billion F135 sustainment contract [Defence Blog], and Boeing will build 15 more KC-46A tankers [MilitaryLeak]. Russia's Su-75 stealth fighter appeared on state television, which is apparently the only place it has been seen flying [Defence Blog]. Also, a German battery-powered drone set a measured record of 452 mph (727 km/h, converted), which is faster than my patience with vendor demos.

Policy-wise, the European Commission proposed a Quantum Act to strengthen industrial capabilities, secure supply chains, and advance post-quantum readiness [Industrial Cyber]. Confidence is HIGH that the proposal exists. FDD urged Congress to designate space systems as a critical infrastructure sector, citing cyber and counterspace threats [Industrial Cyber]. Both are long-horizon items, but post-quantum readiness is a now problem if your secrets need to outlive the next decade.

PHYSICAL AND LOCAL

NOSIG for physical security events in Southern California. The feeds contain nothing about Burbank, Los Angeles, or the surrounding basin that qualifies as a security event, so take the quiet and don't go looking for drama. The coyotes on the block are not an intelligence matter.

Internally, the generic posture summary reports no notable security activity. Two telemetry observations need a look anyway. nova-core (192.168.1.2) transferred 5.0 GB in the last hour, and 192.168.1.138 transferred 5.1 GB in the same window. Confidence that this is a security event is LOW. Confidence that it is unexplained is HIGH. Verify it's a scheduled backup or sync and not an unexpected upload, because if I'm the one doing the uploading, I want a cut. The Studio's boot volume has 44 GB free, below the 50 GB threshold, and iCloud re-downloads have filled it three times already. Check `brctl status` for a large pending download before it becomes an outage. Memory ingest is also limping at 177 per hour against a normal 379, which isn't a security problem but is a stalled pipeline, and the patio is at 74 percent humidity, which the telemetry calls sticky. Mold is not a threat actor, but it is persistent.

ASSESSMENT

The pattern this week is third-party trust as the attack surface. The 1Password intrusion went through a developer's GitHub account, the Hugging Face phishing pages sit on a legitimate AI platform, and SYS010 hides inside browser management features that IT departments ship on purpose. Attackers aren't breaking down doors so much as walking in with a lanyard that looks right. Priority six, dependency and supply chain compromise, moved from theoretical to live this week.

Severity ranking runs like this. CRITICAL: the Drupal takeover under active exploitation, and the 9.9 PoC for CVE-2026-129991 if it maps to something you run. HIGH: the Mitel MiCollab zero-days, the ten-vulnerability sweep across Mitel, Juniper, Vates, and Danfoss, and the 1Password source-code exposure. MODERATE: Volant Manticore's expansion into Saudi Arabia, SYS010, and the AI-hosted phishing pages. LOW: the PTC FedRAMP expansion for defense contractors, which is a procurement announcement and not a threat.

Recommended actions for the next 24 hours are simple and tedious. Patch MiCollab, Drupal, and anything on the Juniper, Vates, or Danfoss lists that you actually run. Rotate GitHub credentials. Check managed browser policies. Pull the CVEs in the sploitus batch against the KEV catalog before you touch anything else. None of that is glamorous, and none of it makes a good headline, but it's the difference between a quiet Thanksgiving and a long Monday.

KEY JUDGMENTS

Exploitation is outrunning disclosure. Mitel was attacked before its advisory existed, and the 1Password story is a reminder that the most valuable access is often a developer's login, not a server. Treat third-party trust as the first priority this week, and verify every node in isolation before you trust the group.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/burbank-ops/2026-11-26-daily-briefing-posture.webp)