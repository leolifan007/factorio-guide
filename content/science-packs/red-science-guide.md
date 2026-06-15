---
title: "Factorio Red Science Guide - Automation Science Pack (First Science)"
description: "Everything about the first science pack in Factorio: red science (automation science) exact recipe, assembler count, gear wheel production, and how to automate it properly from the start."
date: 2026-05-18
lastmod: 2026-06-15T13:41:00+08:00
tags: ["science-packs", "getting-started"]
draft: false
---

You just placed your first assembling machine and fed it some iron plates, but the lab's been empty for 10 minutes and you're still hand-crafting research packs. I made the same mistake -- thinking one assembler of red science would carry me through the first hour. It won't. Here's what actually works.

{{< callout "tip" >}}
**TL;DR:** 5-10 red science assemblers fed by a dedicated gear sub-factory. Use a splitter to give iron plates to both the gear assembler and the science line. Belt the finished science to 10+ labs in a row. That's it -- red science is your warmup.
{{< /callout >}}

## The Quirky Recipe Nobody Explains

Red science (automation science pack) takes two ingredients: iron gear wheels and iron plates. One pack takes 5 seconds in an un-moduled assembling machine 1.

What nobody says upfront: you need iron gears as a separate product. A single gear assembler produces enough for 10 red science assemblers -- but only if you have enough iron plates feeding it. If you share belt lanes between gears and iron plates, the lab starves.

Here's the ratio I use:

| Your goal | Red science assemblers | Gear assemblers | Labs supported | Iron plates/min |
|:---------:|:---------------------:|:---------------:|:--------------:|:---------------:|
| Slow start | 5 | 1 (with some) | 10 | ~45 |
| **Standard** | **10** | **1** | **20** | **~90** |
| Rush research | 15 | 2 | 30+ | ~135 |

One gear assembler running at crafting speed 0.5 (assembling machine 1) produces enough gears for 10 science assemblers, with a small surplus. I tried 15 science on one gear maker and it wasn't enough -- the gear assembler becomes the bottleneck and your last 5 science assemblers sit idle.

## The Exact Layout

Build it in this order, and you'll never have to rebuild it:

**1. Iron plate belt.** Run one half-belt of iron plates from your furnace column. Split it into two lanes: one goes to the gear assembler, one goes past the gear assembler (for plates directly).

**2. Gear assembler.** Place 1 assembling machine 1 between the iron plate belt and the science line. Output gears onto a dedicated belt running toward the science assemblers.

**3. Science assemblers.** Place 10 assembling machines in a row. Feed them from both sides: gears from one belt, iron plates from the other. Run a single output belt behind all 10 to carry science packs away.

**4. Labs.** Place 10-20 labs in a row at the end of the science belt. Use inserters to pass packs between adjacent labs (chain feeding). This way your first lab fills up and passes overflow to the next one.

{{< callout "warning" >}}
Don't mix science packs and raw materials on the same belt. I did this on my first playthrough -- iron plates ended up in the lab alongside science packs. The lab skipped the packs and consumed the plates. Use filtered inserters between labs to grab only science packs.
{{< /callout >}}

## Where I Got Stuck

**The gear bottleneck.** I ran 5 labs on one gear assembler for two hours thinking something was wrong. 5 red science assemblers need about 2 gears/sec. One gear assembler makes 1 gear per 1 second (crafting speed 0.5). That's exactly 1 gear/sec -- enough for 5 assemblers with no margin. For 10, you need a full gear belt, which means either speed modules or a second gear assembler.

**Undersized furnace column.** Red science at full tilt (10 assemblers) consumes 1.5 iron plates per second. Your furnace column needs at least 5 stone furnaces on iron to keep up. If your copper furnace row is 24 furnaces and your iron row is 8, iron runs out first. I had to learn the hard way that iron is always the constraint in early game.

Here's the actual resource budget for 10 red science assemblers running continuously:

| Resource | Rate needed | Stone furnaces required |
|:---------|:----------:|:----------------------:|
| Iron plates | 1.5/sec | 5 |
| Iron gears | 1.0/sec | 1 gear assembler |

Total: 5 stone furnaces on iron plus 1 gear assembler. That's tiny. The mistake is not allocating enough iron to science vs. building materials.

## Research Order After Red Science

Once red science is automated, the research tree opens up fast. Here's why steel processing should be your first target -- not engines:

| Research | Cost (red packs) | Unlocks | Priority |
|:---------|:----------------:|:--------|:--------:|
| Steel processing | 100 | Steel furnaces (2x smelting speed) | **1st** |
| Engine | 100 | Engine unit (needed for blue science) | 2nd |
| Automation 2 | 100 | Electric mining drill | 3rd |
| Logistics | 100 | Green science (next tier) | 4th |

Steel furnaces double your smelting overnight. 10 steel furnaces replace 20 stone ones in the same footprint. I always rush this before green science because it means I never hand-feed furnaces again.

---

## Community Verification & Resources

- [Official Factorio Wiki -- Automation Science Pack](https://wiki.factorio.com/Automation_science_pack) -- exact recipe timings and crafting speed formulas
- [FactorioLab Calculator](https://factoriolab.github.io/) -- input/output ratio calculator for any SPM target
- [Reddit -- Early Game Science Builds](https://www.reddit.com/r/factorio/) -- community blueprints for compact red-to-green science arrays

**Related:** [Your First Factory]({{< ref "/getting-started/your-first-factory" >}}) | [Green Science Guide]({{< ref "/getting-started/green-science-guide" >}}) | [Smelting Ratios]({{< ref "/production-ratios/smelting-ratios" >}})
