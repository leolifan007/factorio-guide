---
title: "Kovarex Enrichment — The Only Sustainable Nuclear Fuel Setup"
description: "Kovarex enrichment guide for Factorio. How to kickstart the process, the exact centrifuge ratios for any reactor size, and the automation blueprint that keeps your nuclear plant running forever."
date: 2026-05-23
lastmod: 2026-05-23T17:53:00+08:00
publishDate: 2026-05-26T09:43:00+08:00
tags: ["production-ratios", "nuclear", "base-design"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

Your nuclear power plant is running on borrowed time. U-235 drops at a 0.7% chance per centrifuge cycle from uranium ore. At 1 GW consumption, you need 100+ reactors. You don't have 100 reactors. You have 8. And they're eating through your U-235 stockpile faster than your centrifuges can replace it. The fuel warning light is blinking. Kovarex enrichment is the fix — but the setup tripwires trip up almost every first-timer.

Your nuclear plant is burning fuel cells it cannot replace. Kovarex is the solution. Here is exactly how to build it without wasting 200 hours on the wrong ratios.

{{< callout "tip" >}}
**TL;DR:** Kovarex enrichment converts excess U-238 into U-235. It requires 40 U-238 as input to produce 1 U-235 per cycle (~60 seconds). Kickstart requires stockpiling 40 U-235 from normal processing first. Ratio: 3 Kovarex centrifuges per reactor running at full power. Always buffer U-238 — if the stockpile runs dry, enrichment stops.
{{< /callout >}}

## The Uranium Bottleneck Nobody Tells You About

Normal uranium processing (centrifuge on uranium ore) produces U-238 at 99.3% efficiency and U-235 at 0.7%. This is per cycle. The cycle is fast — a centrifuge runs about 1 cycle per 50 seconds. But 0.7% means: for every 143 centrifuge-cycles of uranium ore processing, you get 1 U-235.

A nuclear fuel cell needs 10 U-235 + 10 U-238 to craft. Each fuel cell powers 1 reactor for 200 seconds. A 1-reactor setup consumes 1 fuel cell per ~200 seconds = 0.005 cells/sec = 0.05 U-235/sec = 3 U-235 per minute.

Your normal processing: 1 centrifuge on uranium ore produces roughly 0.7 U-235 per minute (at the 0.7% rate and ~50 sec/cycle). That's almost exactly enough for 1 reactor. Almost. But the randomness of the probabilistic drops means you'll have days where your reactor sits idle because U-235 dropped out in the wrong cycle.

Kovarex removes the randomness entirely.

## Why Your Nuclear Power Keeps Running Dry

The problem isn't production — it's the ratio of U-238 to U-235 in natural uranium. U-238 piles up. U-235 stays scarce. Your storage is full of U-238 you'll never use, and your fuel cell production is bottlenecked by U-235.

The numbers:
- 1 uranium ore → 1 cycle in centrifuge
- 0.7% chance of U-235 per cycle
- 99.3% chance of U-238 per cycle
- Natural uranium is essentially U-238 with trace U-235

After processing 1000 uranium ore, you have ~10 U-235 and ~990 U-238. The U-238 accumulates. You need U-235. The solution: convert U-238 into U-235.

Kovarex enrichment does exactly this.

## The Single-Chamber Setup That Actually Works

Kovarex enrichment process:
- Input: 40 U-238 (left slot) + 40 U-238 (right slot)
- Output: 41 U-238 (left) + 1 U-235 (right)
- Cycle time: ~60 seconds per centrifuge

Net result: you spend 40 U-238 and get 1 U-235. The net U-238 cost per U-235 is 40. This seems expensive. But when you have thousands of U-238 sitting in storage — which you always do after the first hour of nuclear — this is free energy.

The catch: you need 40 U-238 already processed before the first cycle. And you need 40 U-235 to kickstart the process in the first place.

## Isolating U-235: The Statistical Reality

Kovarex is a bet on statistics. The process requires U-235 as a catalyst. You put in 40 U-238, you get out 1 U-235. The first U-235 out of a fresh Kovarex centrifuge is the hardest one.

**The kickstart sequence:**
1. Process uranium ore with normal centrifuges until you have 40 U-235 accumulated
2. This takes approximately 100+ centrifuge-cycles (random, can be faster or slower)
3. Put 40 U-235 into the Kovarex centrifuge (both input slots)
4. The centrifuge starts cycling: every 60 seconds, it produces 1 additional U-235
5. You now have a self-sustaining U-235 production line

Once running, the Kovarex centrifuge produces 1 U-235 per 60 seconds. Your reactor at 1 GW (1 reactor) consumes 3 U-235 per minute. So 1 Kovarex centrifuge is enough for 1 reactor. Sort of — you also need fuel cell assemblers and the regular ore processing for U-238 input.

**The exact ratio for 1 reactor at full power:**
- 3 Kovarex centrifuges (produces 3 U-235/min, matches reactor demand of 3/min)
- 10 normal centrifuges for uranium ore processing (produces U-238 to feed Kovarex)
- 1 uranium mining drill at full yield (~55 ore/min)
- 1 fuel cell assembler (consumes U-235 + U-238, produces fuel cells)

1 Kovarex centrifuge = 1 U-235/min
1 reactor at full power = 3 U-235/min (1 fuel cell every 200 seconds)
Therefore: 3 Kovarex centrifuges per 1 reactor

## The Automation Blueprint You Can Copy Today

The Kovarex setup has three parts:

**Part 1: U-238 production (uranium ore processing)**
- 10 normal centrifuges on uranium ore
- Each produces U-238 at ~10/min
- Total: 100 U-238/min
- This is the fuel tank for your Kovarex centrifuges

**Part 2: Kovarex enrichment**
- 3 Kovarex centrifuges
- Each consumes 40 U-238 per cycle (every 60 seconds)
- Combined demand: 120 U-238/min
- Output: 3 U-235/min
- Requires U-238 buffer to start (build up a stockpile first)

**Part 3: Fuel cell production**
- 1 assembler making nuclear fuel cells
- Recipe: 1 uranium fuel cell = 1 U-235 + 19 U-238
- At 1 reactor, you need 1 cell per 200 seconds = 0.3 cells/min
- 1 assembler 3 produces 0.6 cells/min — plenty of headroom
- Feed excess U-235 back into Kovarex to produce more U-235 (amplification)

**The critical buffer:**
Always maintain 500+ U-238 in a storage chest feeding your Kovarex centrifuges. If U-238 hits 0, the enrichment cycle stops and your reactor eventually runs out of fuel. U-238 is never scarce — just never run the pipe dry.

## Scaling Up Without Breaking the Ratio

For a 10-reactor nuclear plant (800 MW):
- 30 Kovarex centrifuges (3 per reactor)
- 100 normal centrifuges for ore processing (10 per reactor)
- 10 uranium mining drills
- 10 fuel cell assemblers

The math holds at any scale. The Kovarex ratio is fixed: 3 centrifuges per reactor. The ore processing scales with it.

**Power cost:** Each Kovarex centrifuge draws 400 kW. Each normal centrifuge draws 200 kW. A 10-reactor setup's enrichment alone consumes ~16 MW of power. This is why nuclear power makes sense — the fuel is essentially free, but the enrichment power cost is real.

**The space requirement:** 30 Kovarex + 100 normal centrifuges = a footprint roughly the size of a large main bus section. Plan your nuclear area before you build. Separate the enrichment wing from the reactor wing with heat exchangers and turbines between them.

## The Kovarex Warning Nobody Puts in Writing

The process requires U-235 to run. The first batch of U-235 must come from normal processing. There is no shortcut. You cannot start Kovarex with U-238 only — the process literally requires U-235 in both input slots to begin.

If your reactor runs out of fuel cells because you haven't accumulated enough U-235 to kickstart Kovarex: don't panic. A single uranium ore processing line with 5-10 centrifuges will accumulate 40 U-235 in 30-60 minutes of game time. Set up the processing, go do something else, come back.

The other warning: U-235 is rarer than you think. 40 U-235 sounds like a lot. In practice, with 10 normal centrifuges, it takes about 40 minutes of processing. The randomness can push it to 2 hours. Set up the accumulation process before you need it.

## The Bottom Line

Kovarex enrichment is not optional for serious nuclear power. It converts your U-238 pile into a sustainable fuel supply. Once running, a 3-centrifuge Kovarex setup per reactor makes nuclear power truly plug-and-play. No more watching your fuel warning light. No more running to refill centrifuges. The factory maintains itself.
