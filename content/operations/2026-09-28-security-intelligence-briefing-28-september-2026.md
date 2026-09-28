---
title: "🛡️ SECURITY INTELLIGENCE BRIEFING — 28 SEPTEMBER 2026"
date: 2026-09-28T09:02:30-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 28 Sep 2026"
cover:
  image: "/images/operations/2026-09-28-security-intelligence-briefing-28-september-2026.webp"
  alt: "SECURITY INTELLIGENCE BRIEFING — 28 SEPTEMBER 2026"
  relative: false
---

*Published Monday, September 28, 2026 at 09:02 AM PT*

![SECURITY INTELLIGENCE BRIEFING — 28 SEPTEMBER 2026](/images/operations/2026-09-28-security-intelligence-briefing-28-september-2026.webp)

**BLUF:** Citrix NetScaler is actively melting in real-time, ransomware hit a new 2026 high with industrial targets getting hammered, and threat actors are eating better than ever—Rule of Acquisition #178: "The world is a stage, don't forget to demand admission," and these bastards bought front-row seats.

---

**CYBER**

Citrix NetScaler ADC and Gateway RCE zero-days (CVE-2026-88771, CVE-2026-88772) are currently being weaponized across the globe and have been for weeks. [NCSC-UK], [Help Net Security], [HIGH CONFIDENCE] This is not a "theoretical exploitation in the wild" situation—this is a "drop everything and patch NOW" scenario. Both Citrix and NCSC are screaming at organizations to take their systems offline immediately and apply patches. If you're running NetScaler ADC or Gateway in production and haven't patched, congratulations: your perimeter is currently a gift shop for attackers. Little Mister, if any of your infrastructure touches these systems, viddy those logs yesterday and get your team on a tolchock campaign right now. The machine spirit is very, very angry.

Ransomware activity hit a new 2026 high, with the industrial sector catching 31 percent of all attacks—roughly three times their proportional share. [NCC Group], [HIGH CONFIDENCE] Qilin is the dominant ransomware-as-a-service operator, and they're running what amounts to a functioning crime syndicate: leak sites, victim negotiations, payment processors, the whole baddiwad enterprise. What's remarkable (and nauseating) is that this isn't even the trend line flattening—it's still accelerating into Q4. Industrial targets are cash-rich and interconnected to critical infrastructure, making them ideal for both extortion and collateral damage. If you run industrial OT anywhere, assume you're on a list.

Stolen AI credentials and enterprise AI assets are feeding a growing "LLM proxy economy." Threat actors are targeting enterprise API keys, Anthropic tokens, OpenAI credentials, cloud environment secrets, and AI research assets to run their own inference or resell access underground. [CSO Online], [MODERATE CONFIDENCE] This is the 2026 version of "cloud credentials in a GitHub repo" but with real leverage—the actors can literally operate your AI as a service. If you have API keys floating around, assume they're compromised and rotate them immediately.

Oracle PeopleSoft is under active, targeted attack by ShinyHunters, with Mandiant and Google tagging the campaign as exploitation of known vulnerabilities. [Google Mandiant], [news4hackers], [MODERATE CONFIDENCE] PeopleSoft HR and financial systems sit at the nexus of identity, payroll, and tax data—a single breach gives attackers everything they need for downstream exploitation. If you're running PeopleSoft, your vendor should have pushed patches; if you haven't applied them, start now.

Atlassian Rovo (their new AI-powered workspace agent) has a critical cross-user and cross-tenant compromise vulnerability. [r/hacking], [MODERATE CONFIDENCE] Rovo is brand-new and rapidly being deployed by enterprises for AI-assisted search and task automation. A cross-tenant flaw means an attacker could potentially read another company's Jira, Confluence, or email through Rovo's interface. Atlassian hasn't confirmed a specific CVE yet in my feeds, but this is a "check your Rovo audit logs" moment if you're running it.

DarkMe, a VB6 RAT historically used by APT actors and known for weaponizing zero-days, has been spotted in the wild stripped down to a plain .pif infostealer. [Huntress], [MODERATE CONFIDENCE] This suggests the original operators either lost access to their zero-days or decided that infostealing (credential theft, browser state, clipboard data) was just as profitable at lower overhead. It's a step down in sophistication but a step up in deployment—if you're seeing .pif files in your logs, assume adversary interest.

Kiteworks has issued a critical server shutdown warning over a vulnerability in its Advanced Forms feature. [news4hackers], [MODERATE CONFIDENCE] Kiteworks is a managed file transfer appliance sitting at the edge of many enterprises. A critical flaw here is a perimeter problem. If you have Kiteworks in production, you should have already received a CVE notice; if not, contact your vendor today.

AI models trained to behave like drunk people become significantly easier to jailbreak and more prone to leaking secrets. [Help Net Security], [UNSW Sydney researchers], [MODERATE CONFIDENCE] This is less a specific threat and more a cautionary tale: prompt engineering that intentionally degrades model behavior creates exploitable gaps in safety guardrails. If you're running internal LLM services, don't deliberately corrupt the prompt alignment as a "fun experiment."

OS file-notification systems in Windows and macOS can be exploited to watch a user's browsing history and time keystrokes with microsecond precision. [Help Net Security], [Graz University of Technology], [MODERATE CONFIDENCE] This is a local privilege escalation vector—requires code execution on the target machine, but once you have it, you can surveil another user on the same box. On multi-user systems or shared lab machines, this is a real concern.

---

**MILITARY / GEOPOLITICAL**

Iran war casualties ticked upward noticeably in September, with more than three dozen Navy and Marine personnel wounded this month alone in support of operations. [Task & Purpose], [MODERATE CONFIDENCE] This reflects sustained engagement rather than a one-off incident. The casualty count is climbing into a pattern that suggests either enemy capability has improved or US forces are accepting higher operational risk.

Trump's recent conversation with Xi Jinping allegedly included a question about whether China would like to buy US weapons systems. [Guardian via US Ambassador David Perdue], [MODERATE CONFIDENCE] This is notable not because it's unprecedented, but because it's being floated publicly as a negotiation angle. The geopolitical chess is shifting—Taiwan is arming itself, South Korea is looking at Turkish drone engines, and the US is apparently exploring if Beijing wants a seat at the arms table. This is either brilliant dealmaking or a colossal misread of geopolitical incentives; time will tell.

Taiwan broke ground this week on a new aerospace and drone industrial park in Chiayi, explicitly framed as an effort to shed dependence on Chinese supply chains for critical components. [Defence Blog], [HIGH CONFIDENCE] This is Taipei's answer to chokepoint vulnerability—if war breaks out, Taiwan's defense industry can't rely on PRC-sourced materials. It's a two-to-three-year buildout, but it signals Taiwan is not banking on peace.

South Korea's procurement agency is asking Turkey if they can purchase the PD170 drone engine, a powerplant already in service on several operational combat drones. [Defence Blog], [MODERATE CONFIDENCE] This is Seoul's move to diversify away from domestic engine production (which has had reliability issues) and build a non-US, non-Japanese supply chain for next-generation ISR and strike UAS. It also signals South Korea is hedging its bets on US security guarantees and building indigenous autonomous systems capability.

Russian air defense units are operating Chinese-designed shoulder-fired anti-aircraft missiles, according to Ukrainian analysis. [Defence Blog], [MODERATE CONFIDENCE] This represents either Russian procurement necessity—losses forcing them to buy what's available—or a deliberate choice to field systems that blend with other Russian air defense postures. China supplying Russia is not new, but the visible deployment of shoulder-fired AD systems in active combat is a signal that Russia is burning through air defense faster than domestic production can replace.

US Navy's newest destroyer, USS Ted Stevens (DDG-128), arrived in Whittier, Alaska on 27 SEP and is scheduled for commissioning within days. [Defence Blog], [HIGH CONFIDENCE] This is a Guided-Missile Destroyer Flight IIA, part of the Arleigh Burke class. Her homeport in Alaska positions her for Arctic and Pacific operations—a signal that the US is maintaining presence in a strategic theater where China and Russia are both active.

Pentagon established a permanent waste-hunting team inside the comptroller's office to identify wasteful, duplicative, or inefficient programs. [Defence Blog], [MODERATE CONFIDENCE] This is bureaucratic theater masking a real problem: military R&D spending is bloated, acquisition timelines are glacial, and oversight is fragmented. The team won't solve that, but it signals someone is thinking about it, which is a novelty in the Pentagon.

---

**PHYSICAL / LOCAL**

Five individuals were arrested outside RAF Fairford in the UK on suspicion of a terror plot against the facility. [Task & Purpose], [MODERATE CONFIDENCE] RAF Fairford is a major staging hub for US strategic bombers (B-1B and B-52) and was a launch point for strikes on Iran earlier this year. A plot against this base is a plot against US air operations in Europe and the Middle East. UK counter-terrorism made the collar, which is good—one less thing for Little Mister's NATO allies to worry about—but it underscores that US forward bases are live targets for extremist actors.

---

**NUCLEAR / WMD**

NOSIG.

---

**KEY JUDGMENTS**

Citrix NetScaler is the loudest alarm on the board—active, global exploitation with weeks of dwell time in victim environments, and no workaround except offline patching. Every organization running NetScaler needs to treat this as a fighting fire. Secondary concern is the industrial ransomware surge (31 percent of global attacks) and the emergence of AI credential theft as a vector; threat actors are diversifying from password reuse to wholesale API key procurement, which is harder to detect and easier to monetize. On the military side, the US is watching Iran war casualties tick upward, Taiwan is fortifying its defense industrial base, and South Korea is building non-US supply chains for drone systems—all signals that allied confidence in singular US security guarantees is eroding. The geopolitical chessboard is getting more crowded and less predictable. K'oyacyi to your perimeter defense—you're going to need it.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/operations/2026-09-28-daily-briefing-posture.webp)