---
title: "🛡️ 🚨 SECURITY ALERT — CISA ADDS TWO VULNERABILITIES TO KNOWN EXPLOITED VULNERABILITIES CATALOG"
date: 2026-06-08T18:33:56-07:00
draft: false
categories: ["operations"]
tags: ["breaking", "alert", "cisa", "current", "activity:"]
description: "BREAKING: CISA Current Activity: CISA Adds Two Known Exploited Vulnerabilities to Catalog (cont)"
cover:
  image: "/images/operations/2026-06-08-security-alert-cisa-adds-two-vulnerabilities-to-known-exploi.webp"
  alt: "🚨 SECURITY ALERT — CISA ADDS TWO VULNERABILITIES TO KNOWN EXPLOITED VULNERABILITIES CATALOG"
  relative: false
---

![🚨 SECURITY ALERT — CISA ADDS TWO VULNERABILITIES TO KNOWN EXPLOITED VULNERABILITIES CATALOG](/images/operations/2026-06-08-security-alert-cisa-adds-two-vulnerabilities-to-known-exploi.webp)

**BLUF:** CISA has added two vulnerabilities to its Known Exploited Vulnerabilities (KEV) Catalog, confirming active exploitation in the wild. All organizations should treat these as priority remediation targets immediately. Federal Civilian Executive Branch (FCEB) agencies are under binding remediation deadlines per BOD 22-01.

---

## DETAILS

- CISA has officially cataloged two newly confirmed exploited vulnerabilities; **specific CVE identifiers and affected products were not included in the source data provided — treat as unconfirmed pending full CISA advisory review**
- Active exploitation has been confirmed by CISA, meeting the threshold required for KEV Catalog inclusion
- BOD 22-01 mandates FCEB agencies remediate KEV-listed vulnerabilities within defined timeframes; non-compliance carries regulatory risk
- CISA explicitly extends its remediation urgency recommendation to **all organizations**, not only federal entities
- The broader threat landscape at time of publication includes active exploitation of FortiClient EMS, WP Maps Pro, Everest Forms Pro, and SolarWinds Serv-U — organizations should assess exposure across all active KEV entries concurrently

---

## IMPACT

- **Directly bound:** All U.S. Federal Civilian Executive Branch agencies (BOD 22-01 compliance required)
- **At risk:** All organizations running unpatched software matching the newly cataloged CVEs — **specific vendor/product scope cannot be confirmed from available data**
- **Scope:** Exploitation is confirmed active; unpatched systems should be considered at elevated and immediate risk

---

## RECOMMENDED ACTIONS

1. **Immediately** cross-reference the full CISA KEV Catalog at [cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) to identify the two newly added CVEs and confirm affected products
2. Initiate emergency patch assessment for any systems matching newly listed vulnerabilities
3. FCEB agencies: confirm BOD 22-01 remediation timelines and begin tracking compliance
4. All organizations: incorporate KEV Catalog into routine vulnerability management cycles — do not treat this as a federal-only concern
5. Review exposure to concurrently active exploitation campaigns (FortiClient EMS, SolarWinds Serv-U, WordPress plugin flaws) given elevated threat tempo

---

## ⚠️ UNCERTAINTY FLAGS

- Specific CVE numbers and affected vendor products **not confirmed** in available source material — verify directly via CISA before scoping remediation
- Threat actor attribution for the two newly added CVEs is **unknown at this time**

---

## SOURCES

- CISA Current Activity: *CISA Adds Two Known Exploited Vulnerabilities to Catalog*
- CISA Binding Operational Directive 22-01 Fact Sheet
- Supporting context: The Hacker News, CISA KEV Catalog (cisa.gov)