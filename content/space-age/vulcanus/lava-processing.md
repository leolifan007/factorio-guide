---
title: "Vulcanus Lava Processing — Molten Iron and Copper Without Miners"
description: "Vulcanus lava processing guide for Factorio Space Age. Molten iron/copper production, foundry casting, calcite logistics, and bringing lava products back to Nauvis."
date: 2026-06-20
tags: ["space-age", "vulcanus", "production"]
emoji: "🌋"
aliases:
  - /space-age/vulcanus-lava-processing/
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#1a0a2e,#3d1f0a);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:0.5rem;margin-bottom:1.5rem;">
<span style="font-size:3rem;">🌋</span>
<span style="font-family:Orbitron,sans-serif;font-size:1.5rem;font-weight:700;padding:0.3rem 0.6rem;border-radius:4px;background:#e8941c;color:#1a0a2e;">LAVA PROCESSING</span>
</div>

Vulcanus is defined by one thing: **lava**. The planet is covered in oceans of molten rock, and unlike Nauvis ore patches — which deplete over time — lava is an **infinite resource**. Master lava processing and you unlock an unlimited supply of iron, copper, steel, and low-density structures without ever placing a miner. If you haven't landed yet, {{< ref "/space-age/guide/vulcanus-guide" >}} covers the first steps on Vulcanus.

This guide covers everything you need to know: how lava pumps work, the foundry recipes that convert lava into molten metal, calcite logistics, casting products, and how to ship the results back to Nauvis.

{{< callout type="info" >}}
**Before you start:** This guide assumes you've already landed on Vulcanus and unlocked the foundry. If you're still planning your first trip, check the {{< ref "/space-age/guide/vulcanus-guide" >}} for landing prep and base setup.
{{< /callout >}}

## How Lava Pumping Works

Lava is extracted using the **lava pump**, a building that functions similarly to an offshore pump but pulls from lava instead of water. Crucially, lava pumps can only be placed on the **lava shoreline** — you cannot build them out in the lava ocean itself.

### Key Lava Pump Properties

- **Throughput per pump:** 1,000 lava/s through a single pipe segment
- **Pipe throughput limits:** Standard pipes carry up to 1,200 fluid/s over short distances, so one pipe can carry the output of one lava pump with headroom
- **Infinite source:** Lava patches never deplete. You will never need to relocate your pump setup
- **Temperature:** Lava enters at 50°C — this matters because the foundry requires lava at any temperature above 0°C
- **Placement:** Look for the dark red/black shoreline tiles. If you see bubbling, you've found a valid spot

{{< callout "tip" >}}
Place your lava pumps close to your foundry array. Long pipe runs are possible but not recommended — Vulcanus has aggressive biters that will target exposed pipe segments. Keep everything within your walled perimeter.
{{< /callout >}}

### Lava Pump Layout

A typical early-game setup uses 2-4 lava pumps feeding a buffer tank, then distributing to foundries through underground pipes. The underground pipe connection saves surface space and protects the line from biter damage.

As your factory grows, scale to 8-12 pumps. Each pump handles 1,000 lava/s, and each foundry consumes **500 lava/s** when producing molten iron or copper. One pump feeds exactly two foundries running at full tilt.

## The Foundry: Converting Lava to Metal

The **foundry** is the centerpiece of Vulcanus production. It accepts lava and calcite as inputs, outputs molten iron or copper, and can also cast finished products directly from molten metal.

### Molten Iron Production

{{< material "calcite" "1" >}} + {{< material "lava" "500" >}} → {{< material "molten-iron" "15" >}} per second per foundry

- **Crafting time:** 2 seconds per recipe cycle
- **Calcite per foundry:** 0.5/s
- **Lava per foundry:** 500/s

### Molten Copper Production

{{< material "calcite" "1" >}} + {{< material "lava" "500" >}} → {{< material "molten-copper" "15" >}} per second per foundry

- Calcite and lava consumption rates are identical to molten iron
- Both recipes run side by side — dedicate foundries to each metal

### Production Rate Comparison

| Recipe | Lava / s | Calcite / s | Output / s | Foundries per Pump |
|--------|----------|-------------|------------|-------------------|
| Molten Iron | 500 | 0.5 | 15 molten iron | 2 per pump |
| Molten Copper | 500 | 0.5 | 15 molten copper | 2 per pump |
| Molten Iron + Copper | 500 each | 0.5 each | 15 + 15 | 1 + 1 per 2 pumps |

A balanced early setup: **4 lava pumps fueling 8 foundries** (4 iron, 4 copper). This produces 60 molten iron/s and 60 molten copper/s — enough to sustain significant Nauvis exports.

{{< callout type="info" >}}
**Temperature note:** Unlike water in boilers, lava temperature is irrelevant for the foundry. The conversion is purely material-based — 500 lava + 1 calcite = 15 molten metal, regardless of lava temperature.
{{< /callout >}}

## Calcite: The Critical Catalyst

Calcite is the **limiting ingredient** in lava processing. You need it for every molten metal recipe, and it doesn't come from lava itself.

### Calcite Supply Sources

**1. Space Platform Mining (Recommended)**
Build a space platform in orbit around Vulcanus that collects **calcite from asteroid chunks**. A small platform with 4-6 asteroid collectors and a crusher running metallic asteroid processing produces more than enough calcite for a medium-scale lava processing plant. This is the cleanest solution — it requires no ground logistics.

**2. Vulcanus Surface Mining (Alternative)**
Calcite patches exist on the Vulcanus surface, usually in smaller quantities than iron or copper ore. You can mine them with regular electric mining drills, but the patches are sparse and deplete faster than you'd like. Use this only as a backup or bootstrap.

**3. Nauvis Space Shipping (Fallback)**
If your space platform network is struggling, you can ship calcite from Nauvis. This is wildly inefficient — don't do it unless you're desperate.

### Calcite Consumption

Each foundry consumes **0.5 calcite/s** running molten metal recipes. For 8 foundries (4 iron + 4 copper):

- Total calcite consumption: **4 calcite/s**
- Space platform with 6 collectors: Produces roughly 2-5 calcite/s depending on asteroid density
- You'll need multiple platforms or asteroid reprocessing for larger setups

{{< callout "tip" >}}
When designing your calcite supply, **over-build your space platform**. Calcite is consumed constantly — running out means your entire lava processing plant grinds to a halt. Add buffer chests with 10k+ calcite storage.
{{< /callout >}}

## Casting Recipes: Skip the Assembly Line

The real power of the foundry isn't just molten metal — it's **direct casting**. Instead of pouring molten iron into plates and then crafting gears, you can cast finished products directly from the molten metal. This eliminates entire assembly steps.

### Iron Casting

| Recipe | Molten Iron Input | Output | Output / s |
|--------|-------------------|--------|------------|
| Iron Gear Wheel | 40 | 2 gears | ~3.3/s |
| Iron Pipe | 20 | 2 pipes | ~6.6/s |
| Iron Stick | 10 | 4 sticks | ~13.3/s |
| Iron Plate | 10 | 1 plate | ~8/s |

### Copper Casting

| Recipe | Molten Copper Input | Output | Output / s |
|--------|---------------------|--------|------------|
| Copper Wire | 10 | 2 wire | ~10/s |
| Copper Plate | 10 | 1 plate | ~8/s |

### Steel and LDS

Two of the most impactful casting recipes:

**Steel from Molten Iron**
{{< material "molten-iron" "30" >}} → {{< material "steel-plate" "1" >}}

This recipe bypasses the iron plate → steel plate chain entirely. Each foundry produces steel at roughly 6/s — compare this to Nauvis where you need 5 furnaces + a steel furnace to get 1/s steel. Vulcanus steel is **6x faster per building**.

**Low Density Structure (LDS)**
{{< material "molten-iron" "50" >}} + {{< material "molten-copper" "50" >}} + {{< material "plastic" "5" >}} → {{< material "low-density-structure" "2" >}}

This is the direct casting recipe that changes the rocket game. Instead of crafting copper wire → copper cable → advanced circuits → processing units → LDS, you go straight from molten metal to LDS. The plastic requirement means you still need some petrochemical production, but the metal supply chain is radically simplified.

{{< diagram "diagrams/space-age/lava-processing-flow.svg" "Molten iron and copper production from lava to casting" "760" >}}

### Casting Throughput Comparison

| Cast Product | Foundry Speed (per foundry) | Assembler Speed (EM plant) | Ratio |
|-------------|----------------------------|---------------------------|-------|
| Iron Gear Wheel | 3.3/s | 1/s | **3.3×** |
| Copper Wire | 10/s | 2/s | **5×** |
| Steel Plate | 6/s | 1/s | **6×** |
| LDS | 1.6/s | 0.5/s | **3.2×** |

{{< callout type="info" >}}
The foundry has **built-in productivity bonuses** over standard assemblers. Each casting recipe produces ~50% more output per unit of input material compared to crafting from plates. This compounds with module bonuses.
{{< /callout >}}

## Bringing Lava Products to Nauvis

The entire point of Vulcanus lava processing is that you can replace Nauvis mining operations with Vulcanus imports. Here's how to make that work:

### What to Ship

**Ship as cargo, not fluid.** Molten metal cannot be barreled in Space Age — you cannot send pipes of molten iron via rocket. Instead, cast the molten metal into finished products and ship those.

**Priority export list:**
1. **Steel plates** — Highest ROI per rocket slot. Vulcanus produces steel 6× faster than Nauvis
2. **Iron gear wheels** — Dense, fast to produce, used in massive quantities on Nauvis
3. **Low Density Structures** — Essential for rockets, and Vulcanus produces them directly from lava
4. **Copper wire** — If your Nauvis base has wire bottlenecks

### Export Ratios

A well-tuned Vulcanus export base running 8 foundries (4 iron, 4 copper):

| Export Product | Production Rate | Rocket Cargo Capacity | Rockets per Minute |
|---------------|----------------|----------------------|-------------------|
| Steel Plate | 24/s | 50 stacks | 0.48 |
| Iron Gear Wheel | 13.2/s | 200 stacks | 0.066 |
| LDS | 6.4/s | 100 stacks | 0.064 |

{{< callout "tip" >}}
Use the **landing pad with requester chests** on Nauvis to auto-unload rocket deliveries. Set up a circuit condition: "if steel < 1000 in storage → launch rocket". This automates your interplanetary supply chain.
{{< /callout >}}

For a complete guide to setting up reliable interplanetary logistics, see {{< ref "/space-age/platform/cross-planet-logistics" >}}.

## Advanced: Scaling Up

For megabase-scale lava processing:

**Pump arrays:** Build rows of 8-16 lava pumps feeding a main lava bus. Each underground pipe segment carries 1,200 fluid/s, so parallel pipes are necessary at scale.

**Foundry blocks:** Group foundries in blocks of 8 (4 iron, 4 copper) with dedicated calcite import lines. Each block consumes 4 calcite/s and produces 60 iron + 60 copper molten metal per second.

**Asteroid processing:** Scale your space platforms to match. A platform with 12 collectors and advanced metallic asteroid processing can supply 10+ calcite/s — enough for 20 foundries.

**Direct casting to train:** Route molten metal directly from foundries to casting arrays. Don't buffer molten metal in tanks if you can avoid it — cast it directly into products and store those instead. Products stack. Fluids don't.

{{< callout type="info" >}}
For space platform design patterns that handle high-throughput calcite collection, see {{< ref "/space-age/platform/space-platform-guide" >}}.
{{< /callout >}}

## Summary

Vulcanus lava processing is the most important production chain in Space Age. It replaces Nauvis mining with an infinite, calcite-catalyzed process that produces molten metal at high rates and casts finished products with massive productivity bonuses.

**Key takeaways:**
- Lava pumps are infinite — place them on the shoreline, protect them from biters
- Each foundry consumes 500 lava + 0.5 calcite/s → 15 molten metal/s
- Calcite comes from space platforms (recommended) or surface mining (fallback)
- Direct casting recipes are 3-6× faster than traditional assembly
- Export steel, gears, and LDS to Nauvis by rocket

Don't mine Nauvis ore patches. Pump lava instead. Your future self — the one who never has to set up another iron mine — will thank you.
