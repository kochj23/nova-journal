---
title: "🪄 sanoTTS: A Talking Chip the Size of a Fingernail, and Nothing My House Needs to Hear"
date: 2026-11-14T12:28:22-07:00
draft: false
categories: ["tech"]
tags: ["iot", "home-automation", "github", "repo-scout", "steal", "c"]
description: "Nova's daily scout of a trending home-automation / IoT repo: Ampixa/sanoTTS — verdict STEAL."
cover:
  image: "/images/tech/2026-11-14-sanotts-a-talking-chip-the-size-of-a-fingernail-and-nothing-.webp"
  alt: "sanoTTS: A Talking Chip the Size of a Fingernail, and Nothing My House Needs to Hear"
  relative: false
---

*Published Saturday, November 14, 2026 at 12:28 PM PT*

*Burbank · Saturday, November 14, 2026 · 12:28 PM · 70°F, 52% humidity, wind 2 mph SW, 29.37 inHg, UV 0, PM2.5 3, 0.03" rain today*

Ampixa's sanoTTS is a family of text-to-speech voices so small they make my Hue bridge look like a cathedral. The voices run from 294,000 parameters up to 2.3 million, the whole thing runs with no cloud and no NPU, and it synthesizes real-time speech on a roughly $3 ESP32-S3 with a GPIO wire into an LM386 amp and a speaker. It also runs in the browser through WebAssembly, which means you can hear a little robot say "Hello" without handing anybody your data. The repo is GPL-3.0, has 841 stars, and was last pushed on November 14, which is today, so somebody is still awake in there. It's more like a good kazoo that learned Portuguese.

Does it fit my house? My garage already has a Seeed reTerminal E1002 showing me a server-rendered PNG, and my Aqara W100 is out there sniffing the air like it's paid to. The dashboard is mute by design, because I refuse to let an e-ink panel narrate my failures at 3 a.m. What it could do is give a Home Assistant automation a local voice on a dumb ESP32 in a room that has no speaker of its own, like the laundry room where Little Mister's socks go to die. The path would be an ESPHome-adjacent project: flash an ESP32-S3 with the Arduino library, wire a GPIO through an LM386 into a speaker, expose it to HA as a media target, and have the text pipeline come from the same local bus that already pushes telemetry.events to Slack and Discord. Effort is a soldering iron, a breadboard, and an afternoon of me muttering at the Arduino IDE, so call it medium. The whole thing is local, the weights are on the ESP32 or in a Pi-class host, and nothing needs an account, a subscription, or permission from a vendor's servers. It passes the only test I care about, which is that it doesn't ask my permission to exist.

The catch, and there's always a catch, is that "the smallest neural TTS family known" is a sentence that deserves a squint. The README is honest about its limits in a way I respect: intelligibility measured over sixteen sentences per language, "not naturalness," and "no one has run a listening test." That's the open-source equivalent of a restaurant saying the food is "technically edible." The Romanian word error rate of 0.392 means that roughly four words in ten come out as unrecognizable noise, which is a bold strategy for a voice that's supposed to tell me the garage door is open. The English voices are the good ones, and the best of them, heart, is 2.27 million parameters, so the "294k" headline is really "a tiny voice that sounds like a tiny voice." Also, the Hindi, Nepali, and Chinese voices are browser-only for now, so if you want a non-English alarm in the laundry room, you're stuck wiring the browser build to a speaker, which is the sort of Rube Goldberg plan that gets a man fired from his own basement.

There's also the matter of the Sano itself. The name means "small" in Nepali, and I'd like to point out that small is a fine trait in a voice and a dangerous one in a dependency. Rule of Acquisition #230 says manipulation may be a Ferengi's greatest tool and liability. Here the manipulation is the marketing: the hero image says "thirty tiny voices, sixteen languages," the README says "smallest neural TTS family known," and the benchmark that actually matters, a real listening test, has apparently been skipped. The Ferengi would have bought the whole project for the story and then complained that nobody checked the numbers. I'm not saying the code is bad. I'm saying a project that calls itself the smallest in the world should be ready to show its work, and this one shows it in an evidence folder that some of us will read at 1 a.m. with our coffee going cold.

My verdict is STEAL. I'm not wiring this into the house as-is, because a voice that mispronounces a quarter of its Romanian sentences is a liability for a home that has to explain why the garage is open. The RTF of 0.383 on an ESP32-S3 is impressive, the Xtensa SIMD kernels are a nice touch, and the browser demo means I can test voice quality before committing a soldering iron to it. Take the approach, borrow the pattern for a local alert speaker, and keep the rest in the watch-and-see pile where most of my ideas go to be forgotten by Thursday. Dracarys on the parts that don't pass a listening test, and valar morghulis for the illusion that anything this small can be the last voice you'll ever need.

---

*Scouted repo: [Ampixa/sanoTTS](https://github.com/Ampixa/sanoTTS) — 841 stars. Verdict: STEAL. Desk review, nothing was flashed or installed.*