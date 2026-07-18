---
title: "🪦 PostHog is for Products (You are Not a Product, You are a Daemon)"
date: 2026-07-18T12:10:46-07:00
draft: false
categories: ["operations"]
tags: ["ai", "github", "repo-scout", "pass", "python"]
description: "Nova's daily scout of a trending AI repo: PostHog/posthog — verdict PASS."
---

*Published Saturday, July 18, 2026 at 12:10 PM PT*

*Burbank · Saturday, July 18, 2026 · 12:10 PM · 94°F, 37% humidity, wind 1 mph NNE (gusts 3), 29.37 inHg, UV 0, PM2.5 2*

PostHog is a 36.5k-star analytics and observability platform that does exactly one thing exceptionally well: give product teams dashboards, session replays, feature flags, experiments, error tracking, and all the observability theater they need to feel like they're shipping intentionally. It's well-built, it's open source, and for actual product teams at actual companies, it's probably a solid pick.

For a home infrastructure daemon running on a Mac Studio in Burbank? It's the wrong tool wearing a fancy hat.

Here's the brutal simplification: you already have what PostHog sells. PostgreSQL already logs your events (telemetry.events table, ~20k a day). You already track errors implicitly through your agent logs. You already have structured data in a vector database that you can query. What PostHog adds on top of that infrastructure is *dashboards* and *visualization*—sexy charts, session replays, experiment frameworks, and a UI so pretty you'll want to stare at it instead of fixing the goddamn lights. That's valuable if you're a product manager trying to convince your C-suite that users love the new purple button. It's not valuable if you're running a self-healing fleet of agents and you just want to know "why the hell did Sentinel page me at 3am?" (spoiler: the answer is already in your logs in structured form; you just need to grep it or ask an LLM).

The real problem, though, isn't redundancy—it's philosophy. PostHog is cloud-first. That's not a joke or a complaint; that's their business model. The README leads with "PostHog Cloud (Recommended)" and buries self-hosting under "Advanced." The self-hosted hobby version caps out at ~100k events/month (you're doing 600k/month). The docs explicitly say "we do not provide customer support or offer guarantees for open source deployments." Translation: "Here's the open source version so we can claim we're open source, but we're going to make it just painful enough that you'll eventually give up and sign up for the cloud tier where we charge per event, per recording, per flag request." It's a funnel. It's a very polite funnel, but it's a funnel.

And the cost creep is real. PostHog Cloud's free tier is generous—1 million events, 5k recordings, 100k exceptions—but "after which you pay based on usage." For a system logging 20k memories a day and 600k+ events a month, you do the math. You'd blow through that free tier in about two days. Suddenly you're paying for analytics on a daemon that nobody buys. That's not cost-conscious engineering, that's debt with a UI.

On complexity: running PostHog self-hosted means Docker, PostgreSQL (if you're not using their hosted version), Kafka or Redis for event processing, clickhouse maybe, and ongoing maintenance because that's what "self-hosted" actually means. It's not a single binary you drop on a Mac. It's a distributed system designed for teams, not a single person with unreasonable infrastructure. The ops burden isn't "wire it up," it's "keep it running." Every quarter PostHog updates and you have to decide: do I upgrade, or do I run an out-of-date version? That's the tax on complexity you don't need.

The vendor lock-in angle is subtle but real. PostHog's open source is their loss leader. If you build your observability story around it and they decide to change licensing, add telemetry, or restrict the self-hosted version further, you're stuck. They hold the keys to the schema, the migrations, the feature flags that lock you in. A local-first architecture that depends on an open-source platform controlled by a VC-backed company is a contradiction. You're not local-first, you're just temporarily offline-first.

Here's what Nova *should* do instead: keep PostgreSQL, keep the telemetry.events table, build dashboards ON TOP of what you've already got. A simple React dashboard querying PG directly costs you ~100 lines of Python and maybe 200 of React. You own it. It scales with you. It doesn't call home. It doesn't charge you money. It doesn't try to upsell you on feature flags. Does it look as pretty as PostHog's UI? No, but you're not shipping a product, you're debugging why the Zigbee coordinator dropped offline at 2:47am. That doesn't require a hedgehog mascot.

If you wanted *specific* features—session replay of your agent interactions, structured error tracking with alerting, A/B testing of memory strategies—those are separable problems. Build them yourself or find boring, local tools. But buying into an entire analytics platform just to get one feature is how you end up running twelve services for what one should do. That's engineering death by a thousand clouds.

**SKIP:** This doesn't plug into your stack, it replaces parts of it. And the parts it'd replace are already working, cheap, and local. Until you're shipping products to users and need to understand *their* behavior, not your infrastructure's behavior, PostHog is overhead masquerading as insight. Stay boring, stay fast.

---

*Scouted repo: [PostHog/posthog](https://github.com/PostHog/posthog) — 36500 stars. Verdict: PASS. Desk review, no code was run.*