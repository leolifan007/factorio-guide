---
title: "Flamethrower Defense — Advanced Wall & Turret Layout"
description: "Complete Factorio flamethrower defense guide: wall layout, turret spacing, oil supply, dragon's teeth patterns, and biter-proof designs for early to endgame."
date: 2026-05-18
tags: ["defense", "base-design"]
draft: false
emoji: "🔥"
---

Flamethrower turrets have the highest raw DPS of any early-to-mid-game turret. They cost almost nothing to feed (one pumpjack supplies 30+ turrets), deal area damage over time, and ignore biter armor. A properly designed wall with flamethrowers handles attacks from early-game small biters through late-game behemoths.

{{< callout "tip" >}}
**TL;DR:** Build a wall with flamethrower turrets every 4 tiles, gun turrets every 2 tiles, and a single crude oil pipe behind them. One pumpjack at minimum speed supplies 30+ turrets. Add repair bots and you're set for the entire game.
{{< /callout >}}

{{< section "Why Flamethrower Turrets?" >}}

Each turret type has trade-offs:

| Turret | DPS | Ammo cost | Power draw | Biter armor |
|--------|:---:|:---------:|:----------:|:-----------:|
| Gun turret (piercing) | Medium | High (iron/copper) | Negligible | Resist 20% |
| Laser turret | Medium | None | Massive (2.4 MW each) | Full damage |
| Flamethrower | Highest | Minimal (crude oil) | Very low | Ignores armor |

Flamethrower turrets deal both direct impact damage and fire-on-ground damage over time. Biters keep burning even after running past the flame. This area denial makes them dramatically more efficient than any other turret for the same resource cost.

{{< section "The Kill Corridor — Wall Layout" >}}

Dragon's teeth walls (zigzag patterns) are outdated since the combat overhaul. Modern defense uses a **kill corridor**:

{{< diagram "diagrams/flamethrower-wall.svg" "Kill corridor wall layout with flamethrower and gun turret spacing, ammo belt, and oil pipe" "760" >}}

**Layer breakdown (from outside in):**

1. **Outer wall:** 2-thick stone wall. Biters will damage this regardless.
2. **Kill corridor:** 3-4 tile gap. Biters funnel through here, getting hit from both sides.
3. **Inner wall:** Single-thick stone wall. Protects turrets from spitter acid.
4. **Flamethrower turrets:** Every 4 tiles. Primary DPS.
5. **Gun turrets:** Between flamethrowers. Cleanup crew for fast biters.
6. **Ammo belt:** Express belt of piercing rounds feeding gun turrets.
7. **Oil pipe:** Underground pipes for crude oil to flamethrower turrets.
8. **Roboport:** Behind the wall for repairs.

{{< section "Turret Spacing and Pattern" >}}

**Pattern:** F(lame), gap (2 tiles), G(un), gap (2 tiles), repeat.

This gives you:
- Flame coverage overlapping across the entire wall
- Gun turrets catching any biter that survives the fire
- No gaps in the damage field

{{< section "Oil Supply — More Efficient Than You Think" >}}

This is what surprised me most: flamethrower turrets barely use oil.

- One turret consumes **3 crude oil per shot**
- One shot creates a flame that burns for ~3 seconds
- At 1 attack wave per minute, each turret needs < 2 oil/s average
- A minimum-speed pumpjack (~2/s) supplies **30+ flamethrower turrets**

**Oil logistics:**
1. Run a single pipe line from your refinery or a dedicated pumpjack
2. Use underground pipes every 2 tiles to keep the path clear
3. Buffer: 1 storage tank per 20 turrets — provides 3+ minutes of sustained fire
4. Circuit condition: connect a tank to your refinery. If crude < 500, send a warning

{{< callout "warning" >}}
**Don't use heavy or light oil for flamethrowers.** They work on any oil type, but crude is the cheapest you'll find. Save light oil for solid fuel and cracking.
{{< /callout >}}

{{< section "Ammo Supply — Belt-Fed Gun Turrets" >}}

Gun turrets chew through ammo during big attacks. Here's a reliable setup:

1. Run an express belt of piercing rounds behind the entire wall
2. Use red inserters from belt into each gun turret
3. Set a circuit condition: belt runs only when turret ammo < 100 rounds

{{< callout "tip" >}}
**Ammo production:** One assembler making piercing rounds runs fast enough for a full perimeter. Place it near your wall and feed directly onto the ammo belt loop.
{{< /callout >}}

{{< section "Repair and Maintenance" >}}

A defensive wall needs ongoing maintenance. Here's the logistics setup:

- **Construction bots** in a roboport network (overlapping coverage along the entire wall)
- **Repair packs** in a requester chest near each roboport section
- **Spare walls and turrets** in logistics storage (bots automatically replace destroyed ones)
- **Power poles** inside the wall (large poles to skip gaps)

Build repair stations every 30-40 tiles along the wall. Each station: 1 roboport, 1 storage chest with replacement walls/turrets, 1 requester chest with repair packs.

{{< section "Artillery and Flamethrower Combo" >}}

Late game, artillery triggers attack waves. Flamethrowers handle the cleanup:

1. Artillery shell lands in biter base
2. Biters aggro and charge toward the loudest sound (artillery)
3. They funnel into your kill corridor
4. Flamethrowers torch the entire wave
5. Gun turrets finish survivors
6. Repeat until biter base is gone

**Artillery range tip:** Overlap your artillery wagon range with neighboring outposts. One artillery train stop per ~4 map chunks creates safe zones.

{{< callout "tip" >}}
Use a circuit network around your artillery to detect incoming attacks. Wire a radar to the artillery — when the outpost gets attacked, the circuit flips an alarm. Works better than listening for distant gunfire.
{{< /callout >}}

{{< section "Troubleshooting" >}}

| Problem | Likely Cause | Fix |
|---------|--------------|-----|
| Walls breached | Not enough flamethrowers | Add one every 4 tiles |
| Oil pipe empty | Pipe throughput limit | Use underground pipes throughout |
| Gun turrets out of ammo | Belt supply too slow | Upgrade to express belt, check assembler |
| Behemoth breakthrough | Need more damage upgrades | Research physical + fire damage together |
| Bots not repairing | Roboport too far | Add roboports every 30 tiles |
| Biters path around wall | Wall not sealed | Check for gaps — water, cliffs, ore patches |

{{< section "Scaling for Megabase" >}}

For a full perimeter around a megabase:

1. Build wall modules in blueprint form (50-tile segments)
2. Each segment: 2 walls, 6 flamethrowers, 6 gun turrets, 1 roboport
3. Connect with a crude oil pipe ring around your entire base
4. Add artillery outposts at chokepoints (bottleneck areas between water/lakes)
5. Train-deliver replacement walls and ammo from central production

A full perimeter using this design handles 99% of attacks autonomously. The only intervention needed is the occasional behemoth wave after artillery expansion.

{{< section "Bottom Line" >}}

Flamethrower defense is the most resource-efficient way to protect your factory. One oil pipe, one ammo belt, and a well-designed kill corridor handle everything from early-game small biters to late-game behemoths.

**Numbers to remember:**
- Flamethrowers every 4 tiles, gun turrets every 2 tiles
- One minimum-speed pumpjack supplies 30+ turrets
- Kill corridor: outer wall → 3-4 tile gap → inner wall → turrets
- Roboports every 30 tiles for full repair coverage

**Related:** [Early Game Defense]({{< ref "/defense/early-game-defense" >}}) — setting up your first walls before flamethrowers.
