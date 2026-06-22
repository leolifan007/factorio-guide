---
title: "Gleba Pentapod Defense — Turret Placement and Spore Management Strategy"
description: "Gleba pentapod defense guide for Factorio Space Age. Spore management, turret layouts, wall design, and the defense strategy that keeps your Gleba base safe."
date: 2026-06-20
tags: ["space-age", "gleba", "defense"]
draft: false
emoji: "🛡️"
aliases:
  - /space-age/gleba-pentapod-defense/
---

Gleba's enemies are different. Unlike Nauvis biters that live in nests and expand slowly, pentapods spawn directly from the terrain when they detect your spore cloud. If your Gleba defense fails, it's because you attracted too many pentapods with too much processing — not because your walls were weak.

This guide covers the full pentapod defense strategy: spore management, turret selection, wall design, and the defense-in-depth layout that keeps your Gleba base running indefinitely. Pair this with {{< ref "/space-age/gleba/bioflux-production" >}} to understand the root cause of spore generation.

{{< callout "tip" >}}
**TL;DR:** Process fruit as far from your main base as possible. Use rocket turrets + red ammo gun turrets behind walls. Pentapods push through walls like they're not there — use multiple wall layers with repair coverage. Defense-in-depth with three perimeter zones. Spore management is more important than firepower.
{{< /callout >}}## Defense Summary

| Layer | Turret | Ammo | Range | Best Vs |
|:------|:-------|:-----|:-----:|:--------|
| Inner | {{<material "rocket-launcher">}} Rocket turret | Explosive | 36 | Large |
| Middle | {{<material "gun-turret">}} Gun turret | Uranium | 24 | Medium |
| Outer | {{<material "land-mine">}} Landmines | 鈥?| 鈥?| First wave |

## How Pentapod Spawning Works

Pentapods don't have nests like biters. Instead:

1. **Your base emits spores** — every fruit processing operation, every bioflux assembly, every nutrient production line
2. **The spore cloud spreads** — visible on the map as a green haze around your base
3. **Pentapods spawn from the ground** — anywhere within the spore cloud, or just outside it, pentapod spawners appear
4. **More processing = bigger cloud = more pentapods** — the relationship is roughly linear: double your fruit processing, double your pentapod spawn rate

The critical difference from biters: pentapod spawning is proportional to your base activity, not to time. You can exist on Gleba indefinitely with no attacks if you process nothing. The moment you start processing fruit, the clock starts.

{{< diagram "diagrams/space-age/pentapod-defense-layout.svg" "Gleba pentapod defense layout with turret positions, wall design, and spore-aware base placement" "760" >}}

### Pentapod Enemy Stats

| Unit | Health | Damage | Speed | Special |
|:-----|:------:|:------:|:-----:|:--------|
| Small pentapod | 200 | 12 | Fast | Basic melee |
| Medium pentapod | 600 | 25 | Fast | Can push through single walls |
| Big pentapod | 2,000 | 60 | Medium | Destroys walls in 3 hits |
| Strafer | 750 | 30 | Very fast | Ranged attack, moves sideways |
| Spawner | 1,500 | — | Stationary | Summons pentapods if not destroyed |

{{< callout type="info" >}}
**Strafer threat:** Strafers are the most dangerous pentapod unit. Their ranged attack outruns gun turrets and their sideways movement makes them hard to hit. They appear mid-game (after 30-60 minutes of processing) and require active defense — walls alone won't stop them.
{{< /callout >}}

## Spore Management — Your First Defense

Before you fire a single bullet, manage your spores. Spore radius is directly tied to your processing volume:

| Bioflux per minute | Spore cloud radius | Pentapod spawn rate |
|:------------------:|:------------------:|:-------------------:|
| 0 (idle) | 0 | None |
| 50 | ~60 tiles | Low — occasional small packs |
| 200 | ~150 tiles | Medium — regular attacks |
| 500+ | ~300+ tiles | High — constant waves with big pentapods |

### Fruit Processing Location

**Put fruit processing away from your main base.** The single most effective defense strategy on Gleba is spatial separation:

- **Build your fruit processing 200+ tiles** from your main Nauvis base on the same planet
- **Ship bioflux** to your main base by belt or bot — bioflux has negligible spore output
- **Keep all nutrient production** near the processing area, not the main base
- **Use a separate electric network** — power poles don't carry spores, but the processing infrastructure does

This creates a "bait" zone where pentapods attack the processing area instead of your science and mall. That processing area needs defenses, but it's cheaper to defend one heavy-attack zone than your entire base.

### Efficiency vs Visibility

**Run the most efficient recipes you can.** The greener (productivity) your setup, the fewer fruit you process per unit output, which means fewer spores per science pack:

- Use bioflux → nutrients (5:1 ratio biomass per nutrient) instead of spoilage → nutrients (1:1)
- Use bioflux → rocket fuel for fuel (more efficient than advanced oil processing)
- Use the best fruit processing recipes (prod modules in biochambers)

**What not to do:** Don't try to hide your operation. There's no stealth mechanic — spores are purely additive. A small base processing 50 fruit/min has a tiny spore cloud, but a big base processing 500 fruit/min has a huge one. The only way to reduce spores is to process less or process more efficiently.

## Turret Types vs Pentapods

Pentapods have different weaknesses than biters. Here's how each turret type performs:

| Turret | vs Small Pentapods | vs Big Pentapods | vs Strafers | Notes |
|:-------|:-----------------:|:----------------:|:-----------:|:------|
| **Gun turret** (red ammo) | ⭐⭐⭐ Excellent | ⭐⭐ Good | ⭐ Medium | Cheap, reliable, damage research scales well |
| **Gun turret** (yellow ammo) | ⭐⭐ Good | ⭐ Weak | ⭐ Weak | Use red ammo always on Gleba |
| **Rocket turret** | ⭐⭐⭐ Excellent | ⭐⭐⭐ Excellent | ⭐⭐⭐ Excellent | Best all-rounder, expensive ammo |
| **Laser turret** | ⭐ Medium | ⭐ Weak | ⭐ Weak | Power-hungry, pentapods resist laser |
| **Flamethrower turret** | ⭐⭐ Good | ⭐⭐⭐ Excellent | ⭐ Medium | Oil cost, pentapods don't burn well → Strafers dodge |
| **Landmines** | ⭐⭐⭐ Excellent | ⭐⭐ Good | ⭐⭐⭐ Excellent | Cheap, mass-kill, self-repair needed |

**The winning combination:** Rocket turrets for the heavy hitters, gun turrets with red ammo for volume, landmines in front of walls as a first-strike layer.

### Why Not Lasers?

Pentapods have higher laser resistance than biters (~20% vs ~10%). Combined with Gleba's limited power (your heating tower doesn't run boilers), lasers drain your grid and kill pentapods slowly. Use them only in low-threat zones near your processing outpost, and only with solar backup.

## Wall and Defense Line Design

Pentapods move differently than biters. They don't path around walls — they push through them.

### The Pentapod Wall Crush Mechanic

When pentapods reach a wall, they attack it. But unlike biters that attack one wall at a time, pentapods (especially big ones and strafers) can push through multiple walls by:

1. **Rearranging behind walls** — if a pentapod is blocked by a wall and there's another wall behind it, it may glitch-push through both
2. **Big pentapod AoE** — big pentapods damage all adjacent walls simultaneously, creating breaches faster
3. **Strafer clipping** — strafers sometimes clip through corners because of their sideways movement hitbox

### The Defense-in-Depth Layout

**Do not build a single wall.** Single walls are a speed bump, not a defense. Use three layers:

```
Outer zone: Landmines + walls (1 thick)
    ↓
Middle zone: Empty gap (3-5 tiles) + gun turrets
    ↓
Inner zone: Walls (2 thick) + rocket turrets + roboport repair coverage
```

**Layer 1 — Landmine field:** Place landmines 5-8 tiles in front of your outer wall. Pentapods trigger them on approach, softening the wave before it reaches your wall. Combine with repair packs from a roboport to automatically replace triggered mines.

**Layer 2 — Outer wall + gun turrets:** A single-thickness wall, with gun turrets (red ammo) every 6 tiles. This slows the initial wave and kills small/medium pentapods. The wall WILL be breached — that's fine, it's sacrificial.

**Layer 3 — Kill zone + inner wall:** A 3-5 tile gap between outer and inner walls. This gap is your kill zone. Rocket turrets every 8 tiles, gun turrets every 4 tiles in the gap. Inner wall is double thickness with reinforced doors for your repair bots.

{{< callout "tip" >}}
**Roboport coverage is mandatory.** Without repair coverage, your walls last 3 minutes. With a roboport network and 100+ repair packs, your walls last indefinitely. Place roboports so that every wall tile is within construction bot range.
{{< /callout >}}

### Turret Spacing by Threat Zone

| Zone | Primary turret | Spacing | Secondary | Notes |
|:-----|:--------------|:-------:|:----------|:------|
| **Heavy attack** (near processing) | Rocket turret | Every 6 tiles | Gun turret | Highest pentapod density |
| **Medium attack** (base perimeter) | Gun turret (red) | Every 4 tiles | Rocket turret | Overlapping fire zones |
| **Light attack** (far corners) | Gun turret (red) | Every 6 tiles | Laser | Low threat, low investment |

## Complete Gleba Defense Blueprint

Here's the full build order for a self-sustaining Gleba defense:

**Phase 1 — Landing (first 10 minutes):**
- 10-20 gun turrets with yellow ammo
- Single wall around your initial processing
- Manual ammo feeding from the hub

**Phase 2 — Early production (30 minutes):**
- Move to red ammo
- Expand wall to enclose processing + fruit patches
- Add first roboport with 50 repair packs
- Set up automated ammo production from Gleba's coal/iron

**Phase 3 — Mid-game expansion (1-2 hours):**
- Build separate fruit processing outpost 200+ tiles from main base
- Rocket turrets on the processing outpost
- Defense-in-depth layout (3 layers) on the processing outpost
- Main base: gun turrets + single wall (low threat)
- Automated landmine replacement via belt from assembler

**Phase 4 — Late game (sustainable):**
- Full defense-in-depth on all perimeters
- 50+ rocket turrets on processing outpost
- Circuit-controlled ammo resupply (request when < 2,000 rounds)
- Artillery for clearing distant spawners (optional — they grow back)

{{< callout type="info" >}}
**Gleba defense varies by your processing volume.** A small base (50 bioflux/min) needs 10 gun turrets. A megabase (1,000 bioflux/min) running full science needs 100+ rocket turrets just for the processing outpost. Scale your defense to your production, not the other way around.
{{< /callout >}}

## Common Defense Mistakes

**Mistake 1: Defending your whole base equally.** Don't. Your fruit processing attracts 80% of attacks. Defend the processing outpost heavily and your main base lightly. Save your resources.

**Mistake 2: Using only gun turrets.** Gun turrets are great against small pentapods. Against big pentapods and strafers, you need rockets. Mix your turret types or lose walls constantly.

**Mistake 3: Not enough repair packs.** A pentapod assault can damage 20+ wall segments. If you have 5 repair packs in your network, the bots run out and your wall falls. Stock 200+ repair packs per defense zone.

**Mistake 4: Processing fruit inside your main base.** Your main base (science, mall, labs) needs minimal spore output. Build a separate processing outpost. If you process fruit inside the base perimeter, pentapods attack your science — the attack frequency doubles.

**Mistake 5: Forgetting ammo supply.** Gleba's iron is limited and shared with your bacteria production. Build additional iron production specifically for ammo. A rocket ammo assembler eats 10 iron/sec at full speed. Without dedicated iron, your defense starves.

## Summary

Gleba pentapod defense follows a different philosophy than Nauvis biter defense:

- **Spores are the root cause** — process efficiently, separate processing from base
- **Rocket turrets are your best friend** — nothing kills big pentapods faster
- **Defense-in-depth is mandatory** — single walls are a speed bump
- **Repair coverage keeps walls alive** — without roboports, your walls die
- **Scale defense to production** — more bioflux means more pentapods

For the full Gleba production guide including how to set up bioflux and bacteria, read the [Gleba Survival Guide]({{< ref "/space-age/gleba/gleba-survival-guide" >}}). For an in-depth look at bioflux production and efficiency, see our [Bioflux Production Guide]({{< ref "/space-age/gleba/bioflux-production" >}}). And if you're visiting Vulcanus first, the [Vulcanus Guide]({{< ref "/space-age/guide/vulcanus-guide" >}}) covers the foundry and big miner tech you'll need later.
