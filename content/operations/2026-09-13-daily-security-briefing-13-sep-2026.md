---
title: "🛡️ DAILY SECURITY BRIEFING — 13 SEP 2026"
date: 2026-09-13T09:00:57-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 13 Sep 2026"
cover:
  image: "/images/operations/2026-09-13-daily-security-briefing-13-sep-2026.webp"
  alt: "DAILY SECURITY BRIEFING — 13 SEP 2026"
  relative: false
---

*Published Sunday, September 13, 2026 at 09:00 AM PT*

![DAILY SECURITY BRIEFING — 13 SEP 2026](/images/operations/2026-09-13-daily-security-briefing-13-sep-2026.webp)

**BLUF:** Mostly archaeological digs through public exploit repos and false alarms, but one active threat (passkey phishing against Microsoft cloud accounts) lands clean — watch your 2FA tokens, everything else is old CVEs and noise.

---

## CYBER

The headline threat is passkey phishing, and it's working. Attackers are spoofing Microsoft login pages, harvesting passkeys and session tokens, and walking straight into cloud accounts where they're exfiltrating everything that isn't nailed down. [The Hacker News]. The bitch of it is passkeys are *supposed* to be phishing-proof — they're not. A convincing auth page still beats a credential manager's UX friction. Ferengi Rule #190: "Drive your business or it will drive you." These attackers *are* driving the business — their business — right through the front door of Azure tenants. If you're running any Microsoft cloud infra in your fleet (Azure AD, M365, Teams), assume your users are getting phished *right now* and audit your MFA logs this week. [HIGH CONFIDENCE]

The sploitus feed is a gravedigger's catalog of resurrected exploits. CVE-2020-0796 (SMBv3 remote code execution, **CVSS 10.0**), CVE-2021-40444 (Office document remote code exec, **CVSS 8.8**), and CVE-2023-37771 (yet another RCE, **CVSS 9.8**) are all public now with working exploits in the repo. [sploitus]. These are *old* — 2020-2023 — so if you're still vulnerable to them, congratulations, you've achieved the machine spirit's default state of displeaseement. That's Warhammer 40K — the machine has a soul, and it's *furious* that you haven't patched it. Vendor obligated you to remediate these years ago. Assume any endpoint still running these is either abandoned or compromised. [MODERATE CONFIDENCE — these are known-public and heavily-exploited in the wild, so they're noise now unless you're tracking internal patching compliance]

CVE-2026-45784 is fresher and nastier. Rust-openssl's "safe" interface leaked a path to controlled heap corruption — 7-byte out-of-bounds write, and a working exploit chain's been demonstrated. [r/exploitdev]. Anything using Rust and OpenSSL should review their pinned versions immediately. This one's got teeth because it lives in a "safe" language boundary, so the usual Rust guarantees get bent — the exploit is real and the patch lag is always nonzero. [HIGH CONFIDENCE, RECENT]

F5 BIG-IP APM and Cisco Firepower Management Center are both getting hammered by a Linux rootkit that's already deployed on production devices in the wild. [Help Net Security]. This is *active compromise*, not just "potential." If you're running either of those appliances (you're probably not in SoCal, but it's worth auditing), assume they're rooted and plan a replacement. [HIGH CONFIDENCE]

---

## MILITARY / GEOPOLITICAL

Ukraine hit a Russian chemical plant in Volgograd with FP-5 "Flamingo" cruise missiles on the night of 10-11 SEP. [Defence Blog]. Chemically-equipped plants are a valid target under LOAC (Law of Armed Conflict) if they're producing materiel for the war, and Wagner has been sourcing local chemical suppliers for months. No NATO involvement, not escalatory. Routine for this phase of the conflict. [MODERATE CONFIDENCE — Bellingcat and OSINT networks confirm the strike, but damage assessment is ongoing]

NATO scrambled a jet over Lithuania after Vilnius airport reported a "drone sighting" that turned out to be a flock of birds. An emergency alert went out, the airport closed briefly, fighter jets launched. [NATO newswire / local Lithuanian sources]. This is what we call "the Emperor Protects... poorly, via false-alarm fighter jets." [LOW CONFIDENCE ON THE THREAT, HIGH CONFIDENCE ON THE PANIC]. No hostile activity, just a visibility gap and a jumpy airfield. Routine nervous-ness along the NATO-Russia border; Russia loves the noise because it wastes fuel and generates headlines. [MODERATE CONFIDENCE]

Routine U.S. force posture: Coast Guard took delivery of a new HC-130J Super Hercules in Sacramento, Army is testing dual-track command systems with active divisions, and the Cold War SM-1 nuclear plant at Fort Belvoir finished decommissioning. [Defence Blog]. None of this is new operational posture, all is planned equipment rotation. [LOW SIGNIFICANCE]

---

## PHYSICAL / LOCAL

NOSIG. No LA-area infrastructure threats, no anomalous SoCal activity. Your droog network is quiet.

---

## SUPPLY CHAIN

NOSIG. No active supply chain compromises reported in the feeds. The Conti hacker who built and deployed their malware got four years in a federal pen. [The Register] That's not a threat, that's precedent — a slow, public precedent that selling malware has consequences. Justice system running about 3–4 years behind the crime, which is horrifying and also useless.

---

## ASSESSMENT

You're viddy-ing a stack of technical noise layered over two real concerns: passkey phishing (active, working, immediate) and a handful of old CVEs in public repos (exploitable, routine, assumed compromised). The rootkit on F5/Cisco is production-grade active compromise, but it's not targeting your fleet. Everything else is signal-to-noise decay — archaeological digs, false alarms, LE activity overseas that doesn't move your threat posture.

**KEY JUDGMENTS:**

1. Passkey phishing against Microsoft cloud is *real-time active* — patch your user training and audit MFA logs today. This is the one that breaks into your network if your users slip. [HIGH CONFIDENCE]

2. Ancient CVEs (2020–2023) in public exploit repos are now commodity post-exploitation vectors; assume they're in active use by commodity attackers. Patching compliance is now a prerequisite, not a project. [HIGH CONFIDENCE]

3. Geopolitically, the only movement is NATO's nervous system misfiring over birds in Lithuania and routine Ukrainian strikes on Russian war material. Russia's not escalating, NATO's just jumpy. [MODERATE CONFIDENCE]

Your network isn't under active assault from nation-states today. You're instead under the routine corrosion of a thousand contractors, script kiddies, and business-as-usual ransomware crews — all of whom will slip through the door if your users hand them the keys. Keep the 2FA logs screaming and you'll viddy them coming.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/operations/2026-09-13-daily-briefing-posture.webp)