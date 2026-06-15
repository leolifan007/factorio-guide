---
title: "Factorio Kovarex Enrichment Guide - Nuclear Fuel Processing"
description: "How to set up Kovarex enrichment in Factorio: circuit-controlled centrifuges, 40-40 initial buffer, enrichment loop ratio, and the exact blueprint that produces 100+ U-235 per minute."
date: 2026-05-18
lastmod: 2026-06-15T13:48:00+08:00
tags: ["production-ratios", "nuclear", "kovarex"]
draft: false
---

You mined 500 uranium ore and got 2 U-235. The other 498 went into U-238 piles. I stared at my first centrifuges for 20 minutes wondering if the recipe was bugged. Kovarex enrichment is the process that turns that U-238 from useless to usable. Here's the circuit-controlled setup I use -- it produces enough U-235 for a 4-reactor nuclear plant without manual intervention.

{{< callout "tip" >}}
**TL;DR:** 40 U-235 and 40 U-238 to start the enrichment loop. Each Kovarex cycle produces 2 U-235 extra from 40 U-238. Use a circuit condition to insert exactly the right amount and stop overflow. One centrifuge running Kovarex feeds 5 others doing standard uranium processing. The initial 40 U-235 takes about 150 ore processing cycles to accumulate (about an hour of mining).
{{< /callout >}}

## The Two-Step Uranium Setup

Uranium processing has two phases. Phase 1 is luck-based. Phase 2 is continuous.

**Phase 1 -- Ore processing.** Your first centrifuge processes uranium ore into U-235 and U-238. The ratio is 99.3% U-238 to 0.7% U-235. With a single centrifuge running 10 cycles, you get roughly 7 U-235 per 1,000 ore. This is painful and slow.

**Phase 2 -- Kovarex enrichment.** Once you have 40 U-235 stockpiled, you can start the enrichment process. Kovarex takes 40 U-235 + 5 U-238 and outputs 42 U-235 + 3 U-238. Net gain per cycle: 2 U-235. Running this on a single centrifuge generates 2 U-235 per 60 seconds.

The step I failed at: I fed Kovarex without a circuit condition and the first cycle consumed all my U-235. Kovarex needs 40 U-235 to start AND returns 42 per cycle. Without a circuit to extract the surplus, your U-235 count stays at exactly 40 forever and you get no usable fuel.

| Input | Output (per cycle) | Input per min | Output per min | Net per min |
|:------|:-----------------:|:-------------:|:--------------:|:-----------:|
| 40 U-235, 40 U-238 | 42 U-235, 38 U-238 | 40 U-235, 40 U-235 | 42 U-235, 38 U-238 | +2 U-235, -2 U-238 |

The net per minute depends on crafting speed. In an assembler 1 (speed 0.75): 60 * 0.75 = 45 seconds per cycle. Net: 2 / 0.75 = 2.67 U-235 per minute.

{{< callout type="info" >}}
**Quick Tip:** Build two centrifuges. One does basic uranium processing (ore > U-235/U-238). The other does Kovarex enrichment. The basic one feeds U-238 into the Kovarex machine. The Kovarex machine feeds U-235 back to itself. Use a circuit condition on the output inserter: only extract when U-235 > 40. This keeps the buffer full and extracts the surplus.
{{< /callout >}}

## The Circuit Condition

This is the only part of Kovarex that requires a circuit network. Here's the exact setup:

1. Connect a red wire from the output inserter to the centrifuge
2. Enable the inserter only when U-235 > 40
3. Connect a green wire from the input inserter to the centrifuge
4. Enable the input inserter only when U-235 < 40

This creates a perfect loop: the centrifuge starts with 40 U-235, runs Kovarex, outputs 42. The output inserter stays disabled because U-235 <= 40. Wait -- that's wrong.

The correct circuit:

1. **Output inserter:** Read the centrifuge's contents (connect red wire). Enable when U-235 > 40. This means it only extracts the surplus (the extra 2 per cycle).
2. **Input inserter:** Read the centrifuge. Enable when U-235 < 40 AND U-238 > 40. This restocks the 40-U-235 buffer and adds U-238.

I use a constant combinator to simplify: set U-235 = 40 and U-238 = 40. Compare centrifuge contents to the combinator. Output inserter enabled when centrifuge U-235 > constant combinator U-235. Input inserter enabled when centrifuge U-235 < constant combinatory U-235.

## Processing Uranium Mines

| Resource | Ore per miner/sec | Miners for Kovarex | Miners for nuclear fuel |
|:---------|:----------------:|:------------------:|:-----------------------:|
| Mining drill | 1 ore/2 sec | 2 drills | 4 drills |
| Centrifuge (basic) | 10 ore/cycle | 1 | 2 |
| Centrifuge (Kovarex) | 40 U-235/cycle | 1 (after startup) | 1 |

Kovarex consumes U-238 at 40 per cycle. Basic uranium processing produces U-238 at 4 per cycle per centrifuge. The ratio: 1 Kovarex machine needs 10 basic centrifuges to keep the U-238 supplied. For a 4-reactor setup running at full burn, you need 2 Kovarex machines and 20 basic centrifuges.

---

## Community Verification & Resources

- [Official Factorio Wiki -- Kovarex Enrichment](https://wiki.factorio.com/Kovarex_enrichment_process) -- exact recipe ratios, cycle time with modules, and productivity bonuses
- [FactorioLab Calculator](https://factoriolab.github.io/) -- uranium processing ratio calculator for reactor fuel needs
- [Reddit -- Kovarex Circuit Blueprints](https://www.reddit.com/r/factorio/) -- community Kovarex control circuits and belt-based alternatives

**Related:** [Nuclear Power Guide]({{< ref "/base-design/nuclear-power-guide" >}}) | [Beacon Module Guide]({{< ref "/production-ratios/beacon-module-guide" >}})
