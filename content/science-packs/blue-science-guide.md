---
title: "Chemical Science Pack — Blue Science Guide"
description: "Everything about blue science in Factorio: oil processing, recipe ratios, sulfur, and automation setup."
date: 2026-05-18
tags: ["science-packs", "production-ratios"]
draft: false
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#1a3a5c,#3778c8);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;">
<span style="font-family:Orbitron,sans-serif;font-size:2rem;font-weight:900;color:#88ccff;">CHEMICAL SCIENCE</span>
</div>

## Recipe

Blue science is the first science that requires **fluids**:

<div class="recipe-grid">

<div class="recipe-slot">
<div class="slot-label">Engine Unit</div>
<div class="slot-icon" style="background:#3a3a3a;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="10" y="14" width="28" height="20" rx="3" fill="#888" stroke="#ccc" stroke-width="1.5"/><rect x="16" y="8" width="16" height="6" rx="2" fill="#666"/></svg>
</div>
<div class="slot-recipe">2 × Steel<br>1 × Gear<br>1 × Pipe</div>
</div>

<div class="recipe-arrow">+</div>

<div class="recipe-slot">
<div class="slot-label">Sulfur</div>
<div class="slot-icon" style="background:#3a3a3a;">
<svg viewBox="0 0 48 48" width="48" height="48"><circle cx="24" cy="24" r="16" fill="#d4a017" stroke="#f0c040" stroke-width="2"/></svg>
</div>
<div class="slot-recipe">Petroleum + 30 Water<br>→ 2 Sulfur / 1s</div>
</div>

<div class="recipe-arrow">→</div>

<div class="recipe-slot">
<div class="slot-label">Chemical Science Pack</div>
<div class="slot-icon" style="background:#1a3a5c;border:2px solid #3778c8;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="8" y="10" width="32" height="28" rx="4" fill="#1a3a5c" stroke="#3778c8" stroke-width="2"/><rect x="14" y="16" width="20" height="16" rx="2" fill="#5599ee"/></svg>
</div>
</div>

</div>

## Oil Refining — The Foundation

Blue science requires **plastic** (coal + petroleum), which means you need oil refining first.

<div class="recipe-grid" style="margin-top:1rem;">

<div class="recipe-slot">
<div class="slot-label">Basic Oil Refining</div>
<div class="slot-icon" style="background:#2a2a2a;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="8" y="12" width="32" height="24" rx="4" fill="#444" stroke="#888" stroke-width="1.5"/><line x1="14" y1="24" x2="34" y2="24" stroke="#888"/><circle cx="24" cy="24" r="6" fill="#d4a017"/></svg>
</div>
<div class="slot-recipe">Crude Oil → Petroleum<br>Heavy Oil<br>Light Oil</div>
</div>

<div class="recipe-arrow">+</div>

<div class="recipe-slot">
<div class="slot-label">Chemical Plant</div>
<div class="slot-icon" style="background:#2a2a2a;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="10" y="12" width="28" height="24" rx="3" fill="#555" stroke="#888" stroke-width="1.5"/><circle cx="24" cy="24" r="8" fill="#3778c8" opacity="0.7"/></svg>
</div>
<div class="slot-recipe">Coal + Petroleum<br>→ Plastic Bar<br>2s craft time</div>
</div>

</div>

## Optimal Ratios

| Component | Machines | Notes |
|-----------|----------|-------|
| Blue science assemblers | 5 | Target: 5 SPM |
| Engine unit assemblers | 2 | Each feeds ~2.5 science assemblers |
| Sulfur chemical plants | 1 | 1 plant supplies ~10 science assemblers |
| Plastic bar chemical plants | 2 | 2 plants for steady supply |
| Refineries (basic) | 1-2 | 1 refinery provides enough petroleum |
| Copper wire assemblers | 1 | For red circuits (if not on bus) |
| Red circuit assemblers | 1 | For blue science modules |

> **Pro tip:** Blue science is the bottleneck for most first-time players. The issue is almost always **oil throughput** — not enough refineries, or imbalanced heavy/light oil storage.

## Blueprint: Compact Blue Science Cell

A single 5-assembler blue science array needs:

<div class="warning-box">
<strong>Warning:</strong> Don't forget to pipe lubricant away from heavy oil! If you don't use it, heavy oil backs up and your refineries stall.
</div>

**Materials bus (top to bottom):**
- Belt 1: Iron + Steel
- Belt 2: Copper + Coal
- Belt 3: Red circuits + Gears
- Pipe 1: Petroleum (sulfuric acid if using modules)
- Pipe 2: Lubricant (for later electric engine units)

## Research Order After Blue Science

1. **Advanced oil processing** — cracking for heavy → light → petroleum
2. **Production science pack** — purple science
3. **Utility science pack** — yellow science
4. **Modules 2 & 3** — massive efficiency gains

**Previous:** [Green Science Guide]({{< ref "/getting-started/green-science-guide" >}})
