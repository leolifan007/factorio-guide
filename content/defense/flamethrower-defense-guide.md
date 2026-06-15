---
title: "Factorio Flamethrower Turret Defense - Highest DPS Weapon Guide"
description: "Flamethrower turret guide for Factorio: highest DPS turret in the game, oil-based ammo logistics, wall synergy with dragons teeth, and circuit-controlled ammo conservation."
date: 2026-05-21
tags: ["defense", "beginner"]
draft: false

---

Your gun turrets chew through 10 magazines per biter wave and you're spending more time crafting ammo than building your factory. Flamethrower turrets solve that: highest raw DPS in the game, area damage that stacks, ignores biter armor entirely, and one pumpjack feeds 30+ turrets indefinitely.

{{< callout "tip" >}}
**TL;DR:** Place flamethrower turrets behind a wall with dragon's teeth. One pumpjack + one chemical plant on heavy oil feeds 30+ turrets. Gun turrets handle the cleanup on anything that leaks through.
{{< /callout >}}

## Why Gun Turrets Alone Don't Scale

Gun turrets deal single-target damage that degrades against biter armor upgrades. Behemoth biters in particular have enough armor that green ammo barely scratches them. The ammo belt alone can consume an entire iron patch.

| Turret Type | Raw DPS | Ammo Cost | AoE | Armor Piercing | Range |
|:------------|:-------:|:---------:|:---:|:--------------:|:-----:|
| Gun (red ammo) | ~350 | High (iron+copper) | No | Partial | Medium |
| Laser | ~180 | Power only | No | Yes (flat damage) | Long |
| Flamethrower | ~650+ | Minimal (oil) | Yes | Yes (fire ignores armor) | Medium |

Flamethrower turrets hit for roughly 650 DPS per turret with damage upgrades -- tripled against groups thanks to fire that spreads and stacks. A row of three flamethrowers handles attacks that would need 15+ gun turrets.

## The Proven Fix -- Wall + Flame + Gun Sandwich

**Layer 1 -- Dragon's teeth.** In front of the wall, place a staggered grid of walls (2-3 deep, with gaps between). Biters path around them, slowing down and bunching up. A bunched group = prime flamethrower target.

**Layer 2 -- Flamethrower turrets.** Behind the wall, spaced 3-4 tiles apart. Each turret covers roughly 30 tiles of wall in a cone in front. Overlap the cones by about 5 tiles -- no gaps.

**Layer 3 -- Gun turret cleanup squad.** Place one gun turret for every 3 flamethrowers, fed by a semi-independent ammo belt. They handle anything that survives the fire (very little, once fire damage research is done).

{{< diagram "diagrams/flamethrower-wall-layout.svg" "Flamethrower turret wall layout with dragon's teeth, wall layers, and cleanup gun turrets" "760" >}}

**Ammo supply:**

- Heavy oil is the best flamethrower fuel (highest damage modifier)
- 1 chemical plant on heavy oil feeds up to 40 turrets
- 1 storage tank holds enough for 250+ waves
- Connect a circuit wire to the tank: when heavy oil drops below 1000, enable the chemical plant. You get automatic ammo production that only runs when needed.

{{< callout type="warning" >}}
**Traps People Keep Falling Into:** Don't run your flamethrower turrets off the same pipe network as your refinery. A deadlocked refinery (heavy oil full → cracking stalled → no petroleum) will starve your defenses just when you need them. Give flamethrower turrets their own pumpjacks and pipe network.
{{< /callout >}}

## Understanding Damage Over Time Mechanics

Fire is the only damage type in Factorio with stacking area-of-effect. Each flamethrower turret fires a stream that ignites a ground fire for roughly 3 seconds. Enemies walking through it take 100% weapon damage per tick plus the ground fire tick.

**The stacking effect:**
- 1 turret = fire covers ~5 tile area for 3s
- 3 turrets overlapping = ~15 tiles burning simultaneously
- A behemoth biter (5,000 HP) crossing 3 flamethrower streams dies in roughly 4 seconds
- Same behemoth takes 12 seconds of sustained laser fire

{{< callout type="info" >}}
**Quick Tip:** Fire damage research is the highest-value combat research in the game. Each level of Stronger Explosives (+10% flamethrower damage) effectively buffs every defense outpost simultaneously. Prioritize it over gun damage once flamethrowers are in place.
{{< /callout >}}

## Where Most Players Mess This Up

**Walls too close to turrets.** Flamethrower turrets need about 3 tiles of clearance between the wall and the turret. Why: fire streams arc. If the wall is too close, the stream hits the wall instead of the biters.

**No oil buffer.** A single pipe segment holds only 100 units. With no storage tank buffer, your first attack wave empties the pipe before the ammo is replenished. Always put a tank between the chemical plant and the turret network.

**Turrets spaced too far apart.** The flamethrower stream arc covers roughly 30 tiles of wall in a cone. Space turrets every 20 tiles, not 40. The overlap is critical for the fire stacking effect.

**Reliance on one oil patch.** Flamethrowers are oil-independent after setup -- a single pumpjack on a 2,000% patch lasts hundreds of hours. But if that patch is your refinery's only source too, restarting both after a biter attack is a pain. Dedicated pumpjacks.

## Scaling It Up -- Megabase Defense

For megabases, flamethrower walls become your primary defense. The upgrade path:

- **Each outpost** gets its own isolated pumpjack + chemical plant circuit
- **Artillery** replaces gun turrets for cleanup at 10k+ SPM -- one artillery train stops by each outpost every 5 minutes
- **Repair packs** on the logistics network fix wall damage automatically
- **Dragon's teeth** can be 5+ layers deep for late-game biters with evolutionary damage bonuses

The ammo economics are the killer feature: a flamethrower wall running for 100 hours consumes roughly 500 crude oil. The same wall with gun turrets would consume 50,000+ iron plates in magazines.

---


I pumped heavy oil to my first flamethrower wall and the damage was half what I expected. Light oil gives 25% more DPS and costs nothing extra.

## Community Verification & Resources

- [Official Wiki -- Flamethrower Turret](https://wiki.factorio.com/Flamethrower_turret) -- exact DPS formulas, damage vs. biter types, and range tables
- [Factorio Forums -- Defense Bible](https://forums.factorio.com/viewtopic.php?t=80398) -- community-tested wall layouts for all biter evolution stages
- [Steam Guide -- Complete Defense System](https://steamcommunity.com/sharedfiles/filedetails/?id=2860674309) -- tileable wall blueprints with circuit-controlled ammo

**Related:** [Early Game Defense]({{< ref "/defense/early-game-defense" >}}) | [Artillery Guide]({{< ref "/defense/artillery-guide" >}})
