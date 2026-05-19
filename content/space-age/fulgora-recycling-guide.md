---
title: Fulgora Recycling Guide — Scrap Processing Made Simple
description: Fulgora scrap processing guide for Factorio Space Age. Scrap recycling ratios, sorting strategies, EM Plant setups, island layouts, lightning protection, and holmium production chain.
date: 2026-05-19
tags: ["space-age", "fulgora"]
draft: false
emoji: "⚡"
---

Fulgora breaks every habit you built on Nauvis. The map is ocean islands connected by narrow paths. Lightning strikes anything metallic. And instead of mining ore, you recycle scrap — and get random outputs.

The randomness is the hard part. One recycler run might give you iron gears. The next gives you concrete. The one after that gives you blue circuits. You cannot predict what comes out. You have to plan for every possibility at once.

I have rebuilt my Fulgora base three times. First time I built on an island with no scrap patch and had to rebuild everything. Second time my sorting system backed up and stopped all production. The third approach finally produced consistent holmium throughput.

{{< callout "tip" >}}
**TL;DR:** Recyclers output scrap at roughly 1 stack per second. Each recycler needs a sorting system behind it: filtered splitters for common items, overflow loops for rare items, and circuit-controlled storage for everything. Process scrap where you mine it on the same island. Build a dedicated island for EM Plant production. Lightning rods every 20 tiles on every island.
{{< /callout >}}

{{< section "Scrap Recycling — What Comes Out" >}}

Scrap recycles into random outputs. Here is the approximate distribution per 1000 scrap processed based on my measurements:

| Item | Quantity per 1000 scrap | Approx chance |
|------|:----------------------:|:-------------:|
| Iron gear | 150 | 15% |
| Iron plate | 120 | 12% |
| Copper plate | 100 | 10% |
| Concrete | 80 | 8% |
| Stone | 70 | 7% |
| Battery | 60 | 6% |
| Holmium ore | 50 | 5% |
| Plastic bar | 45 | 4.5% |
| Red circuit | 35 | 3.5% |
| Blue circuit | 25 | 2.5% |
| Processing unit | 15 | 1.5% |
| Ice | 250 | 25% |

The exact percentages vary slightly by game version, but the pattern holds: iron and ice dominate the output. Holmium ore is rare at about 5% per scrap. This means you need a lot of recyclers to get meaningful holmium throughput.

{{< diagram "diagrams/fulgora-scrap-output.svg" "Scrap recycling output distribution chart showing iron gear and ice as highest volume outputs" "700" >}}

{{< section "The Sorting Challenge" >}}

The biggest design problem on Fulgora is not production — it is sorting. Recyclers output random items quickly, and any belt can fill up with one item type while other types stop flowing. When a belt is full of iron gears, the new concrete has nowhere to go.

**The solution: filtered splitter cascades.**

Each recycler feeds into a row of filtered splitters arranged by item priority:
1. First splitter: filter iron gear (highest volume item)
2. Second splitter: filter iron plate
3. Third splitter: filter copper plate
4. Continue down the chain for each item type by volume

Each filtered output goes to a buffer chest. When the chest fills up, the item type backs up on the belt. But the splitter cascade keeps flowing — backed up items overflow to the next filter in the chain automatically.

{{< callout "tip" >}}
If iron gear backs up, it overflows to the iron plate filter. If that backs up too, it overflows to concrete. Eventually everything ends up in a final passive provider chest at the end of the cascade. Nothing stops the recyclers from running.
{{< /callout >}}

Wire each buffer chest to a circuit. When chest contents exceed a threshold, route excess items to additional recyclers for disposal. This prevents the entire system from locking up due to one item type.

{{< section "Holmium Processing — Why You Are Here" >}}

Holmium ore is the reason you travel to Fulgora. It processes into holmium plates, then into supercapacitors and eventually into Electromagnetic Plants.

**Full production chain:**
- 50 holmium ore plus sulfuric acid = 1 holmium plate
- Holmium plate plus copper wire plus plastic = 1 supercapacitor
- Supercapacitor plus circuits plus concrete = 1 EM Plant component

A single EM Plant requires roughly 2000 scrap to be processed. For reference:
- 1 recycler at full speed = about 60 scrap per minute
- 4 recyclers = about 240 scrap per minute
- Holmium plates per minute from 4 recyclers: only 2-3 plates

Scale accordingly. You need at least 12 recyclers for steady holmium plate production. I run 20 recyclers on my main Fulgora base.

{{< recipe name1="holmium_ore" qty1="50x" name2="sulfuric_acid" qty2="10x" result="holmium_plate" rqty="1x" >}}

{{< section "Island Connection Strategy" >}}

Fulgora islands are separated by water. You connect them with elevated rails. Planning your island network is critical.

**Best island setup for Fulgora:**
- Scrap islands: dedicated to recyclers and sorting only (multiple small islands)
- Processing island: one large island for holmium refining and EM Plant assembly
- Science island: a separate island for electromagnetic science production
- Logistics island: rocket silos and cargo hub for interplanetary transport

Build elevated rail bridges between islands. Each bridge segment needs pylons every 15 tiles. Plan your rail routes before building — rebuilding bridges is expensive.

{{< section "Ice and Water Management" >}}

Ice is the most common scrap output at about 25% of all recycling. Managing ice is critical for acid production.

Each recycler outputs roughly 15 ice per minute. For 20 recyclers, that is 300 ice per minute. Ice melts into water in a chemical plant: 20 ice = 200 water. That water feeds your acid production.

**Ice circuit condition:** Wire your ice chest to a decider combinator. If ice exceeds 500, activate an extra chemical plant to melt it. This prevents ice from filling your sorting system and blocking other outputs.

Excess water from ice melting can be vented. Place an extra pipe connected to a pump. Wire the pump to activate when water exceeds 10,000. Vent the overflow into the ocean.

{{< section "Lightning Protection" >}}

Lightning strikes exposed surfaces on Fulgora every few minutes during storms. It damages anything metallic and can destroy power poles, assemblers, and chests instantly.

**Protection rules for each island:**
- Place a lightning rod every 20 tiles in every direction
- Each rod protects a 10-tile radius from its position
- Connect rods to the power grid — they collect free energy from strikes
- All buildings within rod range are immune to lightning

The rod network overlaps by default at 20-tile spacing. I place rods first before any other building on a new island. I learned this the hard way when a single lightning strike took out half my holmium production line.

{{< section "EM Plant Production Block" >}}

The EM Plant is Fulgora signature building. It replaces assemblers for circuit production and is significantly faster than anything on Nauvis.

Build a dedicated island for EM Plant production:
- 6 recyclers feeding into a sorting cascade system
- 2 chemical plants producing acid from ice and sulfur
- 4 holmium plate refineries processing ore into plates
- 2 supercapacitor assemblers making capacitors
- 1 EM Plant assembler for final assembly

Each EM Plant built on Fulgora can be shipped to other planets via rocket. I bring three back to Nauvis for my green circuit lines — they quadruple circuit production compared to assembler 3s.

{{< section "Common Mistakes" >}}

**Building on the wrong island.** Some islands have scrap resource patches, some do not. Scout with radar before building. Build recyclers directly on scrap islands to minimize belt distance between scrap and processing.

**No overflow path for sorting.** If every filter fills up, the recycler stops. Always leave an overflow path to a final chest or secondary recycler loop. Design for the worst case.

**Forgetting ice processing.** Ice is the highest volume scrap output at about 25%. It melts into water. Water goes to acid production. Without enough ice processing capacity, your acid line starves and holmium production stops.

**Not enough recyclers.** Holmium is rare. Underestimating recycler count is the most common Fulgora failure. Build 50% more than your initial estimate. Extra recyclers are cheap compared to a dead base.

**Skipping lightning rods.** One strike during a storm can destroy hours of progress. Rods are cheap. Build them everywhere.

{{< section "FAQ" >}}

**Q: Can I bring scrap to Nauvis for processing?**
A: Yes. Ship scrap via rocket to Nauvis and recycle it there. The sorting challenge is the same, but lightning is not an issue on Nauvis. This is a good option for getting EM Plants without building a large Fulgora base.

**Q: How much holmium do I need for the full tech tree?**
A: About 2000 holmium plates total for all Space Age technologies. That is roughly 8 full stacks of holmium ore.

**Q: What about the Fulgora-specific science pack?**
A: Electromagnetic science uses EM Plant components plus circuits. Build the science assembler on the same island as the EM Plant production block.

**Q: How do I connect islands?**
A: Elevated rails connect islands. Build rail bridges over water between islands. Each bridge needs pylons every 15 tiles.

{{< section "Related Guides" >}}

- [Use quality modules on your recyclers]({{< ref "space-age/quality-module-guide" >}})
- [Transport EM Plants between planets]({{< ref "space-age/space-platform-guide" >}})
- [Automate sorting with circuit networks]({{< ref "blueprints/circuit-network-guide" >}})
- [Design a main bus for Fulgora supply lines]({{< ref "base-design/main-bus-guide" >}})
- [Survive Gleba for bioflux production]({{< ref "space-age/gleba-survival-guide" >}})
