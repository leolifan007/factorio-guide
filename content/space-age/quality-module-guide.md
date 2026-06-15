---
title: "Factorio Quality Module Guide - Space Age Quality Mechanic Explained"
description: "How the Quality module system works in Factorio Space Age: quality tiers, probability math, quality module insertion strategy, and how to build a quality production line that actually pays off."
date: 2026-05-18
lastmod: 2026-06-15T13:42:00+08:00
tags: ["space-age", "quality", "modules"]
draft: false
---

You built your first quality module, stuck it in an assembler, and nothing happened. I spent my first week in Space Age wondering why my rare quality modules never produced rare items. The mechanic isn't broken -- it just works differently than you think. Here's the actual system and how to exploit it.

{{< callout "tip" >}}
**TL;DR:** Quality modules in assemblers give a % chance to upgrade the output tier. Quality 1 = 1%, Quality 2 = 5%, Quality 3 = 10%. The real trick is the recycler loop: recycle + assemble = infinite quality-upgrade attempts. Beacons are the highest-value quality upgrade target. Priority list: Beacons > Speed modules > Furnaces > Miners > Power armor.
{{< /callout >}}

## How Quality Tiers Actually Work

Space Age introduced 5 quality tiers. Higher quality items are strictly better -- faster speed, lower energy, more range. The jump from common to uncommon alone is worth it for most production.

| Tier | Color | Speed bonus | Energy reduction | Extra effects |
|:----:|:-----:|:-----------:|:----------------:|:-------------|
| Common | Gray | Baseline | Baseline | None |
| Uncommon | Green | +20% | -20% | None |
| Rare | Blue | +40% | -40% | +2 range (turrets) |
| Epic | Purple | +60% | -60% | +4 range |
| Legendary | Orange | +80% | -80% | +6 range, +2 AoE |

The speed bonus stacks multiplicatively with other speed bonuses. A legendary speed module 3 in a legendary beacon gives obscene output. I've seen a single beaconed assembling machine produce 12x its normal output with legendary everything.

## The Quality Module Math

Quality modules give a flat % chance per module to upgrade the output by one tier. The upgrade chain works as: Common > Uncommon > Rare > Epic > Legendary.

| Module | Quality chance per module | Speed penalty | Best for |
|:-------|:------------------------:|:-------------:|:---------|
| Quality 1 | 1% | -10% | Starting out, cheap |
| Quality 2 | 5% | -15% | Beachhead setup |
| Quality 3 | 10% | -20% | Endgame production |

The catch: quality chance is additive per module, but each tier upgrade is a separate roll. If you have 4 quality 3 modules (40% chance), that doesn't mean 40% of outputs are legendary. It means 40% of outputs are at least uncommon. Then the 40% rolls again for rare, then epic, then legendary.

Actual math for 4 quality 3 modules:
- 60% stay common
- 40% upgrade to at least uncommon
- 40% of those roll rare = 16% of total
- 40% of those roll epic = 6.4% of total
- 40% of those roll legendary = 2.56% of total

So 4 quality 3 modules produce roughly 2.5% legendary outputs. That's 40 items per legendary. For beacons, that's fine. For rocket parts, it's painful.

{{< callout type="info" >}}
**Quick Tip:** Quality chance rolls independently per item. On a machine producing in bulk (like a centrifuge or rocket silo), you get consistent quality output because you're rolling the dice 100+ times per minute. On slow machines (one-off assemblers), quality feels like it never triggers. The law of averages works in your favor at scale.
{{< /callout >}}

## The Recycler Trick -- Double Your Quality Attempts

This is the mechanic that makes quality viable. Recyclers break items into component materials -- but they also roll for quality upgrade.

Here's the loop I use:
1. Place an assembler with quality modules producing the item you want
2. Output feeds into a recycler (also with quality modules)
3. Recycler breaks items with a % chance to upgrade
4. Use filtered inserters to sort outputs by quality tier

The recycler has quality module slots too. A recycler with 4 quality 3 modules has the same 40% chance to upgrade. But it also reduces output by 75%. So you lose 75% of materials per pass, and the survivors get a quality roll.

The math: starting with 100 items through one recycler loop, you get roughly 25 items back (75% destroyed), of which 10 are upgraded. Net gain: 15 common + 10 higher-tier. The 75 destroyed items are gone. This is why the recycler trick is only worth it for rare materials or items you can afford to lose.

Where it pays off: **beacon production.** Beacons are expensive but you only need 20-50 of them. The recycler loop on beacon assembly turns 100 common beacons into roughly 25 beacons with 40% quality rate. After 3-4 passes, you have rare/epic beacons.

{{< callout "warning" >}}
Don't use the recycler trick on science packs or ammo. You'll destroy 75% of your production and the quality bonus on a red science pack is worthless. Reserve it for modules, beacons, furnaces, and power armor -- items where quality has a multiplicative effect on your factory.
{{< /callout >}}

## What to Upgrade First (Priority List)

I made the mistake of trying to make legendary iron plates before upgrading my beacons. The order matters a lot:

| Priority | Item | Why this matters |
|:--------:|:-----|:-----------------|
| 1 | Beacons | More beacons = more speed modules affecting more machines |
| 2 | Speed modules | Faster machines = more production per tile |
| 3 | Electric furnaces | Faster smelting = more plates without expanding the bus |
| 4 | Miners | More mining speed = fewer drills needed per ore patch |
| 5 | Power armor | Better personal equipment = faster building |

Beacons first because the effect cascades. A rare speed module in a rare beacon affects every machine in range, not just one. Upgrading assemblers individually gives a smaller marginal benefit.

---

## Community Verification & Resources

- [Official Factorio Wiki -- Quality](https://wiki.factorio.com/Quality) -- exact tier upgrade probabilities and recycler quality mechanics
- [Reddit -- Space Age Quality Discussion](https://www.reddit.com/r/factorio/) -- community-tested quality loops and priority lists
- [Factorio Forums -- Quality Module Math](https://forums.factorio.com/viewforum.php?f=69) -- advanced analysis of recycler loops vs. direct assembly

**Related:** [Aquilo Guide]({{< ref "/space-age/aquilo-guide" >}}) (Quality 5 unlock) | [Space Platform Guide]({{< ref "/space-age/space-platform-guide" >}})
