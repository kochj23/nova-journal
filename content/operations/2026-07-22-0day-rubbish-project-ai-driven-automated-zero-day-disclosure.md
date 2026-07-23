---
title: "🛡️ **0DAY RUBBISH PROJECT: AI-DRIVEN AUTOMATED ZERO-DAY DISCLOSURE AT SCALE**"
date: 2026-07-22T20:58:02-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "seclists-a-project-is-publishing-full-an", "security"]
description: "BREAKING: seclists: A project is publishing full analyses of AI-discovered 0-days - first batch of 10 with rep"
cover:
  image: "/images/operations/2026-07-22-0day-rubbish-project-ai-driven-automated-zero-day-disclosure.webp"
  alt: "**0DAY RUBBISH PROJECT: AI-DRIVEN AUTOMATED ZERO-DAY DISCLOSURE AT SCALE**"
  relative: false
---

*Published Wednesday, July 22, 2026 at 08:58 PM PT*

![**0DAY RUBBISH PROJECT: AI-DRIVEN AUTOMATED ZERO-DAY DISCLOSURE AT SCALE**](/images/operations/2026-07-22-0day-rubbish-project-ai-driven-automated-zero-day-disclosure.webp)

**BLUF:** Project "0day Rubbish" is actively publishing full technical analyses and reproducible exploits for AI-discovered zero-day vulnerabilities; first batch of 10 released July 22. Multi-LLM ensemble (Claude, OpenAI, DeepSeek, GLM) systematically identifies flaws. Threat actors now have weaponized disclosure model plus working proof-of-concept code. All connected infrastructure should assume 10 new unpatched vectors are in active reconnaissance/exploitation phases.

**DETAILS:**
- **Confirmed scope:** First batch contains 10 documented 0-day vulnerabilities with reproducible, published exploits. Full technical analyses (not summaries) are publicly available.
- **Confirmed automation:** Vulnerability discovery driven by multi-LLM ensemble combining Claude, OpenAI, DeepSeek, and GLM models; not manual research.
- **Confirmed intent:** Project explicitly states continuous disclosure model — this is first batch; more to follow on an undisclosed cadence.
- **Confirmed distribution:** Posted to public security mailing list (seclists) July 22, 2026. No gating or responsible-disclosure process mentioned.
- **Timing uncertainty:** No visibility into whether these are zero-days in currently-deployed systems, legacy software, or research targets. Threat actors have likely begun reverse-engineering the exploits within hours.

**IMPACT:**
- **Immediate:** Every organization running software in the affected CVE families faces unpatched attack surface with public working exploits.
- **Systemic:** Establishes proof-of-concept that LLM ensembles can systematically mine vulnerability patterns faster than vendors can patch. This is a new class of at-scale disclosure risk.
- **Escalation vector:** Prior incidents show threat actors rapidly weaponize published 0-day PoCs; expect exploit kits within 48–72 hours.

**RECOMMENDED ACTIONS:**
- **Now:** Query your vulnerability management platform for any CVEs matching the 10 disclosed; assume they're actively scanned.
- **Now:** Brief security and engineering teams that public exploits exist; raise vulnerability triage priority to critical.
- **Within 24h:** Contact your major software vendors (OS, cloud, application) asking ETA for patches; plan emergency change windows.
- **Ongoing:** Monitor threat intelligence feeds (Shodan, CISA, vendor advisories) for active exploitation reports.

**SOURCES:**
- Seclists post, Jul 22, 2026 (zz lin). Project: "0day Rubbish"
- Multi-LLM ensemble: Claude, OpenAI, DeepSeek, GLM

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-07-22-breaking-alert-posture.webp)