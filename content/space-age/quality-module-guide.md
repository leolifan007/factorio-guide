---
title: "Quality Modules — Space Age New Mechanic Explained"
description: "How the Quality module system works in Factorio Space Age. Tiers, probabilities, and how to build a quality production line."
date: 2026-05-18
tags: ["space-age", "quality", "modules", "space-age"]
emoji: "💎"
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

In Space Age, items can have **5 quality tiers**. Higher quality items work better:

| Tier | Color | Bonus |
|------|-------|--------|
| Common (1) | Gray | Baseline |
| Uncommon (2) | Green | Plus 20 percent speed, minus 20 percent energy |
| Rare (3) | Blue | Plus 40 percent speed, minus 40 percent energy, plus 2 range |
| Epic (4) | Purple | Plus 60 percent speed, minus 60 percent energy, plus 4 range |
| Legendary (5) | Orange | Plus 80 percent speed, minus 80 percent energy, plus 6 range, plus 2 area of effect |

## How Quality Is Generated

**Quality modules** in assemblers/machines give a chance for the output to be a higher quality tier.

| Module | Quality Chance | Speed Penalty |
|--------|----------------|----------------|
| Quality module 1 | 1 percent per module | Minus 10 percent |
| Quality module 2 | 5 percent per module | Minus 15 percent |
| Quality module 3 | 10 percent per module | Minus 20 percent |

<div class="warning-box">
<strong>Important:</strong> Quality modules <em>slow down</em> production. Balance quality chance vs. production speed.
</div>

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

Quality modules pair naturally with [Fulgora’s scrap recycling]({{< ref "/space-age/fulgora-recycling-guide" >}})—recyclers can upgrade item quality while breaking scrap down. Here’s what to prioritize:

## Which Items to Upgrade First?

Priority list for quality:

| Priority | Item | Why |
|----------|-------|------|
| 1 | **Beacons** | More beacons = more speed modules affecting machines |
| — | **Space platform thrusters** | Rare thrusters use less fuel—see [Space Platform Guide](/space-age/space-platform-guide/) |
| 2 | **Speed modules** | Faster machines = more production |
| 3 | **Electric furnaces** | Faster smelting = more plates |
| 4 | **Miners** | More mining speed = more ore |
| 5 | **Power armor** | Better defense and equipment |

**Next:** [Space Age Overview]({{< ref "/space-age/" >}}) — all new planets and mechanics.
