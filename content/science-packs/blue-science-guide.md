---
title: "Factorio Blue Science Guide - Chemical Science Pack Setup and Ratios"
description: "Complete blue science (chemical science pack) guide for Factorio: oil processing setup, sulfur production, plastic automation, and the exact assembler ratios that scale to megabase."
date: 2026-05-18
tags: ["science-packs", "production-ratios"]
draft: false
emoji: "🔵"
---

Blue science is the first real complexity spike in Factorio. It's not just about adding a new ingredient — it introduces fluids, cracking, and multi-step production chains. I've seen countless factory tours stall right here because the oil setup wasn't thought through.

{{< callout "tip" >}}
**TL;DR:** Blue science needs oil processing for plastic and sulfur. Build 2 refineries, 1 sulfur plant, 2 plastic plants, and 5 science assemblers. The bottleneck is almost always petroleum throughput.
{{< /callout >}}

{{< section "Recipe and Requirements" >}}

Each chemical science pack needs three components:

{{< recipe name1="engine" qty1="1x" name2="circuit_red" qty2="1x" name3="sulfur" qty3="1x" result="chemical_science" rqty="1x" >}}

Two of these three require oil products. Red circuits need plastic (petroleum + coal). Sulfur needs petroleum gas and water. That means you can't automate blue science until you have a working oil refinery setup.

{{< section "Oil Refining — The Hard Part" >}}

Here's the chain from well to blue science:

| Step | Input | Output | Machine |
|------|-------|--------|---------|
| Oil extraction | Crude oil | Crude oil | Pumpjack |
| Basic refining | Crude oil | Heavy, Light, Petroleum | Refinery |
| Sulfur | Petroleum + Water | Sulfur | Chemical plant |
| Plastic | Coal + Petroleum | Plastic bar | Chemical plant |
| Red circuits | Plastic + Copper + Green | Red circuit | Assembler |
| Engine | Steel + Gear + Pipe | Engine unit | Assembler |
| Blue science | Engine + Red circuit + Sulfur | Blue pack | Assembler |

The critical path is petroleum. You need enough refineries producing petroleum gas to feed both plastic and sulfur production.

{{< diagram "diagrams/blue-science-flow.svg" "Blue science production chain from oil wells through refineries to chemical science packs" "760" >}}

{{< section "Optimal Ratios for 5 SPM" >}}

Here's the ratio that works for a stable 5 blue science per minute setup:

| Component | Machines | Notes |
|-----------|:--------:|-------|
| Blue science assemblers | 5 | Target output rate |
| Engine unit assemblers | 2 | Each feeds about 2.5 science assemblers |
| Sulfur chemical plants | 1 | One plant supplies ~10 science assemblers |
| Plastic chemical plants | 2 | Steady supply for red circuits |
| Refineries (basic) | 1-2 | One refinery provides enough petroleum for this scale |
| Red circuit assemblers | 1 | For blue science modules |
| Copper wire assemblers | 1 | Feeds red circuits (if not already on bus) |

{{< callout "warning" >}}
The most common mistake is not enough refineries. With basic processing, one refinery outputs 40 petroleum gas per second. Plastic uses 20/s, sulfur uses 30/s. One refinery can't keep up with both. Build two refineries early.
{{< /callout >}}

{{< section "Layout — Compact Blue Science Cell" >}}

A compact blue science array fits in roughly 15×30 tiles. Here's the layout pattern:

{{< diagram "diagrams/bluescience-cell.svg" "Compact blue science cell with engine and sulfur sub-factories feeding 5 science assemblers" "760" >}}

The engine assemblers sit next to the bus, pulling steel, iron, gears, and pipes. The sulfur plant takes petroleum from the pipe and outputs to a belt. Red circuits come from an existing production line.

{{< section "Transitioning to Advanced Oil Processing" >}}

Once you research advanced oil processing, your refinery setup changes significantly:

| Aspect | Basic | Advanced |
|--------|-------|----------|
| Crude per cycle | 100 | 100 + 50 Water |
| Heavy oil output | 30/s | 50/s |
| Light oil output | 30/s | 50/s |
| Petroleum output | 40/s | 30/s |
| Cracking needed | No | Yes |

The catch with advanced processing: it produces more heavy and light oil but less petroleum. You need cracking (heavy→light→petroleum) to balance the outputs. Without cracking, your refineries stall from heavy oil backup.

{{< section "Common Pitfalls" >}}

**Heavy oil backup.** Advanced refining without cracking. The refineries fill up with heavy oil, stop producing, and suddenly your entire base runs out of plastic. Solution: crack heavy oil to light, and light to petroleum. Use a circuit condition to only crack when heavy > 1k.

**Running out of water.** Sulfur and advanced refining both consume water. A single offshore pump feeds about 10 chemical plants. If your sulfur production stalls, check water first.

**Petroleum vs. plastic balance.** One plastic bar needs 20 petroleum gas. At 5 SPM, you need roughly 10 plastic per minute. That's one chemical plant running full time. If red circuit production backs up, plastic is the bottleneck — not copper.

{{< section "Scaling Blue Science" >}}

To go from 5 SPM to 30 SPM:

- Add more refineries (6-8 with advanced + cracking)
- Scale up to 30 blue science assemblers
- Add more engine and sulfur production
- Upgrade belt tiers to keep up with throughput

The refinery setup scales linearly. With advanced processing and cracking, 8 refineries plus 1 heavy→light and 7 light→petroleum crackers provide perfect balance for large-scale production.

{{< section "Bottom Line" >}}

Blue science is the first multi-fluid production chain in Factorio. The key takeaway: petroleum is always the constraint. Build more refineries than you think you need, set up cracking before your tanks fill with heavy oil, and keep water flowing.

**Numbers to remember:**
- 2 refineries minimum for 5 SPM
- 1 engine assembler per 2.5 science assemblers
- Petroleum demand = plastic (20/s) + sulfur (30/s) per chemical plant

**Previous:** [Green Science Guide]({{< ref "/getting-started/green-science-guide" >}})
**Next:** [Oil Processing Guide]({{< ref "/production-ratios/oil-processing-guide" >}})
