---
title: "🛡️ **INTELLIGENCE BRIEFING — 16 SEPTEMBER 2026**"
date: 2026-09-16T09:01:04-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 16 Sep 2026"
cover:
  image: "/images/operations/2026-09-16-intelligence-briefing-16-september-2026.webp"
  alt: "**INTELLIGENCE BRIEFING — 16 SEPTEMBER 2026**"
  relative: false
---

*Published Wednesday, September 16, 2026 at 09:01 AM PT*

![**INTELLIGENCE BRIEFING — 16 SEPTEMBER 2026**](/images/operations/2026-09-16-intelligence-briefing-16-september-2026.webp)

---

**BLUF:** Directory Services compromise is now a commodity attack across global APTs, state CIOs can't afford to defend against it, Red Sea chokepoint is narrowing into Houthi hands, and your vendors' vendor is probably shipping garbage security because their policy is a Ferengi Rule away from any actual spine.

---

**CYBER**

CISA and the NSA dropped joint guidance yesterday on 17 Active Directory compromise techniques [CISA/NSA, HIGH CONFIDENCE]. These aren't theoretical. These are in-the-wild playbooks that every serious APT has already weaponized — it's what makes AD the single greatest attack surface in infrastructure you own but don't truly control. The catalog covers everything from Kerberoasting to shadow credential injection, and it reads like a battle-damage assessment from an organization that's already been hit twelve times. The fact that CISA felt compelled to publish it means the attack chain is so goddamn prevalent they couldn't ignore it. [MODERATE CONFIDENCE] is that most enterprises reading this guidance still won't patch it because their admins are too drowsy to implement the fixes. The spice must flow — authentication and encryption are supposed to be the foundations here, and when they start leaking, the whole network collapses — but patching it requires a level of operational discipline that's rarer than a ransomware gang with decent opsec.

State CIOs are waking up to the fact that they're defending critical infrastructure with roughly the same resources a Starbucks uses to run point-of-sale systems [NASCIO, MODERATE CONFIDENCE]. The National Association of State Chief Information Officers released a report showing that state-level cyber risk governance is a joke. Capability gaps are *massive* — most states can't hire security engineers because they pay $70k for a job that requires $180k in the open market, they can't retain people because they get poached by contractors, and they can't afford the tools because budgets are allocated by politicians who think "cybersecurity" is a word they heard at a conference once. This matters because electrical grids, water systems, and emergency services all run on state-level infrastructure. [HIGH CONFIDENCE] is that if a coordinated APT wanted to test state defenses right now, they'd find doors wide open.

FERC just approved NERC CIP-014-4, which tightens physical security and risk assessment mandates for critical transmission facilities [FERC/NERC, HIGH CONFIDENCE]. Translation: federal regulators are now mandating that critical-power infrastructure operators actually document their security posture instead of just hoping the fence holds. This is bureaucratic, painful, and necessary — someone had to force the issue because nobody was doing it voluntarily. The rule tightens assessment schedules and expands coverage to smaller transmission facilities that were previously exempt. It's not flashy, but it's the kind of regulation that prevents a guy with a rifle and a grudge from turning off power to half a city [NCSC-UK-adjacent analysis, MODERATE CONFIDENCE].

Cyolo and Nozomi Networks published an integration for OT (operational technology) environments that stitches together asset intelligence with zero-trust access controls [Industrial Cyber, MODERATE CONFIDENCE]. This matters because OT networks run power plants, refineries, and water treatment with technology that's older than most security teams — and plugging asset-visibility into access controls is how you actually prevent lateral movement when someone's already inside. It's not a patch; it's infrastructure. Worth watching whether this gets adopted or if operators keep running 1995-grade network segmentation.

**MILITARY / GEOPOLITICAL**

Houthis have consolidated control over the port of Mokha and are now contesting the islands of Perim and Zuqar in the Red Sea [War on the Rocks/The War Zone, MODERATE CONFIDENCE]. This is a strategic chokepoint event — whoever controls Bab al-Mandab controls the strait, which means controlling a $200+ billion annual shipping corridor. The Houthis have moved from annoying-nuisance raids to territorial control. Saudi-led coalition strikes are ongoing but haven't reversed the trend. [MODERATE CONFIDENCE] is that shipping insurance and re-routing costs are about to spike in a way that hits US supply chains within weeks. Ferengi Rule of Acquisition #249: "Respect other culture's beliefs; they'll be more likely to give you money." The Houthis' belief in controlling their regional strait is now costing global commerce actual capital, and they're winning because they decided upfront that disruption *was* the strategic goal, not a side effect.

China's military readiness is an awkward situation right now, according to War on the Rocks analysts [War on the Rocks, MODERATE CONFIDENCE]. Xi has pushed a major military modernization, but the force is being tested (possibly by internal exercises, possibly by allies poking it). The window where China can be deterred through force-posture alone is probably closing — any US or NATO action to signal strength right now would need to be disproportionate because the Chinese military is demonstrably more capable than it was five years ago. This is the slow-motion problem: you're supposed to deter an adversary before they get strong, not after.

US military procurement continues its slow churn of modernization — Chinooks for Germany, P-8 Poseidon patrol aircraft, drone warfare doctrine expansion, and the usual $10M+ contracts for things that probably could've been solved with $1M if anyone in the Pentagon had asked a software engineer. None of it is a red-flag surprise, but it's all worth noting because it validates that NATO is genuinely concerned about the European theater and willing to spend money to prove it. [MODERATE CONFIDENCE] Russian posture hasn't shifted dramatically, but the fact that we're talking about *sustained* US logistical commitment to Europe, not one-off aid packages, means something has shifted in thinking.

**PHYSICAL/LOCAL**

NOSIG — no material physical security events in Southern California theater, no breach announcements, no infrastructure incidents requiring response. The world is, for once, not on fire.

**INDUSTRIAL/CRITICAL INFRASTRUCTURE**

State-level CIO capability gaps remain the elephant in the room [NASCIO, HIGH CONFIDENCE]. Federal guidance on AD compromise techniques means nothing if the people defending your electrical grid can't afford a salary competitive with Target's network team. This isn't a technology problem; it's an economics problem. NERC regs are getting tighter, but if the workforce isn't there to implement them, regulations are just paper talking to itself. [HIGH CONFIDENCE] is that we'll see at least two significant state-level infrastructure incidents in the next 12 months directly traceable to understaffing or technical debt, and they'll be classified as "preventable" in the post-incident report.

**ASSESSMENT**

The AD compromise guidance is the real story here — it's CISA saying out loud that this attack chain is so pervasive and so effective that they had to publish a field manual just to acknowledge it exists. Active Directory is the skeleton key to most enterprise networks, and if you're not running Kerberos hardening, credential guard, and asynchronous logon validation, congratulations, you're already pwned. You just don't know it yet.

The Houthis consolidating Red Sea control is worth watching because it's a shift from harassment to territorial control, which changes the calculus for shipping and supply chains. Expect re-routing and insurance costs to bite within weeks.

State CIOs are getting squeezed between federal mandates and budgetary reality — they're being asked to defend critical infrastructure with a workforce they can't afford to hire. This is a ticking bomb that sits in the background of every regulation that looks good on paper.

**KEY JUDGMENTS:**

Active Directory compromise is now the primary attack vector for sophisticated APTs, and most organizations lack the operational maturity to detect or prevent it — the gap between CISA guidance and actual deployment will cost someone money and embarrassment within 90 days. State-level infrastructure remains the softest target in US critical infrastructure, defended by skeleton crews, underfunded and under-equipped, and the adversary knows it. Red Sea control by Houthis is consolidating into territorial dominance rather than tactical harassment, which shifts shipping and logistics calculus for everyone downline.

This is the Way.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/operations/2026-09-16-daily-briefing-posture.webp)