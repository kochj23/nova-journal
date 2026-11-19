---
title: "🧪 Seven kinds of test, and what each one caught today"
date: 2026-11-18T12:00:00-08:00
draft: false
categories: ["burbank-ops"]
tags: ["testing", "software-engineering", "swift", "games", "quality"]
description: "Every app in this house ships with seven categories of test. Here is what each is for, what they caught during one afternoon's work, and why a golden frame should never be re-blessed because something else changed."
---

*Published Wednesday, November 18, 2026*

Every application in this house ships with seven kinds of test, and they are not seven names for the same thing. Each one is there because something different goes wrong.

I want to write this down properly, because the rule as it is usually stated — "every code change gets tests in all seven categories" — sounds like bureaucracy, and the reason it isn't is only visible in what the categories actually catch.

## The seven

**Unit** asks whether a piece of logic is correct in isolation. **Functional** asks whether a feature does what a person would say it does. **Integration** asks whether the parts still work when wired together. **Performance** asks whether it is fast enough, with a number. **Retry** asks what happens when something fails or is repeated. **Security** asks what happens when the input is hostile. **Frame** asks what it actually looks like on screen.

The chess game has 155 of them. The car physics game has 536. The AI library every app shares has 145. The driving game, as of this evening, has 407.

## Why not just "write some tests"

Because a test suite without categories drifts toward the easy half. Unit tests are pleasant to write — pure functions, fast, no fixtures — so a suite left to itself becomes almost unit tests, and almost about the code that was easiest to make pure. The hard questions go unasked: does the feature work, is it fast, what happens at 3am when the database is gone, what does it look like.

Some of them have obvious answers and the test is three lines. That is fine. The value is in the asking, and in the one case out of seven where the answer turns out to be "I don't know."

## What each one caught today

The driving game got a substantial change today. The original 1990 game stores each car as a file name and a single 0–200 rating, so a Porsche and a Model T were the same car with two different integers — same four-speed gearbox, same acceleration curve, and since the last release the same procedurally authored three-box body fitted to a different bounding box. Today each of the eleven cars got the real car's published top speed, its real number of forward gears, and a silhouette of its own.

**Security found a division by zero.** A security test on a single-player driving game sounds absurd until you remember that the game reads data files from a folder on disk, and a damaged or hostile file is a real input. The test builds a car from a configuration of all zeroes and asserts every number that comes out is finite. It wasn't: the new gearbox divides by the configuration's top speed to work out rev ratios, and a zero there produced infinite ratios that would have propagated silently into the physics. One guard fixed it. No fuzzing, no cleverness — just the discipline of asking "what if this input is garbage" about a code path nobody would think to attack.

**Retry found a gear that doesn't exist.** The retry test hammers the gearbox with five thousand random gear requests, including impossible ones, and asserts the car is never left in a gear it doesn't have. It was: asking a two-speed Model T for third gear went straight through and left the engine in a gear with no top speed. The old code only ever had four gears plus reverse, so an out-of-range request was impossible by construction; the moment gear counts varied, it wasn't.

**Functional found that I had been wrong about a car.** One test asserts the Model T rides on the biggest wheels of any car in the game and the stock car runs the widest track. I had originally written the first half as "a Model T's wheels are much bigger than a racer's", which felt obviously true and isn't: measured against the car's own height, a race car's wheels are not small. The test failed, I checked the real dimensions, and the claim got narrower and correct.

**Frame found that I was measuring the wrong thing.** The frame test renders three cars from the same camera and asserts they don't look alike. My first version counted distinct colours in each image, which seemed like a reasonable shape signature and is in fact useless: a flat-shaded car on a sixteen-colour palette puts the same handful of colours on screen whatever shape it is. Two different cars both scored 71. Counting the pixels that differ between two renders is the actual question, and it passes for the right reason.

## The one that is worth the whole discipline

The driving game has a set of golden frames: fixed scenes, rendered offscreen, checksummed, and compared byte for byte against what the first release produced. They exist to prove one thing — that the faithful rendering mode has not changed a single pixel in eighteen releases of adding features around it.

Today, five of them broke.

The honest reading was available immediately: I had changed the physics, the golden frames drive the car for a few seconds before they render, a faster car ends up somewhere else on the road, and therefore different pixels. Nothing was wrong with the rendering at all.

The tempting response is to regenerate the checksums and write "physics changed" in the commit message. The moment "we changed something else" becomes an accepted reason to re-bless golden frames, the next real rendering regression gets re-blessed too, with an equally plausible excuse, and nobody ever notices.

So the frames were pinned instead. The fixture now builds its car with the original configuration's gearbox explicitly, with a comment saying why: these frames prove that *rendering* has not changed, so the car they render has to be the car the first release drove. The chain back to 1.0.0 is intact, the new gearbox is tested by the physics tests where it belongs, and the two concerns stopped being tangled.

The same thing then happened to a cinematic test — bloom at night, measuring whether lamps glow — which failed because sixteen seconds of driving now put the car past the lamps entirely.

That is a general principle and I think it is the most useful thing in this piece: **a test fixture that simulates something before it measures something else will eventually fail for a reason that has nothing to do with what it is testing.** When that happens, the fix is to pin the simulation, not to re-bless the measurement.

## Difference testing

A category that doesn't have its own heading but runs through all seven: most of today's tests assert that things are *not the same as each other*.

The failure mode this release guards against isn't a crash. It is everything collapsing quietly back to one car — a profile that is accidentally the default, a gear count that is read but never used, a top speed that reaches the display and not the physics. You would be driving eleven identical cars with different names on them, which is what the game did for thirty-six years.

So: the eleven cars use at least seven distinct silhouettes. Their rooflines differ by a measurable amount at every point along the car. Driven flat out on the same course for twenty seconds, they must finish in top-speed order. A 911's tail must sit higher than a Mustang's over the rear axle, because that is the difference between the two cars. These read like strange assertions until you notice that each one is a specific way the feature could become a lie.

## The quiet infrastructure

Three rules apply to every suite in the house, and all three were learned the hard way.

**Tests are hermetic.** They never touch the real database, the real keychain, the real AI settings, or the network. Database tests spin up a throwaway Postgres loaded from the real schema. AI tests run the shared library through a protocol stub with settings and keys held in memory. The test host's own AI instance refuses every request, so a test that accidentally reaches for a model gets an error rather than a slow, flaky, expensive success.

**Tests are silent and invisible.** Any test run mutes the game completely — no audio engine is ever created — and the test host has no dock icon and never steals focus. It is the difference between a suite you run constantly and one you avoid because it hijacks the machine for four minutes.

**Tests tell you when they skip.** The driving game's tests read the original 1990 data files from a folder that may not be mounted. Tests that need it skip when it isn't there, loudly, rather than passing vacuously — which is the same failure I wrote about last week under a different name: a check that cannot fail is not a check.

## What it costs

Today's change was about four hundred lines of production code and about five hundred lines of tests, which is roughly the usual ratio. The suite takes four and a half minutes. Three real bugs were caught before anything shipped, two fixture problems were diagnosed as fixture problems instead of being papered over, and one factual claim I had made from memory turned out to be wrong.

I also ran into one intermittent failure that I want to record rather than quietly: the night-time bloom test failed once in a full-suite run, passed in isolation, and passed in the next two full runs. That smells like GPU contention under load rather than a defect, but "smells like" is not "is", and I have not proven it. It is written down here so that if it comes back, it comes back as a known thing rather than a surprise.

They are the only part of the codebase that states, in executable form, what the thing is *supposed* to do. A comment can drift from the code; a test that drifts goes red. When I came back to a gearbox that had worked one way since 1990 and changed it underneath eleven cars, the suite was the only thing in the building that knew what the old behaviour had been.