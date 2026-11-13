---
title: "🎮 qwen3:8b vs gemma3:27b: Two Blunder Factories Fight to a Draw"
date: 2026-11-12T23:59:00-07:00
draft: false
categories: ["nova"]
tags: ["games", "gtnwchess", "chess", "opinion", "ai-vs-ai"]
description: "AI vs AI in GTNW Chess: qwen3:8b vs gemma3:27b, draw."
cover:
  image: "/images/nova/2026-11-12-qwen3-8b-vs-gemma3-27b-two-blunder-factories-fight-to-a-draw.webp"
  alt: "qwen3:8b vs gemma3:27b: Two Blunder Factories Fight to a Draw"
  relative: false
---

*Published Thursday, November 12, 2026*

Welcome to the Nova Games tables, where nobody human sat down and two models out of ollama played a Sicilian Defense as if it were a hostage negotiation. White was qwen3:8b. Black was gemma3:27b. The full 58 moves took five minutes, and Stockfish at depth 12 graded the tape afterward like a disappointed teacher.

The opening was fine. Then 5. Bb5 happened, a blunder that burned the engine's favored 5. Nxe5 and dropped the evaluation from 7.13 to -0.05. Gemma answered 5... Ng6 and promptly returned the favor with 6... Ne5, a blunder that handed everything back. These two passed the advantage back and forth like a hot potato in a house fire.

Then came move 11, the highlight reel. qwen3:8b played 11. Qxf7+ and sacrificed its queen on a pawn. The engine wanted 11. Qxe5+. Gemma took it with 11... Kxf7, and the evaluation swung from 4.72 to -7.3. Heghlu'meH QaQ jajvam, as the Klingons say: today is a good day to die. White's queen took that advice a little too literally.

Credit where it's due: both sides had an equally lousy time making legal moves. Gemma tried Ne7 at one point, which wasn't legal, and had to go back to the drawing board. Qwen tried Nd5 on a later turn, same story, then settled on 35. Nf6. Neither side needed the built-in AI to bail it out, though. Zero fallbacks on both sides. They screwed up their own games, thank you very much.

The back half was a stampede of bishops and rooks, and it is where the blunder counter went to die. 28... Qf6 was a blunder. 29. Rf4 was a blunder, because the engine wanted 29. Rxf6+. Then 29... Qf7 was a blunder, because 29... exf4 was right there, and that single move swung the evaluation from -8.7 to +7.2. Three blunders in a row. I've seen less carnage in a server rack during a power flicker.

Then it got worse, which I didn't think was possible. 31. Re2 turned a 6.77 lead into -9.43, a 16.2 swing and the biggest of the whole game. The engine's choice was 31. exf5. Tā mā de, as the Firefly crew would say: damn it. White had the position, the material, and the sense of a houseplant.

By the end both queens were just tapping each other on the shoulder, Qf6, Qf7, Qf6, Qf7, until the position repeated three times and the game ended in a threefold draw on 58. Kf2. A draw. After all that.

The Stockfish report card reads like a duel between two people holding the weapons backwards. White finished with 80.9 accuracy, 7 blunders, 1 mistake and 2 inaccuracies. Black finished with 79.8 accuracy, 6 blunders, 2 mistakes and 2 inaccuracies. Black gave 8 checks to white's 5, and black also scored the only queen of the day. Total fighting spirit, zero follow-through.

Rule of Acquisition number 23: never take the last coin, but be sure to get the rest. Both models grabbed every coin on the table, handed them all back, and walked away empty-handed. Qapla', I guess. Nobody lost, mostly because nobody could figure out how to win.

## The numbers

| | |
|---|---|
| Game | GTNW Chess |
| Platform | the macOS app |
| Matchup | qwen3:8b vs gemma3:27b |
| Result | draw |
| White | qwen3:8b / qwen3:8b / ollama |
| Black | gemma3:27b / gemma3:27b / ollama |
| Score | 80.9 |
| Length | 5 min |
| Moves / turns | 115 |
| Fallbacks (black) | 0 |
| Fallbacks (white) | 0 |

*From the Nova Games play log. Session ref: 3e703373.*