---
title: "Artillery 鈥?Range, Shells, and Outpost Setup"
description: "Artillery guide for Factorio. Shell production, range research, outpost placement, and the logistics chain that keeps your perimeter safe from biter attacks."
date: 2026-05-23
lastmod: 2026-05-23T19:09:00+08:00
publishDate: 2026-05-27T16:52:00+08:00
tags: ["defense", "artillery", "military"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

Artillery is the endgame solution to biter bases. {{< material "gun_turret" >}} Gun turrets and {{< material "laser_turret" >}} laser turrets defend your walls. Artillery deletes the threat before it reaches you.

{{< callout "tip" >}}
**TL;DR:** Build artillery turrets at outposts, connect them to your rail network, and supply shells via trains. Research range to extend coverage. One shell destroys most biter bases in 2-3 shots.
{{< /callout >}}

{{< diagram "diagrams/artillery-outpost.svg" "Artillery outpost logistics chain 鈥?main base shell production, train delivery, and targeting range" "900" >}}

## How Artillery Works

The artillery turret fires explosive shells at biter bases within range. Each shell deals massive area damage, destroying nests, worms, and biters in the blast radius.

**Key mechanics:**
- Manual targeting: click the map, the turret fires
- Automatic targeting: turrets auto-fire at biter bases in range (configurable)
- Shell consumption: each shot uses one artillery shell
- Range: base 7 tiles, max 140 tiles with research

## Shell Production Chain

Artillery shells are expensive. Plan your factory:

| Component | Source | Notes |
|-----------|--------|-------|
| Explosive cannon shell | Military science | Standard ammo production |
| Radar | Green circuits + iron | One per turret for targeting |
| Artillery shell | Explosive shell + radar | Assemble at dedicated factory |

**Throughput:** One assembler 2 produces 1 shell every 15 seconds. For sustained fire, build 4-6 assemblers.

## Outpost Setup

Artillery outposts need three things: a turret, a buffer chest, and a train connection.

**The buffer rule:** Store 200 shells locally. This covers 50-100 biter bases before resupply is needed. Use requester chests wired to the train stop 鈥?trains only dispatch when stock is low.

**Placement strategy:**
- Space outposts 200+ tiles apart (overlap coverage by ~40 tiles)
- Connect to your main rail network
- Defend the outpost itself 鈥?biters attack artillery

## Range Research

Research extends artillery range dramatically:

| Level | Range | Coverage Area |
|-------|-------|---------------|
| 0 (base) | 7 tiles | Tiny |
| 3 | 60 tiles | Small perimeter |
| 7 (max) | 140 tiles | Entire visible map |

**Priority:** Artillery range 3 unlocks practical outpost placement. Range 7 is endgame convenience.

## What Veterans Learn the Hard Way

- **Shells are heavy** 鈥?one stack is only 10 shells. Trains need dedicated artillery shell cars.
- **Biters evolve** 鈥?artillery fire draws evolution. Expect retaliation.
- **Outposts need defense** 鈥?the turret fires outward, but biters attack the outpost itself. {{< material "wall" >}} Walls and {{< material "gun_turret" >}} turrets required.
- **Don't overbuild** 鈥?3-4 outposts cover most maps. More = shell drain without benefit.

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| No shell buffer | Turret runs dry during attack |
| Outpost too far from rail | Manual shell delivery = tedious |
| No outpost defense | Biters destroy your investment |
| Firing at everything | Wastes shells, accelerates evolution |

## The Bottom Line

Artillery turns biter defense from reactive to proactive. Build shells at main base, deliver by train, store 200 at each outpost. Research range to 3, then 7. Clear the map on your terms.

---

**Related:** [Early Game Defense]({{< ref "/defense/early-game-defense" >}}) | [Flamethrower Defense]({{< ref "/defense/flamethrower-defense-guide" >}})