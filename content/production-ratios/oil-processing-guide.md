---
title: "Oil Processing — Ratios, Cracking, and Refinery Setup"
description: "Complete Factorio oil processing guide: refinery ratios, cracking math, heavy/light balancing, basic vs advanced refining, and cheat sheet for perfect balance."
date: 2026-05-18
tags: ["production-ratios", "base-design"]
draft: false
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#3a2010,#8b6914);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;">
<span style="font-family:Orbitron,sans-serif;font-size:2rem;font-weight:900;color:#d4a017;">OIL PROCESSING</span>
</div>

Oil processing is where most factory layouts fall apart. Unlike ore patches that just run, oil wells deplete over time, refineries produce three outputs at once, and if any of those outputs backs up, everything stops. I've rebuilt my refinery block more times than any other section of the factory.

{{< callout "tip" >}}
**TL;DR:** Build 8 refineries with advanced processing. Crack heavy→light (1 plant), light→petroleum (7 plants). That's the magic 8:1:7 ratio. No backups, maximum plastic throughput.
{{< /callout >}}

{{< section "Basic vs. Advanced Refining" >}}

You start with basic refining, but you'll want advanced as soon as possible.

| Aspect | Basic Processing | Advanced Processing |
|--------|:----------------:|:-------------------:|
| Unlocked | Start | Oil Processing research |
| Input | 100 Crude Oil | 100 Crude + 50 Water |
| Heavy Oil | 30 | 50 |
| Light Oil | 30 | 50 |
| Petroleum | 40 | **30** |
| Total units | 100 | 130 (30% more) |

Here's the trade-off: advanced processing gives you 30% more total output per refinery, but it shifts the ratio toward heavy and light oil. You get less petroleum per cycle, which means you absolutely need cracking to convert the excess heavy and light into more petroleum.

{{< diagram "diagrams/oil-cracking-flow.svg" "Oil cracking balance showing the 8:1:7 refinery to cracking ratio" "760" >}}

{{< section "The Three Outputs — Where Everything Goes" >}}

Each oil product has specific uses:

**Heavy Oil**
- Lubricant production (1 heavy = 10 lubricant)
- Cracking to light oil (40 heavy → 30 light)
- Flamethrower turret ammo

**Light Oil**
- Solid fuel production (most efficient source: 1 light = 1 solid fuel)
- Rocket fuel (10 solid fuel + 10 light = 1 rocket fuel)
- Cracking to petroleum gas (30 light → 20 petroleum)

**Petroleum Gas**
- Plastic bars (20 petroleum + 1 coal = 2 plastic)
- Sulfur (30 petroleum + 30 water = 2 sulfur)
- Sulfuric acid (5 sulfur + 1 iron + 100 water = 50 acid)
- Solid fuel (least efficient from petroleum)

{{< section "The Critical Cracking Ratio" >}}

With advanced processing, 8 refineries produce per second:

| Output | Per refinery | 8 refineries total |
|--------|:------------:|:------------------:|
| Heavy Oil | 50/s | **400/s** |
| Light Oil | 50/s | **400/s** |
| Petroleum | 30/s | **240/s** |

The consumption rates for a typical mid-game factory:

| Consumer | Input type | Rate per machine |
|----------|-----------|:----------------:|
| Heavy→Light cracker | Heavy Oil | 40 every 2s (20/s) |
| Light→Petro cracker | Light Oil | 30 every 2s (15/s) |
| Plastic plant | Petroleum | 20/s |
| Sulfur plant | Petroleum | 30/s |

**The 8:1:7 ratio:**

With 8 refineries (all heavy/light going to cracking and petroleum being consumed):

| Plant | Count | Output consumed |
|-------|:-----:|:---------------:|
| Refinery | 8 | — |
| Heavy→Light cracker | 1 | 20 heavy/s out of 400/s (lubricant takes the rest) |
| Light→Petro cracker | 7 | 105 light/s (remainder goes to solid fuel) |
| Plastic plants | N | 240 petroleum/s from cracking + remaining |

The math works out: crack just enough heavy and light to meet petroleum demand. The rest goes to lubricant and solid fuel.

{{< callout "warning" >}}
If you don't consume or crack heavy oil, refineries will stall. This is the single most common oil processing failure. Always have a lubricant buffer tank AND a cracking plant connected to heavy.
{{< /callout >}}

{{< section "Fluid Handling Tips" >}}

**Storage tanks:** One tank per fluid type is enough for buffering. More doesn't help — your goal is to keep fluids moving, not store them.

**Underground pipes:** These reduce the pipe entity count and improve game performance. They also make your refinery block look cleaner.

**Pump control:** Use circuit conditions to control cracking:

<pre style="background:#1a1a1a;padding:0.75rem;border-radius:4px;border:1px solid #444;font-size:0.72rem;line-height:1.6;">
  Pump connected to heavy oil tank:
    Enable when heavy_oil > 20,000
    → Feeds heavy→light cracker

  Pump connected to light oil tank:
    Enable when light_oil > 20,000
    → Feeds light→petroleum cracker
</pre>

This ensures your heavy oil tank always has some lubricant reserve before cracking kicks in.

{{< section "Troubleshooting Oil Processing" >}}

| Symptom | Cause | Fix |
|---------|-------|-----|
| Refineries stalled | Heavy oil full | Add lubricant buffer + cracking |
| Petroleum starving | Not enough cracking | Add light→petroleum plants |
| Lubricant empty | Too much cracking | Increase heavy→light threshold |
| Wells below 2/s | Depleted | Speed modules + beacons, or expand |
| Plastic backed up | Belt full, not consumed | Check red circuit consumption |

{{< section "Cheat Sheet — Copy-Paste Setup" >}}

For a mid-game refinery block, build this:

**Building list:**
- 8 Refineries (advanced processing)
- 1 Chemical plant (heavy→light cracking)
- 7 Chemical plants (light→petroleum cracking)
- 4+ Plastic plants
- 1 Sulfur plant
- 1 Lubricant plant
- Storage tanks: heavy, light, petroleum
- 4 Offshore pumps (water for refining + cracking)

**Pipe layout:**
```
[Water in] ──┬─────────────────────────────
              │  │  │  │  │  │  │  │  │
            [R1][R2][R3][R4][R5][R6][R7][R8]   Refineries
              │  │  │  │  │  │  │  │  │
[Hvy] ────────┴──┴──┴──┴──┴──┴──┴──┴──┴──→ Lube + Cracker×1
[Lgt] ────────┴──┴──┴──┴──┴──┴──┴──┴──┴──→ Fuel + Cracker×7
[Pet] ────────┴──┴──┴──┴──┴──┴──┴──┴──┴──→ Plastic + Sulfur
```

{{< section "Bottom Line" >}}

Oil processing looks intimidating, but the 8:1:7 ratio handles everything. Build refineries in a line, pipe outputs down three parallel lines, and use circuit-controlled cracking to keep everything balanced.

**Numbers to remember:**
- 8 refineries + 1 heavy cracker + 7 light crackers = perfect balance
- Heavy oil → lubricant first, crack the rest
- Petroleum is the most consumed output. Cracking toward it always
- One pump-controlled cracking plant prevents backpressure

**Related:** [Blue Science Guide]({{< ref "/science-packs/blue-science-guide" >}}) — putting oil to work, [Nuclear Power Guide]({{< ref "/base-design/nuclear-power-guide" >}}) — the next major power upgrade.
