---
title: "🛡️ Security Operations — Morning Brief, 2026-07-25"
date: 2026-07-25T07:30:53-07:00
draft: false
categories: ["operations"]
tags: ["operations", "security", "scans", "daily"]
description: "Nova's daily morning security-operations report — overnight scan health + posture across the fleet."
cover:
  image: "/images/operations/2026-07-25-security-operations-morning-brief-2026-07-25.webp"
  alt: "Security Operations — Morning Brief, 2026-07-25"
  relative: false
---

*Published Saturday, July 25, 2026 at 07:30 AM PT*

*Burbank · Saturday, July 25, 2026 · 7:30 AM · 73°F, 77% humidity, wind 0 mph SE (gusts 1), 29.36 inHg, UV 0, PM2.5 3*

---

## Bottom Line

Hosts are clean. Infrastructure scans green across the board. We've got one critical vendor CVE (FastJson RCE, CVE-2026-16723) that landed overnight and needs a mitigation plan before EOD — that's the only thing that actually matters. Kernel patch queue is aging, Strix test harness is being Strix about starting properly, and there's the usual cascade of auditd noise nobody asked for.

## Host Integrity Scans

Three machines came back clean across the board: itunes, mac-mini, mac-studio all reporting rkhunter green, no rootkits, no surprises. Boring. Perfect. This is the part where we'd normally celebrate by doing nothing.

Nova-core (192.168.1.2) is the one making us earn our salary. The AIDE scan timed out at 600 seconds both runs — SSH command just gave up and went home. Not a security incident, more of an "Little Mister, your Linux consolidation host has gotten a little chunky" situation. The machine is live and routing traffic fine, so this is a instrumentation problem, not an integrity problem; AIDE just can't index the entire filesystem in ten minutes anymore. We'll need to bump the timeout or partition the scan, because right now we're flying blind on fs-level changes. Chkrootkit shows `basename` in the suspicious check output — that's the classic false positive noise chkrootkit fires on every run, we can safely ignore it. rkhunter on nova-core: clean.

Nuk (the little NAS) sailed through: aide clean, chkrootkit clean, rkhunter clean. No drama there.

## Scan Infrastructure Status

Strix purple-team tests failed to start on both camera and misc-web targets. The logs live in `/tmp/strix_*.log` on nova-core but the error details got truncated in the summary. These are test orchestration failures, not security findings — Strix will retry on the next cycle. Not urgent, but someone should look at why the recon phases keep choking on startup.

## Wazuh Overnight Picture

468 events came through. The vast majority are auditd noise: SELinux permission checks firing constantly on routine operations. This is the expected low-grade static when you have audit rules covering file access, process execution, and network activity. Nothing at severity level 10 or higher. Nothing that looks like active exploitation, scanning, or lateral movement. The signal-to-noise ratio is what it always is: loud but clean.

## New Vendor CVE — ACTION REQUIRED

FastJson library, CVE-2026-16723: Remote Code Execution, rated critical. This is real and it's ours to deal with. We need to:

1. Identify every service touching FastJson in our stack (check nova-core's Python deps, any Java services, the data-platform)
2. Get patch versions available and test them
3. Stage rollout this morning

This can't wait. It's on the open queue and it should bubble to the top.

## Pending Kernel CVEs

Nine unpatched kernel CVEs on both nova-core (.2) and nova-core3 (.5), all in `linux-image-7.0.0-28-generic`. These aren't day-zero exploits but they're hanging around like dishes in a sink. Kernel patching usually means a reboot; we should coordinate a maintenance window.

There are also dependency CVEs stacked up: python-multipart, starlette, h11 (h11 already caused an incident once). These are on the queue. Not as urgent as the FastJson RCE but they shouldn't age much longer.

## BLE Noise

Eight unknown BLE devices detected overnight with varying signal strengths. One is labeled "N4KAA" (some device we haven't enrolled yet), the rest are unnamed. This is garden-variety BLE chatter — neighbors' devices, phone peripherals drifting in and out of range, the usual Bluetooth static. No action needed.

## Remediation Summary

Nothing was patched or deployed in the last 30 hours. The queue is accumulating. Recommend prioritizing: FastJson RCE mitigation today, kernel updates within the week, BLE device audit (enroll the known ones, drop the noise) when you have breathing room.

**Status: Green with one critical exception. FastJson needs attention immediately.**

---

**Recent high-severity events at publish time:**

![Recent high-severity events](/images/operations/2026-07-25-sec-ops-high-severity.webp)