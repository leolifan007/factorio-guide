---
title: "Artillery Turret — How to Clear Biters and Map the Whole World"
description: "Factorio artillery turret guide. Shell recipes, outpost chains, circuit-controlled auto-fire, and the supply train setup that keeps your artillery firing without manual babysitting."
date: 2026-05-23
lastmod: 2026-05-23T19:09:00+08:00
publishDate: 2026-05-26T14:17:00+08:00
tags: ["defense", "biters", "artillery"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

Your walls are up. Flamethrowers are hot. And yet biter bases keep spawning just outside your pollution cloud, eating through defenses in waves. The artillery turret is the fix — but placing one turret and watching it miss isn't automation.

{{< callout "tip" >}}
**TL;DR:** Artillery fires at biter bases within targeting range (starts at 7 tiles, researchable to 140). You need: 1 shell assembler + 1 turret + circuit-controlled auto-fire + 200-shell buffer per outpost. Train resupplies when shells drop below 50.
{{< /callout >}}

{{< diagram "diagrams/artillery-outpost.svg" "Artillery outpost circuit diagram — turret, shells, circuit network, and supply train" "800" >}}

## How Artillery Actually Works

Three conditions must be met for a turret to fire:

1. **Biter base inside targeting range** (circle around turret, radius = researched level × 20 tiles)
2. **Circuit network sends fire signal** (or manual aim)
3. **Shells in inventory** (turret holds 100 max)

Without circuit control, you're manually aiming a targeting camera. That's not automation.

## Targeting Range Research

| Level | Range (tiles) | Coverage |
|-------|--------------|----------|
| 0 (base) | 7 | Barely clears adjacent nests |
| 3 | 60 | Small perimeter defense |
| 5 | 100 | Covers most expansion zones |
| 7 (max) | 140 | Entire small vanilla map |

**Rule:** always research range before building outposts. A 7-tile turret is nearly useless.

## Shell Production Ratio

| Item | Recipe | Time |
|------|--------|------|
| Explosive cannon shell | 1 iron + 1 copper + 1 sulfur | 3 sec |
| **Artillery shell** | 8 explosive shells + 1 radar | 10 sec |

**The ratio:** 1 assembler making explosive shells feeds ~1.2 artillery shell assemblers. Start with **1 shell assembler per 2 turrets** for continuous fire.

Each turret fires every ~20 seconds when loaded. 100 shells = ~33 minutes of continuous engagement. Buffer **200 shells minimum** per outpost.

## Outpost Design

Every artillery outpost needs these components:

| Component | Purpose |
|-----------|---------|
| Artillery turret | Fires at targets in range |
| Requester chest (200 shells) | Triggers resupply at <50 shells |
| Provider chest | Receives train/bot deliveries |
| Inserter (provider → turret) | Auto-feeds shells |
| Radar (optional) | Reveals bases for auto-targeting |
| Wall + flamethrower backup | Survives biter retaliation |

## Circuit-Controlled Auto-Fire

The setup that makes artillery truly automatic:

1. Wire requester chest to **decider combinator** via red wire
2. Set combinator: `shells < 50 → output signal "fire"` (or wire directly to turret enable)
3. Turret receives signal → fires at any target in range
4. When shells drop below threshold → train dispatches from depot

**Simpler alternative:** skip the radar. Aim the turret manually on first visit, then leave it. Biters wander into range naturally (attracted by pollution). The turret handles the rest.

## Resupply: Trains vs Bots

| Method | Best For | Limitation |
|--------|----------|------------|
| Logistic bots | 1-3 outposts, close to base | Range limited by roboport coverage |
| Delivery train | 3-10 outposts, any distance | Requires depot with idle trains |
| Belt/inserter chain | Outposts <100 tiles from production | Not scalable |

**For 5+ outposts:** dedicated supply train with circuit-condition schedule is the only solution that scales. Schedule: train waits at depot until any outpost signals `shells < 50` → delivers 200 shells → returns to depot.

## Biter Expansion Mechanics

Biters send expansion squads every ~30-60 seconds if an empty chunk exists within range. Artillery's firing range creates a permanent no-spawn zone — as long as it keeps firing.

**Warning:** artillery is loud. Within ~100 tiles, biters hear it and send attack waves. At max range research (140 tiles), your turret outranges their perception. Before max research, pair outposts with walls and flamethrowers.

## Common Mistakes

| Mistake | Why It Fails |
|---------|-------------|
| Building before researching range | 7-tile range = useless |
| Buffering <100 shells | Turret runs dry mid-clearing |
| Gun turret defense (not flamethrower) | Ammo depletes under sustained attack |
| Placing turret inside walls | Range wasted — outposts go ahead of walls |
| Unwired requester chest | Manual refill job forever |

## The Bottom Line

Artillery converts biter management from active chore to background process. The three essentials: circuit network for auto-fire, 200+ shell buffer, and train resupply. Get those right and your network clears the map while you design production lines.
