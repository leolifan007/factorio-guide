---
title: "Smelting Ratios - How Many Furnaces Per Belt"
description: "Exact Factorio smelting ratios for iron, copper, and steel. How many stone and electric furnaces fill one belt, the steel ratio almost everyone gets wrong, and a layout that upgrades without rebuilding."
date: 2026-05-18
lastmod: 2026-09-26T15:47:00+08:00
tags: ["production-ratios", "smelting", "belts"]
draft: false
---

{{< callout "tip" >}}
**Short answer:** one full basic belt of ore needs **24 stone furnaces** or **12 electric furnaces** to consume it completely. Fast belt doubles that to 48/24, express belt triples it to 72/36. For steel, the number everyone gets wrong: steel takes **17.5 seconds and 5 iron plates**, so you need roughly **5x more furnace time** than copper - plan a dedicated steel line, never a side output.
{{< /callout >}}

{{< section "The Three Numbers You Need" />}}

Everything in smelting comes down to three rates. Learn these and every ratio below is derivable.

| Item | Rate | Notes |
|:-----|:-----|:------|
| Basic belt | 7.5 items/sec | 15 items/sec per lane |
| Fast belt | 15 items/sec | Double |
| Express belt | 22.5 items/sec | Triple |
| {{<material "stone-furnace">}} Stone furnace | 0.3125 plates/sec | 1 plate per 3.2s |
| {{<material "electric-furnace">}} Electric furnace | 0.625 plates/sec | 1 plate per 1.6s |
| {{<material "steel-furnace">}} Steel furnace | 0.625 plates/sec | Same as electric, no module slots |

An electric furnace is **exactly twice** a stone furnace. That single fact generates the whole table below.

{{< section "Iron and Copper: Furnaces Per Belt" />}}

{{< diagram "diagrams/space-age/smelting-ratio.svg" "Factorio smelting ratio chart showing stone and electric furnace counts needed per belt for iron and copper" "760" >}}

Iron and copper share identical smelting times, so one table covers both.

| Belt Type | Items/sec | Stone Furnaces | Steel Furnaces | Electric Furnaces |
|:----------|:---------:|:--------------:|:--------------:|:-----------------:|
| Basic (half) | 3.75 | 12 | 6 | 6 |
| Basic (full) | 7.5 | **24** | **12** | **12** |
| Fast belt | 15 | 48 | 24 | 24 |
| Express belt | 22.5 | 72 | 36 | 36 |

**The rule of thumb:** one full basic belt of iron ore fits exactly **24 stone furnaces**, or **12 electric furnaces**. Fast belt doubles it, express triples it.

| Belt | Stone | Electric | Space Needed |
|:-----|:-----:|:--------:|:------------:|
| Basic | 24 | 12 | Compact column |
| Fast | 48 | 24 | Split into two columns |
| Express | 72 | 36 | Three columns + balancers |

{{< section "Steel: The Ratio Everyone Gets Wrong" />}}

Steel is where most bases break down. The recipe takes **5 iron plates** and **17.5 seconds** in a stone furnace.

| Setup | Steel/sec per Furnace | Furnaces for Full Belt |
|:------|:---------------------:|:----------------------:|
| Stone furnace | 0.057 | 131 for a basic belt |
| Steel furnace | 0.114 | 65 for a basic belt |
| Electric furnace | 0.114 | 65 for a basic belt |
| Beaconed electric | ~0.5 | 15 for a basic belt |

**Never try to make bulk steel with stone furnaces.** You would need over 130 of them to fill a single belt, which is more than most bases build in total.

| Mistake | Consequence |
|:--------|:------------|
| Steel on a shared iron line | Starves everything downstream |
| Too few steel furnaces | Steel trickles, blocking progression |
| No dedicated steel line | Constant rebuilding |

Give steel its own furnace column fed from an iron plate belt, separate from your main iron smelting.

{{< section "Layout That Upgrades Without Rebuilding" />}}

The single best design decision in Factorio smelting is leaving room to upgrade.

{{< diagram "diagrams/space-age/smelting-column-layout.svg" "Smelting column layout showing ore input, furnace row, and plate output with space for beacon upgrades" "760" >}}

| Design Element | Why It Matters |
|:---------------|:---------------|
| Ore belt down the back | Furnaces pull from one side, output the other |
| Plate belt down the front | Direct feed to bus or train |
| 3-tile gap between columns | Room for beacons later |
| Underground belts at column ends | Prevents belt crossings |

**Leave a 3-tile gap between furnace columns from day one.** Retrofitting beacons into a cramped layout means tearing the whole thing down.

{{< section "Furnace Type Comparison" />}}

| Furnace | Speed | Fuel | Modules | When to Use |
|:--------|:-----:|:-----|:-------:|:------------|
| {{<material "stone-furnace">}} Stone | 0.3125/sec | Any | No | First hour only |
| {{<material "steel-furnace">}} Steel | 0.625/sec | Any | No | Before electric, good upgrade |
| {{<material "electric-furnace">}} Electric | 0.625/sec | Electric | **Yes** | Main line once you have power |
| Beaconed electric | ~2.5/sec | Electric | Yes | Megabase |

Stone furnaces are fine for your first hour. Switch to steel furnaces as soon as you can craft them - it **doubles throughput for free** with the same footprint.

{{< section "Beaconed Smelting (Megabase)" />}}

With speed module 3 in furnaces plus speed beacons:

| Setup | Plates/sec per Furnace | Furnaces Per Half Belt |
|:------|:----------------------:|:----------------------:|
| Unbeaconed electric | 0.625 | 12 |
| 8-beacon electric | ~2.5 | 3 |
| 12-beacon electric | ~3.0 | 2.5 |

Beaconed smelting cuts your furnace count by roughly 75%, which is why megabases use it. See the [beacon and module guide]({{< ref "/production-ratios/beacon-module-guide" >}}) for the layout.

{{< section "Related Guides" />}}

- {{< ref "/base-design/main-bus-guide" >}} - matching bus width to furnace output
- {{< ref "/production-ratios/beacon-module-guide" >}} - beacon layouts for megabase smelting
- {{< ref "/science-packs/red-science-guide" >}} - how many furnaces feed red science

{{< section "Community Verification and Resources" />}}

- [Factorio Wiki: Furnace](https://wiki.factorio.com/Furnace) - official crafting speeds and fuel values
- [Factorio Cheat Sheet](https://factoriocheatsheet.com/) - community-verified ratio tables

*Last updated: 2026-09-26 | Verified against Factorio 2.0.*
