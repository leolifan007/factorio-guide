---
title: "Factorio Main Bus Guide - Standard Base Layout Explained"
description: "How to build a main bus in Factorio, including bus width, lane allocation, balancers, and the exact layout that carries you through blue science without bottlenecks."
date: 2026-05-18
lastmod: 2026-06-15T13:44:00+08:00
tags: ["base-design", "main-bus", "beginner"]
draft: false
---

Your base is spaghetti. Belts cross each other in six directions, nothing reaches the right assembler, and you've spent 2 hours chasing iron plates across the map. Every Factorio player builds spaghetti at first. The main bus is the upgrade that fixes it. Here's the exact bus layout I use -- 4 belts of iron, 4 of copper, with space for everything.

{{< callout "tip" >}}
**TL;DR:** Run 4 lanes of iron, 4 of copper, 2 of steel, 2 of green circuits, 1 of plastic, 1 of coal, 1 of stone/brick, 1 of batteries, 2 of red/blue circuits. Leave 4 tiles between each group of 4 belts. Branch off with splitters, never steal from the bus directly. Carry fluids via underground pipes parallel to the bus. This layout scales to rocket launch without rework.
{{< /callout >}}

## What a Main Bus Is

A main bus is a set of parallel belt lanes carrying the most common materials through your factory. Production units branch off the bus on one side (or both), use what they need, and output finished goods. The bus never stops -- it flows from the furnace column at the start to the science pack assembly at the end.

The alternative is a spaghetti base where you weave belts between assemblers and tear half of it down every time you need a new product. I rebuilt my first factory three times before switching to a bus. The fourth time, I stopped rebuilding and just extended the bus.

## The Bus Width -- How Many Lanes

The standard bus uses 4 lanes of iron and 4 of copper because these are the most consumed materials by volume. After hundreds of hours across multiple playthroughs, I've settled on this allocation:

| Material | Lanes | Why this many |
|:---------|:-----:|:--------------|
| Iron plate | 4 | Most-used material in the game |
| Copper plate | 4 | Green circuits eat copper faster than anything |
| Steel plate | 2 | Used in engines, rails, and furnaces |
| Green circuit | 2 | Consumed by everything mid-game |
| Plastic | 1 | Red circuits and LDS |
| Coal | 1 | Plastic, grenades, power |
| Stone/Brick | 1 | Walls, furnaces, rails |
| Batteries | 1 | Accumulators, flying robot frames |
| Red circuit | 1 | Blue science, modules |
| Blue circuit | 1 | Yellow science, rockets |
| Sulfur | 1 (pipe) | Blue science, red circuits |

Total: 18 belt lanes + 1 fluid pipe. That sounds like a lot, but each lane only takes 2 tiles of space.

{{< callout type="info" >}}
**Quick Tip:** Leave at least 4 tiles between every 4 lanes. This gap becomes your walkway and your underground belt crossing zone. I use this space for splitters that tap off the bus. Without the gap, you can't fit the splitters.
{{< /callout >}}

## The Layout -- Start to End

The bus flows in one direction: from raw materials to science packs. Build in this order:

1. **Furnace column** at the start. 24 stone furnaces per iron lane, 24 per copper lane. Steel column next to iron (needs iron plates).
2. **Main bus** running straight from the furnace column. Belts organized by usage volume: iron left-most, then copper, then circuits.
3. **Production branches** on one side of the bus. Each branch pulls via a splitter, uses a few materials, outputs a finished product back to the other side.

The critical rule I broke my first time: **pull from the bus with splitters, never direct inserters.** If you put an inserter from the bus into an assembler, that lane is now blocked. A splitter leaves the lane intact and only pulls what you need.

Build production units on one side of the bus only. Leave the other side for expansion. When I needed more green circuit production, I had room to add 10 more assembling machines without touching anything on the bus. If both sides are built up, you can't expand without deconstructing.

## Balancers -- Why You Need Them

A bus without balancers will empty on one lane while the other is full. Splitters don't balance lane utilization. A 4-lane iron bus with no balancers runs unevenly -- the first consumer drains lane 1, the next drains lane 2, and by the time you reach science packs, only lane 4 has iron.

Where to place balancers:

| Position | Balancer type | Purpose |
|:---------|:-------------|:--------|
| After furnace column | 4-to-4 lane balancer | Distribute fresh ore evenly |
| After each major consumer | 4-to-4 lane balancer | Redistribute after circuit/steel production |
| Before science pack line | 4-to-4 lane balancer | Ensure science section gets even supply |
| At bus end | 4-to-4 lane balancer | Catch remaining materials for overflow |

The balancer design: four splitters in a 2x2 grid with underground belts crossing. Copy this from a blueprint book once, paste at each balance point. I have 4 balance points on my bus: after furnaces, after green circuits, after steel, before science.

## End-of-Bus Management

The bus eventually ends. What do you do with leftover materials on belts that have nothing to consume?

**Option 1 -- Chest collection.** Place a steel chest at the end of each bus lane with a fast inserter. The chest collects overflow. This gives you a free stack of materials whenever you need to build by hand.

**Option 2 -- Circuit-based overflow control.** Connect the chest to a decider combinator. If chest iron exceeds 2,000, enable an inserter that feeds into a requester chest or recycling array. This prevents belt full-block -- when a full belt stalls the furnace column behind it.

I use option 1 for my main lanes and option 2 for circuits (which block the fastest).

{{< callout "warning" >}}
The biggest bus mistake I see beginners make: putting science pack production BEFORE the bus end. Science packs are the final product. They should be the last thing on the bus. If you place them in the middle, lanes running past them create wasted throughput. I moved my entire science section from the middle of the bus to the end and production jumped by 30%.
{{< /callout >}}

## Scaling Past the Bus

The main bus works well for a 60-SPM starter base. Beyond that, you'll hit belt throughput limits. The transition to city blocks or train-based megabase starts at the same location: the furnace column gets replaced by off-site smelting delivered by train. The bus stays as your starter base while the train network expands outward.

When I outgrew my 4-lane bus, I kept it as the mall (building production) and built a separate train-fed smelting yard for science packs. The bus still feeds assembler, belt, and inserter production -- things you need constantly but don't need at megabase scale.

---

## Community Verification & Resources

- [Official Factorio Wiki -- Main Bus](https://wiki.factorio.com/Guide:Main_bus) -- official guide with bus layouts, lane counting, and common variants
- [Reddit -- Bus Design Discussion](https://www.reddit.com/r/factorio/) -- community bus builds, lane allocation debates, and balancer blueprints
- [Factorio Prints -- Bus Balancers](https://factorioprints.com/) -- pre-built 4-to-4 and 8-to-8 belt balancers

**Related:** [Your First Factory]({{< ref "/getting-started/your-first-factory" >}}) | [City Block Guide]({{< ref "/base-design/city-block-guide" >}}) | [Smelting Ratios]({{< ref "/production-ratios/smelting-ratios" >}})
