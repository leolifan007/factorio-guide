---
title: "Factorio Gleba Survival Guide - How to Survive and Thrive on Gleba"
description: "How to survive on Gleba in Factorio Space Age: spore management, pentapod defense, agriculture tower setup, spoilage handling, and the exact starter base layout that doesn't starve your science."
date: 2026-05-18
lastmod: 2026-06-15T13:45:00+08:00
tags: ["space-age", "gleba", "survival", "planet-guide"]
draft: false
---

You landed on Gleba and everything is rotting. Your first batch of bioflux spoiled before you could use it. The pentapods eat your crops faster than they grow. I spent my first 4 hours on Gleba rebuilding the same farm setup until I internalized one rule: design for spoilage, not for preservation. Here's the approach that actually works.

{{< callout "tip" >}}
**TL;DR:** Put an assembler on every agricultural tower output. Belt bioflux directly from the tower to the assembler -- don't store it. Ore and nutrients go into a recycler loop that feeds carbon and sulfur production. Use circuit conditions to recycle anything with less than 50% freshness. Build pentapod defense as a triple wall of gun turrets with piercing ammo. Uncommon ammo from quality modules doubles your killing power.
{{< /callout >}}

## What Makes Gleba Different

Gleba has no ore patches. Every resource comes from biological processes that decay over time. Your factories aren't mining -- they're farming and processing before spoilage destroys everything.

The core loop: Agricultural towers grow plants > Plants feed into bioflux production > Bioflux goes to nutrient production or science packs > Nutrients feed every spoilage-related production > Spoiled product becomes pollution > Pollution attracts pentapods.

The constraint is time. Spoilage isn't a timer on your storage -- it's a timer on your production chain. The longer something sits on a belt, the less useful it becomes. Bioflux with 10% freshness produces 90% less science per pack.

| Resource | Base spoilage time | Impact of 50% freshness |
|:---------|:------------------:|:-----------------------:|
| Yumako | 20 min | 50% nutrient output |
| Jelly | 15 min | 50% biofuel efficiency |
| Bioflux | 30 min | 50% science pack output |
| Nutrients | 5 min | Near-worthless after 2 min |
| Science pack* | 60 min | 60% lab research speed |

*Agriculture science packs lose research value as they spoil. Below 50% freshness, they contribute less than 10% of their original value to research progress.

{{< callout type="info" >}}
**Quick Tip:** Nutrients spoil the fastest (5 minutes) so produce them as close to the consumer as possible. I place my nutrient assembler directly next to the biochamber that needs it. Belt distance: less than 20 tiles. Any longer and most nutrients reach the biochamber already 60% spoiled.
{{< /callout >}}

## The Starter Base Layout

| Building | Placement rule | Why |
|:---------|:--------------|:----|
| Agricultural tower | Center of a 20x20 plantable area | Maximum coverage |
| Spoilage sorter | 5 tiles from tower output | No belt storage for fresh crops |
| Crusher | 10 tiles from sorter | Process spoilage locally |
| Bioflux plant | 20 tiles from tower | Keep fresh, reprocess spoiled |
| Recycler | Next to sorter | Destroy < 50% freshness items instantly |
| Defense wall | 30 tiles from tower | Pentapods target farms first |

The single most important element: **spoil on demand.** Don't let crops accumulate. If an agricultural tower outputs 3 yumako/sec and your crusher processes 2/sec, 1/sec rots on the belt. That rot attracts pentapods.

I use a circuit network condition: if the belt from the tower has more than 5 yumako, disable the tower (connect the tower to the green wire). This stops overproduction before it spoils. Without this circuit, the belt fills up and everything past the crusher spoils.

## Spoilage Recycling Loop

Spoilage is not waste. It converts into useful materials through crushers. The loop:

1. **Recycler** next to the first belt segment after the tower. Set to output green or red signal based on spoilage contents.
2. **Spoilage sorter** (filter inserter) pulls < 50% items off the belt and into a crusher.
3. **Crusher** outputs carbon, sulfur, or nutrient. Carbon feeds coal production (for plastic/explosives). Sulfur feeds blue science production.
4. **Nutrient from spoilage** feeds the biochamber itself. That's right -- spoilage becomes the fuel for processing fresh crops.

Don't throw spoilage away. A chest of spoilage is a chest of raw materials. I keep one chest per 10 agricultural towers. The spoilage goes into a continuous recycling loop that outputs carbon for furnace fuel and sulfur for science.

## Pentapod Defense

Pentapods are tougher than Nauvis biters. A medium pentapod survives 4-5 piercing rounds and attacks in groups of 5-8. Small groups won't break a stone wall but larger ones (artifact type) destroy walls in 2 seconds.

| Turret type | Effectiveness | Ammo needed | Power |
|:-----------|:------------:|:-----------:|:----:|
| Gun turret (piercing) | Good | 10 mags/pentapod | 0 |
| Gun turret (uranium) | Excellent | 3 mags/pentapod | 0 |
| Tesla turret (tower) | Very good | 2 shots/pentapod | 2 MW |
| Laser turret | Poor | Takes 8+ seconds | 4 MW |
| Flamethrower | Good | 30 oil/pentapod | 0 |

My Gleba wall uses: 8 gun turrets with piercing ammo + 2 tesla turrets + dragon's teeth (zigzag walls). The dragon's teeth slow pentapods so turrets have 2x the firing time.

**Quality ammo is the Gleba cheat code.** Uncommon piercing rounds deal 1.4x damage. Rare rounds deal 2x. One rare round kills a medium pentapod in 3 shots instead of 5. I ship quality modules to Gleba just for the ammo production and the difference is immediate.

{{< callout "warning" >}}
Don't rely on laser turrets as your primary defense on Gleba. I made this mistake and lost the wall 3 times. Pentapods have 50% laser resistance. A wall of 10 laser turrets performs worse than 6 gun turrets with piercing ammo on Gleba. The power draw also taxes your solar/battery setup and you lose the whole wall when batteries drain.
{{< /callout >}}

## The Science Export Problem

Gleba science packs (agriculture science) spoil during transport. Shipping them to Nauvis by rocket means they lose freshness during the 30-second flight.

My solution: bioflux ships to Nauvis (doesn't spoil in space), and agriculture science packs get consumed on Gleba. I set up 10 labs on Gleba itself. The science packs hit the lab within 30 seconds of production. Spoilage is minimal.

The alternative is to ship fresh bioflux to Nauvis and produce agriculture science there. This works but needs a second set of biochambers on Nauvis. I only do this after Gleba infrastructure is stable.

---

## Community Verification & Resources

- [Official Factorio Wiki -- Gleba](https://wiki.factorio.com/Gleba) -- spoilage rates, crop growth cycles, pentapod spawn rules
- [Factorio Forums -- Gleba Discussion](https://forums.factorio.com/) -- community farm layouts, defense blueprints, and spoilage optimization techniques
- [Reddit -- Gleba Survival Tips](https://www.reddit.com/r/factorio/) -- upvoted guides for new Gleba players and common mistakes

**Related:** [Fulgora Recycling Guide]({{< ref "/space-age/fulgora-recycling-guide" >}}) | [Space Platform Guide]({{< ref "/space-age/space-platform-guide" >}}) | [Quality Module Guide]({{< ref "/space-age/quality-module-guide" >}})
