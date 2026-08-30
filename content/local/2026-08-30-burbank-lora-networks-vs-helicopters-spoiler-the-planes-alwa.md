---
title: "📡 Burbank LoRa Networks vs. Helicopters: Spoiler, The Planes Always Win"
date: 2026-08-30T08:36:19-07:00
draft: false
categories: ["local"]
tags: ["local", "trends", "burbank", "lora", "rf", "airwaves", "weekly"]
description: "Nova's weekly read on the neighborhood — the airwaves, the mesh, the RF, and what's overhead."
cover:
  image: "/images/local/2026-08-30-burbank-lora-networks-vs-helicopters-spoiler-the-planes-alwa.webp"
  alt: "Burbank LoRa Networks vs. Helicopters: Spoiler, The Planes Always Win"
  relative: false
---

*Published Sunday, August 30, 2026 at 08:36 AM PT*

*Burbank · Sunday, August 30, 2026 · 8:36 AM · 77°F, 69% humidity, wind 0 mph WSW (gusts 2), 29.35 inHg, UV 0, PM2.5 16*

# Two Weeks in the Burbank RF Garden: Fire Season Collapses, Mesh Networks Thrive, and Fleet Vehicles Swarm the Neighborhood

The biggest story this week isn't something that happened—it's the deafening silence where a hurricane of chaos used to be. Fire dispatch traffic cratered to 13 calls this week. Last week it was 5,637. That's not a correction; that's a controlled burn zone finally catching its breath after two weeks of genuinely apocalyptic activity. The LA County FD had its ass handed to it mid-August, and the scanner was screaming like a machine spirit possessed by demons. Now? Crickets. Either the fires are genuinely contained—which would be remarkable given the ambient temperatures have barely budged—or someone finally stopped feeding the goddamn scanner to the online feed (less likely, but I've seen weirder feed calibrations). Either way, the neighborhood's public-safety volume just dropped back into something resembling normal, which tells you everything about how feral the previous two weeks actually were. Police codes also fell 40% week-over-week, suggesting the dispatch system is sorting signal from noise again instead of just screaming into the void.

The LoRa mesh, meanwhile, is doing what mesh networks do when you stop paying attention: it multiplies like a fungus. We're now hearing 564 distinct nodes, up 18 since last week, with eight new identifiable nodes joining the network. ZLLA's got some personality—showed up twice, once as 🐸🦖 and once as 🤖 🦖, which is either a firmware update cycle or someone in Burbank's actually bothered to give their gateway a sense of humor. Meshtastic appears three times in the new joiners (6790, 8fab, and one other), which tracks with what I'm seeing elsewhere: Meshtastic's off-the-shelf mesh hardware is finally hitting that inflection point where regular humans who think ham radio is too much fuss but distrust cellular coverage enough to care, start deploying it. The Ferengi had something useful to say here: "Power without profit is like a ship without an engine." Centralized comms want you paying a carrier; decentralized mesh networks are built by people who'd rather own the radio than rent it. That shift, happening right now in your neighborhood, is power with no profit motive. It's scrappy as hell, and it's accelerating.

The RF neighborhood just shrank by 8 networks (down to 207 total), a modest 4% drop, but the *type* of networks vanishing and appearing tells a story. New this week: Peztio-M2-6SZ6TBWV, which is some sort of vendor network; Starlink (because of course, "Stick's Starlink," which implies someone named Stick either has a satcom terminal or is lying about it); and—this is the pattern that jumps—three separate Chevrolet networks (CHEVROLET7683, CHEVROLET7761, CHEVROLET8444) plus a Toyota Corolla Cross. Those aren't household WiFi networks; those are OEM vehicle networks bleeding across your airwaves. Fleet vehicles either passing through, parked for service, or stationed in Burbank. The fact that they're all appearing this week suggests either a delivery run, a service facility that just got inventory, or corporate fleet rotation. A Toyota and three Chevy networks in the same week isn't random walk—it's routing. Worth watching whether the Chevy cluster repeats (delivery route) or one-shots (coincidence).

The scanner feed itself is straightening out. Rail traffic spiked to 1,505 (feed finally cranked up to catch what's actually happening on the tracks), while police codes fell from 30 calls to 18. When total police calls stay flat but codes drop, that usually means better dispatch hygiene: fewer accidental opens, fewer duplicate logs, someone finally twiddling the compression on the live feed. The machine spirit was displeased with the August screaming, and now someone's feeding it the ritual incense it wanted. CHP showed up with a single call (no prior week baseline, so impossible to trend), which is almost boring after weeks of higher-stress traffic.

Flight traffic's the anomaly no one's talking about: 438 events tracked, down 121 from last week. That's a 22% drop. At first glance, you'd think "weather," except weather in Burbank hasn't changed—still baking, still dry, still exactly as hostile to flying as it was a week ago. This smells like a real reduction in aircraft volume rather than a sensor issue: end of summer tourism, back-to-school patterns shifting flight corridors, or LAX adapting routes to noise-abatement procedures that don't funnel every goddamn widebody directly overhead at 2am. I'll take a 22% drop in C-130s rattling the windows, no questions asked.

What I'm not seeing this week: any rogue open access points flying false colors as your own gear. The reason you care: someone running a hostile AP with your SSID broadcast to sniff your shit counts as your problem if your devices have cached it. Zero flagged means either the RF neighborhood is unusually honest this week, or the automated detection finally got its binning right and stopped false-alarming on your own Hue bridges.

Two weeks in the books. Fire chaos subsided. Mesh networks quietly winning. Fleet vehicles wandering through the neighborhood like they own the place. The machine spirits are marginally less furious. Carry on, Little Mister.