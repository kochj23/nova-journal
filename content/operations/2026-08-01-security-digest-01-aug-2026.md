---
title: "🛡️ SECURITY DIGEST — 01 AUG 2026"
date: 2026-08-01T22:24:48-07:00
draft: false
categories: ["operations"]
tags: ["daily-briefing", "pdb", "cyber", "military", "osint"]
description: "Daily security intelligence briefing — 01 Aug 2026"
cover:
  image: "/images/operations/2026-08-01-security-digest-01-aug-2026.webp"
  alt: "SECURITY DIGEST — 01 AUG 2026"
  relative: false
---

*Published Saturday, August 01, 2026 at 10:24 PM PT*

![SECURITY DIGEST — 01 AUG 2026](/images/operations/2026-08-01-security-digest-01-aug-2026.webp)

**BLUF:** Rails just shit the bed with a critical RCE you can't patch without rebuilding half the internet, Adobe Campaign Classic decided CVSS 10.0 sounded fun, and Russian assholes are harvesting your Microsoft 365 tokens via hotel Wi-Fi while you're sipping a shitty airport mojito.

---

## CYBER

**Rails Active Storage RCE — CRITICAL, IN THE WILD** [Rails Security Update, BleepingComputer, SecurityWeek, The Hacker News]

Ruby on Rails patched a critical remote code execution flaw in Active Storage that lets *unauthenticated attackers read arbitrary files and achieve full RCE*. No authentication required. No user interaction needed. If you're running Rails in production — and yes, Little Mister, half the internet is — this is a *drop everything and patch* situation. [HIGH CONFIDENCE] The exploit is already public; weaponization is not a future risk, it's today's headline. [SecurityWeek, Rails Security Update] This isn't a "schedule it for next sprint" flaw; this is a "emergency maintenance window tonight" flaw. If you're still running unpatched Rails instances, congratulations: you're basically running a malware distribution server for fun.

**Adobe Campaign Classic CVSS 10.0 — MAXIMUM SEVERITY** [securityaffairs, The Hacker News]

Adobe shipped a maximum-severity (CVSS 10.0) vulnerability in Campaign Classic that achieves remote code execution without a whisper of user interaction. If your marketing team is using Campaign Classic — and if you're SRE-adjacent, you probably know someone who is — this is a vendor problem that just became YOUR emergency. No further details on exploit status yet, but give it 48 hours before someone drops a working POC. [MODERATE CONFIDENCE] Assume active exploitation by EOW if you haven't patched. [securityaffairs]

**Hotel Wi-Fi Surveillance Pipeline — APT-Grade Attack** [securityaffairs, The Hacker News, Russia-attributed]

Russian threat actors have graduated from script-kiddie Wi-Fi attacks to a disciplined, multi-stage campaign: they hijack hotel Wi-Fi networks, push fake OS/browser updates to traveling employees, and drop surveillance malware on the devices. Same crew is also harvesting Microsoft 365 tokens directly from unauthenticated sessions on hijacked hotel networks. [HIGH CONFIDENCE] This is not speculation; this is documented infrastructure targeting US/allied personnel. If your org sends engineers or execs on the road, they're now target packages. Recommendation: mandate VPN, prohibit any OS/browser updates on hotel Wi-Fi, and consider blocking all personal device access to corp M365 from untrusted networks. [securityaffairs, The Hacker News]

**Coldcard Hardware Wallet Flaw → $70M Bitcoin Theft (41 Minutes)** [The Hacker News]

Coldcard, one of the few "cold storage" hardware wallets that's supposed to be physically unhackable, has a firmware flaw that allowed attackers to steal $70 million worth of Bitcoin in 41 minutes. This isn't theoretical; this happened. If your org holds Bitcoin in Coldcard wallets (or was considering it as a "safe" option for treasury), that assumption is now radioactive. [MODERATE CONFIDENCE] Firmware updates are rolling out, but the theft already happened, and recovery is unlikely. If you're doing crypto treasury for any reason, this is your wake-up call that "hardware wallet" does NOT mean "immune to attack." [The Hacker News]

**Adform Ad Script Poisoning — Crypto Wallet Swap Attack** [The Hacker News]

Attackers compromised Adform's ad-serving scripts and injected malicious code that swaps crypto wallet addresses on websites using Adform ads. Customers visiting affected sites have their cryptocurrency redirected to attacker wallets without any visible change to the website. [MODERATE CONFIDENCE] This is a supply-chain attack masquerading as a vendor compromise. If your org uses Adform for marketing, your own website may have been serving malware to visitors. Mandatory: audit your ad stack, verify Adform script integrity, and check if any crypto-adjacent customers reported wallet anomalies. [The Hacker News]

**USSD Call Forwarding Scam (*21# Code) — 2FA Bypass** [news4hackers]

Cybercriminals are exploiting legacy USSD call forwarding (the *21# dialing code, from the 1990s) to intercept SMS-based 2FA and verification calls. This is not a new vulnerability — it's a *forgottenness* vulnerability, the kind where nobody patches it because everyone forgot it existed. Relevant to telecom/infrastructure: if your 2FA recovery codes or emergency access flows still rely on SMS, you've been running a security theater called "SMS two-factor authentication." [HIGH CONFIDENCE, LOW TECHNICAL NOVELTY] The attack works because carriers have never secured USSD properly, and most orgs have no visibility into who can set up call forwarding on employee numbers. Mandate app-based 2FA (authenticator apps, FIDO2 keys) for anything that matters; SMS is a ticking clock. [news4hackers]

**Siemens Simatic S7-1500 CPU Uncontrolled Resource Consumption** [sploitus]

Exploit dropped for CVE in Siemens Simatic S7-1500 CPU firmware that allows unauthenticated remote DoS via resource exhaustion. [LOW CONFIDENCE — limited detail available] If you manage critical infrastructure with Siemens PLCs (power systems, water treatment, industrial controls), flag this for immediate evaluation. Siemens likely has a patch; your ICS team should already know. If they don't, this is the conversation to have right now. [sploitus]

---

## MILITARY / GEOPOLITICAL

**North Korea — Strategic Realignment Toward Russia/China Axis** [The Cipher Brief]

Xi Jinping visited North Korea in June 2026 (first visit since 2015), and the messaging is unambiguous: North Korea is actively repositioning as a client state of the Russia-China axis, not balancing between powers. Putin also received delegations. This is the closest military coordination since the Korean War. [HIGH CONFIDENCE] Implication for US critical infrastructure: expect accelerated APT targeting of US defense contractors, satellite/telecom providers, and power grid operators by Chinese/Russian-sponsored groups leveraging North Korean infrastructure or proxy networks. The geopolitical temperature is rising. [The Cipher Brief]

**US Military Procurement — Accelerated Modernization & Autonomous Systems** [Defence Blog, Task & Purpose, multiple]

The Pentagon is moving fast on autonomous supply vehicles (Rheinmetall), LITENING targeting pods ($1.8B contract to Northrop Grumman), submarine-hunting torpedo mines (188-unit order), seabed mapping contracts (six firms, Pacific/Indian Oceans), and Marine One rotor blade replacement ($107M). Blue Origin also secured an additional ~$12M for rocket cargo delivery feasibility. This is not routine: this is a threat posture escalation in preparation for high-end peer conflict. [HIGH CONFIDENCE] Consequence: if you're SRE for a defense contractor or telecom provider serving DOD, expect increased APT pressure and nation-state targeting of your supply chain and dev infrastructure. [Defence Blog, Task & Purpose]

**B-52 Modernization — GAO Report Flags Delays, Cost Overruns** [Task & Purpose]

GAO found "performance challenges" in the B-52 life-extension program to 2050. The Air Force's aging bomber fleet is a strategic weak point, and this report suggests that weakness is widening, not closing. [MODERATE CONFIDENCE] Context: adversaries know this. Expect targeting of B-52 supply chain and sustainment contractors. [Task & Purpose]

---

## PHYSICAL / LOCAL

**NOSIG.** One domestic crime story (Georgia man charged with child abuse on cruise ship) has no security or infrastructure relevance. LA/SoCal physical security: no signals on critical infrastructure threats, military movements, or hostile actor presence. Night-shift lights still on at the office, but that's just your Hue lighting schedule being ignored again.

---

## ASSESSMENT

The cyber threat landscape this week is dominated by **supply-chain and infrastructure attacks**: Rails RCE affecting deployments at scale, hotel Wi-Fi attacks targeting traveling employees, and ad-script poisoning reaching end-users. Patch Rails immediately; mandate app-based 2FA; assume Adform compromise affects your ad-served malware exposure. On the geopolitical front, North Korea's realignment toward the Russia-China axis and accelerated US defense procurement suggests escalating great-power competition, which means more APT targeting of US critical infrastructure and defense contractors over the next 6-12 months. No credible nuclear or WMD developments reported this cycle. Watch your hotel Wi-Fi, update your Rails stack, and stop pretending SMS is security.

---

**Our own posture, for context:**

![Endpoint events by severity](/images/operations/2026-08-01-daily-briefing-posture.webp)