---
title: "Aquilo Landing Preparation - What to Bring and How to Survive in Factorio Space Age"
date: 2026-06-20
tags: ["space-age", "planets"]
draft: false
---

{{< callout "tip" >}}
**Aquilo survival at a glance:** Bring heating towers, rocket fuel, ice platforms, rocket turrets, and energy weapons. Land only after you have unlocked all previous planet sciences. Build a heat pipe grid first, then power, then defense, then science. Aquilo has no local resources except frozen ammonia -- everything else must be imported from other planets.
{{< /callout >}}

{{< section "When to Go to Aquilo" >}}

Aquilo is the fifth planet you should visit (after Vulcanus, Fulgora, Gleba, and Nauvis upgrades). Do not attempt Aquilo until you have:

- All 4 planet sciences (metallurgic, electromagnetic, agricultural, and your Nauvis sciences) producing consistently
- A robust [space platform]({{< ref "/space-age/space-platform-guide" >}}) that can survive the trip through the asteroid belts to reach Aquilo orbit
- Heating tower technology unlocked (from earlier planet research)
- Production capacity to ship bulk resources via cargo rocket

| Prerequisite | Minimum Level | Why It Matters |
|-------------|:------------:|----------------|
| Space platform durability | Uncommon quality + | Aquilo route has dense asteroid fields |
| Rocket fuel production | 1000+ in storage | You will ship massive quantities |
| All planet sciences | Tier 1 completed | Aquilo tech requires previous planet research |
| Turret upgrades | Damage 6+ | Strafers are fast and hit hard |

{{< /section >}}

{{< section "What to Bring to Aquilo" >}}

{{< diagram "diagrams/aquilo-checklist.svg" "Aquilo survival essentials showing what to bring, threats to face, and build order for the frozen planet" "760" >}}

Aquilo has zero local resources except frozen ammonia (and even that is limited). Pack everything. These items are not optional:

| Category | Items | Quantity | Use |
|---------|-------|:--------:|-----|
| Heat | Heating towers | 4-6 | Prevent buildings from freezing |
| Fuel | Rocket fuel / Solid fuel | 2000+ | Fuel for heating towers and power |
| Defense | Rocket turrets | 10-15 | Anti-strafer main defense |
| Defense | Laser turrets | 10-20 | Backup defense, free ammo |
| Defense | Rocket ammo | 1000+ | Feeds rocket turrets |
| Expansion | Ice platforms | 200+ | Buildable surface on frozen water |
| Construction | Solar/Accumulators | 50+ | Solar works (low light but stable) |
| Construction | Assemblers/Chem plants | 20+ | Base production infrastructure |
| Transport | Cargo rocket parts | 100+ | Return to Nauvis when done |

{{< callout "warning" >}}
**Aquilo has no:** iron ore, copper ore, coal, stone, oil, or water (only frozen ammonia lakes). Your entire factory must be fed by cargo rockets from other planets. Every belt, assembler, and ammunition shipment must be planned before you land.
{{< /callout >}}

{{< /section >}}

{{< section "Build Order on Aquilo" >}}

**Phase 1: Heat grid (immediate)**
Land and build a heating tower immediately. Connect it to heat pipes that radiate through your base. Without heat, buildings work at reduced speed. In sub-zero conditions, unheated assemblers stop entirely within 60 seconds.

- Place one heating tower per 30-40 buildings
- Burn rocket fuel or solid fuel (rocket fuel has 2x the heat value)
- Run heat pipes in a grid pattern. Each heat pipe segment radiates heat to adjacent buildings within 2 tiles

**Phase 2: Power**
Heating towers double as power generators through steam turbines. Pump water from frozen ammonia -- heat it with the tower, run it through turbines, then pipe the steam around.

- 4 heating towers with turbines generate roughly 20-30 MW
- Supplement with imported nuclear fuel if your power demands exceed 50 MW
- Store steam in tanks for surge capacity

**Phase 3: Defense perimeter**
Strafers are flying biters that ignore walls and attack from range. Rocket turrets are the primary counter. Place them in overlapping fields around your base perimeter. Laser turrets work well as secondary coverage because freezing slows strafers but does not reduce laser damage.

- 10 rocket turrets cover a small island base completely
- Add laser turrets for the gaps between rocket fields
- Belt-feed rockets from a central ammo assembler

**Phase 4: Science production**
The Aquilo-specific science pack (cryogenic science or similar) requires cryogenic plant processing. Research the heat-related upgrades first, then science production.

{{< /section >}}

{{< section "Strafers and How to Handle Them" >}}

| Threat | HP | Damage | Counter | Priority |
|--------|:--:|:------:|---------|:--------:|
| Small strafer | 500 | 15/shot | Rocket turret x3 | Medium |
| Medium strafer | 1500 | 25/shot | Rocket turret x5 | High |
| Large strafer | 5000 | 40/shot | Rocket + laser turrets | Critical |

Strafers spawn from nests on the ice. They path directly toward your heat sources. If you have a single large heating tower without turret coverage, expect a wave of strafers converging on it within 20 minutes of setup.

**Key strategy:** Rocket turrets outrange strafers. Build them at your perimeter so strafers enter rocket range before they can fire on your buildings. Keep a repair pack ready -- strafer attacks happen in waves (3-5 strafers per wave on Aquilo normal difficulty).

If you have [flamethrower defense]({{< ref "/defense/flamethrower-defense-guide" >}}) experience from Nauvis, note that strafers take reduced fire damage. Stick to kinetic (rocket turrets) and laser.

{{< /section >}}

{{< section "Shipping Logistics" >}}

| Resource | Shipped From | Frequency | Amount per Shipment |
|----------|-------------|:----------:|:------------------:|
| Rocket fuel | Nauvis | Every 30 min | 200-500 |
| Iron/copper plates | Nauvis | Every hour | 1000 each |
| Turrets/ammo | Nauvis | Before waves | 500 rocket ammo |
| Ice platforms | Nauvis or platform | On expansion | 100 at a time |
| Science packs | Aquilo | To Nauvis | 500-1000 at a time |

Use cargo rockets rather than space platform drop pods for bulk supply. The Aquilo orbit route is dangerous for space platforms without heavy defense.

{{< /section >}}

{{< section "Bottom Line" >}}

Aquilo is the survival exam of Factorio Space Age. It forces you to manage heat distribution, import every resource, and defend against a fast new enemy type. The payoff is the cryogenic science tree, which unlocks fusion power and the final victory condition. If you can survive Aquilo's first 2 hours, you can beat Space Age.

**Planet order review:** Vulcanus first (foundry), then Fulgora (quality), then Gleba (bioflux), then return to Nauvis to scale up, and finally Aquilo. See the [planet order guide]({{< ref "/space-age/planet-order-guide" >}}) for the full progression path.

{{< /section >}}

{{< section "Community Verification" >}}

- [Factorio Wiki: Aquilo](https://wiki.factorio.com/Aquilo) -- Planet surface data and hazards
- [Factorio Wiki: Heating tower](https://wiki.factorio.com/Heating_tower) -- Heat mechanics and fuel ratios
- [Factorio Wiki: Strafer](https://wiki.factorio.com/Strafer) -- Enemy stats and engagement ranges

{{< /section >}}