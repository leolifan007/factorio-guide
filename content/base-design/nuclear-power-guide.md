---
title: "Nuclear Power — Complete Setup Guide"
description: "Factorio nuclear power explained: reactor layout, heat pipes, steam turbines, and fuel math from startup to 1GW."
date: 2026-05-18
tags: ["base-design", "production-ratios"]
draft: false
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#0a1a2a,#1a4a3a);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;">
<span style="font-family:Orbitron,sans-serif;font-size:2rem;font-weight:900;color:#44ff88;">NUCLEAR POWER</span>
</div>

## Why Go Nuclear?

Solar is zero-maintenance but **huge**. Steam is cheap but **fuel-hungry**. Nuclear is the sweet spot:

- ~40 MW per reactor tile (with neighbor bonus)
- One uranium patch lasts hundreds of hours
- UPS-friendly compared to 10,000 solar panels
- Scalable from 40 MW to multi-GW

## Fuel Cycle Overview

<div class="recipe-grid">

<div class="recipe-slot">
<div class="slot-label">Mining</div>
<div class="slot-icon" style="background:#2a2a2a;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="12" y="8" width="24" height="32" rx="3" fill="#444" stroke="#888" stroke-width="1.5"/><circle cx="24" cy="24" r="10" fill="#44ff88" opacity="0.3"/></svg>
</div>
<div class="slot-recipe">Electric drill →<br>Uranium Ore</div>
</div>

<div class="recipe-arrow">→</div>

<div class="recipe-slot">
<div class="slot-label">Centrifuge</div>
<div class="slot-icon" style="background:#2a2a2a;">
<svg viewBox="0 0 48 48" width="48" height="48"><circle cx="24" cy="24" r="16" fill="none" stroke="#888" stroke-width="2"/><circle cx="24" cy="24" r="6" fill="#44ff88"/></svg>
</div>
<div class="slot-recipe">10 Ore → 1 U-235 (0.7%)<br>10 Ore → 99+ U-238 (99.3%)</div>
</div>

<div class="recipe-arrow">→</div>

<div class="recipe-slot">
<div class="slot-label">Fuel Cell Assembly</div>
<div class="slot-icon" style="background:#2a2a2a;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="10" y="14" width="28" height="20" rx="3" fill="#444" stroke="#44ff88" stroke-width="1.5"/></svg>
</div>
<div class="slot-recipe">1 U-235 + 19 U-238<br>→ 10 Fuel Cells<br>200s fuel per cell</div>
</div>

</div>

## Reactor Layouts

### 1×1 (Standalone) — 40 MW

Simplest setup. No neighbor bonus. Good for early nuclear.

<div class="depiction-box" style="background:#1a1a2a;padding:1rem;border-radius:8px;border:1px solid #44ff88;font-family:'JetBrains Mono',monospace;font-size:0.75rem;line-height:1.6;">
<pre>
┌───────────┐
│  Reactor  │  ← Heat exchangers → Turbines (×4)
└───────────┘
Total: ~40 MW from 4 turbines
</pre>
</div>

### 2×1 (Paired) — 160 MW

Two reactors touching gives +100% neighbor bonus each.

```
[Reactor A] — [Reactor B]
     │              │
 HeatEx×4       HeatEx×4   → 14 turbines each → 28 total
```

### 2×2 (Standard) — 480 MW

The classic 4-reactor 2×2 layout. Each center reactor gets +300% bonus.

<div class="warning-box">
<strong>Optimal first build:</strong> A 2×2 reactor produces 480 MW — enough to run a full megabase. Start here if you have enough uranium.
</div>

**Component counts:**
- Heat exchangers: 48 (12 per reactor)
- Steam turbines: 84 (21 per reactor)
- Offshore pumps: 4 (each feeds 12 exchangers)

### N×N Tileable Blueprint

For truly large setups, 2×N reactor rows are the most tileable. Each additional pair of reactors adds 160 MW.

## Heat Pipe Physics

Heat propagates through pipes up to ~16 tiles before significant loss. **Rules of thumb:**

- Max 4 heat exchangers per heat pipe segment
- Keep heat pipes ≤ 20 tiles from reactor
- Use double heat pipes for 2+ reactor wide setups
- Place heat exchangers on BOTH sides of the heat pipe

## Fuel Efficiency

| Setup | Reactors | Fuel/hr | MW | MW per fuel cell |
|-------|----------|---------|-----|-----------------|
| 1×1 | 1 | 18 | 40 | 2.22 MW |
| 2×1 | 2 | 36 | 160 | 4.44 MW |
| 2×2 | 4 | 72 | 480 | 6.67 MW |
| 2×3 | 6 | 108 | 800 | 7.41 MW |

> **Pro tip:** A single centrifuge processing uranium ore is enough to fuel a 2×2 reactor indefinitely once Kovarex enrichment is running.

## Kovarex Enrichment

The game-changer for nuclear. Turns the rare U-235 into a renewable resource:

```
Recipe: 40 U-235 + 5 U-238 → 41 U-235 + 2 U-238
Time: ~60 seconds in a centrifuge
```

**Bootstrapping:** You need 40 U-235 to start (about 6,000 ore with no modules). Stockpile while running the reactor manually or supplement with solar.

## Steam Storage Strategy

Steam tanks bridge the gap while reactors idle (fuel lasts 200s):

- 1 tank holds 25,000 units of steam (2.425 GJ)
- 1 steam turbine consumes 60 units/s at 5.82 MW
- **Buffer:** 20 tanks store enough for ~5 minutes at full load

## Common Pitfalls

- **Not enough water** — One offshore pump feeds 12 heat exchangers. With more reactors, you need dedicated pump lines.
- **Heat pipe too long** — Past ~16 tiles, heat transfer drops significantly. Add more pipe connections.
- **Fuel overproduction** — Inserters feed fuel at the start of each cycle. Circuit-controlled inserters save fuel.
- **Ignoring neighbor bonus** — A 2×2 reactor costs the same fuel as 4 standalone reactors but produces **480 MW vs 160 MW**.

**Related:** [Main Bus Guide]({{< ref "/base-design/main-bus-guide" >}}) — integrating nuclear into your bus base.
