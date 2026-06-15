---
title: "Factorio Smelting Ratios - How Many Furnaces Per Belt (Iron/Copper/Steel)"
description: "Exact smelting ratios for Factorio: how many furnaces per yellow/red/blue belt of iron, copper, steel, and stone. Electric furnace vs steel furnace math - never waste furnaces or belt capacity again."
date: 2026-05-18
lastmod: 2026-06-15T13:40:00+08:00
tags: ["production-ratios", "smelting", "belts"]
draft: false
---

Your smelting column is 30 furnaces long and there's still not enough iron plates. You add more furnaces, but the belt doesn't fill up. I spent my first 50 hours in Factorio doing exactly this -- adding more stone furnaces until the input belt backed up and the entire thing stalled. The problem wasn't enough furnaces. It was the wrong ratio of furnaces to belt capacity.

{{< callout "tip" >}}
**TL;DR:** One half of a basic belt needs 12 stone furnaces (6 electric). A full basic belt needs 24/12. Fast belt doubles that: 48/24. Express belt: 72/36. Steel: 5 iron plates per steel bar --one electric furnace produces steel at the same rate as 5 stone furnaces smelting iron.
{{< /callout >}}

## What I Got Wrong About Furnace Math

The first mistake I made was assuming more furnaces always meant more output. It doesn't -- not after you hit belt capacity. A basic yellow belt carries 7.5 items per second at full compression. If your furnaces produce faster than that, the belt compresses fully and the surplus furnaces just sit idle.

Here's the per-furnace throughput:

- **Stone furnace:** 1 plate per 3.2 seconds = 0.3125 plates/sec
- **Steel furnace:** 1 plate per 2 seconds = 0.5 plates/sec (unlocked at Automation 2)
- **Electric furnace:** 1 plate per 1.6 seconds = 0.625 plates/sec (unlocked after blue science)

I ran stone furnaces for way too long because I didn't realize steel furnaces are a 60% throughput upgrade -- same footprint, no power cost. Electric furnaces add another 25% on top but need the power grid.

## Iron and Copper Smelting -- the Exact Ratios

| Belt Type | Plates/sec needed | Stone furnaces | Steel furnaces | Electric furnaces |
|-----------|:-----------------:|:--------------:|:--------------:|:-----------------:|
| Basic belt (half lane) | 3.75 | 12 | 8 | 6 |
| Basic belt (full lane) | 7.5 | 24 | 15 | 12 |
| Fast belt (half lane) | 7.5 | 24 | 15 | 12 |
| Fast belt (full lane) | 15.0 | 48 | 30 | 24 |
| Express belt (half lane) | 11.25 | 36 | 23 | 18 |
| Express belt (full lane) | 22.5 | 72 | 45 | 36 |

The pattern: a half-lane of fast belt matches a full lane of basic belt (7.5/sec). This means you can upgrade belt tier and halve your furnace array -- or keep the furnaces and switch to express, which I found was the better strategy when transitioning to megabase.

{{< callout "warning" >}}
Don't build your smelting column at the edge of your base. I did this on my first playthrough and had no room to add steel furnaces later. Leave 10+ tiles of space on both sides of the furnace line. You'll thank yourself when you switch from stone to steel.
{{< /callout >}}

## Steel -- the Ratio That Trips Everyone Up

Steel is the most misunderstood recipe in early-game smelting. One steel bar takes 17.5 seconds in a stone furnace and needs 5 iron plates. But here's what I see most beginners get wrong: they think one stone furnace of iron feeds one stone furnace of steel.

The math:
- 1 stone furnace iron: 0.3125 plates/sec
- 1 stone furnace steel: 1 plate per 17.5 seconds = 0.057 plates/sec
- At 5 iron per steel: you need 0.057 × 5 = 0.285 iron plates/sec
- That's just 1 stone furnace of iron (0.3125 > 0.285)

So 1 iron furnace feeds 1 steel furnace? Barely. But that's at stone furnace speed. Here's the real floor:

| Steel furnaces | Iron furnaces feeding them (stone) | Steel plates/sec | Belt saturation |
|:--------------:|:----------------------------------:|:----------------:|:---------------:|
| 1 | 1 | 0.057 | Negligible |
| 10 | 10 | 0.57 | 8% of basic belt |
| 24* | 120 (not practical) | 1.36 | 18% of basic belt |
| 40 with beacons | ~80 electric furnaces | ~10 | Full express belt lane |

*24 steel furnaces (steel furnace building, not stone) with 5 speed-3 beacons each produces roughly 10 steel/sec -- one full fast belt lane. The iron smelting needed for that alone is 50 plates/sec -- three and a half express belts of iron. I learned this the hard way when I built a steel column and watched my iron bus drain instantly.

## Where I Messed Up My First Smelting Column

**I built it too close to the bus.** My first factory had the furnace column right next to the main bus with no room. When I needed to add steel furnaces, I had to tear down half the bus. Now I leave a 10-tile gap between the last furnace and the bus start.

**I didn't balance belt sides.** A splitter feeding furnaces only pulls from one belt lane. Iron ore accumulates on one side and the other half of furnaces starve. A lane balancer after the splitter fixes this -- I use a 1-to-2 belt balancer blueprint that I paste at every furnace column start.

**I forgot to upgrade.** I ran 48 stone furnaces for 20 hours when 24 electric furnaces would have fit the same space with more output and no pollution. Set a reminder to upgrade to electric furnaces once you have nuclear power -- the pollution reduction alone is worth it.

## Beaconed Smelting -- Megabase Scale

Once you have productivity module 3s and speed beacons, the ratios change completely. Each beaconed electric furnace with 2 speed module 3s surrounded by 8 beacons produces roughly 2.5 plates per second:

| Setup | Plates/sec per furnace | Furnaces per belt lane | Total for full express belt |
|:------|:----------------------:|:----------------------:|:---------------------------:|
| Electric, no modules | 0.625 | 18 | 36 |
| Electric + prod3 (x2) | 0.44 | 26 | 52 |
| Electric + prod3 + 8 beacons | ~2.5 | 5 | 10 |
| Electric + prod3 + 12 beacons | ~3.3 | 4 | 7 |

The huge jump with beacons means 10 furnaces replace 36 -- one beacon array produces more than a non-beaconed setup three times its size. But the iron ore consumption also triples. A full express belt of iron plates needs roughly 150 iron ore per second -- which is 6+ electric mining drills.

---

## Community Verification & Resources

- [Official Factorio Wiki -- Furnace ratios](https://wiki.factorio.com/Furnace) -- exact crafting speeds and pollution values for all furnace types
- [FactorioLab Calculator](https://factoriolab.github.io/) -- input/output ratio calculator for any belt and furnace combination
- [Reddit -- Megabase Smelting Arrays](https://www.reddit.com/r/factorio/) -- community beaconed smelting blueprints and lane balancer designs

**Related:** [Oil Processing Guide]({{< ref "/production-ratios/oil-processing-guide" >}}) | [Nuclear Power Guide]({{< ref "/base-design/nuclear-power-guide" >}}) | [Kovarex Enrichment Guide]({{< ref "/production-ratios/kovarex-enrichment-guide" >}})
