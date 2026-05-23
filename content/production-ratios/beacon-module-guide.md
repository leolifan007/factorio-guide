---
title: "Modules and Beacons — The Late-Game Multiplier"
description: "Factorio modules and beacons guide. Speed vs productivity module math, beacon coverage math, the 8-beacon optimal layout, where to use each module type, and the Space Age quality module layer on top."
date: 2026-05-23
lastmod: 2026-05-23T19:09:00+08:00
publishDate: 2026-05-28T13:47:00+08:00
tags: ["production-ratios", "base-design", "modules", "beacon"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

You added Productivity Module 3s to your assemblers. Production went up slightly. Then you added beacons. The machine consumes 5× power for 2× output. Something is wrong.

The problem: productivity modules **slow down** machines. Speed beacons **speed them up**. Getting the ratio right is the whole game.

{{< callout "tip" >}}
**TL;DR:** 4 Productivity Module 3s in a machine = -40% speed, +30% items per craft. Surround with **8 Speed Beacon 3s** (each +50% speed) to cancel the slowdown and gain +10% net speed. Result: **+30% productivity at full speed**. This is why 8 beacons is the standard.
{{< /callout >}}

{{< diagram "diagrams/8-beacon-layout.svg" "8-beacon layout — module slots, speed beacon coverage, and 7-tile grid spacing" "820" >}}

## Module Stats

| Module | Speed | Productivity | Power |
|--------|-------|-------------|-------|
| Speed 1 | +20% | -15% prod | +50% |
| Speed 2 | +40% | -30% prod | +60% |
| **Speed 3** | **+50%** | **-40% prod** | **+70%** |
| Prod 1 | -15% spd | +10% | +50% |
| Prod 2 | -30% spd | +15% | +60% |
| **Prod 3** | **-40% spd** | **+30%** | **+70%** |
| **Prod 4 (Space Age)** | -15% spd | +10% base (+quality) | +80% |

## The Speed-Productivity Paradox

The scenario that breaks most setups:

1. Put 4 PM3s in an assembler making advanced circuits (6 sec craft)
2. Machine slows by 40% → each craft now takes **10 seconds**
3. You get 30% more circuits per craft, but 67% slower
4. **Net result: fewer circuits per minute than before**

**The fix:** 8 beacons with SM3s around that assembler:
- 8 × SM3 = +400% speed spread → fully cancels PM3's -40%
- Net speed: **+10% faster than base**
- Net productivity: **+30% more items per craft**

## Why Exactly 8 Beacons

A beacon's effect range = **4 tiles** in all directions. An assembler is 3×3 tiles. Placing 8 beacons at the positions immediately adjacent to the assembler gives maximum coverage — every module slot receives full speed bonus.

| Layout | Coverage | Result |
|--------|----------|--------|
| 0 beacons (PM3 only) | None | -40% speed, +30% prod — **slower overall** |
| 4 beacons | Partial | Some slowdown remains |
| **8 beacons** | **Full** | **Speed cancelled, +10% bonus, +30% prod** |

Any fewer than 8 = incomplete coverage = wasted module potential.

## Tile Layout: The 7-Tile Grid

```
[B] [B] [ASM] [ASM] [ASM] [B] [B]
[B] [B] [ASM] [ASM] [ASM] [B] [B]
    ↑ 3-tile machine   ↑ 4-tile gap for beacons
    = 7-tile repeating unit
```

Use underground belts and pipes through beacon gaps. This layout minimizes beacon count per machine output.

**Space platform note:** beacon range is reduced on platforms. Expect 12-16 beacons for equivalent ground coverage.

## Where to Use Each Module Type

### Productivity Modules — High ROI Targets

| Target | Why |
|--------|-----|
| Rocket silo | Highest cost per craft — biggest absolute savings |
| Processing units | Expensive science ingredient |
| Low density structures | Moderate cost, high volume |
| Science packs (purple/yellow) | Expensive ingredients compound over time |

### Speed Modules — Better Alternatives

| Target | Why |
|--------|-----|
| Smelters | No productivity available — pure speed win |
| Oil refineries | No productivity — speed reduces bottleneck |
| Cheap intermediates (inserters, green circuits) | Ingredient cost too low for productivity ROI |
| Space platforms | Lower beacon density — speed modules maximize output/tile |

### Quality Module 4 (Space Age)

Install in rocket silo and key science assemblers after unlocking from Aquilo. Rare-quality QM4 can reach +15% productivity — worth the investment for endgame components.

## Smelter Speed Case Study

| Setup | Plates/min per furnace | Furnaces needed for 60k plates/min |
|-------|----------------------|-----------------------------------|
| No modules | ~17 | ~3,500 |
| 4× SM3 | ~26 (+50%) | ~2,300 |
| 8-beacon + 4× SM3 | ~39 (+130%) | ~1,500 |

Power cost increases proportionally, but space savings are massive.

## Build Order

| Phase | Action |
|-------|--------|
| 1 | Add 4× SM3 to smelter row (quick throughput win) |
| 2 | Install PM3 in science assemblers + 8 SM3 beacons (maximize research) |
| 3 | Rocket silo: 4× PM3 + 8× SM3 beacons (fastest ROI in game) |
| 4 | Space Age: QM4 in silo + key science (endgame efficiency) |

## Pollution Note

Productivity modules reduce pollution **per item** (more output per ore). But total pollution often **increases** because you produce more items with the same infrastructure, and speed beacons draw significant power. The planet cares about total cloud size, not per-item efficiency.

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| PM3 without beacons | Machine slower than base — net loss |
| Fewer than 8 beacons | Partial speed cancellation — still losing time |
| PM3 in cheap-item machines (green circuits) | 30% of nearly nothing = nearly nothing |
| Forgetting smelters can't use productivity | Wasted module slot — use speed instead |
| Ignoring power cost | 8 beacons + 4 PM3 = ~5× base power draw |

## The Bottom Line

The 8-beacon standard exists for a reason: it's the exact number needed to cancel PM3's -40% speed penalty while adding +10% net speed. Put productivity in expensive-output machines (rocket silo, science), speed everywhere else, 8 beacons per machine. Your megabase produces 30% more with the same ore input.
