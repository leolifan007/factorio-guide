---
title: "Science Packs: Complete Automation Guide"
description: "Every science pack in Factorio, how to produce them, the ratios that matter, and the production chains you need to set up each one."
date: "2026-05-16"
---

## TL;DR

Science packs are how you buy research in Factorio. Each pack costs resources to produce. Here's the minimum you need to know to automate all seven science tiers without running short on any ingredient.

---

## Science Packs Overview

There are seven science packs in a standard Factorio run. Each one unlocks new technologies:

| Science Pack | Unlocks | Key Ingredients |
|---|---|---|
| Red | Early tech | Copper cable, iron gears |
| Green | Automation | Copper cable, iron plates |
| Gray (military) | Combat | Piercing rounds, walls |
| Blue | Oil processing | Electric furnaces, modules |
| Yellow (production) | Productivity modules | Speed modules, low density structures |
| Purple (high tech) | Electronics | Processing units, speed modules |
| Space | End game | Everything combined |

The first three (red, green, gray) are your early game. Blue unlocks oil, which is where most players hit their first real wall.

## Red Science Packs

Red science is the simplest pack. You need:

- 1 inserter (recipe: 1 iron gear + 1 copper cable)
- 1 copper cable (recipe: 0.5 copper plate)

**Build ratio: 1 assembler making inserters can feed about 1 assembler making red science.**

The bottleneck is almost always inserters. Make sure your inserter assembler is never running dry.

## Green Science Packs

Green science requires:

- 1 inserter
- 1 copper cable
- 1 iron gear

The issue: green circuits. You need copper wire AND iron plates to make green circuits, and green circuits feed into everything from this point on.

**Recommended setup: dedicate 2 assemblers to green circuits per 1 green science assembler.**

Green circuits are also used for:
- Advanced circuits (blue circuits)
- Processing units (yellow circuits)
- Modules
- Circuit networks

Build a big green circuit factory early. You will always need more than you think.

## Gray Science Packs (Military)

Gray science is the one most players forget about. It requires:

- 1 piercing round magazine (1 iron plate + 1 copper plate)
- 1 grenade (1 coal + 1 iron plate)
- 1 wall (1 stone brick)

The wall requirement catches everyone. Make sure you have stone brick production going before setting up gray science.

**Gray science is optional in peaceful mode. But if biters are on, automate it early.**

## Blue Science Packs

Blue science is where the complexity jumps. You need:

- Electric furnace (1 steel plate + 5 copper cable + 5 iron gear)
- Express transport belt (1 fast transport belt + 1 iron gear)
- Express inserter (1 fast inserter + 1 iron plate)
- Engine unit (1 steel plate + 1 iron plate + 1 lubricant)
- Electric mining drill (5 steel plate + 10 iron gear + 5 copper cable)

Lubricant is the tricky part. It requires heavy oil, which comes from petroleum. This means you need:

1. Oil extraction (pumpjacks)
2. Refining to petroleum, heavy oil, light oil
3. Lubricant production from heavy oil

The refinery setup alone takes most players 30-60 minutes to figure out the first time. The short version: three refineries feeding into cracking reactors, with valves controlling which products you get.

## Yellow Science Packs (Production)

Yellow science introduces productivity modules. You need:

- Processing unit (3 advanced circuits + 2 copper wire + 1 sulfuric acid)
- Speed module (5 advanced circuits + 5 iron plate)
- Low density structure (2 steel plate + 2 copper plate + 5 plastic bar)

Low density structures are expensive. Steel plates, copper plates, AND plastic bars. Each low density structure requires plastic, which requires petroleum gas from your refinery.

This is the point where you really need to optimize your oil setup or you'll run out of petroleum constantly.

## Purple Science Packs (High Tech)

Purple science needs:

- Processing unit (same as yellow — 1 per pack)
- Speed module (same as yellow — 1 per pack)
- Lithium cathode (electrolyzer setup, requires water + electricity)
- Flying robot frame (1 electric engine unit + 1 battery + 1 steel plate)

Flying robot frames are the bottleneck here. The electric engine unit requires electric engine units, which require engine units, which require lubricant.

Build the full production chain and stock up. Purple science is the last major science before space science, and you'll need a lot of it.

## Space Science Packs

Space science is unique: you can't produce them with assemblers. They come from launching rockets.

Each rocket launch gives you one space science pack. The rocket requires:

- 1 rocket part (100 rocket parts = 1 rocket)
- 1 satellite (expensive: solar panels, accumulators, rocket fuel, etc.)

**Minimum setup for space science: build 100 rocket silos, 100 launch facilities, or... just accept you'll have one or two rockets launching at a time and plan accordingly.**

Most players go with a single massive rocket. Some go with many small rockets. Both work.

## Science Ratios That Actually Matter

These are the ratios I've tested and use in my own bases:

- **Red science**: 1 inserter asm : 1 red science asm (roughly)
- **Green science**: 2 green circuit asm : 1 green science asm
- **Blue science**: 3 blue circuit asm + 2 engine unit asm + 1 electric furnace asm + 1 belt asm + 1 inserter asm → 1 blue science asm
- **Yellow science**: ~3 processing unit asm → 1 yellow science asm
- **Purple science**: ~3 processing unit asm + ~2 speed module asm → 1 purple science asm

The exact ratios depend on beacon and module setups. For a vanilla unmodded run, these approximate ratios will keep you from running out of any ingredient.

## Common Production Chain Mistakes

**Bottlenecking on green circuits**
I cannot stress this enough. Green circuits are used in so many recipes that if your circuit production is slow, your entire factory is slow. Build big.

**Ignoring oil early**
Get oil set up before blue science becomes urgent. Setting up oil under time pressure is how you get a broken refinery that produces nothing but light oil for 2 hours.

**Underestimating lubricant demand**
Electric engine units consume a lot of lubricant. Don't crack all your heavy oil to light oil too aggressively — keep some flowing to lubricant production.

**Not building enough mining drills**
Iron and copper patch depleted? Already have a new patch lined up? If not, your entire factory is about to stop. Always have the next ore patch ready before the current one runs out.

## The Research Queue Trick

In Factorio, you can queue multiple research projects. The trick is to queue expensive research (like the 1000+ packs type) and fill the gaps with cheap research that you can complete quickly.

This keeps your science assemblers running at full capacity instead of waiting for expensive packs to finish.

---

## Bottom Line

Science pack automation follows a simple pattern: identify the bottleneck ingredient, build more of it, check if something else becomes the bottleneck, repeat.

The base will grow. New bottlenecks will appear. That's the game. The key insight is that green circuits and oil are the two things that trip up every new player. Get those two production chains running smoothly, and blue through space science is just more of the same pattern.

Keep the belts fed. Keep the inserters fed. Automate everything.
