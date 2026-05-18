---
title: "Logistic Science Pack — Green Science Guide"
description: "Complete guide to automating green science in Factorio: exact recipe, optimal ratios, and a buildable layout."
date: 2026-05-18
tags: ["getting-started", "science-packs"]
draft: false
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#556b2f,#6abe30);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;">
<span style="font-family:Orbitron,sans-serif;font-size:2rem;font-weight:900;color:#222;">LOGISTIC SCIENCE</span>
</div>

## Recipe

The Logistic Science Pack (green science) requires two ingredients:

<div class="recipe-grid">

<div class="recipe-slot">
<div class="slot-label">Inserter</div>
<div class="slot-icon" style="background:#3a3a3a;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="16" y="10" width="16" height="28" rx="2" fill="#666"/><rect x="12" y="30" width="24" height="10" rx="2" fill="#6abe30"/></svg>
</div>
<div class="slot-recipe">1 × Iron Gear<br>1 × Circuit<br>1 × Iron Plate</div>
</div>

<div class="recipe-arrow">+</div>

<div class="recipe-slot">
<div class="slot-label">Transport Belt</div>
<div class="slot-icon" style="background:#3a3a3a;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="8" y="20" width="32" height="8" rx="2" fill="#888"/><circle cx="16" cy="24" r="4" fill="#555"/><circle cx="32" cy="24" r="4" fill="#555"/></svg>
</div>
<div class="slot-recipe">1 × Iron Plate</div>
</div>

<div class="recipe-arrow">→</div>

<div class="recipe-slot">
<div class="slot-label">Logistic Science Pack</div>
<div class="slot-icon" style="background:#556b2f;border:2px solid #6abe30;">
<svg viewBox="0 0 48 48" width="48" height="48"><rect x="8" y="10" width="32" height="28" rx="4" fill="#556b2f" stroke="#6abe30" stroke-width="2"/><rect x="12" y="14" width="24" height="20" rx="2" fill="#6abe30"/></svg>
</div>
</div>

</div>

## Ratio Math

At 5 science packs per second (0.5s craft time):

| Machine | Output | Required |
|---------|--------|----------|
| Green science assemblers | 5/s | 5 assemblers |
| Inserter assemblers (0.5s) | 5/s | 1 assembler (runs 2× ratio) |
| Belt assemblers (0.5s) | 5/s | 1 assembler (runs 2× ratio) |
| Circuit assemblers | 5/s | Already running for red science |

> **Key insight:** 1 inserter assembler + 1 belt assembler can feed **10 green science assemblers**. Build belt/inserter production in the middle, science on both sides.

## Starter Layout

<div class="warning-box">
<strong>Planning ahead:</strong> Build green science near your red science line. Labs accept both packs, so one belt of each science alongside your lab row keeps things simple.
</div>

**Recommended belt setup (one side of a bus):**

1. **Iron plates** on far left belt lane
2. **Copper plates** next (for circuits)
3. **Red circuits** ready for later blue science
4. **Green science** output belt running back to labs

## Common Mistakes

- **Inserters vs. Belt production ratio** — You need roughly equal numbers. One assembler of each at green science tier is plenty
- **Not enough copper wire** for circuits — one copper wire assembler feeds ~6 circuit assemblers
- **Output belt backed up** — use a splitter to prioritize science output, or feed directly into labs

## Research Path After Green Science

With green science automated:

1. **Oil processing** — unlocks blue science
2. **Advanced electronics** — unlocks red circuits
3. **Fluid handling** — pipes and storage tanks
4. **Military science** — gray science pack

**Next up:** [Blue Science Guide]({{< ref "/science-packs/blue-science-guide" >}}) — chemical science pack.
