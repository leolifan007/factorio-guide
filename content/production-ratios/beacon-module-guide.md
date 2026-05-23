---
title: "Modules and Beacons — The Late-Game Multiplier"
description: "Factorio modules and beacons guide. Speed vs productivity module math, beacon coverage math, the 8-beacon optimal layout, where to use each module type, and the Space Age quality module layer on top."
date: 2026-05-23
lastmod: 2026-05-23T17:57:00+08:00
publishDate: 2026-05-28T13:47:00+08:00
tags: ["production-ratios", "base-design", "modules", "beacon"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

Modules and beacons are the late-game power tools that separate a working factory from a megabase. But the math is confusing, the numbers in most guides are wrong in at least one place, and the productivity-versus-speed tradeoff breaks most players' first attempts at a proper module setup. You added modules to your assemblers. Production went up slightly. Then you added beacons. Everything broke. The machine is consuming five times the power for two times the output. Your UPS dropped. Your power bill is through the roof.

The problem isn't the modules. It's understanding how the three module types interact with each other and with beacons. Here's the actual math.

Modules and beacons are the two most misunderstood systems in Factorio. You add modules to machines, beacons spread their effects to nearby machines. Sounds simple. The math that governs how they interact is not.

The reason most module setups fail: productivity and speed modules have opposite effects on machine speed. Productivity modules slow machines down. Speed modules compensate. Beacons only carry speed modules. Getting the ratio right is the whole game.

Speed Module 1: +20% speed, -15% productivity
Speed Module 2: +40% speed, -30% productivity
Speed Module 3: +50% speed, -40% productivity

Productivity Module 1: +10% productivity, -15% speed
Productivity Module 2: +15% productivity, -30% speed
Productivity Module 3: +30% productivity, -40% speed

Productivity Module 4 (Space Age, made with tungsten carbide): +10% base + quality bonus, -15% speed

The trade-off is real. Productivity modules produce more items per craft, but each craft takes longer. Speed modules cancel out the slowdown. Together: +30% productivity at full speed.


{< diagram "diagrams/8-beacon-layout.svg" "8-beacon layout — module slots, speed beacon coverage, and 7-tile grid spacing" "820" >}

## The Speed-Productivity Paradox Nobody Explains Right

Here is the exact scenario that breaks most module setups:

You put 4 Productivity Module 3s in an assembler making advanced circuits. Advanced circuits take 6 seconds per craft normally. With productivity 3, the machine slows by 40% — now each craft takes 10 seconds. You get 30% more circuits per craft, but each craft takes 67% longer. Net: you're making fewer circuits per minute than before.

The fix: beacons with speed modules. If you surround that same assembler with 8 beacons, each containing Speed Module 3 (+50% speed), the 40% slowdown from productivity is cancelled by the 50% speed bonus from beacons. Net: 30% more items per craft, at the original speed.

The math for the perfect productivity setup:
- 4x Productivity Module 3 in the machine: -40% speed
- 8x Speed Module 3 in surrounding beacons: +400% total speed spread (each beacon contributes +50% to nearby machines)
- The 8-beacon layout provides enough speed coverage to cancel the -40% slowdown and add a +10% net speed bonus
- Result: +30% productivity, +10% speed, massive power consumption

This is why the 8-beacon standard exists. It is the minimum beacon coverage to cancel productivity module slowdown while adding a small net speed bonus.

## Beacon Coverage: Why 8 Beacons Per Assembler Is the Standard

A beacon applies speed bonus to all machines within its range (range 4 tiles). The beacon emits 8 directional beams — one for each of the 8 adjacent tiles. If a machine is within range of a beacon, it gets the full bonus.

A single beacon covers up to 8 adjacent tiles (if placed in the exact center of an 8-tile grid). An assembler is 3x3 tiles. The optimal placement for maximum coverage is at the corners and sides of the assembler.

The 8-beacon configuration: place 8 beacons at the 8 positions immediately adjacent to a 3x3 assembler (2 tiles away, covering the corners and edges). This gives the assembler the maximum possible beacon coverage — enough to apply the full speed bonus to all 4 module slots in the assembler.

Any fewer than 8 beacons = incomplete coverage = some module slots get less than full speed bonus = the machine is slower than intended.

## The Module Priority Problem

Not every machine should get productivity modules. The decision tree:

**Use Productivity Modules in machines that:**
- Produce expensive intermediates (low density structures, processing units, rocket control units)
- Craft science packs (purple and yellow especially — high ingredient cost)
- Operate in the rocket silo (biggest ROI in the game — each rocket costs huge resources)
- Have long craft times with valuable outputs

**Use Speed Modules in machines that:**
- Have no productivity available (smelters, oil refineries)
- Have productivity available but ingredients are cheap (basic inserters, electronic circuits)
- Are on a bottleneck production line where speed matters more than ingredient efficiency
- Are in a space platform (beacon density is lower on platforms, speed modules maximize output)

**Use Productivity Module 4 (Space Age) in machines that:**
- Already run Productivity Module 3 and are still bottlenecked
- Produce endgame components (quantum processors,holmium-based products)
- Run in the rocket silo (maximizes the resource efficiency of your most expensive production)

## Productive Modules: When to Use Them, When NOT to

The productivity bonus applies to the output item only. Some items have very low base cost — applying productivity to them gives almost no benefit.

**High ROI for productivity:**
- Rocket control units: base cost ~3 seconds of advanced circuits + 1 speed module. Productivity 3 gives +30% per craft. At scale, this saves thousands of intermediate items per rocket.
- Low density structures: base cost includes 3 copper plates + 1 plastic + 1 steel. Productivity 3 recovers 30% more per craft.
- Processing units: expensive science tier ingredient. Every 10% productivity saves significant intermediate production.

**Low ROI for productivity:**
- Basic inserters: 1 iron plate, 1 iron gear. Productivity gives 30% more per craft, but you were making millions of inserters anyway. Speed modules make more sense here.
- Electronic circuits (green chips): 1 copper cable + 1 iron plate. The ingredient cost is trivial. Speed over productivity.
- Steel plates: smelters don't get productivity modules. Speed modules yes, productivity no.

## Building the Perfect Beacon Array

The tile-perfect beacon layout:
1. Place assemblers on a 7-tile grid (3-tile machine + 4-tile gap for 8 beacons)
2. Place 8 beacons in the 4-tile gaps around each assembler
3. Use underground belts and pipes to route inputs/outputs through the gaps
4. This layout minimizes beacon count per machine output

**The math on efficiency:**
- Perfect 8-beacon layout: 8 beacons covering 1 assembler = 8 beacons per 45 items/min (for a 3x3 assembler at normal speed)
- Alternative 4-beacon layout: 4 beacons covering 1 assembler = partial speed coverage, productivity slowdown not fully cancelled

The perfect layout is always the 8-beacon layout. Any compromise reduces output and efficiency.

**Space platform beacon limitation (Space Age):**
On space platforms, beacon range is reduced. You need more beacons per machine. The layout changes: instead of 8 beacons per 3x3 assembler, you need 12-16 beacons for equivalent coverage. This means space platform production is less efficient per tile than ground production. Plan accordingly.

## Speed Modules: The Late-Game Multiplier

Speed Module 3s in smelters are the most underrated application. Here's why:

A normal electric furnace with no modules produces 1 plate per ~3.5 seconds = ~17 plates/min. A smelter with 4 Speed Module 3s produces 1.5x speed = 1 plate per ~2.3 seconds = ~26 plates/min. That's a 50% increase in smelting output without changing the furnace count.

For a megabase consuming 60,000 iron plates per minute, this is the difference between 3,500 furnaces and 2,300 furnaces. The power cost increases proportionally, but the space saving is massive.

The formula for speed module efficiency in smelters:
- Base: 1 plate/3.5 sec
- Speed Module 3 x4: 1.5x multiplier
- Net: 1 plate/2.3 sec = 50% more output
- Power: 180 kW base x 1.5 = 270 kW per furnace (but you need half as many)

## Pollution Implications of Modules

Productivity modules reduce pollution per item produced — you make more items per unit of ore, so per-item pollution drops. But: they also increase total power consumption (speed beacons draw significant power), and power on coal = pollution.

The net: productivity reduces pollution per item but increases total pollution because you produce more items with the same infrastructure. The planet doesn't care about per-item efficiency — it cares about total pollution cloud.

Space Age addition: quality modules add a new dimension. A rare-quality productivity module 4 might have +15% productivity instead of +10%. This means even better efficiency for the rare items you manage to produce at rare quality.

## The Perfect Module Build Order

Build your module production in this order:

**Phase 1: Smelter row (Speed Module 3)**
- When your base hits mid-game and smelters are a bottleneck, add 4 Speed Module 3s to every smelter
- This is a quick win with immediate UPS and throughput improvement

**Phase 2: Science pack assemblers (Productivity Module 3 + Speed Beacons)**
- When you can afford Productivity Module 3s (expensive to produce), install them in science pack assemblers
- Surround with 8 Speed Beacon 3s per assembler
- This maximizes your science output per research point

**Phase 3: Rocket silo (Productivity Module 3 + Speed Beacons)**
- The rocket silo is where productivity modules pay for themselves fastest
- Each rocket costs hundreds of intermediate items. +30% productivity = +30% rockets per resource.
- Install 4 Productivity Module 3s + 8 Speed Beacon 3s immediately upon unlocking Productivity Module 3

**Phase 4: Space Age quality modules**
- Once you have Quality Module 4 from Aquilo, install them in the rocket silo and key science assemblers
- Quality rare items at +15% productivity are worth the investment

## The Bottom Line

Modules and beacons are not optional for a serious megabase. The productivity-versus-speed paradox resolves cleanly: productivity in expensive-output machines, speed everywhere else, 8 beacons per machine to cancel the productivity slowdown. The 8-beacon standard is not arbitrary — it is the exact number needed to fully cancel the -40% speed penalty from 4 Productivity Module 3s and add a small net speed bonus. Get this ratio right and your megabase produces 30% more with the same ore input.
