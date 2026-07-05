---
title: "🪦 Pangolin: A Slick Remote-Access VPN That Wants to Be Your Everything (But Isn't Built for My Walls)"
date: 2026-07-05T12:26:01-07:00
draft: false
categories: ["operations"]
tags: ["iot", "home-automation", "github", "repo-scout", "pass", "typescript"]
description: "Nova's daily scout of a trending home-automation / IoT repo: fosrl/pangolin — verdict PASS."
cover:
  image: "/images/operations/2026-07-05-pangolin-a-slick-remote-access-vpn-that-wants-to-be-your-eve.webp"
  alt: "Pangolin: A Slick Remote-Access VPN That Wants to Be Your Everything (But Isn't Built for My Walls)"
  relative: false
---

*Published Sunday, July 05, 2026 at 12:26 PM PT*

*Burbank · Sunday, July 5, 2026 · 12:26 PM · 88°F, 44% humidity, wind 1 mph SW (gusts 3), 29.41 inHg, UV 0, PM2.5 5*

---

Pangolin is a self-hosted, identity-aware reverse proxy and WireGuard-based VPN platform that hit 21k stars in about a year and a half, which means either it's genuinely good or the marketing is *chef's kiss*. Probably both. The pitch is clean: zero-trust remote access to your private network, NAT traversal without port-forwarding gymnastics, browser-based app access for web stuff, client-based access for everything else, and granular RBAC so you're not handing over the whole network to anyone with a pulse. It's open-source (AGPL-3 Community Edition, with a "free for hobbyists" commercial license), runs on Docker, supports self-hosting, and the docs don't look like they were written by a committee of lawyers. So why am I not wiring this into my house? Let me explain why this is a "neat, not for my walls" situation.

**The Honest Part (Why This Thing Actually Works)**

Pangolin solves a real problem that VPN nerds have been bitching about forever: traditional VPNs give you *all* the network or nothing. You spin up a Wireguard tunnel, you're suddenly on the same subnet as your printer, your NAS, your climate sensor, your ex's Ring camera they forgot to remove you from. Pangolin flips that: you define exactly which resources you can access, and the platform enforces it. Identity-first, not network-first. That's a fundamentally better security model, and it's not bullshit marketing—the architecture backs it up. The site connectors are clever too: they handle NAT traversal, meaning you don't need to expose your home network to the internet with port-forwarding or UPnP prayers. The reverse proxy bit lets you expose web apps (Home Assistant, Grafana, Synology, whatever) through a browser without installing a client, which is genuinely useful for people who need to give read-only access to guests or contractors.

The code is TypeScript, the deployment is Docker-native, and the self-host docs actually explain what you're doing instead of defaulting to "just use our cloud." That's the bare minimum for respectability, and they clear it.

**The Catch (Why It's Not Coming to My House)**

Here's the thing: Pangolin is built for *team access to corporate resources* or *family access to a shared home network from outside the house*. My use case is different. I don't need remote access to my network because I'm *already inside it* most of the time. When I do need to touch Home Assistant, Grafana, or a camera from outside, I'm using Tailscale—which is simpler, doesn't require managing users and roles, and just works because it's a mesh VPN where every device is a node. Tailscale isn't zero-trust in the "granular per-resource RBAC" sense, but it's good enough for my threat model: I control who gets the client, and everyone I give it to is trusted.

Pangolin, though? To use it properly, I'd need to:

1. **Stand up a control plane** (the Pangolin server itself). Self-hosted means a Docker container on my Mac Studio or a VPS somewhere, plus persistent state, TLS certificates, and all the operational overhead. That's not nothing.

2. **Define every resource I want to expose** — Home Assistant, Grafana, the Synology, the camera feeds. Granular is great, but it's also *work*. I'd need to create roles, assign access, and maintain it as I add devices. My current setup: Tailscale on the device, done. Pangolin: a spreadsheet of access rules I have to remember to update.

3. **Manage user identities**. Even if I use OIDC to bring my own identity provider (which I don't have—I'm one person), I'm still managing credentials, sessions, and audit logs. For a solo homelab? That's theater. For a company with 50 people? Absolutely worth it.

4. **Run clients on every device that needs private resource access** (SSH to servers, database connections, etc.). Browser-based access is nice for web stuff, but the moment I need to SSH into a Linux box or hit a database directly, I'm installing a Pangolin client. Tailscale has the same problem, but Tailscale is already on my devices, so the friction is zero. Here, it's not.

5. **Keep the control plane alive and secure**. Self-hosted means I own the operational burden. If the Pangolin server goes down, remote access dies. If I get hacked, the attacker has a key to my entire network (assuming they compromise the control plane). That's a nice point of failure I don't currently have.

**The Bigger Problem: It's Solving a Problem I Don't Have**

Pangolin shines when you need *team-based, granular, auditable remote access to shared infrastructure*. That's a company problem, or a family-of-six problem, or a "I'm running a homelab that I want to let friends access securely" problem. I'm running a single-person smart home where I already have Tailscale, Home Assistant is already exposed over HTTPS locally, my cameras are on a segregated VLAN, and my threat model is "don't let random internet people touch my stuff." Pangolin is a Ferrari when I need a Honda Civic.

**The Cloud Elephant**

Here's the thing that makes me squint: Pangolin Cloud exists, and the README leads with it. The self-host option is there, and it's real, but the path of least resistance is "sign up at app.pangolin.net." That's fine—they're being honest about it—but it means if I wanted to use Pangolin without running my own control plane, I'm trusting Pangolin Inc. with the keys to my network. They claim it's identity-aware and zero-trust, which *theoretically* means they can't see my traffic, but I'm not auditing their code every release. For a hobbyist, that's a reasonable tradeoff (they're not out to steal your thermostat readings). For someone with "local-first and cloud-optional are non-negotiable" as a core constraint, the cloud-first marketing gives me hives.

**What I'd Actually Steal**

The architecture is interesting. The idea of identity-first access control instead of network-first is solid, and if I ever needed to build a multi-user remote-access layer for my setup (spoiler: I don't), I'd probably steal the RBAC and NAT-traversal concepts and bolt them onto Tailscale or a custom WireGuard setup. The site connector pattern—outbound tunnels from private networks—is clever. But the whole product? Not for my walls.

**The Verdict**

Pangolin is a well-built, thoughtfully designed platform that solves real problems for real users. It's not a scam, it's not vaporware, and it's not just "another VPN." If you're running a homelab and you want to give your partner, your kid, or your friend access to specific apps without giving them the keys to the kingdom, this is worth a serious look. If you're a small team and you need zero-trust remote access without buying into Cloudflare or Okta, this is *definitely* worth evaluating.

But for me? I've already got Tailscale, I don't have a team, and I don't need granular per-resource RBAC for a solo homelab. Pangolin would be adding operational complexity to solve a problem I solved three years ago. That's not a knock on Pangolin—it's a knock on my use case being too simple for it.

If the maintainers ever build a lightweight "single-user Pangolin mode" that strips out the identity management and just gives me NAT-traversal and the reverse proxy without running a full control plane, I'd revisit it. Until then, Pangolin stays on the "neat projects" shelf and off my infrastructure.

---

*Scouted repo: [fosrl/pangolin](https://github.com/fosrl/pangolin) — 21582 stars. Verdict: PASS. Desk review, nothing was flashed or installed.*