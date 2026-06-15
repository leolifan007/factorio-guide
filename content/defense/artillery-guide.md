---
title: "Factorio Artillery Guide - Automated Shelling and Outpost Defense"
description: "How to use artillery in Factorio: artillery shell production, range upgrade, automated outpost clearing, and the exact artillery outpost blueprint that keeps biters away permanently."
date: 2026-05-18
lastmod: 2026-06-15T13:47:00+08:00
tags: ["defense", "artillery", "turrets"]
draft: false
---

I spent 10 hours clearing biter nests by hand before I built my first artillery outpost. Every nest I destroyed triggered expansion parties from 8 different directions. Artillery fixes this -- it clears nests automatically and the range pushback keeps cleared areas clear. Here's the exact artillery wagon + outpost setup I use.

{{< callout "tip" >}}
**TL;DR:** Two artillery wagons per outpost, surrounded by 6 gun turrets with piercing ammo. Shell range upgrades are the priority research (x3 before purple science). Automated delivery via train: artillery shell production feeds a provider station, each outpost has a requester. Without the ammo train, your outpost runs out of shells in 3 minutes of continuous firing.
{{< /callout >}}

## How Artillery Changes the Game

Artillery is the only weapon that clears biter nests from outside the pollution cloud. One shell destroys a nest cluster in a 5-tile radius. The range at max upgrade covers 7 chunks -- more than any other weapon.

When artillery fires at a nest, the biters attack your outpost. The shell hits the nest, the natives swarm the nearest structure. This means your artillery outpost needs defense against the retaliation wave.

The pattern: shell > biters attack your wall > turrets kill the biters > repeat. Each outpost goes through this cycle every 30-60 seconds during active clearing. After 5-10 cycles, the nearby nests are gone and the outpost goes dormant.

| Upgrade level | Range (chunks) | Shells per nest destroyed | Ammo cost per cycle |
|:-------------|:--------------:|:------------------------:|:-------------------:|
| 1 | 3 | 2-3 | 40 piercing rounds |
| 2 | 5 | 1-2 | 30 piercing rounds |
| 3 | 7 | 1-2 | 25 piercing rounds |
| Max (3 + quality) | 7+ | 1 | 15 piercing rounds |

I rush range upgrade 3 before starting purple science. Higher range means the artillery clears nests without triggering new expansion parties that spawn at the edge of your cleared area.

## The Outpost Blueprint

Every artillery outpost I build uses the same components:

| Component | Count | Purpose |
|:----------|:-----:|:--------|
| Artillery wagon | 2 | Deliver shells and auto-shell nests |
| Gun turret | 6 | Defend against retaliation waves |
| Wall | 30-50 | Surround the turrets in a box |
| Station | 1 | Requester for shells and ammo |
| Chest | 4 steel | Shell storage for the wagon |
| Power pole | 3 | Connect to main grid |

Two artillery wagons is the sweet spot. One wagon fires too slowly (the next shell is still in the assembler). Two wagons alternate, keeping continuous fire on the nearby nests.

**The layout:** 10x10 walled area. Artillery wagons sit in the center. 6 gun turrets line the walls on each side. The train station sits outside the wall on one side with requester chests feeding shells and ammo into the compound via underground belt.

{{< callout type="info" >}}
**Quick Tip:** Put the ammo chest behind a circuit condition. Set the inserter to only enable when turret ammo < 100. This prevents the chest from emptying into full turrets, and keeps the turret ammo level consistent. Without this circuit, the first six turrets consume all the ammo and the last four sit empty.
{{< /callout >}}

## Ammo Production and Delivery

Artillery shells need: 5 explosives + 10 steel + 1 radar. I automate this at my main base and ship via train.

**Shell production per assembler:** 1 shell per 8 seconds in assembler 3. I run 4 assemblers for a single outpost. Shells go into a provider station with 2 trainloads of buffer.

**Feeding the outpost:** Each outpost has a train station named "[Request] Artillery Ammo." The train schedule: Provider > Depot > Request. The depot adds a 60-second wait timer so the train doesn't bounce between stations.

The mistake I made: one train per outpost. With 3 outposts, that's 3 trains plus ammo production. The correct approach: use the same train for all outposts with train limits set to 1. The train dispatches to whichever outpost requests ammo first. With stack threshold at 100 shells, each outpost gets a full resupply when it drops below that.

## Artillery Wagon vs. Turret

| Feature | Wagon | Turret |
|:--------|:-----|:-------|
| Range | 7 chunks (upgraded) | 4 chunks (fixed) |
| Shell capacity | 50 | 15 |
| Auto-fire | Yes (with radar) | Yes |
| Manual fire | Yes | Yes |
| Automated reload | Inserter from chest | Belt or requester chest |
| Train-nest clear | Drive-by | Stationary |

The wagon is better for clearing new areas (drive through nests, fire automatically). The turret is better for defending a chokepoint (always active, larger shell buffer per turret). I use wagons for expansion and turrets for perimeter defense.

---

## Community Verification & Resources

- [Official Factorio Wiki -- Artillery](https://wiki.factorio.com/Artillery) -- shell damage, range upgrades, and priority targeting mechanics
- [Reddit -- Artillery Outpost Designs](https://www.reddit.com/r/factorio/) -- popular outpost blueprints with integrated defense
- [Factorio Forums -- Base Defense](https://forums.factorio.com/viewforum.php?f=55) -- wall, flamethrower, and artillery combination builds

**Related:** [Flamethrower Defense Guide]({{< ref "/defense/flamethrower-defense-guide" >}}) | [Early Game Defense]({{< ref "/defense/early-game-defense" >}}) | [Basic Rail Network]({{< ref "/trains-logistics/basic-rail-network" >}})
