---
title: "Nuclear Reactor Ratios & Tileable Design — The Only Setup You Need"
description: "Step-by-step Factorio nuclear reactor setup with exact tileable layouts, heat pipe ratios (1:20:40), steam turbine math, Kovarex enrichment loop, and fuel efficiency from 40 MW to multi-GW. Copy-paste ready for your megabase."
date: 2026-05-21
tags: ["base-design", "production-ratios"]
draft: false
emoji: "☢️"
---

Your coal power graph is in the red. You expanded three new outposts and the steam engines are barely keeping up. Before you paste 10,000 solar panels — nuclear: 480 MW fits in the space of 8 solar panels, one uranium patch lasts hundreds of hours, and the UPS hit is negligible.

{{< callout "tip" >}}
**TL;DR:** 2×2 reactor = 480 MW. You need 48 heat exchangers, 84 steam turbines, 4 offshore pumps, and one centrifuge running Kovarex. Build it once, never think about power again.
{{< /callout >}}

## The Root Cause — Why Coal Eventually Caps Out

At 40+ steam engines you're spending more time laying belts than building your factory. Coal patches deplete. Belt throughput maxes out. Solar works but the space requirement becomes absurd — 480 MW needs roughly 8,000 panels plus 6,700 accumulators.

| Power Source | MW per tile | Fuel cost | UPS impact | When to switch |
|-------------|:-----------:|:---------:|:----------:|:--------------|
| Steam engines | ~0.3 | Free (coal) | Low | Early game |
| Solar panels | ~0.06 | Free | Best | Mid game if patient |
| Nuclear | ~5 | Uranium | Good | **Mid game — this one** |

A single 2×2 nuclear block delivers roughly 55 MW per tile loaded. For comparison, the same tile footprint with solar would net you 0.6 MW on a good day.

## Building the Fuel Chain First

Before you place a single reactor, set up fuel production. The nuclear chain needs three stages:

**Stage 1 — Uranium mining.** One electric mining drill on a uranium patch produces enough ore for a 2×2 reactor. The catch: you need sulfur for sulfuric acid (10 acid per ore). Run a pipe from your oil base.

**Stage 2 — Centrifuge processing.** Each centrifuge runs a 12-second cycle. 10 uranium ore in → 99.3% U-238 + 0.7% U-235. Without modules you'll net roughly 1 U-235 per 140 cycles. Start at least 5 centrifuges.

**Stage 3 — Fuel cell assembly.**
- 19 U-238 + 1 U-235 → 10 fuel cells
- Burn time: 200 seconds per cell
- Consumption: ~18 cells/hour per reactor
- A 2×2 burns ~72 cells/hour

One assembler with speed modules running for 5 minutes produces enough cells for hours.

{{< callout type="info" >}}
**Quick Tip for Min-Maxers:** Don't rush Kovarex. The first 40 U-235 (needed to bootstrap) takes about 6,000 ore. Run centrifuges continuously from the moment you have uranium processing unlocked — stockpile U-235 while your first reactor runs on manual.
{{< /callout >}}

## The Proven Fix — 2×2 Reactor Layout

Four reactors touching in a square. Each adjacent reactor adds +100% heat output (neighbor bonus). This is the standard for a reason.

{{< diagram "diagrams/nuclear-reactor-layout.svg" "2x2 nuclear reactor layout with heat pipes, heat exchangers, and steam turbines" "760" >}}

**Neighbor bonus math:**
- Corner reactors: 1 neighbor → +100% = 80 MW each
- Center reactors: 2 neighbors → +300% = 160 MW each
- Total: 480 MW from 4 reactors

**The exact component list for a 2×2:**

- **Reactors:** 4 (must touch)
- **Heat exchangers:** 48 (12 per reactor worth of output)
- **Steam turbines:** 84 (21 per reactor worth)
- **Offshore pumps:** 4 (one per 12 heat exchangers)
- **Fuel cells per hour:** 72

{{< callout type="warning" >}}
**Don't circuit-control fuel insertion without a plan.** A common trap: insert fuel only when steam < threshold. Works great until a power spike drains the buffer and your entire base browns out. Use at least 50 steam tanks as a buffer before attempting fuel-saving circuits.
{{< /callout >}}

## Understanding Heat Pipe Physics (Where Most Builds Fail)

Heat travels through pipes like a fluid with two hard limits:

1. **Range:** ~16 tiles from reactor before meaningful dropoff begins
2. **Capacity:** One heat pipe segment handles heat for ~4 heat exchangers

**The three rules that prevent a brownout:**
- Keep heat pipes within 20 tiles of the reactor
- Run double pipes for 2+ wide reactor rows
- Place exchangers on both sides — not just one
- More pipes increase capacity, not range

For a 2×2, use 3-5 parallel heat pipes running from the reactor block to the exchanger array. Single-file heat pipes will choke at scale.

## The Bootstrapping Problem — Getting Kovarex Started

Kovarex converts 40 U-235 + 5 U-238 → 41 U-235 (+5 U-238 recipe cost, net +1 U-235 per cycle). Once running, it produces U-235 faster than any reactor block can burn it.

**The bottleneck:** Getting 40 U-235 to start. At 0.7% enrichment with 5 centrifuges, that's about 2-3 hours of continuous mining and processing.

**Skip the wait:**
- Start centrifuges the moment you research uranium processing — even before you build the reactor
- Prod modules in centrifuges speed this up significantly
- If 40 U-235 feels slow, don't wait — build your reactor on the first 10 and run it manually with solar as backup

## Traps People Keep Falling Into

**Not enough water.** One offshore pump feeds 12 heat exchangers. Period. A 2×2 needs 4 dedicated offshore pumps. Running more exchangers per pump causes steam starvation that's hard to diagnose.

**Heat pipe too long.** Past ~16 tiles, heat transfer drops off a cliff. You can extend it with more parallel pipes, but after 25 tiles you need a separate reactor row.

**Overproducing fuel cells.** 72 cells per hour is the burn rate. One assembler running for 5 minutes keeps you running for hours. Do not build four assemblers.

**Ignoring the neighbor bonus.** A 2×2 sharing bonuses produces 480 MW. Four standalone reactors with the same fuel produce 160 MW. The difference: touching the reactors.

## Scaling Past 1 GW

For megabase power, use tileable 2×N rows:

| Configuration | Reactors | Cells/hr | Total MW | MW/cell | When to build |
|:-------------|:--------:|:--------:|:--------:|:-------:|:-------------|
| Single 1×1 | 1 | 18 | 40 | 2.2 | Test setup |
| 2×1 row | 2 | 36 | 160 | 4.4 | Early expand |
| 2×2 square | 4 | 72 | 480 | 6.7 | **Standard** |
| 2×4 | 8 | 144 | 1,120 | 7.8 | Full megabase |

Each additional reactor pair adds roughly 160 MW. A 2×8 setup pushes 2,240 MW — enough for any base size achievable without UPS mods.

---

## Community Verification & Resources

- [Official Factorio Wiki — Nuclear Power](https://wiki.factorio.com/Nuclear_power) — exact heat exchange formulas and pipe throughput tables
- [Factorio Forums — Nuclear Power Discussion](https://forums.factorio.com/viewforum.php?f=18) — community reactor blueprints and bug reports
- [Alt-F4 Blog — Nuclear Throughput Deep Dive](https://alt-f4.blog/) — engineering analysis of heat pipe mechanics
- [Kirk McDonald's Factorio Calculator](https://kirkmcdonald.github.io/calc.html) — exact ratios for any reactor configuration
