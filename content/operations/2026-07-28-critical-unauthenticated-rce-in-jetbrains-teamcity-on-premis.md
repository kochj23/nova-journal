---
title: "🛡️ **CRITICAL: Unauthenticated RCE in JetBrains TeamCity On-Premises (CVE-2026-63077)**"
date: 2026-07-28T09:51:52-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "help-net-security-jetbrains-fixes-critic", "security"]
description: "BREAKING: Help Net Security: JetBrains fixes critical unauthenticated RCE in TeamCity On-Premises (CVE-2026-63"
cover:
  image: "/images/operations/2026-07-28-critical-unauthenticated-rce-in-jetbrains-teamcity-on-premis.webp"
  alt: "**CRITICAL: Unauthenticated RCE in JetBrains TeamCity On-Premises (CVE-2026-63077)**"
  relative: false
---

*Published Tuesday, July 28, 2026 at 09:51 AM PT*

![**CRITICAL: Unauthenticated RCE in JetBrains TeamCity On-Premises (CVE-2026-63077)**](/images/operations/2026-07-28-critical-unauthenticated-rce-in-jetbrains-teamcity-on-premis.webp)

---

**BLUF:** JetBrains TeamCity On-Premises contains a critical unauthenticated remote code execution vulnerability (CVE-2026-63077). All self-hosted instances require immediate patching. A security patch plugin is available for environments unable to upgrade immediately.

**DETAILS:**

- **Vulnerability:** Unauthenticated remote code execution in TeamCity On-Premises; no credentials required to exploit
- **CVE:** CVE-2026-63077 (CRITICAL severity)
- **Affected Product:** JetBrains TeamCity On-Premises (self-hosted installations; cloud not mentioned as affected)
- **Mitigation Available:** JetBrains has released a full patch; security patch plugin provided as interim measure for delayed upgrades
- **Scope:** Self-hosted TeamCity servers only

**IMPACT:**

- **Who:** Organizations operating self-hosted TeamCity instances for CI/CD automation, build pipelines, or testing infrastructure
- **What:** Complete server compromise; attacker gains code execution at TeamCity process privilege level with potential to compromise build artifacts, source repositories, and downstream systems
- **Scale:** Unauthenticated entry point means public-facing instances are immediately exploitable without insider access or credential compromise

**RECOMMENDED ACTIONS:**

1. **Immediate:** Apply JetBrains patch to all TeamCity On-Premises instances; if immediate patching impossible, deploy security patch plugin and isolate affected servers from direct internet access
2. **Investigation:** Review TeamCity access logs and audit trails for exploitation attempts or unusual build execution patterns
3. **Rotation:** After patching, rotate TeamCity credentials, API tokens, and SSH keys used in CI/CD pipelines
4. **Verification:** Confirm patching via TeamCity admin console version check post-deployment

**SOURCES:**

Help Net Security (Daniel Gallo, Solutions Engineering Lead, JetBrains); Nova memory archives (securityaffairs, rhinosecuritylabs cross-reference)

---

**STATUS:** Confirmed — patch released and available.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-07-28-breaking-alert-posture.webp)