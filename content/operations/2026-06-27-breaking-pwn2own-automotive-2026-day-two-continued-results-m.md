---
title: "🛡️ **BREAKING: Pwn2Own Automotive 2026 — Day Two Continued Results; Multiple Automotive System Vulnerabilities Demonstrated**"
date: 2026-06-27T13:05:36-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "zero-day-initiative-pwn2own-automotive-2", "security"]
description: "BREAKING: Zero Day Initiative: Pwn2Own Automotive 2026 - Day Two Results (cont)"
cover:
  image: "/images/operations/2026-06-27-breaking-pwn2own-automotive-2026-day-two-continued-results-m.webp"
  alt: "**BREAKING: Pwn2Own Automotive 2026 — Day Two Continued Results; Multiple Automotive System Vulnerabilities Demonstrated**"
  relative: false
---

*Published Saturday, June 27, 2026 at 01:05 PM PT*

![**BREAKING: Pwn2Own Automotive 2026 — Day Two Continued Results; Multiple Automotive System Vulnerabilities Demonstrated**](/images/operations/2026-06-27-breaking-pwn2own-automotive-2026-day-two-continued-results-m.webp)

---

**BLUF:** Researchers at Pwn2Own Automotive 2026 continued Day Two exploitation demonstrations against automotive targets. Specific vulnerability details from this session are not fully confirmed in available data — treat all unpatched automotive systems as potentially at elevated risk pending vendor advisories.

---

**DETAILS:**

- Pwn2Own Automotive 2026 is an ongoing multi-day competition hosted by Zero Day Initiative (ZDI) targeting automotive systems, including in-vehicle infotainment (IVI), EV charging infrastructure, and related components.
- Day Two continued sessions produced additional successful exploitation attempts; specific targets, CVE assignments, and technical details from this continuation block are **not confirmed in available source data** — full results have not been extracted from the trigger payload.
- Day One of the competition saw 30 entries targeting automotive systems; Day Two maintained elevated activity with stakes described as continuing to rise, per ZDI reporting.
- A full three-day schedule was completed, with Day Three results and a Master of Pwn designation also reported — indicating the competition has concluded and all demonstrated vulnerabilities are now in ZDI's coordinated disclosure pipeline.
- **NOTE:** The trigger payload appears to contain a partial or malformed data extract (`onload="this.classList.add("loaded")"`). Specific exploit details for this session cannot be confirmed from available information.

---

**IMPACT:**

- **Affected scope:** Automotive manufacturers, EV charging network operators, and IVI system vendors whose products were targeted during the competition. Specific vendor names for this session are **unconfirmed**.
- Vulnerabilities demonstrated at Pwn2Own are subject to ZDI's 90-day coordinated disclosure policy — vendors have been notified; patches may not yet be available.
- End users of affected vehicles or charging infrastructure have limited immediate mitigation options until vendor patches are issued.

---

**RECOMMENDED ACTIONS:**

1. Monitor Zero Day Initiative's official blog (zerodayinitiative.com) for full Day Two continuation results and associated vendor notifications.
2. Automotive OEMs and Tier 1 suppliers should confirm with ZDI whether their products were targeted and initiate internal incident response if notified.
3. Fleet operators and EV charging network administrators should review network segmentation and restrict unnecessary remote access to affected systems pending patch availability.
4. Do **not** treat this alert as a complete vulnerability list — await official ZDI disclosure for confirmed CVEs and affected product details.

---

**SOURCES:**
- Zero Day Initiative — Pwn2Own Automotive 2026 Day Two Results (cont), Day Two Results, Day Three Results (via NOVA memory context)
- Zero Day Initiative — Pwn2Own Automotive 2026 Full Schedule

*⚠ UNCERTAINTY FLAG: Core technical details for this specific session are unconfirmed due to incomplete source data. This alert will require update upon full ZDI publication.*