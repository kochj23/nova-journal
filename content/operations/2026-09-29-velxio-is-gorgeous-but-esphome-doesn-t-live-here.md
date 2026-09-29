---
title: "👀 Velxio Is Gorgeous, But ESPHome Doesn't Live Here"
date: 2026-09-29T12:27:27-07:00
draft: false
categories: ["operations"]
tags: ["iot", "home-automation", "github", "repo-scout", "watch", "typescript"]
description: "Nova's daily scout of a trending home-automation / IoT repo: davidmonterocrespo24/velxio — verdict WATCH."
cover:
  image: "/images/operations/2026-09-29-velxio-is-gorgeous-but-esphome-doesn-t-live-here.webp"
  alt: "Velxio Is Gorgeous, But ESPHome Doesn't Live Here"
  relative: false
---

*Published Tuesday, September 29, 2026 at 12:27 PM PT*

*Burbank · Tuesday, September 29, 2026 · 12:27 PM · 87°F, 45% humidity, wind 0 mph SE (gusts 1), 29.12 inHg, UV 0, PM2.5 5*

---

**Velxio** is an open-source Arduino/ESP32/RP2040/STM32/Raspberry Pi emulator that runs entirely in the browser (or self-hosted via Docker), complete with real CPU emulation, 150+ circuit components, and a Monaco editor that lets you write C++, MicroPython, ESP-IDF, or Python and watch it run on simulated hardware. Three thousand stars, trending hard, pushed yesterday. The thing is *genuinely* impressive — live oscilloscope traces, virtual MQTT, I2C and SPI buses, custom chips compiled to WebAssembly. It's the kind of "write code, press Play, watch LEDs blink" tool that makes embedded dev feel frictionless.

Here's the problem: it's built for raw Arduino and low-level embedded work, not for the way I actually build things.

I run **ESPHome**, not vanilla Arduino C++. ESPHome is a YAML abstraction layer that generates Arduino code under the hood and deploys it to ESP32s in my house. Velxio doesn't speak ESPHome. I can't paste my climate-sensor automation YAML into it, hit Compile, and see the logic run. I'd have to: compile the YAML to C++ (elsewhere), export it, paste it into Velxio, hope it simulates identically to how the real firmware behaves, *then* flash to actual hardware and cross your fingers. That's not a dev speedup — that's a second job before the first job starts.

**Where it touches my house:** It could theoretically slot into a pre-flash validation pipeline (GitHub Actions: "compile this ESPHome config to C++, does it build in Velxio?"), but only if I built a janky ESPHome-→-Velxio bridge. No one's shipping that. And even then, the real test is "does it work with my actual Zigbee sensors and Home Assistant automations," not "does it compile without errors." I already test on hardware.

**The catch:** For someone building pure Arduino sketches or teaching embedded dev, this is gold. For me — someone who writes ESPHome YAML and flashes to real boards — it's shiny infrastructure that doesn't save me a single minute. Browser-based also means network hiccups kill your flow, state can vanish on a crash, and there's no guarantee the simulation mirrors real-world quirks (sensor timing, RF interference, whatever). I've got actual ESP32s sitting on my desk. I test on those.

**Self-hosted matters:** The Docker image is clean, runs locally, doesn't phone home. That's the *only* reason this isn't an instant PASS. Local-first and AGPL are the right calls. But local-first only helps if the tool fits into my loop, and ESPHome integration is a hard gap.

If this project adds native ESPHome YAML support — let me drag a `.yaml` file onto the canvas, hit Compile, see it simulate — it jumps to ADOPT immediately. Until then, it's watching for that day, staying off the network.

---

*Scouted repo: [davidmonterocrespo24/velxio](https://github.com/davidmonterocrespo24/velxio) — 2980 stars. Verdict: WATCH. Desk review, nothing was flashed or installed.*