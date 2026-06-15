---
title: "Factorio Vulcanus Guide - Space Age Planet Strategy"
description: "How to survive and thrive on Vulcanus in Factorio Space Age: lava foundry, calcite mining, tungsten production, and the exact setup for infinite iron/copper from lava."
date: 2026-05-18
lastmod: 2026-06-15T13:49:00+08:00
tags: ["space-age", "vulcanus", "planet-guide"]
draft: false
---

You land on Vulcanus and there are no ore patches. Just lava, cliffs, and demolisher worms that eat your buildings. I spent my first landing trying to build a furnace array before realizing Vulcanus doesn't need furnaces -- it uses foundries that cast molten metal directly. Here's how I set up iron and copper production from lava that never runs out.

{{< callout "tip" >}}
**TL;DR:** Pump lava > Foundry > Cast iron/copper directly. Calcite is the only limiting resource (mine it and ship from orbit). Two pumps of lava + one strip of calcite belt = enough iron and copper for 60 SPM. Build underground from the lava edges and use elevated rails to cross worm territories. Dump stone from iron casting into the lava to clear your belts.
{{< /callout >}}

## What Makes Vulcanus Different

Vulcanus has infinite base resources. Lava wells never run dry. Calcite is finite but 5 rich patches last for hundreds of hours. There are no biters -- the threat is demolisher worms protecting resource-rich areas.

The production chain is short:

1. **Pump lava** from a lava lake (place the pump on the lava edge)
2. **Foundry** takes lava + calcite > molten iron or molten copper
3. **Quick-cast** the molten metal directly into plates, gears, wire, or pipes
4. **Dump byproducts** (stone from iron casting) back into lava

That's it. The foundry replaces furnaces, assemblers, and half the belt infrastructure. I had lava-to-plate production running within 5 minutes of landing.

{{< callout type="info" >}}
**Quick Tip:** Place the lava pump at the deepest part of the lava lake (darker color in map view). Shallow lava gives half the flow rate. One deep lava pump = 1,200 fluid/sec, which feeds 1 foundry running molten iron. If you're doing both iron AND copper, you need 2 pumps.
{{< /callout >}}

## Foundry Setup

| Pump location | Flow rate | Iron/sec | Copper/sec | Calcite/sec |
|:--------------|:---------:|:--------:|:----------:|:-----------:|
| Shallow lava | 600/sec | 180/min | 160/min | 1/sec |
| Deep lava | 1,200/sec | 360/min | 320/min | 2/sec |
| Deep lava + speed beacon | 1,200/sec | 720/min | 640/min | 4/sec |

The foundry has 4 module slots. I use speed modules + one productivity module as the default. Productivity saves calcite (which is the constraint). Speed saves space (foundries are large).

**Iron production for 60 SPM:** 2 deep lava pumps + 4 foundries (2 iron, 2 copper) + 1 calcite belt. The iron foundries output molten iron > cast into iron plates. The copper foundries output molten copper > cast into copper plates. Stone byproduct from iron casting runs into the lava or a recycler.

The stone problem: iron casting produces stone as a byproduct. 100 molten iron > 1 plate + 2 stone. After 10 minutes of continuous smelting, you have 1,200 stone blocking your foundry output. Solution: place a fast inserter next to the foundry output that dumps stone into the lava lake. Yes, lava accepts item dumping.

## Calcite Management

Calcite is the one finite resource on Vulcanus. You need it for two things: as a catalyst in the foundry (lava + calcite = molten metal) and for making concrete.

How to get calcite:

| Method | Rate | Sustainability |
|:-------|:----:|:--------------|
| Mine calcite patches on Vulcanus | 600/min per miner | Finite (50+ hours per patch) |
| Drop from space platform orbiting Vulcanus | 50/min per crusher | Infinite (requires asteroid) |
| Orbit calcite from Nauvis | 20/min per asteroid crusher | Infinite but slow |

I use mining for my main calcite supply (1 patch = 50 hours) and supplement with orbital drops when the furnace column runs low. The space platform trick: set an asteroid crusher to process metallic asteroids, filter calcite, and drop to Vulcanus via landing pad.

{{< callout "warning" >}}
Don't mine calcite on Vulcanus without worm protection. Calcite patches often sit on worm territory. I lost 3 miners to a small demolisher before I built a wall. Place 4 gun turrets with piercing ammo per miner cluster. The small demolishers take 6-8 piercing rounds to kill. Set the turrets to attack worms manually or use a circuit condition to auto-fire when a worm enters range.
{{< /callout >}}

## Demolisher Worm Warning

Small demolishers are manageable (6-8 piercing shots). Medium demolishers (uncommon quality) need uranium ammo and multiple turrets. Large demolishers need artillery.

I explore new areas on Vulcanus with a tank. The tank drives around lava lakes (not over them). When I find a clear area with no worms, I land a constructor pod and build an elevated rail to the foundry site. Elevated rails cross worm territory while staying above their attack range.

The known strategy: build walls on the edge of worm territory with flamethrowers. The worms attack the wall, the flamethrowers deal 100+ damage/sec, and after 3-4 worm kills, the territory is safe. Each kill triggers a significant expansion of your safe zone.

---

## Community Verification & Resources

- [Official Factorio Wiki -- Vulcanus](https://wiki.factorio.com/Vulcanus) -- planet stats, foundry recipes, and worm behavior
- [Reddit -- Vulcanus Discussion](https://www.reddit.com/r/factorio/) -- community landing strategies and foundry-only production layouts
- [Factorio Forums -- Space Age Guides](https://forums.factorio.com/) -- advanced Vulcanus setups with multiple lava wells

**Related:** [Fulgora Recycling Guide]({{< ref "/space-age/fulgora-recycling-guide" >}}) | [Gleba Survival Guide]({{< ref "/space-age/gleba-survival-guide" >}}) | [Quality Module Guide]({{< ref "/space-age/quality-module-guide" >}})
