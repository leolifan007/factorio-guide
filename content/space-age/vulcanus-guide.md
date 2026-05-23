---
title: "Vulcanus — The Lava Planet Full Setup Guide"
description: "Vulcanus guide for Factorio Space Age. Foundry mechanics, calcite supply chains, tungsten carbide production, metallurgic science, and the full setup that makes Vulcanus worth the trip."
date: 2026-05-23
lastmod: 2026-05-23T17:54:00+08:00
publishDate: 2026-05-27T11:28:00+08:00
tags: ["space-age", "vulcanus", "production-ratios"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

You land on Vulcanus and your circuits stop working. Your smelting column is glowing red and eating plates faster than it produces them. There's lava everywhere and no water in sight. The local ore patches glow orange — iron and copper, but different somehow. Your Fulgora and Gleba blueprints are useless here. Vulcanus has its own rules.

The foundry is not a furnace. Your existing factory knowledge breaks here. This guide is the exact order of operations to build a functional base on Vulcanus without wasting your first 10 cargo pods on the wrong materials.

{{< callout "tip" >}}
**TL;DR:** Vulcanus replaces smelting with the Foundry. Foundry takes iron ore + calcite → molten iron → steel plate in one building. Calcite is the unique resource from volcanic ash. Build the calcite chain first. Then the Foundry. Then tungsten carbide for the endgame module chain. Vulcanus Demons are cleared with artillery or lasers — walls are optional.
{{< /callout >}}

## Lava, Calderite, and Why Your Existing Factory Breaks Here

Vulcanus is a volcanic planet with three critical differences from Nauvis:
- No water patches — no steam power, no offshore pumps
- No coal patches — no solid fuel chain from coal, no plastic from petroleum gas (wait, petroleum still works, but more on that)
- Iron and copper ore exist but behave differently: ore chunks are surrounded by basalt, and the ore grades vary wildly

The bigger problem: you can't use electric furnaces here. Electric furnaces require electricity, which requires power. On Vulcanus, the primary power sources are nuclear (imported fuel) or the lava itself. But the lava doesn't do what you'd expect — you can't pump lava into a boiler.

The actual power solution: bring nuclear fuel cells from Nauvis. Vulcanus has no uranium ore. Every nuclear fuel cell you burn here is imported. Plan accordingly.

## The Foundry: Making Steel Without Iron Ore

The Foundry is the defining building of Vulcanus. It is not a smelter. It is a complete metal processing facility in one tile.

The Foundry takes three inputs:
- Ore (iron ore, copper ore, or iron ore for steel)
- Calcite (the unique Vulcanus reagent)
- Molten metal from the other output of the Foundry

The recipe system is circular: you need molten copper to process iron ore, and you need molten iron to process copper ore. This circular dependency is why the Foundry is confusing on first read.

**The basic Foundry cycle:**
1. Iron ore + calcite → molten iron + volcanic ash
2. Molten iron + calcite → steel plate (if you route it back)
3. Copper ore + molten iron (from step 1) + calcite → molten copper + volcanic ash
4. Molten copper → plates normally

The practical setup:
- 1 Foundry running iron ore → molten iron (feeds steel plate Foundry)
- 2 Foundries running copper ore → molten copper (feeds plates)
- The steel Foundry takes molten iron input from the iron Foundry + calcite

This is why Vulcanus production chains are larger than Nauvis equivalents. The Foundry replaces an entire smelting row + a steel processing plant. The footprint is smaller, but the recipe complexity is higher.

**Calcite: the currency of Vulcanus.**
Every Foundry operation consumes calcite. Calcite comes from volcanic ash — a byproduct of iron and copper ore processing on Vulcanus. When you process ore in the Foundry, you get volcanic ash as output. Ash can be recycled back into calcite through a processing step.

The calcite loop: volcanic ash → calcite (via Foundry processing). The net calcite consumption per ton of metal is low, but you need a dedicated calcite recycling line to avoid running dry.

## Metal Mining Here Changes Everything

Vulcanus iron and copper ore patches are different from Nauvis:
- Ore density is higher per tile (more ore per mining drill)
- Ore patches are surrounded by basalt (purely cosmetic)
- Mining drills on Vulcanus operate at normal speed but produce higher yield per ore node

The practical advantage: you need fewer mining drills for the same metal output. A Vulcanus iron mining operation can be half the size of an equivalent Nauvis operation.

The practical disadvantage: no water for mining drills. Mining drills on Vulcanus are burner mining drills (not electric). This means: they run on coal, coke, or wood. Coke is the Vulcanus fuel of choice — made from processing coal (imported or from Nauvis) or from heavy oil via solid fuel chain.

**Coke production on Vulcanus:**
- Import coal from Nauvis via space platform
- Or: crude oil → heavy oil → solid fuel → coke (from solid fuel processing)
- Burner drills run on coke indefinitely

The mining + coke loop is self-sufficient once established. You don't need to keep importing fuel if you have a crude oil processing setup.

## Tungsten Carbide — the New High-Tier Module

Tungsten carbide is the Vulcanus unique material used to manufacture Productivity Module 4 and Speed Module 4 (the highest tier in the game). This is the endgame production chain that justifies the Vulcanus trip.

**Tungsten carbide recipe:**
- 5 tungsten ore + 5 iron plate + 5 coke → 1 tungsten carbide
- Crafted in an assembling machine (not a Foundry)

**Tungsten ore:** unique to Vulcanus. Rare patches scattered across the map. You'll need asteroid mining to supplement surface deposits for long-term production.

**Module 4 production:**
- Productivity Module 4 = 5 tungsten carbide + 5 productivity module 3 + 5 advanced circuit → 1 productivity module 4
- Speed Module 4 = 5 tungsten carbide + 5 speed module 3 + 5 advanced circuit → 1 speed module 4
- These replace module 3s in your late-game beacon arrays

The key advantage of module 4 over module 3: 30% productivity (vs 10% for mod 3) for productivity modules. This is a 3x improvement in rare resource efficiency. A rocket silo with 4 Productivity Module 4s produces 30% more rockets per resource than with mod 3s.

## The Locomotive Problem and How to Solve It

Vulcanus has no water. Steam locomotives are useless. You need one of:
- Nuclear fuel cells (imported from Nauvis)
-iesel fuel from oil processing (works on Vulcanus)
- Battery power (imported lithium batteries from Aquilo)

The practical answer for most players: nuclear. Bring fuel cells. Run a small nuclear plant on Vulcanus (1-2 reactors). The reactors are for the trains and the factory — not the main power, just the locomotion.

The train network on Vulcanus runs on nuclear fuel cells and imported diesel. You need a Vulcanus-specific train fleet because steam doesn't work.

**The Vulcanus train schedule:**
- Pick up: calcite / tungsten ore / metallurgic science packs
- Deliver to: space platform pad
- Import: nuclear fuel cells / construction bots / backup calcite

## Demons: The Unique Enemy of Vulcanus

Vulcanus has no traditional biters. Instead, there are Demons — flying enemies that spawn from lava vents. They are:
- Fast: faster than spitters
- Fragile: one laser turret kills them quickly
- Annoying: they target anything, including construction bots mid-build

Demons do not expand like biters. They are a fixed population around lava vents. Clear the vents in your build area with artillery or laser turrets, and the area stays clear.

The lazy solution: landfill the lava vents. Fill them with stone or concrete. Demons can't spawn without vents. One landfill + one concrete tile = permanent demon-free zone.

The active solution: laser turrets wired to a power switch. When power is available, lasers fire. Simple, effective, zero maintenance.

## What Gleba and Fulgora Forgot to Tell You

Vulcanus is the supply chain planet. Fulgora handles recyclables. Gleba handles biology. Vulcanus handles the metallurgic backbone that both of those planets need.

**The Vulcanus export priority:**
1. Tungsten carbide (for module 4 production — highest value)
2. Metallurgic science packs (required for advanced research)
3. Calcite surplus (Calcite is also needed on Gleba for bioflux production)

Import priority:
1. Nuclear fuel cells (unless you have local uranium — you don't)
2. Construction bots (vulcanus construction is brutal without bots)
3. Backup calcite (until your own recycling loop is established)

## The Calcite Chain: The Foundation of Everything

The most common failure mode on Vulcanus: calcite starvation. The Foundry stops because no calcite is available. This cascades: no steel plates → no advanced circuits → no science.

**The calcite setup that works:**
1. Build 2 Foundry units dedicated to calcite production: process volcanic ash → calcite
2. Buffer 500 calcite in a storage chest
3. Route calcite to all other Foundry inputs
4. Check the buffer every 10 minutes until the loop is stable

The volcanic ash byproduct from ore processing should nearly cover your calcite demand. "Nearly" is doing a lot of work here — the first time you run a Foundry without enough calcite backup, the entire chain halts.

## The Vulcanus Research Unlock Order

The research tree on Vulcanus is separate from Nauvis science. The order:
1. Metallurgic science pack 1 (requires basic foundry products)
2. Foundry efficiency upgrades (reduces calcite consumption per plate)
3. Metallurgic science pack 2 (requires tungsten carbide — wait for this)
4. Tungsten carbide technology (unlocks module 4 production)
5. Advanced metallurgic science (combines Vulcanus products with Fulgora/Gleba science)

The critical path: get calcite stable → get iron/copper plates → get metallurgic science pack 1 → unlock efficiency upgrades → get tungsten → unlock module 4 → build the endgame production chain.

## The Bottom Line

Vulcanus is the hardest Space Age planet to set up and the most rewarding to optimize. The Foundry is the center of everything — get the calcite loop right and the rest follows. Tungsten carbide is the endgame reward that justifies the trip. Build the calcite chain first, then the Foundries, then the train network, then the tungsten. Everything else is footnotes.
