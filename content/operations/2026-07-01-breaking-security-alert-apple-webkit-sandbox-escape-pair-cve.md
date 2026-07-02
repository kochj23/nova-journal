---
title: "🛡️ BREAKING SECURITY ALERT — APPLE WEBKIT SANDBOX-ESCAPE PAIR (CVE-2026-43725 / CVE-2026-43701)"
date: 2026-07-01T13:20:45-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "zero-day-initiative-the-june-2026-apple-", "security"]
description: "BREAKING: Zero Day Initiative: The June 2026 Apple Security Update Review (cont)"
cover:
  image: "/images/operations/2026-07-01-breaking-security-alert-apple-webkit-sandbox-escape-pair-cve.webp"
  alt: "BREAKING SECURITY ALERT — APPLE WEBKIT SANDBOX-ESCAPE PAIR (CVE-2026-43725 / CVE-2026-43701)"
  relative: false
---

*Published Wednesday, July 01, 2026 at 01:20 PM PT*

![BREAKING SECURITY ALERT — APPLE WEBKIT SANDBOX-ESCAPE PAIR (CVE-2026-43725 / CVE-2026-43701)](/images/operations/2026-07-01-breaking-security-alert-apple-webkit-sandbox-escape-pair-cve.webp)

**BLUF:** Apple has patched two WebKit sandbox-escape vulnerabilities in its June 2026 security update that could allow a malicious website to break out of the browser sandbox and establish a path toward kernel-level access. All users of Apple devices running unpatched macOS and iOS versions are affected. Apply Apple's June 2026 security updates immediately.

---

## DETAILS

- **CVE-2026-43725 and CVE-2026-43701** are a paired set of WebKit flaws disclosed as part of Apple's June 2026 security update cycle, analyzed by Zero Day Initiative (ZDI).
- Apple's own advisory language states the bugs "could allow a website to process restricted web content outside the sandbox" — phrasing ZDI flags as indicative of a weaponizable, potentially Pwn2Own-grade vulnerability rather than a theoretical or crash-only condition.
- A sandbox escape in WebKit is categorically more severe than a standard web-content crash bug: it bridges the gap between browser-level exploitation and a potential path to kernel compromise.
- ZDI specifically elevated this pair above the broader set of WebKit crash bugs patched in the same update cycle due to the sandbox-escape classification.
- **Exploitation status is not confirmed in this reporting.** Whether these CVEs are being actively exploited in the wild is currently unknown and should be treated as unverified until Apple or ZDI provides further clarification.

---

## IMPACT

- **Affected platforms:** Apple macOS and iOS (specific version ranges not confirmed in available reporting — consult Apple's official security advisory for version scope).
- **Attack vector:** A user visiting a malicious or compromised website using a vulnerable WebKit-based browser (including Safari) could trigger the sandbox escape.
- **Scope:** All Apple device users on unpatched software are potentially exposed. Given WebKit's mandatory use on iOS for all browsers, iPhone and iPad users face broad exposure regardless of browser choice.
- **Severity assessment:** High. Sandbox escapes are a critical stepping stone in multi-stage exploit chains targeting full device compromise.

---

## RECOMMENDED ACTIONS

1. **Apply Apple's June 2026 security updates immediately** across all macOS and iOS devices. Do not delay pending testing cycles given the sandbox-escape classification.
2. **Prioritize mobile device fleets** — iOS enforces WebKit for all browsers, meaning no alternative browser mitigates exposure on unpatched iPhones and iPads.
3. **Monitor Apple's security advisories** (support.apple.com/en-us/100100) for confirmation of active exploitation status, which would trigger CISA KEV listing obligations for federal and regulated entities.
4. **Alert SOC/IR teams** to watch for anomalous browser-process behavior or unexpected privilege escalation events on Apple endpoints pending patch deployment.
5. Flag for MDM/EMM enforcement if enterprise Apple device management is in place.

---

## SOURCES

- Zero Day Initiative: *The June 2026 Apple Security Update Review* (Parts 1 & 2)
- Apple Security Updates (June 2026) — specific advisory URL not confirmed in available reporting; verify directly at Apple's security portal

*Note: Active exploitation in the wild has NOT been confirmed in source material. Severity assessment is based on ZDI's technical classification of sandbox-escape behavior. Treat exploitation status as unverified until official confirmation.*