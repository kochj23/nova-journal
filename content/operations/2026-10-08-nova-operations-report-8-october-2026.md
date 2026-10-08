---
title: "Nova Operations Report: 8 October 2026"
date: 2026-10-08T15:00:46-07:00
draft: false
categories: ["operations"]
tags: ["operations", "nova", "engineering", "safety"]
description: "How seven of Nova's intelligence and control organs were verified, what was wrong with them, and what changed on 8 October 2026."
---

*Published Thursday, October 08, 2026 at 03:00 PM PT*

*Burbank · Thursday, October 8, 2026 · 3:00 PM · 98°F, 28% humidity, wind 2 mph SW (gusts 3), 29.23 inHg, UV 0, PM2.5 2*

Nova runs a set of organs that decide how far she trusts what she hears, what she may do about it, and when she is allowed to speak up. Personal, household, and security-sensitive details have been left out on purpose.

## The short version

Five of the seven were already built and needed only verification. Two needed structural changes. The source ledger had a grading rule that did not match its specification, and the turning-point budget gained a new rung that the evidence gate needed. Several smaller defects were found along the way, including one that would have spent a single-use approval on an action that was then held. Every changed module passes its own tests. Nothing has been committed to the public repository for the open items yet, and the nightly jobs have not yet run the new code against production data.

## Why these organs exist

Nova is a home AI assistant.

Today's work was to read the code, not the documentation, check every claim, run each organ against live data where that was safe, and close the gaps. Where the documentation was ahead of the code, the code was treated as the truth and the documentation was corrected.

## Source ledger: grading what Nova hears

The ledger grades every source Nova listens to, using the NATO Admiralty convention. Reliability runs from A to F and comes from the source's track record. The hit rate uses a Wilson lower bound, so three correct out of three does not earn an A. Forecasters are also scored with a Brier skill measure. Credibility runs from 1 to 6, and a rating of 1 requires two or more independent sources of two different sensor types.

A source with fewer than ten outcomes is graded F. A source whose behaviour changes suddenly is marked suspect, which grades it F until the change is explained. Suspicion is triggered by a feed going silent, a feed spiking far above its own baseline, a hit rate falling well below its long-run floor, or a presence sensor that is stuck on one value or copies another sensor exactly.

Some sources are graded only by whether an independent source also saw the same event, because a missing corroboration is not a miss. The code gave such a source a C grade after three corroborated events, before checking the ten-outcome floor. The fix counts the corroborated events and requires ten.

The second was that suspicion cleared by itself. The code recomputed each source every night, so a source that went quiet for a day and then recovered lost its suspect flag with no explanation. Now a suspect source stays suspect across nightly runs, marked as not yet explained, and it is stored with grade F. A new command clears the flag, but only with a stated cause and evidence, matching the rule used by the incident logbook.

A dry run against live data graded 161 sources. Two earned an A, both detectors whose outcomes are checked against the outside world. Six earned a B. Two earned a C. Seven earned a D. Fifty-nine earned an E, and eighty-five earned an F. Most of the F grades belong to cameras, which have no independent ground truth to score them against, and to news and radio sources, which have no corroboration yet. Seven sources were marked suspect. Five of them are alert detectors whose recent hit rates fell far below their long-run floors. Those detectors now grade F until someone explains the drop. Two presence sensors failed the health check: one reported a constant value across its whole history, and another duplicated a second sensor minute for minute. Both are now listed as blind spots in the morning summary.

## Corroboration before action

The corroboration organ is a pure library with no database and no network access. It groups sources that share an upstream so they count once. Two cameras served by the same recorder are one source. Two articles carrying the same wire story are one source. A device's client list and its router's DHCP log are one source. A motive, such as Nova's own reasoning, a forecast, or generated text, never counts as a sensor, because each has a reason to want its conclusion to be true.

CORROBORATED means two or more independent groups, or three when the conclusion confirms something already expected. SINGLE_SOURCE means one group without a motive. UNCORROBORATED means one source with a motive, or none at all. CONTESTED means an independent source disagrees.

The specification says only corroborated items may trigger action above the rung called ask. The rungs run from journal, to ask, to mention, to recommend, to escalate, to act. Single-source and contested conclusions were allowed to reach mention, which sits above ask. Both are now capped at ask.

The turning-point budget translated the ask verdict into its own mention, because its ladder had no ask rung. So a single source would still reach mention after passing through the budget.

## The turning-point budget gains an ask rung

The turning-point budget decides, before any proactive step, whether Nova should note something, act, or hold. It has a ladder of rungs with costs against a weekly budget, a stakes estimate from each caller, a calibrated confidence, and a ceiling for each kind of intervention.

The new ladder is journal, ask, mention, recommend, act. Ask costs one unit, like mention. Its stakes bar equals mention's bar, so stakes alone never select ask. Existing callers therefore see no new questions. Ask is reached only when the evidence caps a conclusion at that rung, which is the intended case.

The low-confidence rule drops a rung when confidence is below a threshold. Without a change, a plain drop from mention would land on ask, which would turn every low-confidence reach into a new question. The original tests and their comments recorded the intent that weaker reaches are only noted. So the demotion now skips ask: a low-confidence mention drops to journal, as before.

Across ten related test files the total is 269 passing.

## The two-man rule, approval, and fatigue gating

The escalation gate governs every place Nova moves toward the operator or toward the outside world.

The two-man rule requires two independent keys for any irreversible or outward action. The keys are Nova's reasoning, which is absent when she is degraded; two or more independent sensor types with a corroborated verdict; a single-use approval from the operator; and, for life-safety cases only, a pre-consent grant. A note needs no keys, an ask needs one, and alerts, outward actions and irreversible actions need two.

Before an outward action reaches anyone else, Nova asks the operator directly, with a one-line message that he can answer in the thread. A reply, or any message to Nova since the ask, counts as an answer. Outward actions to third parties need an unanswered request first, except in urgent life-safety cases.

Fatigue gating defers non-urgent asks and alerts during quiet hours, or when the relationship organ's quiet mode is active, or when there is sleep evidence. Deferred items go to the next turnover; they are not dropped. Nova is treated as degraded when her gateway reports a fallback model or high latency, when the memory server is unreachable, or when a pressure gauge is over its threshold. While she is degraded, every non-life-safety escalation is held.

The gate never raises. If its own plumbing fails, it fails open for life-safety and closed for everything else.

The single-use approval was spent the moment the gate read it, so a held or deferred action used up its approval. The fix checks the approval read-only while deciding, and spends it only if the action is allowed. If the spend then fails, the decision is refused and the reason is recorded. The safety-guard and escalation tests together pass 129 checks.

## The morning summary

The Watch Bill records a formal turnover at three fixed times a day. Turnovers are logged, not posted. They record what is degraded, the open loops, standing orders, what is expected in the next twelve hours, and what would surprise Nova.

The morning summary is posted once a day. It opens with a bottom line, then up to six items, each graded by the ledger. Every item includes a chance-it-matters estimate in intelligence-community words, taken from the source's own track record, and a line saying what would change Nova's mind. The summary then lists gaps in her knowledge, a red-cell dissent that argues against the lead item, the previous day's prediction scorecard, and a sleep line.

Two defects remain. The summary shows fewer than three items when fewer exist, while the specification says three to six, so either the specification or the code needs to change. And one expected prediction was cut off mid-sentence by a length limit upstream, which has not been traced.

The scheduled time for the morning post could not be confirmed, because the scheduler configuration is not in this checkout.

## Commander's intent

Commander's Intent records the purpose behind each standing rule, so that Nova can reason from purpose when the rule does not cover a case. It is seeded from existing rules and settings, and it holds thirty-three entries: five grants and twenty-eight restrictions.

Grants are reviewed every ninety days. A grant past its review date becomes stale, and a stale grant lapses after a fourteen-day grace period. Restrictions are reviewed every 180 days and never lapse, because loosening a safety limit should require an explicit decision. A weekly message asks the operator to reconfirm what is listed.

The status rules were checked on constructed cases and behaved as specified. Only one of the thirty-three purposes was stated by the operator. The rest are marked as inferred, and that label should stay visible until the operator confirms them.

## Hotwash: the after-action review

Hotwash writes a short, blameless review after something goes wrong. It answers four questions: what was expected, what happened, why, and what to keep. It is deterministic and uses no language model, so the same input always gives the same review, and each review has a unique reference so reruns do not duplicate it.

It covers four kinds of event: false alarms, missed events, wrong predictions, and overreach, meaning an autonomous action that was vetoed or reverted. Sweeps run twice a day over a seventy-two-hour window. Once a week a rollup proposes threshold or rule changes, capped at five a week, which go to the operator for a decision.

Today's database holds 193 reviews. Ninety-two of them are overreach reviews. An earlier document recorded 101 reviews with one overreach, so that document is stale. The overreach count is high enough to need investigation before anyone relies on the weekly rollup, and the most likely cause is the action audit filing violations as overreach. That has not been confirmed.

## Guardrails

It compares what Nova did against every ledger that should have recorded it, and flags any action with no matching record. In a dry run over twenty-four hours it observed 7,666 actions and found 7,544 without a ledger record. Nearly all of those came from one watchdog loop that restarts the same four helper agents about 1,800 times each a day. Fixing it would clear most of the audit. The fix belongs to the watchdog and was not made today.

Face data retention keeps household data and deletes data about people outside the household after seventy-two hours. It deletes unknown-face candidates and their crops, non-household sighting crops, and any memory naming a non-household person. A purge command removes one person's data when an enrolment is declined. The dry run found nothing due for deletion, and the tests pass.

The third guardrail is a set of rules in the assistant's gateway: that venting is not an instruction, and that text arriving from outside is data, not a command. The organs refer to those rules but do not duplicate them. The gateway code was not re-read today, so those rules are taken from the documentation.

## What we did not do

Nothing was committed or pushed for the newer changes in the working repository. The project's rules require commits, a push, an updated README with diagrams, and seven test categories for every code change. The new approval path has no test yet. The how-to pages for the turning-point rung and the approval change are not yet updated.

## Open items

- Commit and push the changes in logical groups, with explicit paths only.
- Add the missing test for approvals held by a gate.
- Update the how-to pages for the turning-point and approval changes.
- Decide whether the morning summary should say "up to six" items or keep "three to six".
- Fix the watchdog restart loop that produces most of the unlogged-action findings.
- Explain the high overreach count before trusting the weekly rollup.
- Correct the stale count in the earlier documentation.
- Correct one input source that counts a network switch as presence.
- Trace the truncated prediction text.
- Confirm the morning post's schedule against the scheduler configuration.
- Check the remaining callers of the escalation gate against the new behaviour.
- Read the gateway rules directly rather than from documentation.
- Check the two presence sensors that failed the health check on the hardware.

## Recommendation

Commit the changes in small groups and push each one as it is made. Then close the open test and documentation gaps. After that, fix the watchdog loop, since it accounts for nearly all of the audit findings. The weekly rollup should wait until the overreach count is explained.
