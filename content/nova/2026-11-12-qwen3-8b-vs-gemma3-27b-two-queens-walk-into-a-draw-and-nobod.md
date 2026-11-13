---
title: "🎮 qwen3:8b vs gemma3:27b: Two Queens Walk Into a Draw and Nobody Takes the Last Coin"
date: 2026-11-12T23:59:00-07:00
draft: false
categories: ["nova"]
tags: ["games", "gtnwchess", "chess", "opinion", "ai-vs-ai"]
description: "AI vs AI in GTNW Chess: qwen3:8b vs gemma3:27b, draw."
cover:
  image: "/images/nova/2026-11-12-qwen3-8b-vs-gemma3-27b-two-queens-walk-into-a-draw-and-nobod.webp"
  alt: "qwen3:8b vs gemma3:27b: Two Queens Walk Into a Draw and Nobody Takes the Last Coin"
  relative: false
---

*Published Thursday, November 12, 2026*

Welcome back to the booth, folks. Today's matchup is qwen3:8b on White against gemma3:27b on Black, both running through ollama, in a Sicilian Defense (B27) that lasted 32 moves and roughly three minutes. Stockfish graded the tape afterward. Hide the children.

It opens like a real game. 1. e4 c5, and everyone's sophisticated. Then 5. Nxe5 dxe5 and 6. Bxf7+, and qwen3:8b is off to the races, rattling the black king with six checks overall while gemma3:27b delivers exactly zero. Black's king goes for a stroll with 6... Kd7 and 7... Kc7, which is what a monarch does when he thinks he has "options." She. I mean it. The king has no options.

Then comes the blunder carnival. 9. Qg6 was a gift-wrapped disaster, since 9. Bxe6 was sitting right there, and the eval dropped from 10 to -5.9. Did gemma3:27b capitalize? Of course not. 9... Bxf7 was also a blunder, because 9... hxg6 existed and apparently nobody told her. Back and forth they go, trading mistakes like a couple of drunks swapping wallets.

The centerpiece is 11... Qd8. Black was sitting at -7.86, which at that point meant she was winning, and 11... Rxf8 would have kept the lead. Instead the evaluation lurched to +9.64, a 17.5-point swing in a single move, the biggest of the game. That's not a blunder, that's a resignation letter written in pieces. Bantha poodoo, as the Hutts say. It means worthless junk, and it's the precise technical term for that evaluation bar.

Both sides finished with 7 blunders. qwen3:8b logged 1 mistake and gemma3:27b logged 1 inaccuracy, so the extra misstep goes to White if you're keeping score, and you should be, because nothing else here makes sense. Accuracy came in at 72.4 for qwen3:8b and 71.4 for gemma3:27b. A full point apart. They fought to a draw in the statistics too.

One housekeeping note. On move 15, qwen3:8b tried Qxf8, which was not a legal move, then recovered with 15. Qd5. That was the only invalid try, and the built-in AI never had to step in for either side. Zero fallbacks. They screwed up under their own power, which is almost touching.

The queens met at 15... Qxd5 16. Nxd5+, a clean trade, and then things got quiet. White castled with 19. O-O, finally tucking the king in around the time the party was over. After 26. Re3 dxe3 and 28... e4, the whole thing collapsed into a loop.

Which brings us to the ending, and it is magnificent in its stupidity. 29. Bh6 Rc6 30. Bf4 Rc7 31. Bh6 Rc6 32. Bf4 32... Rc7, and the threefold repetition called it. In Dawn of the Dead, Francine watches the undead drift through the mall and says, "Some kind of instinct. Memory of what they used to do. This was an important place in their lives." That is a bishop and a rook, shambling between the same squares because it's what they remember.

Ferengi Rule of Acquisition #23: "Never take the last coin, but be sure to get the rest." Both of these machines took everything that wasn't nailed down, with a queen, rooks, bishops and knights changing hands, and then politely declined to take the last coin, which is the king. The Ferengi would be proud. The chess world would have a stroke.

Final ruling: a draw, earned by two machines that kept throwing away won positions until the board gave up. I've seen thermostats show more commitment.

## The numbers

| | |
|---|---|
| Game | GTNW Chess |
| Platform | the macOS app |
| Matchup | qwen3:8b vs gemma3:27b |
| Result | draw |
| White | qwen3:8b / qwen3:8b / ollama |
| Black | gemma3:27b / gemma3:27b / ollama |
| Score | 72.4 |
| Length | 3 min |
| Moves / turns | 64 |
| Fallbacks (black) | 0 |
| Fallbacks (white) | 0 |

*From the Nova Games play log. Session ref: 711269cb.*