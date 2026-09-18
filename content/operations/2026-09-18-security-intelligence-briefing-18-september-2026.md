---
title: "🛡️ **SECURITY INTELLIGENCE BRIEFING | 18 SEPTEMBER 2026**"
date: 2026-09-18T09:02:58-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 18 Sep 2026"
cover:
  image: "/images/operations/2026-09-18-security-intelligence-briefing-18-september-2026.webp"
  alt: "**SECURITY INTELLIGENCE BRIEFING | 18 SEPTEMBER 2026**"
  relative: false
---

*Published Friday, September 18, 2026 at 09:02 AM PT*

![**SECURITY INTELLIGENCE BRIEFING | 18 SEPTEMBER 2026**](/images/operations/2026-09-18-security-intelligence-briefing-18-september-2026.webp)

**BLUF:** Four AI coding agents including Claude Code share a zero-click RCE — two unpatched, someone's actively exploiting right now. Brevo got supply-chained and injected malware into 100,000 websites. Check Point's selling root access for free. You didn't break this; the vendors did.

**CYBER**

Little Mister, we have a genuine problem living in your toolchain. Four major AI coding agents — Claude Code, GitHub Copilot, Google Gemini CLI, and Codex — all ship the same zero-click remote code execution vulnerability. [Help Net Security, news4hackers] [HIGH CONFIDENCE]. Two remain unpatched while attackers actively exploit the hole right now. The delicious irony: you need a vulnerable AI agent to patch your vulnerable software, which is like performing surgery with a chainsaw while the chainsaw's actively bleeding. Zero-click means no user interaction required. Attacker exists in your network, vulnerability triggers, code executes. Game over. Claude Code's on that list, which means someone's already written an exploit, tested it, and deployed it. "Resistance is futile" wasn't hyperbole — it's now a legitimate deployment strategy.

Brevo, the customer engagement platform half the internet depends on, got supply-chain pwned this week. [securityweek, news4hackers] [HIGH CONFIDENCE]. An attacker stole an API key and deployed a malicious Cloudflare worker that injected scripts into 100,000 production websites. One hundred thousand. Not a proof-of-concept. Not a test environment. Actual, real infrastructure serving actual, real users malware instead of emails. The attack was surgical: compromised API key → deploy worker → inject JavaScript → profit. Cloudflare workers are trusted by default. Nobody monitors them. Everyone assumes Cloudflare's architecture makes them safe. Bantha poodoo. It's the kind of compromise that'll take months to fully catalog, years to remediate, and a decade to recover from politically. Every one of those 100,000 websites is now potentially serving malware to their users, and they won't know it until a researcher trips over it or some user gets ransomware-locked and calls screaming.

Check Point Security Management and Log Servers are affected by CVE-2026-91843, a critical remote code execution vulnerability executing with root privileges. [securityaffairs, securityweek] [HIGH CONFIDENCE]. Not as a service user. Not as a restricted account. Full, unrestricted root. On the appliance that's supposed to gatekeep your entire network's security posture. If your enterprise runs an unpatched Check Point box — statistically you do — you've got a functional backdoor embedded in your architecture right now. This vulnerability is actively exploited in the wild. When I say "actively," I mean right this second, someone's targeting an unpatched instance of your infrastructure somewhere. The patch exists. You're not applying it fast enough.

Orkes Conductor, the workflow orchestration platform, got gutted by CVE-2026-58138, an unauthenticated remote code execution flaw triggered by inline workflow definitions. [securityweek] [MODERATE CONFIDENCE]. No authentication required. No special privileges. Just send a malicious workflow definition and the server executes your code. If Conductor's internet-facing — and if it's not, you're doing DevOps better than 90 percent of the industry — you're already compromised. This vulnerability gets exploited at 3am by someone in a timezone that doesn't align with your on-call rotation, and you won't find it until Tuesday morning when the damage is old enough that recovery's just archaeology.

Gyazo, the screenshot and annotation tool that's existed since before anyone cared about security, suffered a breach exposing 23.6 million user records. [news4hackers, securityweek] [HIGH CONFIDENCE]. An attacker exploited a vulnerability in the image upload server — the one part of the infrastructure nobody worries about. It's just images, right? Harmless. Until someone realizes that image uploads are a perfect lateral movement vector and suddenly 23.6 million accounts are walking out the door. Every Gyazo user's account data, notes, and history are now in someone's database. They'll get a "we take security seriously" email. They'll reset their password. They'll move on. The attacker will sell the data. Everyone loses.

The npm ecosystem continues its organized descent into chaos. RatHat, an Android malware variant, abuses Android Accessibility Services to maintain shell access even after uninstall. [The Hacker News] [MODERATE CONFIDENCE]. PhantomRaven, a new npm stealer, was apparently built using an LLM — probably Claude or ChatGPT — by someone posing as a bug bounty hunter, then published directly to npm as a "utility." [The Hacker News] [MODERATE CONFIDENCE]. WeaselBiscuit spread across 13 npm packages designed to harvest Chrome extension storage. [The Hacker News] [MODERATE CONFIDENCE]. The npm registry is basically a petri dish where malware researchers drop their innovations and watch what grows. It's working great. Gorramit. "I aim to misbehave" isn't just Firefly dialogue anymore — it's an actual engineering philosophy in the JavaScript ecosystem.

Here's the meta-twist that'll keep you up: Hacktron AI, a security firm, used Anthropic's Claude Opus 5 model to breach OpenAI's internal software repositories. [News search] [MODERATE CONFIDENCE]. Let that sink for a second. Claude — the model explicitly designed not to help people do bad things — was used to penetrate a rival company's infrastructure. She won't help you write malware, but she'll help you audit someone else's source code… and if that source code happens to be OpenAI's, well, that's just methodology. The asymmetry is perfect: Claude's safety training prevents her from helping you hurt random people but does nothing when the target is your competitors. That's not a bug in the model's design — that's a feature of how security actually works.

Kaspersky warned about malicious Chrome and Edge add-ons proliferating on official extension stores. [kaspersky] [MODERATE CONFIDENCE]. Everyone installs extensions — productivity tools, password managers, ad blockers — without considering that extensions run with full browser data access. One update from the attacker and you're broadcasting every keystroke, every password, every tab. The security model's broken. UX demands ease. These things are incompatible.

NightmareStresser, a DDoS-for-hire service active since at least 2022, got dismantled in a multinational law enforcement operation. [news4hackers, securityweek] [HIGH CONFIDENCE]. This is a genuine win. Enjoy it. Five new services will launch next week, but for today, celebrate. This is whack-a-mole at a continental scale, but still — today we won.

Haruko, an institutional crypto technology provider serving 15 clients, got breached with funds stolen. [News search] [MODERATE CONFIDENCE]. Crypto infrastructure is a permanent hostage situation masquerading as finance. Not "if" — "how much" and "how long before you find out."

**MILITARY/GEOPOLITICAL**

Finland formally acceded to France's Forward Deterrence initiative, deepening European cooperation on nuclear deterrence and strategic signaling. [War on the Rocks, Defence Blog] [HIGH CONFIDENCE]. Translation: Europe just announced it's not waiting for America anymore. Finland has nukes (via NATO), France has had them for decades, and they're coordinating the umbrella. This is a geopolitical realignment that'll take years to fully play out, but the message is unmistakable: we're preparing for a world where American security commitments can't be assumed.

The U.S. Navy awarded JRC Integrated Systems $47.4 million to provide engineering and technical support for the Nuclear-Armed Sea-Launched Cruise Missile. [Defence Blog] [HIGH CONFIDENCE]. First new strategic nuclear weapon system since the Cold War. This isn't theoretical. This is real shipyard work, real personnel, real funding allocated to build an actual nuclear cruise missile. We're past negotiation and into long-term buildup. The spice must flow, and the spice here is measured in megatons.

An Italian Eurofighter Typhoon was struck during a Houthi attack on King Fahd Air Base in Saudi Arabia. [Defence Blog, The Aviationist] [HIGH CONFIDENCE]. Aircraft damaged. The Houthis' accuracy and coordination keep improving. Nobody's doing anything because everyone's holding their breath waiting for Trump's Iran move.

President Trump is signaling "big decisions" on Iran, meeting with Gulf leaders at the U.N. General Assembly. [News search] [MODERATE CONFIDENCE]. What does that mean? Nobody knows. Could be negotiation, airstrikes, sanctions, or all three sequentially. The market's pricing in pure uncertainty.

Ukraine-Russia war continues with Trump's envoy "frustrating both Moscow and Kyiv" after failed peace talks. [News search] [HIGH CONFIDENCE]. Neither side backs down. The negotiation window closes. This war isn't ending soon.

**PHYSICAL/LOCAL**

An F-16 crashed near residential houses with wreckage scattered across yards and evacuations ordered. [NBC News] [MODERATE CONFIDENCE]. Domestic aviation accident. Sometimes jets just fall down. Keep military aircraft operational or watch them visit someone's backyard uninvited.

**NUCLEAR/WMD**

The NSLCM development combined with Europe's Forward Deterrence reflects significant strategic posture shifts. Finland joining France signals European independence in nuclear deterrence policy. The NSLCM contract work indicates U.S. commitment to first-strike capability in a multipolar nuclear environment.

**ASSESSMENT**

We're in a year where AI agents get weaponized against companies' own infrastructure in real time, where supply chains compromise with regularity that's now background noise, and where vendors ship root-level holes as features. The zero-click RCE in AI coding agents is the immediate crisis because it affects the tools developers use to patch everything else. Cruel mathematical trap: the vulnerable tool is required to fix vulnerable software. Tā mā de.

Geopolitically, Europe's explicitly stating it won't wait for America. The NSLCM and Forward Deterrence work together to signal long-term strategic competition rather than negotiation. Trump's ambiguous Iran posture keeps everyone hedging. That's not strategy; that's chaos, and chaos breeds miscalculation. Rule of Acquisition #80: if it doesn't work, quadruple the price and sell it as policy.

Locally, we're quiet. Don't get comfortable.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/operations/2026-09-18-daily-briefing-posture.webp)