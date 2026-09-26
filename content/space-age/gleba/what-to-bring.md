---
title: "Factorio Gleba What to Bring - First Landing Checklist"
description: "Everything to load into your first rocket to Gleba in Factorio Space Age, plus what never to bring. Landing pad loadout, biome selection, power plan and the first 60 minutes build order."
date: 2026-09-26
lastmod: 2026-09-26T00:20:00+08:00
tags: ["space-age", "gleba", "planets"]
draft: false
---

{{< callout "tip" >}}
**Short answer: bring landfill, iron and copper plates, lubricant/plastic, and guns.** Gleba has **no crude oil**, its metals come from **bacteria cultivation** (not mining drills), and most of its surface is marsh you cannot build on. Everything else - fruit, seeds, stone, water, coal - you make on-planet. Do **not** bring food stockpiles: every biological item carries a spoilage timer that starts the moment it is crafted.
{{< /callout >}}

Gleba is the planet that punishes players who land unprepared, because almost nothing works the way it does on Nauvis. There are no drillable ore patches. There is no crude oil. Half the map is standing water. And every item you produce is quietly rotting.

{{< section "Why Gleba Breaks Standard Landing Habits" />}}

The core problem: **the standard "bring machines, mine locally" loop does not exist here.** Your first hour depends entirely on a biological chain that takes time to spin up.

| Resource | Available locally? | How you get it | Landing consequence |
|:---------|:-------------------|:---------------|:--------------------|
| {{<material "iron_plate">}} Iron | Indirect | {{<material "nutrients">}} Iron bacteria cultivation in a biochamber | Need imported plates to bootstrap |
| {{<material "copper_plate">}} Copper | Indirect | Copper bacteria cultivation in a biochamber | Same bootstrap gap |
| {{<material "crude_oil">}} Crude oil | **No** | Replaced by bioplastic / biosulfur / biolubricant | Bring processed oil products |
| {{<material "coal">}} Coal | Indirect | Coal synthesis | Do not plan around boilers |
| {{<material "stone">}} Stone | Yes | Mine patches in the dark highlands biome | Only mineable far from the marsh |
| {{<material "water">}} Water | Yes | {{<material "offshore-pump">}} Offshore pump | Trivial, do not waste cargo space |
| {{<material "nutrients">}} Nutrients | Yes | Mash from {{<material "yumako">}} yumako / {{<material "jellynut">}} jellynut fruit | Spoils in 5 minutes |
| {{<material "lubricant">}} Lubricant | Indirect | Biolubricant recipe | Bring barrels to start |

Note the pattern: **you can make everything eventually, but not in the first 20 minutes.** That gap is exactly what your rocket payload has to cover.

If you are still deciding whether Gleba is even the right second planet, check {{< ref "/space-age/guide/planet-order-guide" >}} before you commit the launch - Aquilo later reuses the heating technology you build here, but Gleba is not mandatory as your first stop.

{{< section "The Loadout: What Actually Goes In The Rocket" />}}

{{< diagram "diagrams/space-age/gleba-landing-checklist.svg" "Gleba landing checklist showing what to bring versus what not to bring in the first cargo rocket" "760" >}}

**The full list, in priority order:**

| Item | Quantity (one person) | Why it is irreplaceable |
|:-----|:----------------------|:------------------------|
| {{<material "stone_brick">}} Landfill | 2000+ | The marsh cannot be built on at all |
| {{<material "iron_plate">}} Iron plates | 4000 | Covers you until bacteria cultivation runs |
| {{<material "copper_plate">}} Copper plates | 2000 | Same bootstrap window |
| {{<material "lubricant">}} Lubricant barrels | 50 | No crude oil means no lubricant refinery |
| {{<material "plastic_bar">}} Plastic bars | 500 | Before the bioplastic line exists |
| {{<material "gun_turret">}} Gun turrets | 20 | Pentapods arrive fast once spores spread |
| {{<material "piercing_rounds">}} Piercing rounds | 1000 | Cheap insurance, stacks well |
| {{<material "transport_belt">}} Belts, inserters, assemblers | Full kit | You cannot build a factory without a build kit |
| {{<material "electric_furnace">}} Power poles and substations | Several hundred | The most commonly forgotten item on the list |
| {{<material "heating-tower">}} Heating tower | 2 | Power generation and later the Aquilo prerequisite |

**Landfill deserves special emphasis.** Gleba's lowlands are shallow water tiles with a marbled, unbuildable surface. Your landing pad itself is fine, but the moment you want to expand outward you either find elevated terrain or pour landfill. Bring more than you think you need.

{{< section "What You Must Never Bring" />}}

| Item | Why it is a mistake |
|:-----|:--------------------|
| {{<material "yumako">}} Yumako / {{<material "jellynut">}} jellynut fruit | Grows everywhere, spoils while sitting in a chest |
| Seeds | Harvested from trees you have not even planted yet |
| {{<material "stone">}} Stone | Mineable in the highlands, just walk there |
| {{<material "coal">}} Coal | Coal synthesis covers it once power is stable |
| {{<material "solar_panel">}} Solar-only plans | Surface solar output is only **50%** here |
| Large buffer stockpiles of anything biological | Buffering does not work - spoilage timers beat you |

This is the single biggest mental adjustment: **throughput beats storage on Gleba.** On Nauvis you can buffer 10,000 iron plates and forget about it. On Gleba, {{<material "nutrients">}} nutrients have a five-minute spoil window, so anything you stockpile turns into {{<material "spoilage">}} spoilage inside the container. When that eventually jams you, {{< ref "/space-age/gleba/spoilage-backup" >}} walks through clearing a backed-up line without tearing the whole block down.

{{< section "Choosing Your Landing Site" />}}

Pick where you drop the {{<material "cargo_landing_pad">}} cargo landing pad before you commit the launch - relocating later is expensive.

**The three biome rules:**

1. **Red and green marshlands** are where {{<material "jellynut">}} jellystem and {{<material "yumako">}} yumako trees grow. You need both.
2. **Dark highlands** hold the {{<material "stone">}} stone patches and sit above the water line, so they are directly buildable.
3. **Pentapod nests only form on shallow water tiles** - so highlands and midlands act as natural walls against expansion.

The trick most players miss: **land on a highland/midland shelf wedged against both food biomes.** You get buildable ground, stone access, food adjacency, and the water being between you and nest expansion instead of around you. You can push the enemy back further later by landfilling the shallow water they would otherwise use.

{{< section "First 60 Minutes: The Build Order" />}}

{{< diagram "diagrams/space-age/gleba-first-hour.svg" "Gleba first hour build order from power and farms through nutrients and bacteria cultivation to first agricultural science" "760" >}}

1. **Power first.** Drop a {{<material "heating-tower">}} heating tower, attach a {{<material "heat_exchanger">}} heat exchanger and steam turbine pair. This also unlocks the heating technology you will need before Aquilo.
2. **Farms second.** {{<material "agricultural_tower">}} Agricultural towers onto the fertile soil tiles surrounding wild trees. Do not place them on random marsh.
3. **Nutrients third.** Fruit into mash into nutrients, headed straight into biochambers. Keep the line short - this is where the 5-minute timer bites.
4. **Bacteria fourth.** Iron and copper bacteria cultivation inside biochambers. Only now does your metal supply become local.
5. **Spoilage sink fifth.** Route {{<material "spoilage">}} spoilage into a {{<material "recycler">}} recycler or burn it. Without a sink, one stalled machine backfills the whole line.
6. **Defense sixth.** Turrets on the side facing the marsh, because that is the only direction attacks come from. The perimeter layouts in {{< ref "/space-age/gleba/pentapod-defense" >}} assume exactly this geometry, so build to match it rather than boxing yourself in.
7. **Science seventh.** {{<material "agri-science">}} Agricultural science packs can only be crafted on Gleba, so this is your export product.

Once you are past step 4 you are self-sustaining, and the imported plates stop mattering. Most failed Gleba runs fail somewhere between step 2 and step 4, because the chain stalls and everything rots.

{{< section "Power Reality Check" />}}

{{<material "solar_panel">}} Solar panels produce at **50% effectiveness** on the Gleba surface, which makes them a supplement rather than a solution. The real chain is:

| Stage | Source | Notes |
|:------|:-------|:------|
| Ignition | {{<material "heating-tower">}} Heating tower burning local scrap | Cheap, needs a manual top-up early |
| Steady state | Heat exchanger plus turbine pair | Requires water from an offshore pump |
| Scaled | {{<material "rocket-fuel">}} Rocket fuel made from jelly | Gleba generates rocket fuel renewably |

Gleba is one of the best power planets in the game **once running** - it just has an awkward startup window. Your imported material should buy you through that window, nothing more.

{{< section "Common Mistakes" />}}

| Mistake | What happens |
|:--------|:-------------|
| Landing without landfill | You are boxed in by marsh in every direction |
| Buffering nutrients | They spoil inside the chest before you use them |
| Building before picking a biome | You end up relocating the pad and losing the launch |
| Assuming you can drill for ore | There is nothing to drill; it is bacteria or imports |
| No spoilage sink at scale | A single stall backfills the entire production line |
| Ignoring spores | {{<material "pentapod_egg">}} Pentapods are drawn to biological output, not pollution |

Past the first hour the pressure shifts from setup to survival. Pentapod waves scale with your biological output rather than pollution, so the base you just built starts drawing attacks precisely because it is working. {{< ref "/space-age/gleba/gleba-survival-guide" >}} covers keeping that base intact once the waves arrive, which is the point where most first landings actually collapse.

{{< section "Community Verification and Resources" />}}

- [Factorio Wiki: Gleba](https://wiki.factorio.com/Gleba) - biome properties, resource restrictions and spoil timers
- [Reddit r/factorio](https://www.reddit.com/r/factorio/) - player-reported landing loadouts and first-hour routes

*Last updated: 2026-09-26 | Verified against Factorio 2.0 / Space Age.*
