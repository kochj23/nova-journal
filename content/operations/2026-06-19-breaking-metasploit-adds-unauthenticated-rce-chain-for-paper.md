---
title: "🛡️ BREAKING: Metasploit Adds Unauthenticated RCE Chain for Paperclip AI, NTLM Relay-to-Self Privilege Escalation Module"
date: 2026-06-19T12:28:21-07:00
draft: false
categories: ["operations"]
tags: ["breaking-alert", "rapid7", "security"]
description: "BREAKING: Rapid7: : "
cover:
  image: "/images/operations/2026-06-19-breaking-metasploit-adds-unauthenticated-rce-chain-for-paper.webp"
  alt: "BREAKING: Metasploit Adds Unauthenticated RCE Chain for Paperclip AI, NTLM Relay-to-Self Privilege Escalation Module"
  relative: false
---

*Published Friday, June 19, 2026 at 12:28 PM PT*

![BREAKING: Metasploit Adds Unauthenticated RCE Chain for Paperclip AI, NTLM Relay-to-Self Privilege Escalation Module](/images/operations/2026-06-19-breaking-metasploit-adds-unauthenticated-rce-chain-for-paper.webp)

**BLUF:** Rapid7 has released new Metasploit modules including a full unauthenticated RCE exploit chain targeting Paperclip AI and a Windows local privilege escalation module abusing NTLM relay-to-self via WebDAV. Organizations running Paperclip AI or Windows domain-joined systems should treat this as an active exploitation risk — weaponized, ready-to-run exploit code is now publicly available.

---

## DETAILS

- **Paperclip AI RCE:** A new Metasploit module delivers a complete unauthenticated remote code execution chain against Paperclip AI. No credentials are required to exploit. Specific CVE identifiers and affected version ranges have not been confirmed in available reporting — treat all Paperclip AI deployments as potentially vulnerable until vendor guidance is issued.

- **NTLM Relay-to-Self (windows/local/ntlm_relay_2_self):** The new module coerces the local machine account to authenticate via the `OpenEncryptedFileRaw` WebDAV API, relays that NTLM authentication to a Domain Controller's LDAP service, then uses the resulting authenticated LDAP session to write Shadow Credentials and obtain a Kerberos service ticket — enabling privilege escalation on domain-joined Windows hosts.

- **VS Code Extension Persistence:** A new technique for achieving persistence via Visual Studio Code extensions has been added. Specific technical details beyond this are unconfirmed at time of publication.

- **Total release:** Five new modules shipped in this Metasploit weekly release. Details on the remaining two modules are not confirmed in available reporting.

- **Exploitation barrier is low:** Metasploit modules represent packaged, point-and-click exploit capability. Availability in the framework significantly lowers the skill threshold required for exploitation.

---

## IMPACT

- **Paperclip AI users:** Any organization or individual running Paperclip AI is potentially exposed to unauthenticated remote code execution. Scope of deployment is not publicly quantified.
- **Windows domain environments:** Domain-joined Windows systems are at risk from the NTLM relay-to-self module, which can enable local privilege escalation to domain-level access via Shadow Credentials abuse. This is particularly dangerous in environments where LDAP signing and channel binding are not enforced.
- **Developer environments:** VS Code persistence technique expands attacker footholds in developer workstations — a high-value target given code repository and credential access.

---

## RECOMMENDED ACTIONS

1. **Paperclip AI:** Isolate or take offline until vendor patches or mitigations are confirmed. Monitor vendor channels for CVE disclosure and patching guidance.
2. **NTLM Relay mitigation:** Enforce LDAP signing and LDAP channel binding on all Domain Controllers. Disable WebDAV client service (`WebClient`) on endpoints where not required.
3. **Shadow Credentials monitoring:** Alert on unexpected writes to the `msDS-KeyCredentialLink` attribute in Active Directory.
4. **VS Code environments:** Audit installed extensions on developer systems; restrict extension installation to approved marketplace sources via policy.
5. **Patch and update:** Ensure EDR/AV signatures are current — detection for new Metasploit modules typically follows release within hours to days.

---

## SOURCES

- Rapid7 Metasploit Weekly Release (via Nova feed)
- *Note: CVE identifiers, specific affected Paperclip AI versions, and full details on two of the five modules are unconfirmed at time of publication. Update expected as vendor advisories are released.*