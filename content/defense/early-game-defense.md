---
title: "Factorio Early Game Defense - How to Survive the First Night"
description: "How to set up Factorio early game defense against biters: turret placement, wall layout, ammo supply, pollution management, and the exact defense setup that carries you to blue science."
date: 2026-05-18
lastmod: 2026-06-15T13:43:00+08:00
tags: ["defense", "beginner", "survival"]
draft: false
---

The biters came at hour 3. My factory had one gun turret and 30 magazines. I rebuilt the wall three times that night. Two hundred hours later, the approach that actually works is simpler than you think: a ring of 6-8 gun turrets with a single belt of ammo. That's it. Here's how to build it before the first attack.

{{< callout "tip" >}}
**TL;DR:** Place 6-8 gun turrets at each chokepoint. Feed ammo from a single belt. Build flamethrowers after oil. Upgrade to laser when you have surplus power. Don't wall off your entire base -- wall the chokepoints between lakes and cliffs. This setup carries to blue science without problems.
{{< /callout >}}

## The First Defense -- Before Red Science

You don't need walls for the first hour. The early biters are small biters with low health. Three gun turrets with 20 magazines each cover the area around your pollution cloud's leading edge.

Placement rule that I found by trial and error: walk to the edge of your pollution cloud on the map (press M). Your turrets should sit just inside that line. Biters attack when pollution reaches them, so intercept them at the pollution edge, not at your furnaces.

I use this placement:

| Turret count | Position | Ammo per turret | Coverage |
|:-----------:|:---------|:--------------:|:---------|
| 2-3 | East (wind typically carries pollution this way) | 30 mags | First 2 hours |
| 2 | North | 20 mags | First 2 hours |
| 2 | South (near spawners) | 20 mags | First 2 hours |
| Add 2-4 | Any new chokepoint | 10 mags | As pollution expands |

The morning after my first night attack, I had only 20 magazines left across all turrets. Hand-crafting ammo for turrets is a trap -- automate it. A single assembling machine 1 making magazines feeds up to 20 turrets with power pole reach.

{{< callout type="info" >}}
**Quick Tip:** Set your turret's ammo limit to 10 magazines (middle click on the turret slot). This prevents the belt from dumping all your ammo into one turret. With 10 per turret, 8 turrets only need 80 total. Your ammo belt won't starve.
{{< /callout >}}

## Walls -- When and How

Add walls when you see medium biters (tinted red on the map). Medium biters deal more damage and come in groups of 5-8. Walls stop them from chewing on the turret directly.

The wall layout I use everywhere:

**Outer layer:** stone wall, single layer.
**Behind wall:** gun turret, 1 tile gap.
**Behind turret:** ammo belt, running perpendicular to the wall.

This gives every turret a direct view of the approaching biters while the wall tanks damage. The 1-tile gap prevents spitters from targeting the belt behind the turret.

Don't surround your entire base. That's 500+ walls for a beginner base. Wall only the chokepoints between lakes, cliffs, and resource patches. Factorio maps are full of narrow passages. A 20-wall gap between two lakes needs 20 walls and 4 turrets -- not 200 walls.

## Ammo Feeding -- The Belt Setup

Hand-feeding turrets stops working after the second attack. The automated belt system is simple:

1. Run one iron plate belt near the turret line
2. Place an inserter from the belt into each turret
3. One assembling machine 1 with iron plates feeds 20+ turrets

The critical piece: **belt direction.** The ammo belt should run parallel to the wall, one tile behind the turrets. Place long-handed inserters from the belt to the turret. This lets you walk between the belt and wall without blocking the ammo flow.

If a biter group breaks through and destroys part of the belt, the remaining turrets keep firing because they hold 10 magazines each. After 50 hours, this belt failure margin has saved my base three times.

## Transitioning to Flamethrowers

Once you research oil processing and flamethrower turrets, the defense game changes entirely. A single flamethrower turret deals area damage and kills groups that would overwhelm 4 gun turrets.

How I integrate them:

| Tech stage | Turret mix | Ammo | Power |
|:----------|:----------|:----|:-----|
| Pre-oil | 6-8 gun turrets | Iron magazine belt | None |
| Oil stage | 2 flamethrowers + 4-6 guns | Heavy oil pipe + ammo belt | Light oil for flamers |
| Blue science | 4 flamethrowers + 4 lasers | Crude/heavy oil pipe + electric | Solar/nuclear |

Flamethrowers use light oil for 25% more damage than heavy oil. I pipe light oil from my refinery to the wall. A single pipe of light oil feeds 8 flamethrower turrets on a standard wall segment.

{{< callout "warning" >}}
Don't skip gun turrets for lasers. Lasers draw 1.2 MW each when firing. Eight lasers firing simultaneously = 9.6 MW. Your mid-game boiler line can't handle that + the factory load. I tried all-laser defense at hour 10 and my entire base brownout-killed me. Gun turrets + flamethrowers are the low-power option.
{{< /callout >}}

## Pollution Management -- Fight the Source

Killing biters is fixing the symptom. Reducing pollution fixes the cause. Before hour 10, check your pollution cloud on the map. If it extends past a nest cluster, you need more defenses or less pollution.

The pollution cheat sheet:

| Source | Pollution/min | How to reduce |
|:------|:------------:|:-------------|
| Boiler (active) | 6/m | Switch to solid fuel, then solar |
| Stone furnace | 0.6/m | Replace with electric furnace (zero pollution) |
| Mining drill (electric) | 10/m | Efficiency module 1 (reduces by 80%) |
| Assembler | varies | Efficiency modules reduce pollution AND power |

The biggest pollution source I see beginners miss: burner mining drills. These produce 10 pollution/m upfront AND burn coal. Replacing them with electric drills and efficiency modules cuts pollution by 70% at the cost of 6 MW per 10 drills.

---

## Community Verification & Resources

- [Official Factorio Wiki -- Enemy](https://wiki.factorio.com/Enemy) -- biter evolution triggers, pollution mechanics, and attack wave sizes
- [Official Factorio Wiki -- Combat](https://wiki.factorio.com/Combat) -- weapon damage stats, turret range, and pierce damage
- [Reddit -- Early Game Defense Blueprints](https://www.reddit.com/r/factorio/) -- popular turret wall designs and chokepoint defense blueprints

**Related:** [Flamethrower Defense Guide]({{< ref "/defense/flamethrower-defense-guide" >}}) | [Artillery Guide]({{< ref "/defense/artillery-guide" >}}) | [Nuclear Power Guide]({{< ref "/base-design/nuclear-power-guide" >}})
