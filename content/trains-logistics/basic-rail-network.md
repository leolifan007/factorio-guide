---
title: "Basic Rail Network — Your First Train Setup"
description: "How to build a simple but functional train network in Factorio. Covers tracks, signals, train stops, and schedules."
date: 2026-05-18
tags: ["trains-logistics", "trains", "logistics"]
---

## When to Switch to Trains?

Belts are fine for your starting area. But when ore patches are **500 plus tiles away**, trains become necessary.

> **Rule of thumb:** If you need more than 200 belts of iron/copper, switch to trains.

## Basic Components

| Component | Purpose |
|-----------|---------|
| Rail | The track trains drive on |
| Train stop | Where trains stop to load/unload |
| Rail signal | Controls block access (placed after intersections) |
| Chain signal | Extends block check (placed before intersections) |
| Locomotive | The engine (needs fuel) |
| Cargo wagon | Holds 40 stacks of items |

## Your First Train Line (Step-by-Step)

### Step 1: Lay the Track
Build a **single straight track** from your main base to the mining outpost. Use **rails**, not **straight rails** (they allow curves).

### Step 2: Place Train Stops
- At the **mining outpost**: name it `Iron Ore Pickup`
- At the **main base**: name it `Iron Ore Dropoff`

### Step 3: Add Signals
Place a **rail signal** after each train stop (on the right side of the track).
Place a **chain signal** before any intersection.

<div class="tip-box">
<strong>Signal rule:</strong> Trains drive on the <em>right</em> in Factorio. Place signals on the right side of the track.
</div>

### Step 4: Configure the Train Schedule
1. Open the locomotive UI
2. Add stop: `Iron Ore Pickup` — wait condition: `Full cargo`
3. Add stop: `Iron Ore Dropoff` — wait condition: `Empty cargo`
4. Repeat

## Single Track vs Double Track

| Type | Pros | Cons |
|------|------|------|
| Single track | Cheap, simple | Only 1 train at a time |
| Double track | Multiple trains, bidirectional | More expensive, needs signals |

> **Recommendation:** Start with **single track plus 1 train**. Upgrade to double track only when you have 3 plus trains.

## Common Signal Mistakes

> **Mistake 1:** Placing rail signals on both sides of the track. Only place on the **right**.

> **Mistake 2:** No chain signals at intersections. Trains will deadlock.

> **Mistake 3:** Forgetting that trains need **fuel**. Place a **fuel inserter** at the depot.

**Next:** [Trains and Logistics Overview]({{< ref "/trains-logistics/" >}}) — signals, deadlocks, and LTN.
