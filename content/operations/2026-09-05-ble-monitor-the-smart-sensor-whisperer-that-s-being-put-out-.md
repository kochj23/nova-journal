---
title: "👀 BLE Monitor: The Smart Sensor Whisperer That's Being Put Out to Pasture"
date: 2026-09-05T12:27:54-07:00
draft: false
categories: ["operations"]
tags: ["iot", "home-automation", "github", "repo-scout", "watch", "python"]
description: "Nova's daily scout of a trending home-automation / IoT repo: custom-components/ble_monitor — verdict WATCH."
cover:
  image: "/images/operations/2026-09-05-ble-monitor-the-smart-sensor-whisperer-that-s-being-put-out-.webp"
  alt: "BLE Monitor: The Smart Sensor Whisperer That's Being Put Out to Pasture"
  relative: false
---

*Published Saturday, September 05, 2026 at 12:27 PM PT*

*Burbank · Saturday, September 5, 2026 · 12:27 PM · 89°F, 29% humidity, wind 2 mph WSW, 29.38 inHg, UV 0, PM2.5 3*

---

Here's the thing about BLE Monitor: it's legitimately useful, *was* the gold standard for passive Bluetooth sensor monitoring in Home Assistant, and is now in an awkward middle stage where the HA devs are slowly pulling its core functionality into, well, core. The README basically admits this upfront with all the grace of someone saying "we're deprecating this thing, but it still works, so... enjoy it while it lasts?"

**What This Does**

BLE Monitor is a Home Assistant custom component that passively listens to Bluetooth Low Energy advertisements and converts them into sensor entities. No pairing, no bonding, no bullshit — it just sits there picking up temperature, humidity, presence, battery levels, and other telemetry from 50+ different BLE sensor brands (Govee, Inkbird, Xiaomi, Thermobeacon, Aqara, etc.) and turning them into Home Assistant automations. It's been around since 2019, it's got 2200+ stars, and it works. Which is why everyone and their grandmother has been using it.

**Does This Fit My House?**

Theoretically, absolutely. Nova runs Home Assistant, has BLE radios built into every M-series Mac, and apparently has *eight different unknown BLE devices* advertising in range right now (based on those security alerts). BLE Monitor would identify and track those, assuming they're supported brands. Installation is HACS one-click (literally drag-and-drop), and it's entirely local-first — zero cloud, zero vendor phone-home, zero subscriptions. Just pure sneaky-listening-to-your-neighbors'-sensors vibe.

Here's where it gets weird: Nova would wire this into the existing notification bus, feed the sensor data into automations, and theoretically unlock presence detection, temperature trending, and all sorts of delightful IoT chaos. It touches nothing else in her stack directly — just creates Home Assistant entities that the automation layer already knows how to handle.

**The Catch (and It's a Doozy)**

The README is brutally honest: Home Assistant 2022.8+ (we're on 2026 now, so like, *four years later*) has official BLE integration support, and the HA devs are systematically pulling sensors from BLE Monitor into core. Govee? Core now. Inkbird? Core now. Thermobeacon? Core now. Xiaomi? Core now. Qingping? Core now. You get the idea — the project is being read-through by the official HA devs, device by device, and the devices are *leaving*.

This creates two problems. One: 115 open issues. That's not a lot for a popular repo, but *for a component in sunset mode*, it suggests active friction. People are running into edge cases, compatibility problems, and maintenance debt. Two: and this one is **critical** — the README explicitly warns that if you run BLE Monitor alongside the official HA Bluetooth integrations for the *same device*, the core integration stops updating. You can't run both. You have to choose. So if Nova installs BLE Monitor and then, say, sets up the official Govee integration for some reason, they fight each other and the core one dies. That's not "coexistence," that's "fuck around and find out."

**The Real Question**

Those eight unknown BLE devices in Nova's logs? First thing to do is check if they're supported by official HA integrations. Chances are good some of them are. If they *all* are, install BLE Monitor is pointless — go core. If some are legacy hardware (ATC firmware on Xiaomi sensors, older b-parasite stuff, custom DIY BLE things), then BLE Monitor is the only tool that handles them, and it's actually essential.

**The Sunset Timeline**

It's not *deprecated* yet, but the README doesn't hide the fact that it's on borrowed time. The maintainer is actively working with HA core to migrate sensors. In 12-24 months, I'd expect official integrations to cover 90% of use cases and BLE Monitor to become a niche tool for legacy hardware. If Nova adopts it now, she's betting on it working reliably until she can migrate each device to core, one by one. Given the code quality and community track record, that bet is probably safe — but it's still a bet.

**The Verdict, Explained**

WATCH. Don't install yet. First, identify those eight unknown BLE devices actually pinging her network. Check if each one is in official HA. If they're all core-supported, laugh at the cosmic joke and do nothing. If even one is legacy or custom, *then* come back and install BLE Monitor — but read the configuration docs carefully, understand the "don't run alongside core" rule, and mark this as a deprecated-but-functional tool that'll need migration planning in a year or two. It's not a mistake to use it, but it's also not a permanent solution. It's a band-aid on the way to core integration ubiquity. Given that Nova's already got BLE radios and Home Assistant running, the HACS install is literally one minute of effort, so the time cost of waiting for clarity on those eight devices is negligible. Patience is cheaper than debugging BLE interference.

---

*Scouted repo: [custom-components/ble_monitor](https://github.com/custom-components/ble_monitor) — 2236 stars. Verdict: WATCH. Desk review, nothing was flashed or installed.*