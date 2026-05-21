---
title: "Your First Factory — Factorio Beginner Guide"
description: "Factorio beginner guide: building your first factory from scratch. Automation, red+green science, furnace columns, mall setup, and the expansion path to mid-game."
date: 2026-05-21
tags: ["getting-started", "beginner"]
draft: false
emoji: "🏭"
---

Your first factory is a mess. That's normal. The inserter grabbing from the furnace is putting iron plates into the gear assembler that's feeding the red science — but the belt looped back and now everything's on the same belt and nothing reaches the lab. Here's a cleaner starting setup.

{{< callout "tip" >}}
**TL;DR:** Build a furnace column feeding a main bus. 4 lanes iron, 2 lanes copper. Science off the bus as a side-factory. Don't belt-engineer on the main bus — build science on dedicated lines that pull from the bus and output packs on a separate belt.
{{< /callout >}}

## The Root Cause — Why First Factories Stall

The mistake is building everything in-line. Smelters → belt → assemblers → belt → labs, all in one long chain. One assembler runs out of input and the entire line stops.

The fix is the **main bus**: a set of parallel belts running through the factory. Each production line pulls what it needs from the bus. The bus keeps flowing even if individual production lines stall.

**Step 1 — Smelting column.** Build 24 stone furnaces per ore type (12 each side of a belt). Iron on one belt, copper on another. Steel needs 5 iron per plate — build a dedicated steel column later.

**Step 2 — The bus.** Run 4 lanes of iron, 2 lanes of copper, 1 lane of gears, 1 lane of green circuits down the middle of your factory. Leave room to add more lanes.

| Resource | Lanes on bus | Why this many |
|:---------|:-----------:|:--------------|
| Iron plates | 4 | Green circuits + gears + science + ammo |
| Copper plates | 2 | Green circuits + red circuits + science |
| Iron gears | 1 | Inserters + belts + red science |
| Green circuits | 1 | Everything past green science |

**Step 3 — Science side-factory.** Don't put science assemblers on the bus. Build them on the side, pulling resources from the bus:

- Red science: 5-10 assemblers on the side of the bus
- Green science: separate sub-factory with its own belt/inserter production
- Science packs output to a single belt → labs

{{< callout type="info" >}}
**Quick Tip:** Your mall (building item production) is a separate thing from your science line. The mall produces belts, inserters, assemblers, furnaces — things you hand-place. Science produces research packs. Don't mix the two on one belt. If your belt assembler runs out of iron, you still want science running.
{{< /callout >}}

## The Exact Setup That Works

**Furnace area** (build first):
- 48 stone furnaces: 24 iron (12 per side), 24 copper (12 per side)
- Output to 4 belts: 2 iron, 2 copper (upgrade to 4 iron lanes later)

**Belt balancer** (after furnaces):
- A 4-to-4 balancer at the start of the bus
- Keeps all lanes balanced even if some furnaces underproduce

**Production off the bus** (build in order):

| Off-bus line | What it makes | Resources from bus |
|:-------------|:--------------|:------------------|
| Line 1 | Red science | Iron plates + gears |
| Line 2 | Green circuits | Iron + copper plates (needs its own copper cable first) |
| Line 3 | Mall: belts, inserters, assemblers | Iron + copper + green circuits |
| Line 4 | Green science | Inserters + belts + green circuits |
| Line 5 | Furnace upgrade (steel) | Iron plates (separate column) |

**Lab area** (at the end of the bus):
- 20 labs in a 2×10 grid
- Feed science from one side
- Use inserters to pass science packs between labs

## Where Most Players Mess This Up

**No space between bus lanes.** The bus needs gaps — 2 tiles between each lane pair. This is where underground belts, splitters, and power poles fit. No gaps means you can't pull from the bus without rebuilding it.

**Science on the bus.** If your science assemblers output back onto the bus, your labs will pull materials intended for other production. Science output needs its own dedicated belt.

**Copper runs out.** Green circuits need 3 iron + 1 copper per circuit. At scale, green circuits consume copper faster than anything else. 2 lanes of copper become 1 lane to circuits and 1 lane to everything else. Expand your copper supply early.

## What's Next After Red + Green Science

Once red and green are automated, the next milestones:

1. **Steel production** — 5 iron plates per steel -> 4 steel furnaces for every 20 iron furnaces
2. **Oil processing** — plastic + sulfur for blue circuits + military science
3. **Blue science** — needs engines (steel + pipes + gears) and red circuits (green circuits + plastic)
4. **Military science** — walls + grenades + piercing ammo. Don't rush this unless biters are pressing

Each milestone is a new side-factory pulling from the bus. The main bus design means you can build all of them without tearing down what already works.

---

## Community Verification & Resources

- [Official Wiki — Tutorial](https://wiki.factorio.com/Tutorials) — beginner walkthroughs and progression guides
- [Official Factorio Wiki — Main Bus](https://wiki.factorio.com/Main_bus) — bus width recommendations and balancer designs
- [Reddit — New Player FAQ](https://www.reddit.com/r/factorio/wiki/faq) — community answers to common first-factory problems
- [FactorioLab Calculator](https://factoriolab.github.io/) — plan your factory ratios before building
