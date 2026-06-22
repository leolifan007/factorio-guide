---
title: "Space Platform Ship Design for All Planets — Asteroid Defense and Fuel Ratios"
description: "Space platform ship design for Factorio Space Age. Asteroid defense layouts, fuel-to-thruster ratios, ammo throughput, and designs for every planet route."
date: 2026-06-20
tags: ["space-age", "space-platform", "strategy"]
draft: false
emoji: "🚀"
aliases:
  - /space-age/space-platform-ship-design/
---

Your first space platform coasts on Nauvis orbit — slow, bulky, barely armed. It made the trip to Fulgora but almost didn't brake in time. The next planet is farther. The asteroids are bigger. The fuel runs out faster. You need a ship design that works for every route: from the calm Nauvis hub to the asteroid hell of the Aquilo run.

Here are three proven ship layouts, matched to planet routes, fuel ratios, and defense requirements. Start with {{< ref "/space-age/platform/space-platform-guide" >}} for platform fundamentals.

{{< callout "tip" >}}
**TL;DR:** Build three ships — not one. A 200-ton spine ship for inner planets (Nauvis ↔ Vulcanus/Fulgora), a 500-ton wide-body for Gleba, and a 1,000-ton fortress for Aquilo. Each needs different thruster ratios, ammo throughput, and collector placement. One ship does not fit all.
{{< /callout >}}## Ship Components

| Component | Function | Count | Weight | Fuel |
|:----------|:---------|:-----:|:------:|:----:|
| Hub | Core, storage | 1 | 10t | 鈥?|
| Thruster | Movement | 2-4 | 12t | {{<material "rocket-fuel">}} Fuel |
| Crusher | Asteroid | 4-6 | 4t | Power |
| Turret | Defense | 4-8 | 4t | {{<material "piercing-rounds-magazine">}} Ammo |

## Ship Layout Templates

### Layout 1: Spine Design (Inner Planets — 200 tons)

The spine design is a narrow, lightweight ship optimized for short inner-planet routes:

```
[Front]
⬡⬡⬡⬡⬡⬡⬡⬡  ← Asteroid collectors (8 on front edge)
⬡ ≡ 1 tile of foundation/platform

Front row:    [C][C][C][HUB][C][C][C]  → Collectors (C), Hub (HUB)
Row 2:        [T][T][__][__][__][T][T]  → Turrets (T)
Row 3:        [__][CR][CR][CR][CR][__]  → Crushers (CR), ammo/belt lines
Row 4:        [__][__][CH][CH][__][__]  → Chemical plants making fuel (CH)
Row 5:        [__][__][FT][FT][__][__]  → Fuel tanks (FT)
Row 6:        [__][__][TH][TH][__][__]  → Thrusters (TH)
[Back]
```

**Key specs:**
- Width: 7 tiles (narrow spine)
- Length: ~20 tiles
- Weight: ~200 tons
- Fuel: 2 thrusters, 3 fuel tanks each
- Defense: 4-6 gun turrets with piercing rounds
- Ammo: 1 assembler making ammo, fed by 2 iron crushers

The spine design keeps everything close to the hub. Belts are short. Fuel flows fast. Weight stays low.

### Layout 2: Wide Design (Gleba — 500 tons)

Gleba is the farthest inner planet. The wide design trades speed for cargo capacity and stronger defense:

```
[Front]
⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡⬡  ← 13 collectors across the front
[Front]

Row 1:  [C][C][T][T][C][C][HUB][C][C][T][T][C][C]
Row 2:  [T][T][__][__][__][__][__][__][__][__][T][T]
Row 3:  [CR][CR][CR][CR][__][AF][AB][__][CR][CR][CR][CR]
Row 4:  [__][CH][CH][__][__][__][__][__][__][CH][CH][__]
Row 5:  [__][FT][FT][__][__][FT][FT][__][__][FT][FT][__]
Row 6:  [__][TH][TH][__][__][TH][TH][__][__][TH][TH][__]
[Back]
```

AF = Ammo factory (front), AB = Ammo belt line

**Key specs:**
- Width: 13 tiles (wide platform)
- Length: ~25 tiles
- Weight: ~500 tons
- Fuel: 4 thrusters in pairs, 2 fuel tanks each
- Defense: 8 gun turrets, 2 rocket turrets for large asteroids
- Cargo: 3 dedicated cargo bays by the hub

The wide design uses a double-thruster row (4 thrusters total) to maintain speed at higher weight. Ammo production is duplicated on both sides for redundancy.

### Layout 3: Compact Fortress (Aquilo — 1,000 tons)

The Aquilo route has the densest asteroid fields. The compact fortress packs everything into a small footprint with maximum defense:

```
[Front]
Row 1:  [C][T][T][T][C][C][C][HUB][C][C][C][T][T][T][C]
Row 2:  [T][__][__][__][__][T][T][__][T][T][__][__][__][__][T]
Row 3:  [RT][__][CR][CR][CR][CR][__][__][__][CR][CR][CR][CR][__][RT]
Row 4:  [T][__][CH][CH][__][__][__][AF][__][__][__][CH][CH][__][T]
Row 5:  [__][__][FT][FT][FT][__][__][AB][__][__][FT][FT][FT][__][__]
Row 6:  [__][__][TH][TH][TH][TH][__][__][__][TH][TH][TH][TH][__][__]
[Back]
```

RT = Rocket turret, AF = Ammo factory, AB = Ammo belts

**Key specs:**
- Width: 15 tiles
- Length: ~30 tiles
- Weight: ~1,000 tons
- Fuel: 6 thrusters, 3 fuel tanks each
- Defense: 10 gun turrets, 2 rocket turrets, railgun for Aquilo asteroids
- Ammo: 4 assemblers making piercing rounds, 2 making rocket ammo

The compact fortress sacrifices cargo space for turret coverage. Every tile of frontage has overlapping turret fire. Two independent fuel lines run down both sides for redundancy.

{{< diagram "diagrams/space-age/ship-layout-templates.svg" "Three space platform layout templates for different planet routes" "760" >}}

## Asteroid Defense by Planet Route

Different routes have different asteroid compositions. Your defense needs to match what you'll encounter:

| Route | Small Asteroids | Medium Asteroids | Large Asteroids | Special Threat |
|:------|:---------------:|:----------------:|:---------------:|:--------------|
| Nauvis orbit | Carbonic (ice) | — | — | Almost nothing |
| Nauvis → Fulgora | Carbonic, metallic | Occasional metallic | Rare | None |
| Nauvis → Vulcanus | Carbonic, metallic | Metallic, carbonic | Occasional | None |
| Nauvis → Gleba | All 3 types | Common | Common | Carbonic chunks |
| Any → Aquilo | Dense all 3 | Very common | Very common | Promethium asteroids |
| Aquilo orbit | Extreme density | Constant | Frequent | Large promethium |

**Defense requirements per route:**

| Route | Gun Turrets | Rocket Turrets | Railguns | Ammo (per trip) |
|:------|:-----------:|:--------------:|:--------:|:----------------:|
| Inner planets | 4-6 | 0 | 0 | 400-800 rounds |
| Gleba | 8-10 | 2 | 0 | 2,000 rounds |
| Aquilo | 10-12 | 4 | 2 | 6,000+ rounds |

{{< callout type="info" >}}
**Quick Tip:** Carbonic asteroids (ice) are the most common type on outer routes. Crushing them yields water for fuel and carbon for ammo. Metallic yield iron for more ammo. A well-balanced crusher setup should have 2 crushers on ice crushing and 1-2 on metallic for every crusher on carbonic.
{{< /callout >}}

## Thruster Fuel Ratios and Tank Sizing

Each thruster consumes **fuel and oxidizer** at a 1:1 ratio. The thruster fuel pump max rates:

| Component | Fuel Throughput |
|:----------|:---------------:|
| Fuel pump | 1,200 fluid/sec |
| Pipe segment | 200-1,200 fluid/sec (depends on length) |
| Thruster inlet | 60 fluid/sec per thruster |

**Fuel required per trip (approximate):**

| Route | Distance | Fuel/Thruster | Total Fuel (4 thrusters) | Tank Storage Needed |
|:------|:--------:|:-------------:|:------------------------:|:-------------------:|
| Nauvis → Fulgora | Short | 1,000 units | 4,000 units | 2 fuel tanks |
| Nauvis → Vulcanus | Short | 1,200 units | 4,800 units | 2-3 fuel tanks |
| Nauvis → Gleba | Medium | 3,000 units | 12,000 units | 3-4 fuel tanks |
| Nauvis → Aquilo | Long | 6,000+ units | 24,000+ units | 5-6 fuel tanks |
| Fulgora → Aquilo | Very long | 8,000+ units | 32,000+ units | 6-8 fuel tanks |

**The fuel tank rule:** Place 1 storage tank directly adjacent to each thruster (pipe connection), plus 1-2 buffer tanks in the fuel production line. Total storage should cover 1.5× the calculated trip fuel to account for braking and maneuvering.

### Fuel Efficiency Upgrades

Quality thrusters make a massive difference. Rare thrusters consume 30% less fuel for the same thrust. Epic: -45%. Legendary: -60%. Converting your thrusters to legendary quality quadruples your effective range without adding weight. Our [Quality Module Guide]({{< ref "/space-age/quality/quality-module-guide" >}}) covers how to set up the quality recycling loop.

## Ammo Production Matching

Your ammo production must match incoming asteroid density. Here's the throughput math:

**Per gun turret (piercing rounds):**
- Fire rate: ~10 rounds/sec (with inserter speed limits)
- Damage per round: 10 (+ bonuses)
- Asteroid health: 50 (small), 200 (medium), 800 (large)
- Ammo consumed per turret per trip: ~50 per minute of combat

**Matching production to route needs:**

| Route | Asteroids/min | Turrets Needed | Crushers on Iron | Ammo Assemblers |
|:------|:-------------:|:--------------:|:----------------:|:---------------:|
| Inner planet | 8-15 | 4-6 | 1-2 | 1 |
| Gleba | 20-40 | 8-10 | 2-3 | 2 |
| Aquilo | 50-100+ | 10-12 | 4 | 4 |

A single assembling machine making piercing rounds produces ~75 rounds/min with speed module 1s. Two assemblers saturate a yellow belt entirely. For Aquilo, upgrade to red belt on the ammo line.

{{< callout type="info" >}}
**Quick Tip:** Feed ammo to turrets from behind, not in front. Ammo belts that pass in front of a turret's line of fire get hit by stray asteroid fragments and break. Run the ammo belt on the row behind the turrets and use inserters reaching forward. With long inserters, you can place assemblers two rows behind the turrets feeding ammo directly — no belts needed for the last 2 tiles.
{{< /callout >}}

## Planet-Specific Design Adjustments

### Vulcanus Route

The Vulcanus route has moderate asteroid density. The main risk is overheating on approach — keep your platform moving. No special design changes needed beyond the base spine layout. Your [Space Platform Guide]({{< ref "/space-age/platform/space-platform-guide" >}}) has the startup checklist.

### Fulgora Route

Short trip, low risk. The spine design works perfectly. Save weight by dropping to 2 fuel tanks — you only need 1,000 fuel per thruster for the round trip.

### Gleba Route

Medium distance with dense carbonic asteroids. Design changes:
- Add 2 extra collectors (carbonics are common — you need the carbon for ammo)
- Replace 2 gun turrets with rocket turrets for large asteroids
- Double the fuel storage (3,000 fuel/thruster vs 1,000 for inner planets)

### Aquilo Route

The most demanding route. Design changes:
- **Railguns are mandatory.** Large promethium asteroids have too much HP for gun turrets alone.
- **4+ crusher rows.** You need the ice for fuel and the carbon for railgun ammo.
- **Multiple ammo belts.** A single yellow belt of piercing rounds won't keep up. Run red belts or two parallel yellows.
- **Heating.** Aquilo is cold. Without heat pipes from a nuclear reactor, your hub freezes. The platform generates its own heat through the fusion reactor you should have before attempting this trip.

### Cross-Planet Logistics

Running cargo between planets requires dedicated haulers. Our [Cross-Planet Logistics Guide]({{< ref "/space-age/platform/cross-planet-logistics" >}}) covers cargo scheduling, landing pad allocation, and how to set up automated rocket resupply from platform to planet surface.

## Common Failure Modes

**Underestimating fuel.** "It's just to Gleba, I'll save weight with 1 fuel tank." You run out right before braking and overshoot. The ship flies past Gleba and you can't steer it back. Always add 50% fuel margin.

**One ammo line for 12 turrets.** A yellow belt carries 15 items/sec. With piercing rounds reloaded at 10/sec per turret, 4 turrets can drain a yellow ammo belt. For 8+ turrets, use red belts or two parallel yellows.

**Collectors too far back.** Collectors work best at the front of the platform. If placed 5+ tiles from the leading edge, they collect 60% fewer asteroids. Front-row collectors are non-negotiable.

**No redundant fuel line.** A single blocked pipe segment starves all thrusters. Run at minimum 2 fuel pipes and 2 oxidizer pipes spaced across the platform width. If one gets hit by an asteroid, the other keeps fuel flowing.

**Weight creep.** Every tile of foundation adds 0.5 tons. Every building adds 2-12 tons. A 300-ton ship needs 6 thrusters to move at the same speed as a 200-ton ship with 4. Before adding anything, ask: "does this need to be on the ship?" Leave non-essential manufacturing on the planet surface.

---

## Community Verification & Resources

- [Official Wiki — Space Platform](https://wiki.factorio.com/Space_platform) — exact thruster fuel formulas, speed calculations, and platform hub mechanics
- [Factorio Forums — Ship Design Thread](https://forums.factorio.com/viewforum.php?f=69) — community blueprints for all planet routes
- [Steam Guide — Platform Design Compendium](https://steamcommunity.com/sharedfiles/filedetails/?id=3278846547) — tested builds for all planet routes including Aquilo
- [Reddit r/factorio — Space Age Megabase](https://www.reddit.com/r/factorio/) — advanced ship designs and 1,000-ton cargo haulers
