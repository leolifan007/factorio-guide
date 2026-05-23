---
title: "Vulcanus — The Lava Planet Full Setup Guide"
description: "Vulcanus guide for Factorio Space Age. Foundry mechanics, calcite supply chains, tungsten carbide production, metallurgic science, and the full setup that makes Vulcanus worth the trip."
date: 2026-05-23
lastmod: 2026-05-23T19:09:00+08:00
publishDate: 2026-05-27T11:28:00+08:00
tags: ["space-age", "vulcanus", "production-ratios"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

You land on Vulcanus and your smelting knowledge breaks. No water for steam. No coal for solid fuel. The foundry replaces everything you know about metal processing.

{{< callout "tip" >}}
**TL;DR:** The Foundry replaces furnaces — it takes ore + calcite → molten metal → plates in one building. Calcite comes from recycling volcanic ash (ore processing byproduct). Build calcite chain first, then foundries, then tungsten carbide for Module 4.
{{< /callout >}}

{{< diagram "diagrams/foundry-cycle.svg" "Vulcanus foundry circular dependency — iron/steel foundry, copper foundry, and calcite recycling" "820" >}}

## Why Vulcanus Is Different

| Nauvis | Vulcanus |
|--------|----------|
| Water everywhere | **No water** — no steam power |
| Coal patches | **No coal** — import or make coke |
| Electric furnaces | **Foundry** (unique building) |
| Simple ore → plate | Circular: iron feeds copper, copper feeds iron |

Power solution: bring nuclear fuel cells from Nauvis. Vulcanus has no uranium ore.

## The Foundry System

The Foundry is a complete metal processing facility in one 3×3 building. It produces **molten metal** as an intermediate — and the recipes create a circular dependency:

| Foundry Recipe | Input | Output |
|----------------|-------|--------|
| Iron smelting | Iron ore + calcite | Molten iron + volcanic ash |
| Steel making | Molten iron + calcite | Steel plate |
| Copper smelting | Copper ore + **molten iron** + calcite | Molten copper + ash |

**The circular trap:** you need molten iron to process copper ore, but you need the copper foundry running to understand why your iron foundry seems incomplete. Break the cycle by bootstrapping with a small buffer of manually-placed iron plates to start the first copper foundry.

## Calcite: The Currency of Vulcanus

Every Foundry operation consumes calcite. Calcite is made from **volcanic ash** — a byproduct of all ore processing on Vulcanus.

The loop: `ore → foundry → volcanic ash → recycler → calcite → back to foundry`

**This is the #1 failure mode on Vulcanus.** If calcite runs out, every foundry stops. Cascade: no steel → no circuits → no science.

**Reliable calcite setup:**
1. Dedicate 2 Foundries to ash→calcite recycling
2. Buffer **500+ calcite** in a storage chest
3. Route to all other Foundry inputs via bots or belts
4. Monitor buffer until stable

## Tungsten Carbide & Module 4

Tungsten carbide is Vulcanus's endgame product — the key ingredient for Space Age's highest-tier modules:

| Product | Recipe | Value |
|---------|--------|-------|
| Tungsten carbide | 5 tungsten ore + 5 iron plate + 5 coke | Module 4 ingredient |
| Productivity Module 4 | 5 TC + 5 PM3 + 1 advanced circuit | +30% prod (vs PM3's +10%) |
| Speed Module 4 | 5 TC + 5 SM3 + 1 advanced circuit | Higher speed bonus |

**Module 4 vs Module 3:** 3× productivity improvement. A rocket silo with 4 PM4s produces 30% more rockets per resource than with PM3s. This justifies the entire Vulcanus expedition.

Tungsten ore is rare on Vulcanus surface. Plan asteroid mining for long-term supply.

## Power & Trains

| Problem | Solution |
|---------|----------|
| No water for steam | Nuclear fuel cells (imported from Nauvis) |
| No coal for burners | Coke from imported coal or oil→solid fuel chain |
| Steam locomotives don't work | Nuclear fuel or diesel locomotives only |

Run 1-2 nuclear reactors on Vulcanus for train locomotion and factory backup. The reactors aren't main power — they're logistics enablers.

## Demons: Flying Enemies from Lava Vents

Vulcanus has no biters. Instead, **Demons** spawn from lava vents:
- Fast (faster than spitters), fragile (one laser kill)
- Don't expand like biters — fixed population around vents
- Target anything, including construction bots mid-build

**Solutions:**
- **Lazy:** landfill the vents. No vent = no demons.
- **Active:** laser turrets on power switch. Zero maintenance.

## Research Order

1. Metallurgic science pack 1 (basic foundry products)
2. Foundry efficiency upgrades (reduces calcite/plate)
3. Metallurgic science pack 2 (requires tungsten carbide)
4. Tungsten carbide tech → unlocks Module 4 production
5. Advanced metallurgic science (combines all planet outputs)

Critical path: **calcite stable → plates → sci pack 1 → efficiency → tungsten → Module 4**

## Import / Export Priority

| Direction | Items |
|-----------|-------|
| **Export** | Tungsten carbide (highest value), metallurgic science, surplus calcite |
| **Import** | Nuclear fuel cells, construction bots, backup calcite |

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| Starting foundries without calcite buffer | Chain halts within minutes |
| Ignoring circular dependency | Copper foundry stuck waiting for molten iron that doesn't exist yet |
| Mining all tungsten upfront | Surface deposits deplete before Module 4 line is built |
| Using steam locomotives | They don't work without water |

## The Bottom Line

Vulcanus rewards players who master the foundry's circular recipe system. Get calcite recycling stable first — everything else depends on it. Tungsten carbide and Module 4 are the endgame payoff. Build compact, import fuel, landfill demon vents.
