---
title: "Artillery Turret — How to Clear Biters and Map the Whole World"
description: "Factorio artillery turret guide. Shell recipes, outpost chains, circuit-controlled auto-fire, and the supply train setup that keeps your artillery firing without manual babysitting."
date: 2026-05-23
lastmod: 2026-05-23T17:52:00+08:00
publishDate: 2026-05-26T14:17:00+08:00
tags: ["defense", "biters", "artillery"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

Your walls are up. Your flamethrowers are hot. And yet biter bases keep spawning just outside your pollution cloud, eating through your defenses in waves. You send construction bots to manually clear — they die. You send trains with landfill and walls — the biters eat them too. The real fix is the artillery turret, but nobody tells you how to actually make it work beyond placing one turret and watching it miss.

Your artillery turret is flashing. Nothing is dying. Here's why, and how to build an artillery network that maps the entire world while your factory hums without you.

{{< callout "tip" >}}
**TL;DR:** Artillery turrets fire at any biter base within targeting range (research-dependent, starts at 7 tiles). You need 1 artillery shell assembler + 1 turret + circuit-controlled auto-fire. For outpost chains: build a turret, add 200 shells in buffer, wire requester chest to circuit network. When shells drop below 50, a train resupplies automatically.
{{< /callout >}}


{< diagram "diagrams/artillery-outpost.svg" "Artillery outpost circuit diagram — turret, shells, circuit network, and supply train" "800" >}

## Why Your Turrets Miss Everything

The artillery turret is not a flamethrower. It does not auto-target. It fires in one direction only — the direction its targeting computer is pointed at. If you place one turret and expect it to sweep the map, you'll stare at it blinking for hours.

Three things must happen for artillery to fire:
1. A biter base must be inside the turret's targeting range circle
2. The targeting computer must have an active firing order (circuit network)
3. Shells must be in the turret's inventory

The targeting range starts at 7 tiles without research. The Artillery targeting range research pushes it to 20 tiles per level, up to 7 levels = 140 tile range. At max research, one turret covers a circle roughly the size of a small vanilla map.

## The Core Fix — Range and Targeting

Without circuit network, artillery fires only when you manually aim it. That's not automation — that's a targeting camera you have to babysit.

The circuit control setup for auto-fire:
1. Place an artillery turret
2. Connect it to a decider combinator with red wire
3. Set the combinator: if [any enemy unit detected] → output 1 to the turret's targeting signal
4. The turret receives the signal and fires

But this only works if biters are within range. The real automation layer: radar.

Place a radar next to the artillery outpost, set to scan. When the radar detects a biter base within its scan range (1 chunk = 32 tiles), the scan reveals the base. Connect the radar to the circuit network. Use the radar's "detach" signal as the firing trigger: when a new base appears in the scan result, fire.

The easier version: just let biters get within range and fire. Set the turret to manual direction when you first visit the outpost, then leave it. As biters wander into range naturally (attracted by pollution), the turret fires. This works for clearing expansion — the turret doesn't need your help once aimed.

## The Artillery Shell Recipe Nobody Talks About

The recipe is straightforward, but the ratio is what breaks most setups.

**Artillery shell recipe (assembler 3):**
- 8 explosive cannon shells + 1 radar → 1 artillery shell
- Craft time: 10 seconds per shell in a normal assembler

8 explosive cannon shells per artillery shell. Each explosive cannon shell takes:
- 1 iron plate + 1 copper plate + 1 sulfur → 1 explosive cannon shell
- 3 seconds in assembler 3

**The ratio math:**
- 1 assembler 3 making explosive cannon shells: ~20 shells/min
- 8 shells/min → 1 artillery shell every 48 seconds
- 1 artillery turret fires every ~20 seconds at max load

So: 1 shell assembler = continuous fire for 2 artillery turrets. Start with 1 shell assembler per turret.

**Shell inventory requirement:** An artillery turret holds 100 shells. At 1 shot per 20 seconds, that's 2000 seconds of firing per 100 shells = ~33 minutes of continuous engagement. Buffer at least 200 shells at each outpost.

## Building the Perfect Outpost Chain

The artillery outpost is not just a turret. It's a mini-factory.

**Required components per outpost:**
- 1 artillery turret
- 1 requester chest (wired to circuit)
- 1 provider chest
- 1 inserter from provider to turret
- Buffer storage for 200+ shells
- Radar (optional but recommended)
- Defensive wall + flamethrower backup

**The circuit setup:**
```
Provider chest: contains artillery shells, wired to logistic network
Requester chest: requests 200 shells, wired to logistic network
Inserter: takes from provider → feeds turret
Turret: automatically fires when base in range
```

When the requester chest drops below 50 shells, a logistic robot flies in from your main base to restock. Or — better — a train.

**Train resupply for artillery outpost:**
- Schedule: delivery train waits at depot until outpost signals "low shells" (circuit condition: shells < 50)
- Train arrives, unloads shells to provider chest
- Train departs when full
- This is the "set and forget" artillery network

For 5+ outposts, a dedicated artillery supply train with a circuit condition schedule is the only scalable solution. Without it, you'll manually refill shells for the rest of your run.

## The Supply Train Problem Nobody Solves

The bottleneck is never the shell production. It's the last-mile delivery to the outpost.

**Three resupply strategies, ranked by reliability:**

Rank 1 — Logistic bots (easiest for 1-3 outposts):
- Roboport in the outpost
- Logistic network extends from main base
- Bots fly shells across the map automatically
- Problem: range limit, power demand

Rank 2 — Delivery train (recommended for 3-10 outposts):
- Dedicated artillery supply train
- Circuit condition at each outpost: wait until shells < 50
- Train carries 200 shells per outpost stop
- Schedule managed by circuit network, no manual intervention

Rank 3 — Bulk inserters from main base (only for close outposts):
- Extremely long inserter chains
- Shell production at main base, belts running to outpost
- Only viable within ~100 tiles
- Not recommended for serious play

## Outmaneuvering Biters: Spawner Aggression Mechanics

Here's what biters do that most guides don't explain: they expand.

Every ~30 seconds, if there's an empty chunk within range of a biter base, biters will send a squad to build a new spawner. This is why you can clear a base, come back in 10 minutes, and there's a new base in the same spot.

Artillery stops this. The turret's firing range creates a permanent no-spawn zone. As long as the turret fires at anything that enters its range, biters cannot expand into that area.

**The expansion timing:** Biters check for new spawn opportunities every 30-60 seconds (randomized). If your artillery fires every 20 seconds, no spawner can take root. If your artillery runs out of shells for an hour, expect a wall of new bases when you return.

**Noise and aggression:** Artillery is loud. If biters can hear it (within their perception range, ~100 tiles), they send attack waves. Always pair artillery outposts with walls and flamethrowers. The outpost should be able to survive a biter attack while the turret is reloading.

**Artillery range vs. perception range:** At max research (140 tiles), your artillery outranges biter perception. They won't hear it and won't attack. Before max research (early game), artillery is within their hearing range. Plan accordingly.

## What This Looks Like on the Map

A mature artillery network has 3-5 outposts arranged in a semicircle around your base, each covering ~120 tile radius. The shells supply train makes a circuit. Your wall is now a relic — biters can't expand to it.

The first outpost goes up at research tier 2 (Artillery range 2). Place it 100 tiles from your walls. Load it with 200 shells manually. Aim it toward the nearest biter nest. Clear everything in range. Repeat. After 3 outposts, your pollution cloud can expand into territory biters will never reclaim.

The long game: once you've cleared the entire reachable map, artillery goes silent. Your walls become optional. The factory maintains itself.

## Common Mistakes That Waste Shells

Mistake 1: Building artillery before researching range. A 7-tile range turret clears 1 biter nest before the biters walk into it. Always research range first.

Mistake 2: Not buffering shells. A turret with 20 shells fires for 6 minutes. If your outpost runs dry in the middle of clearing, biters recolonize the area.

Mistake 3: Defending the outpost with gun turrets instead of flamethrowers. Gun turrets run out of ammo under sustained attack. Flamethrowers need fuel — but fuel is easier to ship than ammo.

Mistake 4: Putting the artillery inside your walls. The turret's range is wasted if it's 30 tiles from the enemy. Outposts should be ahead of the walls.

Mistake 5: Not wiring the requester chest. A disconnected outpost is a manual refill job forever.

## The Bottom Line

Artillery is the answer to Factorio's endgame defense problem. Once you have artillery, biter management stops being a chore and starts being a background process. The key is the circuit network, the shell buffer, and the resupply train. Set those three things up correctly and your artillery network clears the world map while you're designing your next production line.
