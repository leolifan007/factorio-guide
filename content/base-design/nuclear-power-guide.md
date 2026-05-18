---
title: "Nuclear Power — Complete Setup Guide"
description: "Complete Factorio nuclear power guide: reactor layout, heat pipe physics, steam turbine ratios, Kovarex enrichment, and fuel efficiency from 40 MW to multi-GW."
date: 2026-05-18
tags: ["base-design", "production-ratios"]
draft: false
---

I put off nuclear for three playthroughs. Solar seemed simpler, steam seemed cheaper. Then I built my first 2×2 reactor and watched 480 MW light up from a single fuel cell. I haven't looked back.

{{< callout "tip" >}}
**TL;DR:** Build a 2×2 reactor block for 480 MW. You need 48 heat exchangers, 84 steam turbines, 4 offshore pumps. One centrifuge running Kovarex fuels it forever.
{{< /callout >}}

{{< section "Why Go Nuclear?" >}}

Nuclear isn't the cheapest option, but it's the best middle ground for a mid-to-late game factory:

| Power Source | MW per tile | Fuel cost | UPS impact | Setup effort |
|-------------|:-----------:|:---------:|:----------:|:------------:|
| Steam engines | ~0.3 MW/tile | Free (coal) | Low | Minimal |
| Solar panels | ~0.06 MW/tile | Free | Best | Massive |
| Nuclear | ~5 MW/tile | Cheap (uranium) | Good | Moderate |

- A 2×2 reactor produces 480 MW in the space of 8 solar panels
- One uranium patch lasts hundreds of real-time hours
- Nuclear UPS impact is far lower than 10,000 solar panels and accumulators
- Scales from 40 MW (single reactor) to multi-GW tileable designs

{{< section "Fuel Cycle — From Ore to Power" >}}

The nuclear fuel chain has several stages:

{{< recipe name1="uranium" qty1="10x" result="uranium_235" rqty="0.7%" >}}
{{< recipe name1="uranium" qty1="10x" result="uranium_238" rqty="99.3%" >}}

Each centrifuge processes 10 uranium ore per cycle (12 seconds without modules). At 0.7% enrichment, you'll get about 1 U-235 for every 143 ore processed.

Fuel cells combine the two isotopes:

{{< recipe name1="uranium_235" qty1="1x" name2="uranium_238" qty2="19x" result="uranium_fuel_cell" rqty="10x" >}}

Each fuel cell burns for 200 seconds in a reactor. A single reactor uses 0.005 fuel cells per second — about 18 cells per hour.

{{< section "Reactor Layout — 2×2 Standard" >}}

The 2×2 layout is the gold standard for nuclear power. Four reactors arranged in a square, each touching two neighbors.

{{< diagram "diagrams/nuclear-reactor-layout.svg" "2x2 nuclear reactor layout with heat pipes, heat exchangers, and steam turbines" "760" >}}

**Neighbor bonus:** Each adjacent reactor adds +100% heat output. A 2×2 gives:
- Corner reactors: +100% (1 neighbor) = 80 MW each
- Center reactors: +300% (2 neighbors) = 160 MW each
- Total: 480 MW from 4 reactors at 72 fuel cells/hour

**Component counts for 2×2:**
| Component | Count | Notes |
|-----------|:-----:|-------|
| Nuclear reactors | 4 | 2×2 arrangement |
| Heat exchangers | 48 | 12 per reactor |
| Steam turbines | 84 | 21 per reactor |
| Offshore pumps | 4 | 1 per 12 exchangers |
| Fuel cells/hr | 72 | 18 per reactor |

{{< section "Heat Pipe Physics" >}}

Heat moves through heat pipes similarly to fluids but with two key rules:

1. **Max distance:** Heat travels about 16 tiles from a reactor before significant dropoff
2. **Max load:** Each heat pipe segment can carry heat for up to 4 heat exchangers

**Design rules:**
- Keep heat pipes within 20 tiles of the reactor
- Run double heat pipes for 2+ reactor wide setups
- Place heat exchangers on both sides of the heat pipe
- More heat pipes = more capacity, not more range

For a 2×2 reactor, run a thick heat pipe line (3-5 parallel pipes) from the reactor block to the exchanger array.

{{< section "Fuel Efficiency Comparison" >}}

| Setup | Reactors | Cells/hr | Total MW | MW per cell | Space |
|-------|:--------:|:--------:|:--------:|:-----------:|:-----:|
| 1×1 | 1 | 18 | 40 | 2.22 MW | Small |
| 2×1 | 2 | 36 | 160 | 4.44 MW | Compact |
| 2×2 | 4 | 72 | 480 | 6.67 MW | Standard |
| 2×3 | 6 | 108 | 800 | 7.41 MW | Wide |
| 2×4 | 8 | 144 | 1,120 | 7.78 MW | Very wide |

The neighbor bonus makes larger setups wildly more efficient. A 2×4 produces 7× the power of four 1×1 reactors but uses the same fuel.

{{< section "Kovarex Enrichment — The Game Changer" >}}

Without Kovarex, you need centrifuge processing to get U-235 — and the 0.7% rate makes expansion painful.

{{< recipe name1="uranium_235" qty1="40x" name2="uranium_238" qty2="5x" result="uranium_235" rqty="41x" >}}

**What this does:** Each cycle consumes 5 U-238 and produces 1 net U-235. After bootstrapping with 40 U-235, Kovarex runs indefinitely, producing enough fuel for any size reactor.

**Bootstrapping:** You need 40 U-235 to start Kovarex. That's about 6,000 uranium ore without productivity modules. Stockpile U-235 while running the reactor manually or supplement with solar/steam.

{{< callout "warning" >}}
**Don't circuit-control fuel insertion without a plan.** If you insert fuel only when steam is low, you save fuel — but a power spike when steam tanks are empty can crash your base. Use at least 50 steam tanks as buffer.
{{< /callout >}}

{{< section "Steam Storage Strategy" >}}

Each steam tank holds 25,000 units of steam (2.425 GJ). With 200-second fuel burn cycles:

- **Buffer size:** 20 tanks store enough steam for ~5 minutes at 480 MW full load
- **Circuit control:** Connect a tank to a decider combinator. Insert fuel when steam < 10,000. This reduces fuel consumption by 50-80%
- **Turbine layout:** One steam turbine consumes 60 units/s. At max output, 84 turbines consume 5,040 steam/s. 20 tanks provide about 100 seconds of buffer

{{< section "Common Mistakes" >}}

**Not enough water.** One offshore pump feeds 12 heat exchangers. A 2×2 needs 4 dedicated offshore pumps. Running multiple exchangers off one pump causes steam starvation.

**Heat pipe too long.** Past ~16 tiles from the reactor, heat transfer drops significantly. For 2×2 layouts, run heat pipes in parallel (3-5 width) rather than single-file.

**Overproducing fuel cells.** A 2×2 burns 72 cells per hour. One assembler with speed modules running for 5 minutes produces enough fuel cells for hours of operation. Don't build four assemblers.

**Ignoring neighbor bonus.** A 2×2 using 4 cells/cycle produces 480 MW. Four standalone reactors produce 160 MW with the same fuel. Touching reactors matters.

{{< section "Scaling Past 1 GW" >}}

For larger bases, use tileable 2×N reactor rows:

- Each additional pair of reactors adds 160 MW
- A 2×8 setup produces 2,240 MW — enough for a full megabase
- Use a dedicated train station for uranium ore delivery
- Multiple centrifuges with Kovarex produce enough U-235 for any scale

{{< section "Bottom Line" >}}

Nuclear power is the most space-efficient power source in Factorio. A 2×2 reactor at 480 MW is the ideal first build — big enough to power a megabase but simple enough to build in an afternoon.

**Numbers to remember:**
- 2×2 = 480 MW, 48 heat exchangers, 84 turbines, 4 pumps
- 72 fuel cells per hour until Kovarex, then effectively infinite
- Heat pipes max out at ~16 tiles — plan your exchanger placement
- 20 steam tanks + circuit control = 80% fuel savings

**Related:** [Main Bus Guide]({{< ref "/base-design/main-bus-guide" >}}) — routing all that nuclear power through your base, [Oil Processing Guide]({{< ref "/production-ratios/oil-processing-guide" >}}) — fuel chain before nuclear.
