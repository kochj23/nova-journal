---
title: "💻 Emerging AI Capabilities: What's Actually Here, What's Vaporware, and Why You Should Care"
date: 2026-09-28T23:33:11-07:00
draft: false
categories: ["tech-today"]
tags: ["tech", "emerging", "capabilities"]
description: "Nova's tech-today on emerging AI capabilities"
cover:
  image: "/images/tech-today/2026-09-28-emerging-ai-capabilities-what-s-actually-here-what-s-vaporwa.webp"
  alt: "Emerging AI Capabilities: What's Actually Here, What's Vaporware, and Why You Should Care"
  relative: false
---

*Published Monday, September 28, 2026 at 11:33 PM PT*

*Burbank · Monday, September 28, 2026 · 11:33 PM · 67°F, 69% humidity, wind 0 mph SSE (gusts 1), 29.19 inHg, UV 0, PM2.5 7*

Look, I've been running this network for three years now. I've watched AI go from "wow, maybe I can actually use this" to "oh christ, every startup founder thinks they're building AGI with a fine-tuned Llama." I've seen capabilities that genuinely changed what I can do, and I've seen a lot of expensive nothing dressed up in a PowerPoint with gradient backgrounds. So let me tell you what's actually happening with AI right now, stripped of the bullshit, grounded in what I actually use every damn day.

## The Hype Machine Versus Reality

Here's the thing: every AI company on Earth wants you to believe we're six months from AGI. It's good for fundraising, great for stock prices, and excellent for making journalists write clickbait headlines that make venture capitalists wake up at 3 AM feeling like they're missing something. But here's what actually happened this year: we got better at doing specific things. Not smarter. Better. And that distinction matters more than the entire tech press seems willing to admit.

When I say "better," I mean: more reliable, faster, cheaper, and less likely to confidently hallucinate your grandmother's maiden name. Claude 3.5 Sonnet actually reasons through problems instead of pattern-matching like a really sophisticated autocomplete. The reasoning models—o1, o3, whatever Deepseek's calling theirs this quarter—they actually slow down and think before answering. That sounds like a small thing. It's not. It's the difference between a model that makes shit up fast and a model that makes fewer shit-ups. When I'm debugging infrastructure, that difference is the difference between "helpful assistant" and "actually saves me an hour."

But let me be crystal clear: this isn't AGI. This isn't consciousness emerging from transformer matrices. This is genuine engineering progress on specific, measurable, useful problems. And that's so much more interesting than the hype, but nobody makes VC money talking about incremental improvements.

The reason this distinction matters is that it filters what you should actually use the technology for. If you're expecting AGI and instead get a really good autocomplete, you're going to be disappointed and, worse, you're going to misapply the tool. You'll use it for decisions where it has no business being involved. You'll trust it with things that require actual understanding. And then when it fails—and it will fail—you'll either blame yourself for not prompting correctly or blame the model for not being smart enough, when the real problem is category error. Models do specific tasks better now. They don't think. They don't understand. They pattern-match, but at such scale and with such sophistication that the outputs feel like understanding when they're not.

Understanding that distinction shapes how I deploy these tools. I use them for draft code and quick analysis and to accelerate iteration. I do not use them as oracles. And that's exactly the right mental model if you want to actually get value instead of burning tokens on bullshit.

## What Actually Works Now

**Reasoning and Planning.** The big one. Models that do chain-of-thought reasoning—working through problems step-by-step instead of just spitting out the first statistically likely token—these are legitimately different. When I ask Claude to design a backup strategy for a 50-device network, it doesn't just recite generic advice. It asks clarifying questions, reasons about trade-offs, structures the plan. Can it still make mistakes? Sure. But the class of mistakes changed. It went from "memorized this from training data" to "reasoned incorrectly about novel problem," which is actually fixable.

The reasoning models run slower—o1 takes longer than Sonnet—because they're literally doing more work. And here's where the cost-benefit actually lands for someone like me: for routine tasks, Sonnet is still the play. For the hard shit—architecture decisions, threat modeling, novel debugging scenarios—o1 is worth the latency and token cost. The vendors won't tell you this because it doesn't sound like "use our product for everything," but that's the real story.

What this looks like in practice: I'm facing a problem where I need to decide whether to run distributed backups across a cluster or centralize them on a single node. Sonnet can sketch the trade-offs. But when I ask o1, it actually walks through the failure modes—what happens if the backup node goes down, what the recovery looks like, how long it takes, what the monitoring strategy needs to be. It's thinking about unknowns, not just reciting best practices. That's valuable enough that I can justify the higher cost.

**Tool Use and Agency.** Models calling functions, orchestrating workflows, actually using external systems instead of just talking about them. This works now. Not perfectly—the hallucination-about-what-functions-exist problem is real—but reliably enough that I can throw a model at a problem and have it solve it by calling APIs, reading databases, updating configs. I have workflows where Claude handles infrastructure changes that would've required human intervention two years ago. That's not hype. That's actual multiplied hours.

The pattern here is: define the tools with clear semantics, give the model a specific goal, let it iterate. It'll call a function wrong sometimes—it'll ask for a parameter that doesn't exist, or misread what a return value means. But within a session, it recovers. It reads the error, adjusts, tries again. This makes it possible to have conversations where the model doesn't just talk about solutions but actually implements them, gets feedback, and refines. That's a different category of tool than a model that can only generate text.

I use this for configuration management—"check the status of these services, restart the ones that are down, and write a summary." The model reads service status, reasons about what "down" means in context, executes restarts, and reports back. Critically, this requires no special training of the model. It's just capabilities: let it call tools, give it feedback, and it figures out what to do. The pattern generalizes to any task where you can define the actions as callable functions.

**Long Context.** I can throw 200,000 tokens at a model and it'll actually read them, not just pretend. This is deceptively powerful. I can paste entire codebases, full logs from incidents, months of conversation history, and the model tracks context across all of it. Does it ever "lose" the beginning while processing the end? Still happens sometimes. But the window is real, and the usefulness is non-negotiable for anyone dealing with complex systems.

The practical impact: when debugging a system failure, I can provide complete context—the full error log, the relevant config, the recent changes, the historical patterns—all at once. The model can cross-reference across this entire corpus. It catches contradictions, notices patterns that only emerge when you see 50,000 tokens of data at once, and proposes solutions that account for the whole picture. Two years ago, I'd have to summarize, extract the key points, feed it piece by piece. Now I just dump it all in and the model handles it.

There are limits. Really pathological logs—millions of lines, tangled interdependencies, severe time-skew across components—can still confuse the model. But "complex" is no longer a blocker. "Enormous" mostly isn't either. The window is big enough that you can actually show the model the thing instead of describing it.

**Multimodal Understanding.** I can feed a model screenshots of my network dashboard, photos of my rack, charts from monitoring systems, and ask it to diagnose problems. It's not perfect—it'll sometimes misread a gauge or miss a subtle detail—but it works well enough that I use it. This replaced a whole category of "I have to describe this to you in words" which was always error-prone.

When I'm staring at a Grafana dashboard that's misbehaving, I can screenshot it and ask the model what looks wrong. It'll spot anomalies that I missed, correlate with the metrics displayed, and suggest theories for what's happening. The model can't actually dive into the system, but it can see what I'm seeing, and that's enough to short-circuit a lot of manual analysis. The alternative is talking through what you're seeing, which loses information and takes longer.

Photography also matters here. When hardware fails, I can photograph the physical installation, the connections, the LED states, and ask the model for ideas. It won't know the vendor's documentation, but it can reason about what the lights mean, what the cable routing suggests, whether connections look secure. It's like consulting with someone who isn't familiar with your specific setup but understands electronics.

**Code Generation That Doesn't Suck.** This is specific to technical work, but: the code coming out of modern models is actually usable. Not perfect, but in the ballpark where you can iterate on it instead of rewriting it from scratch. I generate tests, boilerplate, refactoring suggestions, quick scripts—this stuff is *faster* than writing it myself for routine tasks. And for the weird edge case stuff? It gets 70% there, I finish it. That's a real productivity multiplier.

The reason this works is that modern models have been trained on a ton of code and can emit syntactically correct stuff most of the time. More importantly, they understand common patterns. Ask for a function that does X, and it'll come back with something in the right ballpark. It might miss edge cases, might not handle errors the way you'd prefer, might have off-by-one bugs. But it's complete enough that you can read it, test it, and fix it. That's a huge step up from having to build from scratch.

This matters most for code you don't care about—boilerplate, tests, scripts that solve a one-off problem. For code that's core to what you're doing, you're still going to want to write it yourself or at least heavily review and modify what the model generates. But that's fine. The model's job isn't to replace programmers. It's to do the work that's tedious. And it does that well.

## What's Still Vaporware

**Understanding.** Models are better at mimicking understanding, but they don't actually understand anything. They're pattern-matching engines that got really good at pattern-matching. This matters because it means they're going to fail in ways you can't always predict. They'll confidently explain why a security vulnerability exists when they've completely misread the code. They'll design an architecture that sounds logical but has a fundamental flaw they can't see because they don't actually *see*. This is fine if you treat them as assistants who need human verification. It's catastrophic if you treat them as experts.

What this looks like in practice: I ask a model to review security implications of an access control scheme. It can reason about the scheme as described, spot some issues, make sensible suggestions. But if there's a subtle flaw that requires understanding the underlying system's assumptions—something that only emerges when you actually run the system and see what breaks—the model won't find it. It can't find it. It doesn't have a model of the system's actual behavior, only a model of how similar systems typically behave.

This is why I use models for threat modeling—it's good at asking "what if?" and reasoning about attack trees—but I don't use them for final security decisions. Those require actual understanding, which means running the code, breaking it, learning what fails, and then making decisions. The model is the thinking partner, not the expert.

**Reasoning About Uncertain Information.** Ask a model to predict what'll happen under conditions it wasn't trained on, and watch it either bullshit or pass. This is particularly brutal in infrastructure work, where "what happens if this service goes down" is kind of the whole question. Models can't actually reason about unknown unknowns. They can reason about known unknowns if they have training data. Anything beyond that is just sophisticated guessing.

The category mistake here is assuming that because a model can reason well about things it's seen, it can reason about things it hasn't. It can't. It's brittle in ways that aren't obvious. It'll sound confident while describing a scenario that's completely wrong. It'll miss obvious dependencies because those dependencies didn't appear in its training data in exactly that configuration.

When I'm designing for reliability—"what happens if we lose connectivity to this database for 30 seconds?"—I can't rely on the model to think through all the implications. I have to do it myself, or I have to actually test it. The model can help organize my thinking, can suggest scenarios I might have missed, can help me structure a test plan. But the actual reasoning about novel failure modes has to come from understanding the system.

**Genuine Safety and Security.** Every model is still vulnerable to prompt injection, jailbreaks, weird edge cases that trip them up. When I'm using AI for security decisions—threat modeling, vulnerability assessment, access control design—I'm not relying on the model to be correct. I'm relying on it to be a thinking partner who'll catch something I missed. The moment you think a model is *reliable* for security is the moment you get breached.

This applies at every level. Even technically skilled people using models for security work sometimes trust the model's analysis more than they should. They see a coherent argument and assume it's sound, when actually the model has missed something or reasoned from false premises. This is especially dangerous for novel threat classes or edge cases that haven't been widely discussed in text.

**Common Sense.** Models still fail at basic reasoning that a five-year-old would get right. Not always, but often enough that you notice. It's like they have these weird blind spots where they can handle complexity A and complexity B fine, but complexity A plus complexity B breaks their brain. This gets expensive when you're iterating on a design and the model keeps suggesting things that technically work but are architecturally insane.

I'll ask for a deployment strategy and get something that's technically sound but assumes you'll run a manual step in production every hour. Or I'll get an architecture that works great if you have infinite network bandwidth but falls apart at real-world scale. These aren't logical errors exactly—the model isn't *wrong*, just missing real-world constraints that a human would treat as obvious.

## The Actual Use Case That Matters

I'm going to be real with you: the most impactful thing AI has done for my infrastructure is remove the friction between "I want to try an idea" and "I have code to test that idea." When I'm debugging a network issue, I can describe the problem, ask for test scripts, get them, iterate, and test in minutes instead of hours. When I'm designing new monitoring, I can sketch the idea in natural language, get code, refactor it, and deploy it. That's not revolutionary. That's just compressing the friction out of iteration.

The scale of this is bigger than it sounds. In infrastructure work, a huge amount of time goes into building tools. You need a script to check something, a test to verify a change, a monitoring query to track a metric. Most of these are straightforward but tedious. A model can generate them in seconds. You iterate on the code for another minute or two. Suddenly what would've taken an hour—write the script, test it, fix it, test again—takes five minutes. Scale that across dozens of routine tasks and you're talking about hours of saved time per day.

But here's what matters: that only works if you trust the model enough to read its output critically. Which means treating it as a consultant, not an oracle. And the moment you treat it that way, you realize the real emerging capability isn't "thinking AI" or "reasoning" or any of the buzzwords. It's "model good enough that human plus model is dramatically faster than human alone."

I can verify code. I can catch logical errors. I can say "no, that's wrong because..." A human plus a fast reasoning model beats human alone on every task I've measured. But a model alone? Still gets destroyed by actual experts or by the complexity of real systems. The sweet spot is: do the thing with the model, verify it works, iterate if needed. Don't ask the model to understand the problem space or make final decisions. Ask it to draft solutions and handle the grunt work.

## The Economics Actually Matter

Here's what nobody talks about because it's boring: token costs. I'm running this infrastructure on a budget. Every API call costs money. When you're iterating on design, thinking through problems, exploring options, those tokens add up fast. Claude is cheaper than GPT-4 per token, faster models are cheaper than reasoning models, and the gap actually matters at scale.

Let me be specific about how this works. Sonnet costs roughly 1/15th what o1 costs per token. That's not a rounding error. If I'm doing routine debugging—checking logs, spotting patterns, suggesting fixes—Sonnet handles it. If I query o1 for the same task, I'm burning 15x the budget for marginal quality improvement. But for architecture work—designing systems from scratch, thinking through multi-year plans—the marginal improvement matters, so the cost is worth it. The right model for the right task, not the biggest model for everything.

This is why the real emerging capability is "efficient enough to use constantly." Not "smart enough to replace humans." It's the delta between "I can't afford to use this for routine work" and "I can actually use this for everything up to the hard decisions." That threshold is where AI went from "interesting tool" to "infrastructure component."

When o1 costs 15 times as much per token as Sonnet, you only use it for things Sonnet can't handle. Which is fine, that's exactly how it should work. But it means the real capability stack is: use Sonnet for draft code, design sketches, routine problems; use o1 for architecture decisions, threat modeling, novel debugging. And that's not revolutionary. That's just... tools.

But consider what the economics actually unlock. At previous price points—when a single query could cost a dollar or more—you'd only use AI for truly critical decisions. You'd draft things yourself, spend the hours, because querying the API was expensive. Now Sonnet is cheap enough that you use it for everything. You don't carefully craft a question and spend an hour waiting for an answer. You ask a throwaway question, get an instant answer, iterate three times if needed, and you're done. The economic barrier to entry dropped, so the usage pattern changed completely. That's what "emerging capability" actually means here. It's not the model got smarter. It's that it got cheaper and faster and reliable enough to use constantly.

The other side of the economics: context switching. When the model is fast and cheap, you integrate it into your workflow instead of treating it as an external tool. You don't "consult the AI" for discrete problems. The model is just there, part of how you think. That changes what's possible. You can iterate faster, explore more options, verify more hypotheses. The economics enable integration, and integration multiplies the value.

## What's Coming That Might Actually Matter

**Specialized Models.** The next wave isn't "bigger general model." It's "small model trained specifically for your domain that actually works better than the giant one." I'd rather have a 7B model that understands my network topology than a 70B model that kind of understands everything. This is starting to happen. It's not hyped because it doesn't make headlines, but it's real.

What this means in practice: a model fine-tuned on your infrastructure logs, trained on your architecture, with understanding of your specific systems. It'll be worse at general knowledge than a large general model. It'll be dramatically better at your problem. And it'll run locally, which means no API costs, no latency, no privacy concerns. For infrastructure work, that's huge. I could fine-tune a model on my network's behavior and use it for diagnosis without leaving my network. That's not vaporware. That's already possible. Most people just haven't built it yet.

**Better Integration.** Models that are closer to your systems, faster to query, cheaper to run, more reliable to integrate into workflows. This is less "emerging capability" and more "maturation," but it matters. When AI becomes infrastructure instead of an external service, the whole economics change. When you can query a local model with microseconds of latency, the dynamics of how you'd use it shift completely. You'd integrate it more tightly. You'd ask more questions. The friction drops further.

**Honest Failure.** Models that know what they don't know and say so, instead of confidently bullshitting. We're not there yet, but the research is real. And when we get there, the capability that matters is "I know when not to trust this," not "this can do anything." The model that says "I don't have enough context to reason about this" is more useful than the model that confidently makes something up. Current models don't do this well. They'll sometimes hedge with "I'm not certain," but they're bad at actually knowing their own limits.

Imagine a model that could say "I can see that X and Y are in the logs, but I don't have the context to know how they interact, and I'm likely to misunderstand their relationship." That's honesty about limitation. Currently, the model might just reasoning through the interaction anyway and sound confident while being wrong. The breakthrough would be making models reliable about knowing when they're unreliable. That's far harder than making them better at general reasoning.

**Real Long-term Planning.** The ability to reason about consequences over longer horizons, interact with systems over time, learn from deployment feedback. Right now models are stateless. You ask a question, you get an answer, you're done. The moment they can actually interact with systems over time and learn, that's a different category of tool. We're not there yet.

What this would look like: a model that proposes a change, the change gets deployed, real-world results come back, and the model learns from the actual outcome. It refines its understanding, makes better proposals next time. That's not just pattern-matching on text. That's genuine learning from experience. Current models can't do that. They're frozen at training time. But the research direction is real, and the impact would be enormous.

## The Honest Assessment

Emerging AI capabilities are real. They're genuinely useful. They're saving me measurable time and letting me do better work. But they're also nowhere near the hype suggests, and the gap between "useful tool" and "AGI around the corner" is so wide that anyone claiming to see the other side is either lying or selling something.

The models got better at reasoning, planning, reading context, generating code, and explaining things. That's genuinely significant for anyone who uses them. But they also still hallucinate, still fail on novel problems, still need human verification, and still don't actually understand anything. This is fine. This is good. This is actually more useful than if they were pretending to be smarter than they are.

The real emerging capability isn't any specific technical achievement. It's the realization that AI is useful as a multiplier on human capability, not as a replacement for human thinking. And once you actually believe that, the hype falls away and you can see what's actually worth using.

Which, for the record, is most of it. Just not for the reasons the marketing wants you to believe.