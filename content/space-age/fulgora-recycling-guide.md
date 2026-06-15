---
title: "Factorio Fulgora Guide - Scrap Recycling, Holmium and Lightning Power"
description: "Fulgora guide for Factorio Space Age: scrap recycling sorter design, holmium processing, lightning power collection, and the recycler loop that does not deadlock."
date: 2026-05-21
tags: ["space-age", "fulgora"]
draft: false

---

You landed on Fulgora, set up a recycler feeding scrap, and within 10 minutes your belts are completely jammed with 12 different items. Random outputs from scrap recycling mean you can't predict what comes out -- but you have to plan for everything that does. If even one item type has no output path, the entire system stops.

{{< callout "tip" >}}
**TL;DR:** Each recycled scrap item needs a dedicated output path -- either to a storage chest, an assembler that uses it, or a recycler that voids it. A sushi belt + filter splitter system handles the sorting. Holmium ore goes to processing, everything else gets used or destroyed.
{{< /callout >}}

## The Mechanics Behind This Bottleneck

Fulgora replaces mining with scrap recycling. One scrap recycler produces a random selection from this pool:

| Material | Weight | Primary use |
|:---------|:------:|:-----------|
| Iron gear | Common | Mall items, steel recycling |
| Ice | Common | Water → steam → power |
| Concrete | Common | Foundations, walls |
| Iron plate | Common | General construction |
| Copper plate | Common | General construction |
| Steel plate | Uncommon | Advanced items |
| Battery | Uncommon | Accumulators, science |
| Blue circuit | Uncommon | Science, modules |
| Holmium ore | Rare | **Science, modules -- the reason you're on Fulgora** |
| Solid fuel | Common | Boiler fuel |
| Stone | Common | Walls, rails |

Every item type needs a place to go. If blue circuits pile up and have no consumer, the belt backs up, the recycler stalls, and you stop getting holmium ore.

## The Proven Fix -- Sushi Belt + Filter Splitter Sorting

**Stage 1 -- The scrap processing line.**
Place recyclers in a row. Each feeds into a red belt running below. This belt carries all output items -- it's your "sushi belt".

**Stage 2 -- Filter splitters.**
After the recycler row, add one filter splitter per item type. Each splitter filters one material onto a dedicated belt:

1. First splitter: filter Holmium Ore → dedicated belt to processing
2. Second: Blue Circuits → requester chest (feed mall)
3. Third: Batteries → requester chest
4. Fourth: Steel → requester chest or recycler void
5. Fifth: Iron/Copper → dedicated storage (you'll use them)
6. Remaining on sushi belt: concrete, stone, ice, solid fuel → recyclers for voiding

{{< diagram "diagrams/fulgora-scrap-sorter.svg" "Fulgora scrap sorting sushi belt with filter splitters and dedicated output belts" "760" >}}

**Stage 3 -- Voiding excess.**
The items you can't use (excess concrete, stone, gears) need to disappear. Route them to a recycler loop: recycler → belt → recycler → belt → ... until items are destroyed. Each recycler reduces items by 75% per pass, so 3 recyclers in series gets rid of anything.

{{< callout type="info" >}}
**Quick Tip:** Don't store items you don't need. I tried buffer chests for everything. Turns out you get copper, iron, and gears way faster than you can use them. A buffer of 4 steel chests per item type is more than enough -- route everything else to the void recycler.
{{< /callout >}}

## The Holmium Processing Chain

Holmium ore is the reason you're on Fulgora. The processing chain:

1. Holmium ore → Holmium plate (needs sulfuric acid)
2. Holmium plate → Electromagnetic science (with other ingredients)
3. Holmium plate → Superconductor (for quality modules)

**The ratio:** 1 scrap recycler produces roughly 0.3 holmium ore per second with average luck. One electromagnetic science assembler needs about 2.5 ore/second. That means ~8 scrap recyclers running constantly for every 1 science assembler.

Scale accordingly: 40 recyclers → 5 science assemblers → 60 SPM of electromagnetic science.

{{< callout type="info" >}}
**Quick Tip for Min-Maxers:** Holmium plate processing uses sulfuric acid. Bring it from Nauvis in barrels until you have a reliable iron supply on Fulgora -- or you'll be running back and forth.
{{< /callout >}}

## Power -- Lighting Into Electricity

Lightning strikes metal objects on Fulgora. Lightning rods capture this and turn it into electricity.

**Power setup:**
- 1 lightning rod covers a ~20 tile radius
- Connect rods directly to accumulators (no power poles needed in the rod-to-accumulator path)
- Lightning strikes are periodic, so build at least 50 accumulators per 10 rods
- A single heavy lightning storm charges 50 accumulators in roughly 10 seconds

**The math:** Each rod produces ~1.5 MW during a strike. 10 rods + 100 accumulators provides continuous 5-8 MW -- enough for a mid-size base. For megabase scale, build separate rod banks across islands and wire them together.

{{< callout type="warning" >}}
**Traps People Keep Falling Into:** Power poles on Fulgora attract lightning. If you run power lines across open ground between buildings, lightning will destroy them. Solution: run power under the metal foundation tiles. Foundation acts as a lightning shield -- pipes and wires beneath it are safe.
{{< /callout >}}

## Where Most Players Mess This Up

**Sushi belt too short.** If the sushi belt doesn't have enough room for all filter splitters, some item types never get filtered and pile up in the recyclers. Make the belt long enough for one splitter per item type.

**No ice void path.** Ice melts into water. Water creates steam. Steam runs turbines. This sounds great until your steam tanks are full and ice is still piling up -- stalling the recycling. Always route excess ice to a recycler after your steam tanks are full.

**Scrap islands run out.** A full scrap patch on a large island lasts ~50 hours. Medium patches last 15-20 hours. Place your recycler grid centrally and extend belts to new scrap patches as old ones deplete.

---

## Community Verification & Resources

- [Official Wiki -- Fulgora](https://wiki.factorio.com/Fulgora) -- scrap recycling weights, holmium processing ratios, lightning mechanics
- [Factorio Forums -- Fulgora Design Thread](https://forums.factorio.com/viewforum.php?f=69) -- community sorting designs and power grid layouts
- [Reddit -- Fulgora Science Builds](https://www.reddit.com/r/factorio/) -- sushi belt designs and compact holmium processing layouts

**Related:** [Gleba Survival Guide]({{< ref "/space-age/gleba-survival-guide" >}}) | [Space Platform Guide]({{< ref "/space-age/space-platform-guide" >}})
