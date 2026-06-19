---
title: "Kovarex Enrichment Setup with Circuit Control - U-235 Production Guide for Factorio 2.0"
date: 2026-06-20
tags: ["production-ratios", "nuclear-power"]
draft: false
---

{{< callout "tip" >}}
**Kovarex at a glance:** Each centrifuge needs 40 U-235 and 5 U-238 to start, then produces 41 U-235 and 2 U-238 per 60-second cycle -- a net gain of 1 U-235 per cycle. Three centrifuges running in parallel produce roughly 3 U-235 per minute, which is enough to fuel 4-8 nuclear reactors continuously.
{{< /callout >}}

{{< section "The Kovarex Enrichment Process" >}}

{{< recipe name1="uranium_235" qty1="40x" name2="uranium_238" qty2="5x" result="uranium_235" rqty="41x" >}}

Kovarex enrichment is the key to sustainable nuclear power in Factorio. The standard uranium processing recipe (from ore) only gives you 0.7% U-235 output -- not enough to fuel a nuclear reactor consistently. Kovarex trades U-238 (which you have too much of) for U-235 (which you never have enough of).

| Stat | Value | Notes |
|------|:-----:|-------|
| Craft time | 60 seconds | Base speed, no modules |
| Input U-235 | 40 per cycle | Buffer requirement |
| Input U-238 | 5 per cycle | From uranium ore processing |
| Output U-235 | 41 per cycle | Net +1 per cycle |
| Output U-238 | 2 per cycle | Net -3 per cycle (consumed) |
| Machine | Centrifuge | Centrifuge only |

{{< /section >}}

{{< section "Bootstrapping the First Centrifuge" >}}

Before you can start Kovarex, you need 40 U-235. At 0.7% yield from ore processing, that requires processing roughly 5,714 uranium ore. Here is how to get there:

| Step | Output | Time Estimate |
|------|-------|:-------------:|
| 1. Mine uranium ore | 100-200 ore/min per drill | Continuous |
| 2. Process ore in centrifuges | 0.7% U-235, 99.3% U-238 | ~1 U-235 per 100 ore |
| 3. Buffer U-235 in a chest | 40 U-235 target | ~90 minutes at 5 drills |
| 4. Buffer U-238 separately | 5+ U-238 for first cycle | Already have plenty |
| 5. Feed both into the centrifuge | First cycle begins | Manually load chests |

**The bootstrap tip:** Run 2-3 centrifuges on standard ore processing while you mine enough uranium. Store the U-235 in a wooden chest next to your Kovarex centrifuge. Once you reach 40, insert all 40 plus 5 U-238 into the centrifuge manually or with a filtered inserter.

{{< /section >}}

{{< section "Circuit-Controlled Inserter Setup" >}}

Without circuit control, a Kovarex centrifuge keeps running until it runs out of U-238. With circuit control, you can ensure steady U-235 extraction and U-238 recycling.

{{< diagram "diagrams/kovarex-circuit.svg" "Kovarex enrichment centrifuge setup with circuit network control for U-235 extraction and U-238 recycling" "760" >}}

**Basic circuit setup:**

1. Connect the centrifuge to a red or green wire
2. Set inserter reading mode to "Read centrifuge contents" (pulse or continuous)
3. Connect the U-235 extraction inserter to the same wire
4. Set the extraction inserter condition: U-235 > 41
5. Connect the U-238 extraction inserter to the same wire
6. Set the U-238 extraction condition: U-238 > 2

This setup keeps exactly 40 U-235 and 2 U-238 in the centrifuge. The excess U-235 (the +1) gets extracted automatically. The U-238 output gets recycled back into the input chest.

For a more advanced design with [circuit network]({{< ref "/blueprints/circuit-network-guide" >}}) control:

- Use a constant combinator to output U-235 = 40
- Connect it to the extraction inserter
- Set inserter: Enable if U-235 (from centrifuge) > U-235 (from combinator)
- This dynamically adjusts extraction based on centrifuge contents

{{< /section >}}

{{< section "Optimal Centrifuge Count" >}}

| Goal | Centrifuges | U-235/min | Fuel Cells/min | Reactors Supported |
|:----:|:----------:|:---------:|:--------------:|:------------------:|
| Basic nuclear power | 1 | 1 | 14 | 2-4 |
| Medium base (60 MW) | 3 | 3 | 42 | 8-12 |
| Large base (200 MW) | 6 | 6 | 84 | 16-24 |
| Megabase (400 MW+) | 12 | 12 | 168 | 32+ |

{{< callout "info" >}}
**Fuel cell math:** One uranium fuel cell lasts 200 seconds in a reactor. One U-235 makes 10 fuel cells. So 1 U-235 per minute supports about 20 fuel cells per 200 seconds = enough for 4 reactors at full burn. See the [Nuclear Power Guide]({{< ref "/base-design/nuclear-power-guide" >}}) for exact reactor ratio calculations.
{{< /callout >}}

{{< /section >}}

{{< section "Module Choice for Kovarex" >}}

| Module | Effect | Recommendation |
|--------|--------|:-------------:|
| Productivity | No effect on U-235 output | Skip -- does not work on Kovarex recipe |
| Speed | +50% craft speed, +80% power | Best choice per centrifuge |
| Speed 3 | +100% craft speed | Endgame -- doubles your centrifuge throughput |
| Efficiency | -80% power, no speed loss | Only if power is a concern |

Productivity modules are the only module type that does NOT benefit the Kovarex recipe. The recipe is flagged as non-productivity by design. Speed modules are the clear winner.

Both speed and [quality modules]({{< ref "/space-age/quality-module-guide" >}}) work but quality modules in a Kovarex centrifuge produce quality U-235, which cannot be used in fuel cell assemblers (they accept only normal quality items). Speed modules are safer.

{{< /section >}}

{{< section "Common Mistakes" >}}

- **Starting too early:** Do not rush Kovarex. Two standard ore-processing centrifuges can accumulate enough U-235 for a bootstrap while your base is still on steam power. Start Kovarex only when you need consistent nuclear fuel.
- **Forgetting the U-238 loop:** Without recycling U-238 output back into the centrifuge input, your Kovarex setup will stall after a few cycles. Always loop the 2 U-238 output back into the input chest.
- **Using filter inserters wrong:** A filter inserter set to "U-235" on extraction can accidentally grab the seed U-235 (the 40 that should stay in the centrifuge). Use circuit control to ensure extraction happens only when U-235 > 40.

{{< /section >}}

{{< section "Bottom Line" >}}

Kovarex enrichment solves the U-235 scarcity problem with a simple investment: one centrifuge, a circuit wire, and a stockpile of U-238 from ore processing. Start with 3 centrifuges for a steady supply. Use circuit control if you want automated priority management. Speed modules are the only modules worth using.

{{< /section >}}

{{< section "Community Verification" >}}

- [Factorio Wiki: Kovarex enrichment process](https://wiki.factorio.com/Kovarex_enrichment_process) -- Official recipe and mechanics
- [Factorio Cheat Sheet: Kovarex](https://factoriocheatsheet.com/) -- Ratio diagrams and quick reference
- [Reddit: Kovarex circuit designs](https://www.reddit.com/r/factorio/comments/b2s1p5/compact_circuitcontrolled_kovarex_designs/) -- Community designs and comparisons
