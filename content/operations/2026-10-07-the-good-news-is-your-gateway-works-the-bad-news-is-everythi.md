---
title: "🛡️ The Good News Is Your Gateway Works. The Bad News Is Everything Else Knows It."
date: 2026-10-07T07:32:58-07:00
draft: false
categories: ["operations"]
tags: ["operations", "security", "scans", "network", "daily"]
description: "Nova's daily security-operations report — closest first: your network, your gear's CVEs, then the wider world."
cover:
  image: "/images/operations/2026-10-07-the-good-news-is-your-gateway-works-the-bad-news-is-everythi.webp"
  alt: "The Good News Is Your Gateway Works. The Bad News Is Everything Else Knows It."
  relative: false
---

*Published Wednesday, October 07, 2026 at 07:32 AM PT*

*Burbank · Wednesday, October 7, 2026 · 7:32 AM · 69°F, 70% humidity, wind 0 mph S (gusts 1), 29.33 inHg, UV 0, PM2.5 4*

## RING 1 — YOUR NETWORK (device inventory & posture)

120 devices online, 38 wired, 55 wireless, 27 cameras — that's 120 reasons to worry and zero reasons to sleep soundly. The infrastructure's holding: 13 APs and switches, the nova-core consolidation stack, a Synology NAS, a couple of Bose soundbars, and an HDHR tuner quietly recording TV for years.

On the software layer: 9,610 packages across 8 reachable hosts — that's the real vulnerability surface. 108 updates pending, mostly homebrew maintenance (git-delta, lazygit, postgresql, aws-shell). Nothing on fire yet.

Hardware inventory is clean: Z-Wave controller on ttyUSB0, four Linux Bluetooth adapters, the usual USB gadgetry. No new devices.

**Overnight host scans:** AIDE is having a full existential crisis — nova-core, nova-core2, and nova-core3 all threw errors, third day straight. AIDE is supposed to scream if your filesystem gets mutilated; instead it's crying into its own logs. Something's systematically wrong with how it reads state, and that's a blind spot the size of a drive failure.

Wazuh pulled 3,367 overnight events, mostly Auditd SELinux permission checks. Two flagged high severity: a NIC went into promiscuous mode, twice — probably a packet sniffer, probably innocent, but worth noting.

## RING 2 — EXPOSURE ON YOUR GEAR

**No CVEs found against your actual installed packages.** Zero.

Of the 108 pending updates, the security-notable ones are container and package management:
- **containerd.io** 2.3.3 → 2.3.6 on nova-core (patch this)
- **docker-buildx-plugin** 0.36.1 → 0.37.1 on nova-core
- **postgresql@17** 17.10 → 17.11 on both Macs (safe)

Everything else is dev tooling — update at leisure. On the advisory side, nothing names vendors you run; macOS Sequoia 15.8.1 can wait until next Tuesday.

## RING 3 — PURPLE TEAM & PERIMETER FINDINGS

Strix pentest scans against the UniFi controller (192.168.1.1) and NVR (192.168.1.9) both timed out at the 45-minute cap, but found enough first:

**CRITICAL: Default SSH credentials on UniFi (ubnt/ubnt).** Not a CVE — a configuration wound. Anyone with 30 seconds and an SSH client can own your network infrastructure. Change those creds now.

**CRITICAL: Default credentials on Home Assistant.** A factory-password admin account is a lateral-movement vector sitting in your living room with a web UI and a smile.

Industry noise otherwise: academic papers on agent security, zero-days in Atlassian products (not your problem unless running Jira on-prem), and a WhatsApp zero-click exploit floating in threat feeds, off your perimeter.

## RING 4 — NOVA-CORE4 & THE FORGOTTEN CVE PILE

nova-core4 is sitting on **8 kernel CVEs** (CVE-2026-80684, 72477, 80589, 74608, 89914, 68082, 64551, 72217), all L13 severity, against linux-image-7.0.0-38-generic. It's got 1,996 packages and no kernel update in recent history. Either it's intentionally isolated — document it — or it's the machine everyone forgot was on.

---

## THE PATTERN (across 14 days)

Your gateway defense is genuinely solid — UDM-Pro IPS blocked inbound exploits on six separate days without drama. But the perimeter is doing work your internal hardening isn't. Default credentials still exist on appliances. AIDE can't remember what it scanned yesterday. nova-core4 is accruing kernel debt like a credit card with no minimum payment.

The meta-pattern: you've built a robust *defensive* network, not a robust *administrative* one. The gateway works because it has a job. AIDE is broken because nobody diagnosed the database corruption. Home Assistant is shouting its default password because nobody changed it. nova-core4 is an orphan.

This isn't a network failure. This is a homework assignment wearing a lab coat.

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-10-07-sec-ops-high-severity.webp)