---
title: "Quality Module Upcycling Loop — From Uncommon to Legendary Without Waste"
description: "Quality module upcycling loop design for Factorio Space Age. Recycling strategies, quality probability tables, optimal module tiers, and legendary equipment production."
date: 2026-06-20
tags: ["space-age", "quality", "modules"]
emoji: "⭐"
aliases:
  - /space-age/quality-module-upcycling/
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#1a0a2e,#2a1a0a);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:0.5rem;margin-bottom:1.5rem;">
<span style="font-family:Orbitron,sans-serif;font-size:1.2rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#666;color:#fff;">COMMON</span>
<span style="font-family:Orbitron,sans-serif;font-size:1.2rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#2ecc71;color:#fff;">UNCOMMON</span>
<span style="font-family:Orbitron,sans-serif;font-size:1.2rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#3778c8;color:#fff;">RARE</span>
<span style="font-family:Orbitron,sans-serif;font-size:1.2rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#9b59b6;color:#fff;">EPIC</span>
<span style="font-family:Orbitron,sans-serif;font-size:1.2rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#e67e22;color:#fff;">LEGENDARY</span>
</div>

In Space Age, quality modules let you craft items at higher tiers — uncommon, rare, epic, and legendary. But the odds of rolling a legendary item from common ingredients are **vanishingly small**. The solution? **Upcycling loops**: a closed-loop system where an assembler and recycler work together to repeatedly process items until they emerge at the desired quality tier. Start with {{< ref "/space-age/quality/quality-module-guide" >}} for the fundamentals of quality probability.

This guide covers the math, the machines, the optimal module loadout, and the items worth upcycling. By the end, you'll know exactly how to build a legendary production line without wasting a single resource.

{{< callout type="info" >}}
**Prerequisite:** This guide assumes you understand the basics of quality — the five tiers, the stat bonuses, and how quality modules work. If you need a refresher, start with {{< ref "/space-age/quality/quality-module-guide" >}}.
{{< /callout >}}## Quality Module Comparison

## Quality Module Comparison

| Tier | Icon | Quality Bonus | Prod Penalty | Best Use |
|:-----|:----|:------------:|:------------:|:---------|
| Quality 1 | {{<material "quality-module">}} | +1% | -5% | Start-up |
| Quality 2 | {{<material "quality-module">}} | +2% | -10% | Mid-game |
| Quality 3 | {{<material "quality-module">}} | +2.5% | -15% | End-game |
| Legendary Q3 | {{<material "quality-module">}} | +6.2% | -10% | Optimal |
| Tier | Quality Bonus | Prod Penalty | Best Use |
|:----|:------------:|:------------:|:---------|
| Quality 1 | +1% | -5% | Start-up |
| Quality 2 | +2% | -10% | Mid-game |
| Quality 3 | +2.5% | -15% | End-game |
| Legendary Q3 | +6.2% | -10% | Optimal |

## How the Upcycling Loop Works

The fundamental insight of upcycling is simple: **the recycler returns 25% of its input, and that 25% gets a fresh quality roll**. When paired with quality modules in both the assembler and recycler, each pass through the loop applies two independent quality checks — doubling your chances of a quality upgrade.

### The Loop

1. **Assembler** crafts an item with quality modules → outputs mixed-quality items
2. **Output belt** carries everything to a filter splitter or circuit filter
3. **Filter** sends higher-tier items (uncommon+) to storage, common items to the recycler
4. **Recycler** destroys 75% of the item, returns 25% at a fresh quality roll
5. **Return belt** feeds recycled common items back to the assembler input
6. Repeat until everything eventually reaches your desired tier

{{< callout "tip" >}}
The loop never stops — it's a steady-state system. Once you have enough legendary items, simply add more machines to scale production. The bottleneck is always the number of **recyclers** because they have 75% material loss per pass.
{{< /callout >}}

## Quality Probability Math

Understanding the odds is essential for designing efficient upcycling loops.

### Base Quality Probabilities

| Module Tier | Quality Chance per Module |
|-------------|--------------------------|
| Quality Module I | 1% |
| Quality Module II | 2% |
| Quality Module III | 2.5% |
| Legendary Quality Module III | 10% |

With 4 modules in a machine, the **effective quality chance** per craft is approximately 4× the module's per-module chance (the actual formula involves binomial probabilities, but linear approximation is close enough for practical design).

### Quality Roll Matrix

With 4 legendary quality module III (~10% effective per craft):

{{< diagram "diagrams/space-age/quality-upcycling-loop.svg" "Quality upcycling loop with assembler, recycler, and quality module placement" "760" >}}

| Input Tier | Common | Uncommon | Rare | Epic | Legendary |
|-----------|--------|----------|------|------|-----------|
| Common | 90.0% | 9.5% | 0.45% | 0.045% | 0.005% |
| Uncommon | — | 90.0% | 9.5% | 0.45% | 0.045% |
| Rare | — | — | 90.0% | 9.5% | 0.45% |
| Epic | — | — | — | 90.0% | 9.5% |

### Expected Crafts to Reach Each Tier

Starting from common items:

| Target Tier | Expected Crafts (one pass no recycler) | With Upcycling Loop |
|------------|--------------------------------------|---------------------|
| Uncommon | ~10 | ~8 |
| Rare | ~220 | ~70 |
| Epic | ~2,200 | ~600 |
| Legendary | ~20,000 | ~4,000 |

The upcycling loop reduces the expected number of crafts by **~5×** because each recycler pass gives you a fresh quality roll on the 25% that survives.

{{< callout type="info" >}}
These numbers assume legendary quality module III (10% per module). With lower-tier modules, the expected crafts roughly double for each tier step down. Never use quality module I or II in upcycling loops — the odds are too low to be practical.
{{< /callout >}}

## Optimal Module Tier Strategy

A common question: should you use rare quality modules to craft common items, or common quality modules to craft rare items?

### The Answer: Use the Highest Quality Modules You Have

Quality modules apply their bonus to every craft, regardless of the item's input tier. A legendary quality module III in an assembler crafting common gears gives the same quality chance as one crafting epic gears. **Always put your best quality modules in the step that processes the highest volume of crafts.**

### Module Priority

1. **Assembler (first pass):** This machine processes the most items. Put your best quality modules here — legendary > epic > rare. The higher quality modules in this machine roll more often on more items.
2. **Recycler:** Second priority. The recycler only processes 25% of items per pass, so its module quality has less impact on total throughput. Rare or epic modules here are usually adequate.
3. **Final assembly (direct legendary craft):** If you're building something from legendary components (like a legendary assembler), use high-quality productivity modules instead. The quality of the finished product is determined by its ingredients, not the assembler modules.

### Example: Legendary Blue Circuit Production

| Machine | Module Loadout | Notes |
|---------|---------------|-------|
| Assembler (green circuits) | 4× Leg QM3 | Highest volume — best modules here |
| Recycler (green circuits) | 4× Epic QM3 | Lower volume — good enough |
| Assembler (red circuits) | 4× Leg QM3 | Second-highest volume |
| Recycler (red circuits) | 4× Epic QM3 | |
| Assembler (blue circuits) | 4× Leg QM3 | |
| Recycler (blue circuits) | 4× Rare QM3 | Lowest volume — least important |

{{< callout "tip" >}}
Don't mix quality modules with productivity modules in the same machine. You can't use both simultaneously — the game forces you to choose. For upcycling loops, always use **quality modules** in both assembler and recycler.
{{< /callout >}}

## Item-by-Item Upcycling Guide

Not all items are equally worth upcycling. The best candidates are:

1. **Simple to craft** — Single-ingredient items with fast craft times
2. **High throughput** — Items your base already produces in volume
3. **Hard to legendary-craft directly** — Items with complex ingredient chains

### Best Items to Upcycle

#### Iron Gear Wheel ⚙
- **Why:** Extremely fast to craft (0.5s), single material (iron plate), used everywhere
- **Setup:** One gear assembler with 4× legendary QM3 can supply enough legendary gears for any base
- **Priority:** ⭐⭐⭐⭐⭐

#### Copper Wire ～
- **Why:** Also very fast (0.5s), high volume, needed for circuits
- **Note:** Foundry on Vulcanus can cast wire directly from molten copper — even better
- **Priority:** ⭐⭐⭐⭐⭐

#### Iron Stick 🟫
- **Why:** Fastest craft in the game (0.2s), trivial material cost
- **Priority:** ⭐⭐⭐⭐

#### Low Density Structure (LDS) 🛩
- **Why:** Slow to craft but **extremely valuable** at legendary quality. Legendary LDS halves the rocket cost
- **Note:** Best upcycled in a foundry using direct casting from molten metal (see {{< ref "/space-age/guide/vulcanus-guide" >}})
- **Priority:** ⭐⭐⭐⭐

#### Electronic Circuit (Green) 💚
- **Why:** The foundation of everything. Upcycle green circuits and use them to craft higher-tier items directly
- **Note:** A legendary green circuit → legendary red circuit → legendary blue circuit chain is the most scalable approach
- **Priority:** ⭐⭐⭐⭐⭐

#### Processing Unit (Blue) 💙
- **Why:** Slow to craft but used in the most critical items (rockets, modules, science)
- **Priority:** ⭐⭐⭐

### Items to Build Directly from Upcycled Components

**Don't upcycle these items — build them from legendary ingredients instead:**

| Item | Why Not to Upcycle |
|------|--------------------|
| Assembling Machines | Craft once from legendary ingredients. Upcycling loses 75% per pass |
| Modules | Craft from legendary circuits. A legendary module needs 10 legendary circuits |
| Furnaces | Single craft, minimal quantity needed |
| Mining Drills | Small quantities, craft from legendary gears and circuits |
| Belts | Not worth the module slots — belt quality effect is minimal |
| Inserters | Only worthwhile for the few inserters you care about (stack inserters at key points) |

For a complete guide to the scrap-based recycling economy, see {{< ref "/space-age/fulgora/fulgora-recycling-guide" >}} and {{< ref "/space-age/fulgora/scrap-overflow" >}}.

### Full Upcycling Comparison Table

| Item | Craft Time | Input Complexity | Legendary Value | Upcycle Priority |
|------|-----------|-----------------|-----------------|------------------|
| Iron Gear Wheel | 0.5s | ★☆☆ (1 mat) | High | ★★★★★ |
| Copper Wire | 0.5s | ★☆☆ (1 mat) | Medium | ★★★★★ |
| Iron Stick | 0.2s | ★☆☆ (1 mat) | Low | ★★★★☆ |
| LDS | 2.0s | ★★★☆ (3 mats) | Very High | ★★★★☆ |
| Green Circuit | 0.5s | ★★☆ (2 mats) | High | ★★★★★ |
| Red Circuit | 4.0s | ★★★ (3 mats) | Very High | ★★★☆☆ |
| Blue Circuit | 8.0s | ★★★★ (4 mats) | Critical | ★★★☆☆ |
| Steel Plate | 1.0s | ★☆☆ (1 mat) | Medium | ★★☆☆☆ |

## Legendary Equipment Priority

Once you have legendary items flowing, what should you build first? Not all equipment benefits equally from legendary quality.

### Tier 1: Massive Impact

**Legendary Quality Module III** — The single most important legendary craft. Each legendary QM3 gives 10% quality chance (vs 2.5% for normal QM3). Put these in your upcycling assemblers and the rest of your factory.

**Legendary Productivity Module III** — +10% productivity (vs +4% for normal). Multiply your entire factory's output.

**Legendary Speed Module III** — +80% speed, -80% energy. Insane for beacons.

### Tier 2: Build These Second

**Legendary Foundry / Electromagnetic Plant** — These buildings have huge built-in productivity bonuses which compound with legendary quality. A legendary foundry on Vulcanus produces molten metal 80% faster with 20% more productivity.

**Legendary Assembler** — Good for your upcycling loop itself. Consistent quality output from faster crafts.

**Legendary Beacon** — Wider area of effect (9 tiles vs 6) plus faster transmission. A single legendary beacon with speed modules can replace 2-3 normal beacons.

### Tier 3: Nice to Have

| Item | Legendary Effect | Worth It? |
|------|-----------------|-----------|
| Steel Furnace | +80% speed | Build if you have spare legendary steel |
| Electric Furnace | +80% speed, -80% energy | Useful for furnace stacks |
| Cargo Bay | +80% inventory | Only if you have tons of legendary steel |
| Chests | +80% slots | Luxury item |
| Pipes | Underground distance +2 | Minimal benefit |

### Legendary Equipment ROI

| Equipment | Legendary Cost vs Common | Production Multiplier | Invest First? |
|-----------|-------------------------|----------------------|---------------|
| Quality Module III | ~4,000 upcycles | 4× quality chance | ✅ **Yes** |
| Productivity Module III | ~8,000 upcycles | 2.5× productivity | ✅ **Yes** |
| Speed Module III | ~6,000 upcycles | 1.8× speed | ✅ **Yes** |
| Beacon | ~12,000 upcycles | 50% more coverage | Maybe |
| Assembler 3 | ~16,000 upcycles | 1.8× speed, 0.4× energy | Later |

{{< callout type="info" >}}
The math is clear: **upcycle components, not finished machines.** If you want a legendary beacon, craft it from legendary circuits and LDS rather than recycling beacons. The 75% recycler loss on a complex item is devastating — on a simple gear, it's negligible.
{{< /callout >}}

## Building Your First Upcycling Loop

### Step-by-Step Setup

1. **Choose your item** — Start with iron gear wheels. Fast, simple, valuable
2. **Build the assembler** — Place an Assembler 3 with 4× quality modules (legendary if possible)
3. **Wire the output** — Splitter with filter: common items go to recycler, uncommon+ go to storage
4. **Build the recycler** — Place a recycler with 4× quality modules, output back toward assembler input
5. **Feed the input** — Belt common items from your main bus into the assembler
6. **Collect the output** — Chests for each quality tier (uncommon, rare, epic, legendary)

{{< callout "tip" >}}
Use **circuit network filters** on splitters to separate quality tiers chest by chest.  A green wire from the splitter reading all belt contents, with combinator logic `each ≥ uncommon → output filter signal`, ensures you never accidentally recycle your precious rare+ items.
{{< /callout >}}

### Scaling

A single gear upcycling loop with legendary modules produces roughly 1 legendary gear wheel every 5-10 minutes. That sounds slow, but it's running 24/7 in the background. Over a 100-hour play session, you'll have 600-1,200 legendary gears — more than enough for any base.

When you need more throughput, build **parallel loops** rather than trying to speed up one loop. Each loop is independent and the yield is roughly linear with the number of loops.

## Summary

Quality upcycling loops transform the impractical — grinding common items into legendary ones — into a reliable, automated process. The key insights:

- **Pair an assembler with a recycler**, both using quality modules
- **Filter higher-quality items out** of the loop, feed common items back to the recycler
- **Respect the math**: ~4,000 crafts per legendary item with legendary QM3, ~20,000 with rare QM3
- **Upcycle simple items** (gears, wire, green circuits) over complex ones
- **Build legendary equipment** from legendary components, not by recycling finished machines
- **Prioritize legendary modules** — they accelerate all subsequent upcycling

The upcycling loop is a long game. It takes hours to produce your first legendary module. But once you have it, every subsequent loop runs 4× faster. Build it early. Let it run. The legendaries will come.
