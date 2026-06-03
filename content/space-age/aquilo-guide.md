---
title: "Aquilo 閳?The Frozen Planet Survival and Research Guide"
description: "Aquilo guide for Factorio Space Age. Ice power mechanics, heat management systems, lithium supply chains, cryogenic science packs, and the strategy that keeps your base alive on the coldest planet."
date: 2026-05-23
lastmod: 2026-06-03T22:51:00+08:00
publishDate: 2026-06-16T00:00:00+08:00
tags: ["space-age", "aquilo", "space-platform"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

Aquilo is where Factorio stops being a factory game and starts being a survival game. {{< material "solar_panel" >}} Solar panels produce nothing here. Steam engines freeze solid. Roboports go dark. Every building is either generating heat or dying of cold.

{{< callout "tip" >}}
**TL;DR:** Burn ice in smelters for heat + steam 閳?turbine = electricity. Heat pipes radiate warmth to every building. Lithium is scarce 閳?import from Gleba. Build only what Aquilo uniquely provides: cryogenic science packs.
{{< /callout >}}

{{< diagram "diagrams/aquilo-ice-power.svg" "Aquilo ice power system 閳?burner drill, ice smelter heat array, steam turbine, and heat pipe network" "900" >}}

## Ice Is Your Power Grid

Ice is Aquilo's primary resource and its entire power infrastructure. You mine it, burn it, and convert the heat into both warmth and electricity.

| Step | Building | Output |
|------|----------|--------|
| Mine ice | Burner mining drill | Ice chunks |
| Burn ice | Electric smelter (array) | Heat + steam |
| Generate power | Steam turbine | ~500 kW per 4 smelters |
| Distribute heat | Heat pipe network | Keeps buildings above freezing |

**The math:** 1 ice-burning smelter produces ~125 kW of usable power (after 25% turbine efficiency). A 4-smelter heat plant powers a small factory at ~500 kW. Scale smelters to match demand.

{{< callout "warning" >}}
**Critical rule:** the heat network must be continuous. Any gap = freeze point. Build 50% extra heat capacity 閳?if one smelter runs dry, the others cover it.
{{< /callout >}}

## The Heating Network

Smelters burning ice radiate heat through heat pipes. Every building on Aquilo needs this:

- {{< material "assembling_machine_3" >}} **Assemblers** 閳?freeze = production stops
- {{< material "roboport" >}} **Roboports** 閳?freeze = logistic network shuts down, bots return to nests
- {{< material "roboport" >}} **Substations** 閳?freeze = power grid flickers
- {{< material "inserter" >}} **Inserters** 閳?freeze = belts back up

Heat pipes transfer warmth 4 tiles per pipe segment. Use underground heat pipes to span large distances. Place your smelter array at the center of your factory for even coverage.

## Lithium: Import It

Lithium is essential for {{< material "battery" >}} batteries, cryogenic science packs, and Quality Module 5 components. Aquilo surface deposits are rare and small 閳?insufficient for sustained production.

**Source: Gleba.** Lithium is a common byproduct in Gleba's bio-processing chain. Export lithium ore via space platform. If you don't have Gleba running yet, mine the pale green surface patches sparingly 閳?you'll need every chunk.

## Cryogenic Science Chain

Aquilo's unique research output:

1. Ice 閳?power the factory (heat plant)
2. Lithium 閳?lithium batteries
3. Battery + ice + advanced circuit 閳?**cryogenic science pack**
4. Research unlocks: Quality Module 5, space platform upgrades, ultimate energy storage

Quality Module 5 is the capstone 閳?+10% base productivity over Module 4 with quality bonuses on top. A rocket silo with 4 QM5s produces 50%+ more rockets per resource than with PM3s.

## What Veterans Learn the Hard Way

- {{< material "solar_panel" >}} **Solar panels are useless here** 閳?they produce power but zero heat. You still need the ice smelter array.
- **Build compact** 閳?every tile of heat pipe costs smelter output. Sprawling layouts = heat distribution nightmare.
- **Import aggressively** 閳?Aquilo is a specialized research facility, not a self-sufficient planet. Import construction bots, nuclear fuel cells, spare parts.
- {{< material "roboport" >}} **Heat roboports directly** 閳?don't rely on proximity to warm buildings. Dedicated heat pipe connections prevent bot network collapse.

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| No heat buffer | One smelter stalls 閳?entire factory freezes |
| Relying on solar for power | Power works, heat doesn't 閳?everything still freezes |
| Mining all local lithium upfront | Depletes stockpile before science chain is stable |
| Spread-out factory layout | Heat can't reach outer buildings 閳?they freeze |

## The Bottom Line

Aquilo demands compact layouts, continuous heat, and imported lithium. The strategy: burn ice for heat first, power second. Import everything possible. Extract cryogenic science and QM5 research. Everything else serves that goal.

---

**Related:** [Vulcanus Guide]({{< ref "/space-age/vulcanus-guide" >}}) | [Space Platform Guide]({{< ref "/space-age/space-platform-guide" >}})