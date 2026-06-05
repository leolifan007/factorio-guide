---
title: "Factorio Green Science Guide - Logistics Science Pack Setup and Ratios"
description: "Green science (logistics science pack) in Factorio: exact assembler ratios, compact layout blueprint, belt balancing, and the sub-factory design that prevents early-game bottlenecks."
date: 2026-05-21
tags: ["getting-started", "science-packs"]
draft: false
emoji: "🧪"
---

Red science was easy: two ingredients, one assembler. Green science is where the actual factory building begins — you need sub-factories for inserters and belts feeding into the science assembler line. Mess up the belt ratio here and you will be hand-crafting belts for the next hour.

{{< callout "tip" >}}
**TL;DR:** 6 belt assemblers + 1 inserter assembler feed 12 green science assemblers. Build a belt/inserter sub-factory that feeds the science line from the side, not through the main bus.
{{< /callout >}}

## The Root Cause — Why Green Science Feels Like a Wall

Green science is the first recipe that requires items requiring other factories. Inserter needs: iron gear + green circuit + iron plate. Transport belt needs: iron plate. Each inserter has an iron gear in it — and those gears compete directly with red science for your gear supply.

The solution is simple math: gear production is your limiting factor, not belt speed.

## The Exact Setup That Works

**The formula:**
- **Green science assemblers:** 12 (two rows of 6 facing each other)
- **Belt assemblers:** 6 (one belt assembler feeds 2 science assemblers)
- **Inserter assemblers:** 1 (one inserter assembler feeds 12 science assemblers)

**Layout (left to right):**

1. Iron plate line runs past both sub-factories
2. First sub-factory: 1 inserter assembler. Output belt feeds toward the science line
3. Second sub-factory: 6 belt assemblers. Output belt merges with the inserter belt
4. Both feed into one belt going to the science line
5. 12 science assemblers in two rows of 6, input belt between them, output belt on the far side

{{< diagram "diagrams/green-science-flow.svg" "Green science production flow — from iron plates to belt and inserter sub-factories to science assemblers and labs" "760" >}}

{{< callout type="info" >}}
**Quick Tip:** Don't put green science production on your main bus. Build it as a standalone side-factory that pulls iron plates from the bus and outputs science packs on a dedicated belt to the labs. It keeps your bus clean and expansion is as simple as copying the side-factory.
{{< /callout >}}

## Where Most Players Mess This Up

**Under-building belt assemblers.** One belt assembler produces 0.5 belts per second. A green science assembler consumes 0.17 belts per second (one pack every 6 seconds). The ratio: 1 belt assembler feeds 3 science assemblers. Many builds use 1 belt assembler for every 6 science assemblers — leads to belt starvation.

**Inserters on the bus.** The inserter recipe produces 1 inserter per 0.5 seconds. One inserter assembler running non-stop produces more than enough for 12+ science assemblers (each needs 0.17 inserters/sec). Don't build three.

**One-sided feeding.** If all ingredients come from one side of the science line, the first assembler hoards materials and the last one runs dry. Use a belt balancer or feed from both ends.

## The Hidden Bottleneck — Gear Consumption

Each inserter needs 1 iron gear. Green science at full tilt (12 packs/sec from 12 assemblers) consumes 2 inserters/sec = 2 gears/sec. Your red science assemblers (assuming 10) need 2 gears/sec too.

That's 4 gears/sec — a full yellow belt of gears. Most builds underestimate this and wonder why the inserter assembler keeps starving even though iron plates are flowing.

**Fix:** Dedicate one gear assembler to green science that doesn't share with red science. 2 gear assemblers on iron will feed both comfortably.

## Scaling It Up

Green science at 60 SPM needs 12 assemblers. For 120 SPM (typical mid-game target):

- 24 science assemblers (4 rows of 6)
- 12 belt assemblers
- 2 inserter assemblers (redundancy helps)
- 4 gear assemblers (2 for inserters, 2 shared)

The footprint stays compact because belt and inserter production is tiny — roughly 1/10th the space of the science line itself.

**Material requirements at 120 SPM:**
- Iron plates: ~45/sec (one compressed yellow belt)
- Copper plates: ~10/sec
- Green circuits: ~20/sec

All fit on a single main bus with room to spare.

---

## Community Verification & Resources

- [Official Wiki — Logistics Science Pack](https://wiki.factorio.com/Logistics_science_pack) — exact recipe timings and crafting speed tables
- [FactorioLab Calculator](https://factoriolab.github.io/) — input/output ratios for any SPM target
- [Reddit — Green Science Builds](https://www.reddit.com/r/factorio/) — community blueprints and layout examples for compact designs
