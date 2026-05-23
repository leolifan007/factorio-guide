---
title: "Kovarex Enrichment — The Only Sustainable Nuclear Fuel Setup"
description: "Kovarex enrichment guide for Factorio. How to kickstart the process, the exact centrifuge ratios for any reactor size, and the automation blueprint that keeps your nuclear plant running forever."
date: 2026-05-23
lastmod: 2026-05-23T19:09:00+08:00
publishDate: 2026-05-26T09:43:00+08:00
tags: ["production-ratios", "nuclear", "base-design"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

Your nuclear plant is running on borrowed time. U-235 drops at 0.7% chance per centrifuge cycle. At 1 GW, you need U-235 faster than normal processing can provide. Kovarex enrichment is the fix — but the setup trips up almost every first-timer.

{{< callout "tip" >}}
**TL;DR:** Kovarex converts 40 U-238 → 1 U-235 per 60-second cycle. Kickstart needs 40 U-235 stockpiled from normal processing first. Ratio: **3 Kovarex centrifuges per reactor** at full power. Buffer 500+ U-238 or enrichment stops.
{{< /callout >}}

{{< diagram "diagrams/kovarex-loop.svg" "Kovarex enrichment loop — normal processing, 3-centrifuge enrichment, and fuel cell production" "800" >}}

## The Uranium Bottleneck

Normal uranium processing in a centrifuge:

| Output | Probability per cycle |
|--------|----------------------|
| U-238 | 99.3% |
| U-235 | 0.7% |

Cycle time: ~50 seconds. Result: for every ~143 ore-processing cycles, you get **1 U-235**. A 1-GW reactor consumes 3 U-235/minute (1 fuel cell per 200 seconds). Normal processing produces ~0.7 U-235/min from one centrifuge — almost enough, but the randomness means idle reactors when drops miss.

Kovarex removes the randomness entirely.

## How Kovarex Works

| Parameter | Value |
|-----------|-------|
| Input | 40 U-238 (both slots) |
| Output | 41 U-238 + **1 U-235** |
| Cycle time | ~60 seconds |
| Net cost | 40 U-238 per U-235 produced |

The catch: you need **40 U-235 as catalyst** to kickstart the first cycle. There is no shortcut — it must come from normal processing.

## The Kickstart Sequence

1. Run 5-10 normal centrifuges on uranium ore
2. Wait for 40 U-235 to accumulate (**30-60 minutes**, randomized)
3. Load 40 U-235 into both Kovarex input slots
4. Centrifuge cycles: produces 1 additional U-235 every 60 seconds
5. Self-sustaining from here — feed excess U-235 back as catalyst for more Kovarex centrifuges

## The Exact Ratio

For **1 reactor at full power (1 GW):**

| Component | Count | Output |
|-----------|-------|--------|
| Kovarex centrifuges | 3 | 3 U-235/min |
| Normal centrifuges (ore) | 10 | ~100 U-238/min |
| Uranium mining drills | 1 | ~55 ore/min |
| Fuel cell assembler | 1 | 0.6 cells/min (0.3 needed) |

**Formula:** 1 reactor = 3 U-235/min = 3 Kovarex centrifuges.

Scaling is linear: **10 reactors = 30 Kovarex + 100 normal centrifuges + 10 fuel cell assemblers.**

## Fuel Cell Math

| Item | Recipe | Time |
|------|--------|------|
| Nuclear fuel cell | 1 U-235 + 19 U-238 | 10 sec |
| Reactor consumption | 1 cell / 200 sec | 0.3 cells/min |
| Assembler 3 output | 6 cells/min | Plenty of headroom |

Feed excess U-235 back into Kovarex for amplification — each new U-235 enables another Kovarex centrifuge.

## Critical Warnings

| Warning | Detail |
|---------|--------|
| **U-238 buffer = life** | If storage hits 0, enrichment stops → reactor starves. Maintain 500+ buffer chest. |
| **Kickstart takes time** | 40 U-235 sounds small. With 10 centrifuges, expect 40 minutes minimum. Randomness can push it to 2 hours. Set up accumulation before you need power. |
| **Power cost is real** | Each Kovarex centrifuge = 400 kW. A 10-reactor enrichment wing draws ~16 MW. Nuclear fuel offsets this — but only if enrichment keeps running. |
| **No shortcut exists** | You cannot start Kovarex with U-238 alone. Both input slots require U-235 for the first cycle. Period. |

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| Starting Kovarex before accumulating 40 U-235 | Centrifuge sits idle forever |
| No U-238 buffer chest | One dry cycle cascades into plant shutdown |
| Underestimating kickstart time | Reactor runs out of fuel while waiting |
| Placing enrichment too far from reactors | Long inserter/belt runs = delivery delays |

## The Bottom Line

Kovarex makes nuclear power truly sustainable. The ratio never changes: **3 centrifuges per reactor**. Buffer U-238 generously. Kickstart before you need the power. Once running, your nuclear plant maintains itself indefinitely.
