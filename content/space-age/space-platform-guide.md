---
title: "Space Platform Design Guide"
description: "Space platform design for Factorio Space Age. Thruster ratio, platform weight, asteroid defense, platform hub setup, and the 3-stage build order that gets you to Gleba alive."
date: 2026-05-21
tags: ["space-age", "space-platform"]
draft: false
emoji: "🚀"
---

The space platform you just launched is drifting toward Gleba without enough fuel to brake. The thrusters are starved, the crushers aren't running, and the asteroids have punched a hole through your ammo belt. Here's the build order that prevents that from happening: build the hub → fuel plant → ammo production → thrusters → go.

{{< callout "tip" >}}
**TL;DR:** Build your platform in this order: hub → crushers/chemical plants → ammo assemblers → thrusters → go. Keep platform weight under 100 tons for first trips. One thruster per 50 tons minimum thrust-to-weight ratio.
{{< /callout >}}

## The Mechanics Behind Space Travel

Space platforms are ships that fly between planets. They have five essential systems:

| System | Purpose | What can go wrong |
|:-------|:--------|:------------------|
| Hub | Core of the platform. Stores items, provides power | Running out of building materials mid-flight |
| Crushers | Break asteroids into ice, iron, carbon | Not enough collectors → no fuel |
| Thrusters | Move the platform | Too much mass → too slow to escape asteroids |
| Turrets | Shoot asteroids before they hit | Ammo runs out before the trip ends |
| Collectors | Catch passing asteroids | Placed too far back → catch nothing |

{{< diagram "diagrams/space-platform-layout.svg" "Space platform layout with hub, crushers, ammo line, and thruster row" "760" >}}

## The Proven Fix — Stage 1 Build Order (First Platform)

Build in this exact order on Nauvis orbit:

**Stage 1 — The hub and foundation.**
Place the hub. Extend a row of foundation tiles forward (direction of travel). This is your spine. Start with 20 tiles.

**Stage 2 — Fuel production (crushers + chemical plants).**
Place 3 asteroid collectors on the front edge. Behind them, 2 crushers (set to ice crushing). Behind crushers, 2 chemical plants making thruster fuel. Run pipes: ice → crusher → water → chemical plant → fuel → thruster.

**Stage 3 — Ammo production.**
Behind the fuel line: 2 more crushers (iron ore crushing) feeding 1 assembling machine making magazines. Run ammo belt forward to the turrets.

**Stage 4 — Turrets.**
Place 3-4 gun turrets on the front edge of the platform, overlapping fields of fire. Feed them from the ammo belt.

**Stage 5 — Thrusters and go.**
2 thrusters at the back. Start with 1 thruster fuel tank (5 storage). Set target: first planet fuel stop. Launch.

{{< callout type="info" >}}
**Quick Tip:** The ratio that trips up most first-time platform builders: one crusher produces enough water to feed exactly 2 chemical plants making thruster fuel. Overbuild crushers (not chemical plants) if you need more. Platforms that stall mid-journey almost always stalled because crushers were underbuilt and fuel stopped flowing.
{{< /callout >}}

## The Thrust-to-Weight Problem

Platform weight is the #1 killer of first platforms. Each tile of foundation adds mass. Each building adds mass. Total mass determines how fast your thrusters can push:

- Start with total weight under 100 tons
- 2 thrusters push 100 tons at ~50 km/s (enough to reach any inner planet)
- Double thrusters for every 100 tons above that
- The thruster tip: place fuel tanks directly adjacent to thrusters. No pipes needed. Pipe runs between fuel production and thrusters are fine, but the last connection to the thruster should be direct tank-to-thruster.

**Weight budget for a 100-ton platform:**
| Component | Weight (tons) | Count |
|:----------|:-------------:|:-----:|
| Hub | 10 | 1 |
| Foundation | 0.5/tile | ~30 tiles |
| Crusher | 4 | 4 |
| Chemical plant | 3 | 2 |
| Assembler | 3 | 1 |
| Gun turret | 4 | 4 |
| Thruster | 12 | 2 |
| Accumulators | 1 | 10 |
| Bulk (belts/pipes/inserters) | ~4 | — |
| **Total** | **~85-95** | |

Under 100 tons, 2 thrusters, plenty of room for cargo.

{{< callout type="warning" >}}
**Traps People Keep Falling Into:** Ammo production is the silent killer. You calculate: "I have 100 red ammo, trip takes 2 minutes, turret fires once per second... I need 120 rounds" — but asteroids come in waves, not steady stream. Build for 3× your calculated ammo consumption for the trip length. Better to build a bigger ammo factory than to deadstick halfway to Gleba.
{{< /callout >}}

## Where Most Players Mess This Up

**Crushers in the wrong spot.** Collectors collect on the front edge. Belts run backward. Crushers where the belts end. If you place crushers too far from collectors, belts fill up with raw chunks and nothing gets processed.

**One thruster fuel tank.** The thruster fuel pump moves fuel fast. One storage tank empties before the trip is done. Build 3-5 tanks per thruster pair.

**No accumulator buffer.** During asteroid storms, power demand spikes. Turrets firing + crushers running + belts moving can spike past what the hub provides. 10 accumulators keep everything running through the storm.

**Belts in the firing line.** Ammo belts that pass directly in front of turret range will get destroyed by stray asteroid fragments. Run ammo belts behind the turrets.

## Scaling Past the First Platform

**Inner planet routes** (Nauvis → Vulcanus/Fulgora): 100-ton platform, 2 thrusters, 4 turrets. Simple.

**Outer planet routes** (to Gleba/Aquilo): Need 300+ tons, 6+ thrusters, 12+ turrets. Build a second, larger platform. Don't try to retrofit the first one — the weight penalty kills speed.

**Rocket transport:** Already launched a platform and forgot something? Pack it in a rocket. Launched platforms are persistent — they stay in orbit of whatever planet they're at. Just launch a resupply rocket.

---

## Community Verification & Resources

- [Official Wiki — Space Platform](https://wiki.factorio.com/Space_platform) — exact thruster fuel formulas, speed calculations, and platform hub mechanics
- [Factorio Forums — Space Age Discussion](https://forums.factorio.com/viewforum.php?f=69) — community platform blueprints and bug reports
- [Steam Guide — Platform Design Compendium](https://steamcommunity.com/sharedfiles/filedetails/?id=3278846547) — tested builds for all planet routes including Aquilo
- [Alt-F4 Blog](https://alt-f4.blog/) — deep dives on Space Age mechanics and platform optimization
