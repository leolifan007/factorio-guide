---
title: "Oil Processing — Ratios & Refinery Setup"
description: "Complete oil processing guide: refinery ratios, cracking math, heavy/light balancing, and optimal layouts."
date: 2026-05-18
tags: ["production-ratios", "base-design"]
draft: false
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#3a2010,#8b6914);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;">
<span style="font-family:Orbitron,sans-serif;font-size:2rem;font-weight:900;color:#d4a017;">OIL PROCESSING</span>
</div>

## Why Oil Processing Matters

Oil is where most players hit their first real production wall. Unlike ore patches, oil wells **deplete over time**, and the refining process produces three fluid outputs that must be balanced.

## Basic vs. Advanced Refining

| Aspect | Basic (Tier 1) | Advanced (Tier 2) |
|--------|---------------|-------------------|
| Unlocked | Start | Oil Processing research |
| Recipe | Crude → 3 outputs | Crude + Water → 3 outputs + 50% more |
| Heavy Oil | 30/s | 50/s |
| Light Oil | 30/s | 50/s |
| Petroleum | 40/s | 30/s — less! But more total converts |

> **Key insight:** Advanced processing gives **more total output** per refinery, but with a different ratio. You need cracking (heavy→light, light→petroleum) to balance.

## The Three Product Paths

<div class="recipe-grid">

<div class="recipe-slot">
<div class="slot-label">Heavy Oil</div>
<div class="slot-icon" style="background:#444;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="10" y="14" width="28" height="20" rx="3" fill="#8b4513" stroke="#d4a017" stroke-width="1.5"/></svg>
</div>
<div class="slot-recipe">→ Lubricant<br>→ Crack to Light Oil<br>→ Flamethrower fuel</div>
</div>

<div class="recipe-slot">
<div class="slot-label">Light Oil</div>
<div class="slot-icon" style="background:#444;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="10" y="14" width="28" height="20" rx="3" fill="#d4a017" stroke="#f0c040" stroke-width="1.5"/></svg>
</div>
<div class="slot-recipe">→ Solid Fuel (most efficient)<br>→ Rocket Fuel<br>→ Crack to Petroleum</div>
</div>

<div class="recipe-slot">
<div class="slot-label">Petroleum Gas</div>
<div class="slot-icon" style="background:#444;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="10" y="14" width="28" height="20" rx="3" fill="#5599ee" stroke="#88bbff" stroke-width="1.5"/></svg>
</div>
<div class="slot-recipe">→ Plastic (most common)<br>→ Sulfur<br>→ Rocket fuel additive</div>
</div>

</div>

## Cracking Ratios

| Cracking Recipe | Input | Output | Craft Time |
|----------------|-------|--------|------------|
| Heavy → Light | 40 Heavy Oil | 30 Light Oil | 2s |
| Light → Petroleum | 30 Light Oil | 20 Petroleum | 2s |

**Critical ratio:** With advanced refining + all cracking, **8 refineries feed 1 heavy→light cracker + 7 light→petroleum crackers** for perfect balance.

## Reader's Cheat Sheet

Here's the most common blueprint-ready setup:

```
[Refinery × 8]
       │
       ├─ Heavy Oil line → Lubricant (drain)
       │                → Cracking plant × 1
       │
       ├─ Light Oil line → Solid Fuel plants
       │                → Cracking plants × 7
       │
       └─ Petroleum line → Storage → Plastic × N
```

<div class="warning-box">
<strong>Petroleum is the most consumed.</strong> You'll always need more plastic than lubricant. Prioritize cracking toward petroleum.
</div>

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Refineries stalled | Heavy oil full | Add lubricant buffer or more cracking |
| Petroleum starving | Not enough light→petroleum cracking | Build 2-3 more cracking plants |
| Lubricant empty | Too much cracking | Keep 1 tank of heavy for lube before crack |
| Wells below 2/s | Depleted | Use speed modules + beacons, or find new fields |

**Related:** [Nuclear Power Guide]({{< ref "/base-design/nuclear-power-guide" >}}) — next major power upgrade.
