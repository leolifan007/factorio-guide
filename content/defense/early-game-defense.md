---
title: "Early Game Defense - Surviving Your First Biter Attacks"
description: "How to defend your Factorio factory in the first hours. The wall-turret-ammo pattern, why gun turrets beat lasers early, pollution control that reduces attacks, and the exact upgrade path. Includes the ammo mistake that loses bases."
date: 2026-05-18
lastmod: 2026-09-26T17:15:00+08:00
tags: ["defense", "beginner", "biters"]
draft: false
---

{{< callout "tip" >}}
**Short answer:** build a **1-tile stone wall ring**, then place **gun turrets every 5-8 tiles**, each fed from a **steel chest with piercing rounds**. The mistake that loses bases is not the wall - it is **ammo starvation**. A turret with no ammo is decoration. Set up a dedicated ammo line *before* your first attack wave, and put efficiency modules in your miners to cut pollution by 30%.
{{< /callout >}}

{{< section "When Biters Actually Attack" />}}

Biters do not attack on a timer. Three things trigger them:

| Trigger | What Happens |
|:--------|:-------------|
| Pollution reaches a nest | Biters become aggressive, send a group |
| You destroy a nest | Immediate retaliation from neighbours |
| Evolution factor rises | Bigger waves, more frequent |

Pollution is the one you control. Every machine you build adds to it, and the cloud spreads until it touches a nest.

{{< diagram "diagrams/space-age/early-defense-layers.svg" "Early game defense layers showing stone wall, gun turrets at spacing, ammo belt, and pollution cloud" "760" >}}

{{< section "Step 1: The Wall (Priority 1)" />}}

A rough circle of **stone walls** around your base. One tile thick is enough for the first several hours.

| Property | Value |
|:---------|:------|
| Cost | Stone bricks only - cheap |
| Effectiveness | Biters cannot chew through quickly |
| Thickness | 1 tile early, 2 tiles once waves grow |
| Shape | Circle or rectangle, no need for perfection |

Do not spend hours designing a perfect wall. A sloppy ring beats no ring by a huge margin.

{{< section "Step 2: Gun Turrets (Priority 2)" />}}

Place **gun turrets every 5-8 tiles** along the wall. Closer means more overlap, which helps against groups.

| Turret | Ammo | DPS | When |
|:-------|:-----|:----|:-----|
| {{<material "gun-turret">}} Gun turret | Firearm magazine | Low | First hours |
| {{<material "gun-turret">}} Gun turret | Piercing rounds | Medium | **Upgrade ASAP** |
| {{<material "laser-turret">}} Laser turret | Electricity | High | Mid game, power hungry |
| {{<material "flamethrower-turret">}} Flame turret | Crude oil | Very high | vs large groups |

**Gun turrets beat laser turrets early** because they need no power infrastructure. A brownout at the wrong moment turns your laser wall off.

{{< section "Step 3: Ammo Management (Where Bases Die)" />}}

Feed each turret from a **steel chest** with a nearby **inserter**.

{{< diagram "diagrams/space-age/early-defense-ammo.svg" "Ammo belt feeding turrets through chests and inserters, with the dedicated production line that keeps it running" "760" >}}

| Ammo Delivery | Reliability |
|:--------------|:------------|
| Dedicated ammo belt + chests | **Best** - set and forget |
| Inserters from a passing belt | Fragile - breaks if belt jams |
| Hand-feeding turrets | Fails within 20 minutes |
| One shared chest for many turrets | Insufficient - runs dry in a wave |

{{< callout "warning" >}}
**Critical:** if your turrets run out of ammo they are just decoration. Build a **dedicated ammo production line** early - assemblers making firearm magazines from an iron plate belt, feeding a belt that runs the whole perimeter. Do this before the first big wave, not after.
{{< /callout >}}

{{< section "Pollution Control (Defense by Not Being Attacked)" />}}

Fewer attacks start with less pollution. This is cheaper than more turrets.

| Method | Effect |
|:-------|:-------|
| Efficiency module 1 in miners | **-30% pollution** |
| Efficiency module 2 in labs | -45% pollution |
| {{<material "solar-panel">}} Solar panels | Zero-pollution power |
| Nuclear power | Near-zero pollution, huge output - see the [nuclear power guide]({{< ref "/base-design/nuclear-power-guide" >}}) |
| Burning excess wood | **More** pollution - do not |

Efficiency modules in your mining outposts are the single highest-value defense investment early. Miners are your biggest pollution source.

{{< section "The Upgrade Path" />}}

As your factory grows, defenses evolve in this order:

| Stage | Wall | Turrets | Ammo |
|:------|:-----|:--------|:-----|
| First hours | Stone | Gun | Firearm magazine |
| Early base | Stone | Gun | **Piercing rounds** |
| Mid game | Stone/Steel | Gun + Laser | Mixed |
| Late | Steel | Laser + Flame | Electricity + oil |
| Expansion | Steel | + Artillery | Shells |

{{< diagram "diagrams/space-age/early-defense-upgrade-path.svg" "Defense upgrade path from stone walls and gun turrets through lasers, flame turrets, and artillery" "760" >}}

Move to **piercing rounds** as soon as you can craft them. It roughly doubles your damage for the same turret count, which is cheaper than building twice as many turrets.

{{< section "Common Early Defense Mistakes" />}}

| Mistake | Consequence |
|:--------|:------------|
| Turrets with no ammo supply | Wall falls on the first wave |
| Wall with gaps at corners | Biters path straight through |
| Lasers before you have stable power | Wall goes down in a brownout |
| Ignoring pollution | Waves grow faster than your defense |
| Building too big too early | Perimeter you cannot afford to staff |

**Do not over-expand early.** A small, well-defended base beats a sprawling one with a thin wall you cannot supply.

{{< section "Related Guides" />}}

- {{< ref "/defense/flamethrower-defense-guide" >}} - the next defense tier
- {{< ref "/defense/artillery-guide" >}} - clearing nests before they attack
- {{< ref "/getting-started/your-first-factory" >}} - the base this defense protects

{{< section "Community Verification and Resources" />}}

- [Factorio Wiki: Enemies](https://wiki.factorio.com/Enemies) - pollution, evolution, and attack mechanics
- [Factorio Wiki: Turret](https://wiki.factorio.com/Turret) - damage and ammo data

*Last updated: 2026-09-26 | Verified against Factorio 2.0.*
