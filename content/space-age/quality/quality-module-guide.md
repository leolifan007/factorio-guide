---
title: "Quality Modules — Space Age New Mechanic Explained"
description: "How the Quality module system works in Factorio Space Age. Tiers, probabilities, and how to build a quality production line."
date: 2026-05-18
tags: ["space-age", "quality", "modules", "space-age"]
emoji: "💎"
aliases:
  - /space-age/quality-module-guide/
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#1a0a3a,#0a1a3a);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:0.5rem;margin-bottom:1.5rem;">
<span style="font-family:Orbitron,sans-serif;font-size:1.2rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#666;color:#fff;">COMMON</span>
<span style="font-family:Orbitron,sans-serif;font-size:1.2rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#2ecc71;color:#fff;">UNCOMMON</span>
<span style="font-family:Orbitron,sans-serif;font-size:1.2rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#3778c8;color:#fff;">RARE</span>
<span style="font-family:Orbitron,sans-serif;font-size:1.2rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#9b59b6;color:#fff;">EPIC</span>
<span style="font-family:Orbitron,sans-serif;font-size:1.2rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#e67e22;color:#fff;">LEGENDARY</span>
</div>

## What Is Quality?

In Space Age, items can have **5 quality tiers**. Higher quality items work better — {{< material "quality-module" >}} quality modules are the gateway to this whole system. For the upcycling loop design, see {{< ref "/space-age/quality/upcycling-loop" >}}.

| Tier | Color | Bonus | Effective Effect |

| Tier | Color | Bonus | Effective Effect |
|------|-------|--------|:----------------:|
| Common (1) | Gray | Baseline | 1x |
| Uncommon (2) | Green | +20% speed, −20% energy | 1.2x faster, 0.8x power |
| Rare (3) | Blue | +40% speed, −40% energy, +2 range | 1.4x faster, 0.6x power |
| Epic (4) | Purple | +60% speed, −60% energy, +4 range | 1.6x faster, 0.4x power |
| Legendary (5) | Orange | +80% speed, −80% energy, +6 range, +2 AoE | 1.8x faster, 0.2x power |

### What Each Tier Unlocks

**Uncommon (Green)** — Your entry point into quality. A single quality module 1 in an assembler gives a 1% chance. At this tier you start accumulating quality gears, circuits, and other intermediates. Use them to build your first uncommon assemblers and miners — the speed boost is noticeable.

**Rare (Blue)** — The practical tier. Rare {{< material "speed-module" >}} speed modules in beacons have a major impact. Rare assemblers with rare modules produce significantly more per machine. This is the tier most mid-game factories should target: it's achievable without dedicated upcycling loops.

**Epic (Purple)** — The commitment tier. Reaching epic consistently requires a dedicated upcycling loop with quality module 3s and recyclers. Epic {{< material "assembler" >}} assemblers with epic modules are the backbone of endgame science production.

**Legendary (Orange)** — The ultimate tier. Legendary items are 1.8x faster and consume 80% less energy. A legendary beacon with legendary speed module 3s affects nearby machines 3.2x more than a common one. The upcycling loop required to reach legendary is complex but deeply rewarding.

## How Quality Is Generated

**Quality modules** in assemblers/machines give a chance for the output to be a higher quality tier.

| Module | Quality Chance | Speed Penalty | Max Chance (4 slots) |
|--------|:--------------:|:-------------:|:--------------------:|
| Quality module 1 | 1% per module | −10% | 4% |
| Quality module 2 | 5% per module | −15% | 20% |
| Quality module 3 | 10% per module | −20% | 40% |

<div class="warning-box">
<strong>Important:</strong> Quality modules <em>slow down</em> production. The speed penalty applies per module, so 4 quality module 3s in an assembler reduce speed by 80%. Always balance quality chance against production speed.
</div>

### Cumulative Quality Probability Table

When multiple quality modules are stacked, the quality chance compounds. Here's the effective probability per craft for reaching **each tier**:

| Configuration | Uncommon | Rare | Epic | Legendary |
|:--------------|:--------:|:----:|:----:|:---------:|
| 1× QM1 | 1% | 0.01% | — | — |
| 2× QM1 | 2% | 0.02% | — | — |
| 4× QM1 | 4% | 0.04% | — | — |
| 1× QM2 | 5% | 0.25% | 0.01% | — |
| 2× QM2 | 10% | 1% | 0.05% | — |
| 4× QM2 | 20% | 4% | 0.4% | 0.02% |
| 1× QM3 | 10% | 1% | 0.1% | 0.01% |
| 2× QM3 | 20% | 4% | 0.8% | 0.08% |
| 4× QM3 | 40% | 16% | 6.4% | 1.28% |

As you can see, a single quality module 3 has a 1% chance per craft to produce a rare item. Four of them push that to 16%. And the chance to produce a legendary from scratch is only 1.28% — that's why the upcycling loop is essential.

{{< diagram "diagrams/space-age/quality-upcycling-loop.svg" "Quality module tier progression from common to legendary via the recycler upcycling loop" "760" >}}

## Building a Quality Production Line

### The Recycler Trick

In Space Age, **recyclers** break items back into raw materials. But they also have a chance to **upgrade** the item's quality!

1. Build an assembler with **quality modules**
2. Output goes to a **recycler**
3. Recycler has a chance to output **higher quality** version
4. Sort the output by quality using **quality filters** on inserters

### Quality Filter Inserters

Inserters can be set to only pick up items of a specific quality:
1. Select the inserter
2. Click the **quality filter** button
3. Choose which quality tier to pick up

Quality modules pair naturally with [Fulgora’s scrap recycling]({{< ref "/space-age/fulgora/fulgora-recycling-guide" >}})—recyclers can upgrade item quality while breaking scrap down. Here’s what to prioritize:

## Which Items to Upgrade First?

Priority list for quality:

| Priority | Item | Why |
|----------|-------|------|
| 1 | **Beacons** | More beacons = more speed modules affecting machines |
| — | **Space platform thrusters** | Rare thrusters use less fuel—see [Space Platform Guide]({{< ref "/space-age/platform/space-platform-guide" >}}) |
| 2 | **Speed modules** | Faster machines = more production |
| 3 | **Electric furnaces** | Faster smelting = more plates |
| 4 | **Miners** | More mining speed = more ore |
| 5 | **Power armor** | Better defense and equipment |

## The Quality Upcycling Loop

To reach {{< material "quality-module" >}} epic and legendary tiers consistently, you need a **quality upcycling loop**:

1. **Feed** common items into an assembler with quality modules
2. **Recycle** the output using a {{< material "recycler" >}} recycler also equipped with quality modules
3. **Filter** higher-quality items into separate chests (use quality-filtered inserters)
4. **Loop** common-quality outputs back into the assembler

The recycler has a 25% chance per recipe to _not_ return the item — it simply deletes it. But when it does return materials, each material has its own independent quality upgrade chance based on the recycler's quality modules. This creates a cascading probability:

### Probability Cascade (4× QM3 in Both Assembler and Recycler)

| Step | Common → Uncommon | Common → Rare | Common → Epic | Common → Legendary |
|:-----|:-----------------:|:-------------:|:-------------:|:------------------:|
| Assembler output | 40% uncommon | 16% rare | 6.4% epic | 1.28% legendary |
| Recycler (of common) | 10% uncommon | 4% rare | 1.6% epic | 0.32% legendary |
| Combined per cycle | ~50% → uncommon | ~20% → rare | ~8% → epic | ~1.6% → legendary |

This means roughly 1 in 60 items turned through the loop will emerge as legendary. Scale up to get there faster.

## Quality on Space Platforms

Quality modules work **only in machines**, not in space platform crushers or furnaces. However, you can use quality {{< material "assembler" >}} assemblers on platforms to craft quality ammo, fuel, and building materials. A common strategy:

1. Build a small quality loop on Nauvis to produce rare/epic platform parts
2. Launch those quality parts to orbit
3. Use quality thrusters and engines on your platform for fuel efficiency

Rare+ thrusters consume significantly less fuel per trip, making deep-space travel to Aquilo and beyond much more feasible.

## When to Start Quality

| Game Phase | Quality Goal | Method |
|:-----------|:------------:|:-------|
| Early Nauvis (pre-rocket) | Ignore for now | Focus on throughput, not quality |
| First planet visited | Start with QM1s on key intermediates | Stick 1-2 QM1s in gear/circuit production |
| Fulgora established | Build first dedicated quality loop | Scrap recycling naturally gives quality items |
| Post-inner planets | Scale to QM3 upcycling | Dedicated loop with full quality infrastructure |
| Megabase (100+ SPM) | Target legendary everything | Multiple parallel loops with circuit control |

The golden rule: **don't optimize quality before you have quantities.** Get your base running at 30-60 SPM on all sciences before investing heavily in quality upcycling.

### Tips and Pitfalls

- **Use circuit conditions** on inserters to prevent mixed-quality chests
- **Quality-filtered logistics requests** in requester chests let you specify legendary items for your mall
- **Speed beacons counteract** the speed penalty from quality modules — place beacons around quality assemblers
- **Don't quality-loop everything** — focus on items with high crafting cost and high impact (modules, beacons, furnaces)
- **Recyclers lose 75% of items**, so choose looped items carefully

**Next:** [Space Age Overview]({{< ref "/space-age/" >}}) — all new planets and mechanics.
