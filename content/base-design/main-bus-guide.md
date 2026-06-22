---
title: "Main Bus Design — The Classic Factorio Base Layout"
description: "How to build a main bus base in Factorio: bus width, lane allocation, and expansion strategy."
date: 2026-05-18
tags: ["base-design", "main-bus", "layout"]
emoji: "🚌"
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#1a2a1a,#0a1a0a);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;">
<span style="font-family:Orbitron,sans-serif;font-size:1.8rem;font-weight:900;color:#6abe30;">MAIN BUS LAYOUT</span>
</div>

## What Is a Main Bus?

A **main bus** is a set of parallel belts (the "bus") carrying raw materials through your base. Assembly blocks **pull** from the bus and **push** finished products back onto it.

Think of it like a highway: resources flow down the middle, factories are off-ramps.

## Recommended Bus Width

| Material | Lanes (Basic Belt) | Lanes (Fast/Express) |
|----------|--------------------|-----------------------|
| Iron plates | 4-6 | 2-3 |
| Copper plates | 4-6 | 2-3 |
| Steel plates | 2 | 1 |
| Green circuits | 2 | 1 |
| Plastic bars | 1-2 | 1 |
| Coal | 1 | 1 |
| Stone | 1 | 1 |

<div class="tip-box">
<strong>Pro tip:</strong> Build your bus with <strong>space between lanes</strong>. You need room for underground belts to cross lanes and for inserters to pull items off the bus.
</div>

## How to Build It

### Step 1: Clear a Large Area
You need at least **200 tiles wide** and **unlimited depth**. The bus grows as you research more technologies.

### Step 2: Lay the First 4 Lanes
Start with iron plates (2 lanes), copper plates (2 lanes). Leave 3-tile gaps between lanes.

### Step 3: Add Off-Ramp Assemblers
Build assemblers perpendicular to the bus. Use **long-handed inserters** to reach across gaps.

### Step 4: Expand as Needed
Add more lanes (steel, green circuits, plastic) as your factory grows.

## Common Mistakes

> **Mistake 1:** Building the bus too narrow. You can't widen a main bus once it's surrounded by assemblers.

> **Mistake 2:** Not planning for smelting throughput. Use our [Smelting Ratios Guide]({{< ref "/production-ratios/smelting-ratios" >}}) to calculate exactly how many furnaces you need to keep your bus lanes saturated.

**Mistake 3:** Not planning for **train unloading**. Trains need to dump into the bus at the start of the line.

> **Mistake 3:** Forgetting **power poles**. Run big electric poles along one side of the bus.

If you’re just starting out, [Your First Factory]({{< ref "/getting-started/your-first-factory" >}}) walks through the complete beginner bus setup step by step. Once you’ve outgrown the basic 4-lane design:

## Is Main Bus Right for You?

| Base Style | Best For | Downside |
|-----------|----------|----------|
| Main Bus | Beginners, mid-size bases | Inefficient at megabase scale |
| [City Blocks](/base-design/city-block-guide/) | Megabases, train-based | Complex setup |
| Megabase (beaconed) | UPS-optimized builds | Requires deep game knowledge |

> **Bottom line:** Main bus is the best starting design. You can always transition to city blocks or beaconed modules later.

**Next:** [Base Design Patterns]({{< ref "/base-design/" >}}) — compare all major design patterns.
