---
title: "Flamethrower Defense — Advanced Wall & Turret Guide"
description: "Complete guide to flamethrower and gun turret defense in Factorio: wall patterns, ammo supply, and biter-proof layouts."
date: 2026-05-18
tags: ["defense", "base-design"]
draft: false
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#2a1000,#8b2500);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;">
<span style="font-family:Orbitron,sans-serif;font-size:2rem;font-weight:900;color:#ff6622;">FLAMETHROWER DEFENSE</span>
</div>

## Why Flamethrower Turrets?

Gun turrets are cheap but chew through ammo. Laser turrets are clean but draw massive power. Flamethrower turrets sit in the middle:

- **Highest raw DPS** of any turret type (direct damage + fire-on-ground)
- **Cheapest to feed** — one pipe of crude oil supplies dozens of turrets
- **Damage over time** — biters keep burning even after leaving the flame area
- **Ignores biter armor** — no damage type resistance early on

## Essential Wall Layout

The classic "dragon's teeth" wall stopped being effective after the combat overhaul. Modern defensive walls use a **kill corridor**:

<div class="depiction-box" style="background:#1a0a0a;padding:1rem;border-radius:8px;border:1px solid #ff6622;font-family:'JetBrains Mono',monospace;font-size:0.7rem;line-height:1.5;">
<pre>
  ← BITER APPROACH →
╔═══════════════════╗  ← Outer wall (2-thick)
║ F  F  F  F  F  F ║  ← Flamethrowers, spaced every 4 tiles
║ G  G  G  G  G  G ║  ← Gun turrets (mix with flamethrowers)
╚═══════════════════╝  ← Inner wall (optional)
     [Wall]              ← Bot repair zone
     [Piercing ammo]     ← Belt-fed from behind
     [Crude oil pipe]    ← Underground pipes to each turret
</pre>
</div>

## Turret Spacing & Circuit Control

| Turret Type | Spacing | Purpose |
|-------------|---------|---------|
| Flamethrower | Every 4 tiles | Primary DPS, area denial |
| Gun turret (piercing) | Every 2-3 tiles | Cleanup, fast biters |
| Laser turret | Behind gun line | Overflow/backup (no ammo needed) |

> **Pro tip:** Add a **red circuit wire** from a storage tank to an inserter to auto-shut off flamethrower supply when the buffer is low. This prevents dry pipes during attacks.

## Oil Supply for Flamethrowers

One pumpjack producing at minimum speed (~2/s) can supply **over 30 flamethrower turrets**:

- 1 turret consumes 3 crude oil per shot
- 1 shot covers ~3 seconds of flame
- At 1 attack per minute, each turret needs <2/s average
- Buffer: 1 tank of crude oil per 20 turrets — enough for sustained fighting

**Belt-fed ammo is a concern** — gun turrets eat piercing ammo fast under sustained assault. Use a **parallel belt circuit** to keep ammo flowing:

1. One express belt of piercing rounds
2. Red inserters from belt into each turret
3. Circuit-conditioned belt only runs when ammo < 100 in turret buffer

## Repair & Logistics Setup

A proper defensive wall needs:

- **Construction bots** in a roboport network behind the wall
- **Repair packs** in a requester chest feeding passive provider chests
- **Spare walls and turrets** in a logistics storage chest
- **Power poles** inside the wall line (large poles to skip gaps)

## Artillery + Flame Combo

Late game, pair flamethrower defense with **artillery**:

1. Artillery shells trigger biter attacks
2. Biters charge toward the loudest thing (your wall)
3. Flamethrowers roast the entire wave
4. Gun turrets clean up survivors
5. Rinse and repeat

**Artillery range tip:** Overlap your artillery range with neighboring artillery to create safe zones. One artillery train outpost per ~4 map chunks.

## Troubleshooting

| Problem | Likely Cause | Solution |
|---------|-------------|----------|
| Walls breached | Too few flamethrower turrets | Add 1 flamethrower every 4 tiles |
| Oil pipe empty | Undersized pipe network | Use underground pipes, upgrade to steel pipe |
| Turret ammo < 50 | Insufficient belt supply | Build an ammo assembler dedicated to the wall |
| Behemoth biters breakthrough | Not enough damage upgrades | Research physical + fire damage upgrades simultaneously |

**Related:** [Early Game Defense]({{< ref "/defense/early-game-defense" >}}) — setting up your first walls.
