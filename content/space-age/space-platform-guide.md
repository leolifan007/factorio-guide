---
title: Space Platform Build Guide — Design and Defense
description: Complete space platform guide for Factorio Space Age. Hub setup, thruster fuel ratios, asteroid processing, platform defense designs, and cargo management for interplanetary travel.
date: 2026-05-19
tags: ["space-age", "space-platform"]
draft: false
emoji: "🚀"
---

Your first space platform will probably explode. Mine did. Your second one will run out of fuel halfway to Gleba. Mine did that too. The third one might actually work if you know what you are doing.

A space platform is a ship that travels between planets. It needs propulsion, power, and the ability to handle asteroid collisions. The design space is wide open, but the constraints are tight. Here is everything I learned across three failed iterations and one successful one.

{{< callout "tip" >}}
**TL;DR:** A minimal platform needs a hub at the front, thrusters at the back, asteroid collectors on the sides, fuel processing in the middle, and walls around anything fragile. Design for the cargo bay first, then add thrusters to match the weight. The thruster-to-weight ratio is the only number that matters. Overbuild crushers — running out mid-journey is the most common failure.
{{< /callout >}}

{{< section "Platform Anatomy — Front to Back" >}}

Every platform has the same basic layout from front to back:

1. **Hub** — command center at the very front, manages cargo and provides initial power
2. **Asteroid collectors** — gather raw materials from space on both sides
3. **Crusher array** — processes asteroids into iron ore, copper ore, carbon, ice, and calcite
4. **Fuel production** — chemical plants making thruster fuel and oxidizer
5. **Fuel storage** — tanks for thruster fuel and oxidizer
6. **Thrusters** — propulsion units at the very rear

The hub must be at the front. The thrusters must be at the back with clear space behind them for the exhaust. Nothing can be placed directly behind a thruster — the exhaust flame damages buildings.

{{< diagram "diagrams/platform-layout.svg" "Space platform side view showing hub at front, collectors on sides, processing mid-section, and thrusters at rear" "700" >}}

Platform tiles come in two types: foundation (standard) and scaffolding (lightweight). Use scaffolding behind thrusters only — it is cheaper but has less health.

{{< section "Thruster Fuel Math" >}}

Thrusters consume thruster fuel (made from iron ore, calcite, and water) and oxidizer (made from iron ore and water). The consumption rate depends on how many thrusters are active and your speed setting.

Here is the fuel math for a medium-sized platform carrying 6 cargo bays:

| Component | Fuel per second | Oxidizer per second |
|-----------|:---------------:|:-------------------:|
| 1 thruster at cruising speed | 4.5 | 3.0 |
| 1 thruster at full burn | 12.0 | 8.0 |
| 4 thrusters at full burn | 48.0 | 32.0 |
| 4 thrusters at cruising | 18.0 | 12.0 |

A single chemical plant making thruster fuel supports about 2 thrusters at cruising speed. For 4 thrusters at full burn, you need 2 chemical plants for fuel and 2 for oxidizer.

{{< callout "tip" >}}
Do not run thrusters at full speed the whole trip. Pulse them. Full burn until you hit cruising velocity, then throttle to 50% for the rest of the journey. This halves fuel consumption and gives your crushers time to restock for the next burn.
{{< /callout >}}

I add 50% extra crusher capacity beyond what the math says. Running out of iron mid-journey is a disaster — your platform drifts with no way to repair.

{{< section "Asteroid Processing — In-Flight Supply Chain" >}}

Asteroids come in three types, each requiring a different crusher recipe:

- **Metallic asteroids** — crushed into iron ore (primary) and copper ore (secondary)
- **Carbonic asteroids** — crushed into carbon (primary) and coal (secondary)
- **Oxide asteroids** — crushed into ice (primary) and calcite (secondary)

Set up at least 6 crushers with circuit control:
- 2 metallic crushers feeding iron and copper into the production line
- 2 carbonic crushers feeding carbon into fuel production
- 2 oxide crushers feeding ice into water and calcite production

Wire each crusher type to a circuit network. If iron falls below 200, activate metallic collectors. If ice falls below 500, activate oxide collectors. This prevents resource starvation mid-journey.

Each crusher type produces waste products too. Metallic crushers produce stone byproduct. Carbonic crushers produce sulfur. Route these byproducts to their own storage and use them for ammo or disposal. A platform that ignores byproducts fills up in 10 minutes and stops.

{{< section "Thruster Configurations" >}}

Different thruster counts change your platform behavior significantly:

**2-thruster platform (minimal):**
- Good for short trips between nearby planets (Nauvis to Fulgora)
- Top speed: about 80 km/s
- Fuel consumption: low (1 chemical plant per fuel type)
- Best for: early-game exploration, supply runs

**4-thruster platform (standard):**
- Handles any interplanetary route
- Top speed: about 150 km/s
- Fuel consumption: medium (2 chemical plants per fuel type)
- Best for: general cargo transport, planet colonization

**8-thruster platform (freighter):**
- Fastest travel times between distant planets
- Top speed: about 220 km/s
- Fuel consumption: high (4 chemical plants per fuel type)
- Best for: bulk cargo between established bases, Aquilo runs

I start with 2 thrusters and upgrade to 4 once I need bulk transport between planets. The 2-thruster platform is cheap enough to build in the early Space Age phase.

{{< section "Asteroid Collector Placement" >}}

Asteroid collectors pull in passing asteroids. Their placement matters for coverage:
- Place 2 collectors on each side of the platform near the front
- Each collector covers about 6 tiles of the platform edge
- Collectors pick up asteroids within a 3-tile range of the platform
- Metallic and carbonic asteroids are more common near planets
- Oxide asteroids are more common in deep space between planets

Wire collectors to circuit conditions. Deactivate collectors when their resource type is full. This saves power and prevents belt clogging.

{{< section "Defense — Surviving the Asteroid Belt" >}}

Between planets, your platform passes through asteroid-dense regions. Without defense, asteroids impact your platform and cause hull damage.

**Minimum defense loadout:**
- 6 gun turrets covering the front and sides of the platform
- Red ammo (piercing rounds) for medium asteroids
- A dedicated ammo production line fed by carbonic asteroids

**Turret positioning:**
- Front: 3 turrets aimed forward (most common impact direction)
- Each side: 1 turret covering the flank (side impacts are less common)
- Rear: 1 turret covering the back (rare impacts from debris)

Walls protect critical components. Wall the hub and fuel tanks with at least one layer. Each wall segment absorbs one asteroid hit before needing replacement.

{{< diagram "diagrams/platform-defense.svg" "Space platform defense layout showing turret coverage zones around hub and fuel storage" "700" >}}

Ammo consumption during the Nauvis-to-Gleba journey is about 300 piercing rounds one way. That is roughly 2 assemblers running for 2 minutes before departure. Build a buffer of 500 rounds for safety.

{{< section "Cargo Bay Design and Expansion" >}}

The cargo bay determines how much you can carry between planets. More cargo bays equals more slots equals heavier platform equals more thrusters needed.

Good rule of thumb:
- 1 cargo bay per 100 stack size of your cargo
- 6 cargo bays for a first trip hauling building supplies
- 10+ cargo bays for bulk transport between established bases

My standard platform uses 6 cargo bays and 4 thrusters. This handles equipment drops at new planets and enough return cargo to be useful. For bulk transport, build a dedicated freighter with 20-plus cargo bays and 8 thrusters.

{{< section "Common Mistakes" >}}

**Building the platform too wide.** Wide platforms catch more asteroids. Keep the hub width at 5-7 tiles. Extend the platform lengthwise rather than adding width. A long thin platform is cheaper and safer than a short wide one.

**Not enough crushers.** Your platform starves mid-journey because crushers cannot keep up with thruster demand. Build 50% more crushers than your initial calculation suggests.

**Weak front armor.** Asteroids hit the front of the platform almost every time during interplanetary travel. Double-layer walls at the front save repair packs and prevent hull damage.

**Single fuel type.** You need both thruster fuel AND oxidizer. One without the other means zero thrust. Keep the production lines balanced.

**No circuit control.** Without circuits, resources pile up in one crusher type while another type starves. Use red wire circuits to balance asteroid distribution across crushers based on current inventory levels.

{{< section "FAQ" >}}

**Q: What is the minimum platform size for interplanetary travel?**
A: About 30 tiles long and 5 tiles wide. This fits 1 hub, 4 collectors, 6 crushers, fuel storage, and 2 thrusters.

**Q: Can I land the platform on a planet surface?**
A: No. The platform stays in orbit. Cargo is delivered to the surface via rocket or cargo pod.

**Q: How many thrusters do I need?**
A: 2 thrusters for a small cargo platform. 4 for a medium freighter. 8-plus for a bulk hauler.

**Q: Do platforms generate pollution?**
A: No. But thrusters create heat. Place heat pipes if you notice temperature buildup around the thruster array.

**Q: Can I upgrade a platform after building it?**
A: Yes. Platforms can be expanded by adding tiles, collectors, and thrusters. Build a module that you can scale.

{{< section "Related Guides" >}}

- [Master quality modules for the platform production line]({{< ref "space-age/quality-module-guide" >}})
- [Survive Gleba with an organized approach]({{< ref "space-age/gleba-survival-guide" >}})
- [Process Fulgora scrap on the platform for holmium]({{< ref "space-age/fulgora-recycling-guide" >}})
- [Use circuits to automate platform logistics]({{< ref "blueprints/circuit-network-guide" >}})
