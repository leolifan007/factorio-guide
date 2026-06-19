---
title: "Train Chain Signal Intersection Guide - Factorio 2.0 Rail Signaling for Beginners"
date: 2026-06-20
tags: ["trains-logistics", "rail-signals"]
draft: false
---

{{< callout "tip" >}}
**Train signaling in one rule:** Place a chain signal **before** every intersection entry. Place a rail signal **after** every intersection exit. Never place a rail signal inside an intersection. This rule applies to every intersection type -- T-junctions, cross intersections, roundabouts, and merge lanes.
{{< /callout >}}

{{< section "Rail Signals vs Chain Signals" >}}

There are only two types of train signals in Factorio. The difference is simple:

| Signal Type | Color | What It Checks | Use Case |
|------------|:-----:|---------------|:--------:|
| Rail Signal | Green/Red | Checks only the track block ahead | Straight track segments, exits |
| Chain Signal | Yellow/Red | Checks the signal ahead of it | Intersection entries, merges |

A **rail signal** turns green when the block ahead is empty. A **chain signal** copies the state of the next signal -- if the next signal is red, the chain signal is also red. This chain reaction prevents trains from stopping inside intersections.

{{< callout "warning" >}}
**Common deadlock scenario:** A train enters an intersection, stops because the exit block is occupied, and blocks all other traffic through the intersection. This happens when you use a rail signal at the entrance instead of a chain signal. Chain signals prevent this by only letting a train enter when the entire path through the intersection is clear.
{{< /callout >}}

{{< /section >}}

{{< section "The Golden Rule Applied" >}}

{{< diagram "diagrams/train-signal-rules.svg" "Train signal placement rules showing correct chain-before-rail-signal pattern and the wrong rail-signal-inside-intersection deadlock scenario" "760" >}}

For any intersection:

1. **Before the intersection** (entry): Place a chain signal on each track entering the intersection
2. **Inside the intersection**: No signals at all
3. **After the intersection** (exit): Place a rail signal on each track leaving the intersection

**Why this works:** The chain signal at entry checks the rail signal at exit. If the exit block is clear, the chain signal turns green (or blue for multi-track paths), and a train can cross the intersection without stopping. If any exit is blocked, the chain signal stays red and trains wait outside the intersection.

**Why a rail signal inside the intersection causes deadlocks:** A train passes through the intersection and stops at the rail signal, blocking the crossing. This is the most common cause of train deadlocks in Factorio and the reason experienced players always use chain signals at intersection entries.

{{< /section >}}

{{< section "Intersection Types" >}}

**T-Junction (3-way):**
- Chain signal on each of the 3 entries
- Rail signal on each of the 3 exits
- No signals on the junction itself

**Cross Intersection (4-way):**
- Chain signal on all 4 entries
- Rail signal on all 4 exits
- Keep the crossing area clear of any signals

**Roundabout:**
- Chain signal on each entry to the roundabout
- Rail signal on each exit from the roundabout
- Chain signals between roundabout exits (breaks the circle into segments)

For existing rail layouts, if you already have a [basic rail network]({{< ref "/trains-logistics/basic-rail-network" >}}) set up, review each intersection. You probably have at least one rail signal inside an intersection that will cause a deadlock when traffic gets heavy.

{{< /section >}}

{{< section "Chain Intersection Chains (Train Yards)" >}}

For tight clusters of intersections (like a train unloading station with multiple parallel tracks feeding a single output):

- Use **chain signals** on every entry
- Use **chain signals** throughout the entire chain of intersections
- Use a **rail signal** only on the final exit of the entire system

This garantee that a single train does not block multiple intersections. If space is tight between intersections (less than a train length), chain signals all the way through.

{{< callout "info" >}}
**Train length spacing:** The safest distance between consecutive rail signals is at least one full train length. If you have shorter gaps between intersections, treat the whole area as a single block and use chain signals exclusively until the final exit.
{{< /callout >}}

{{< /section >}}

{{< section "Common Mistakes" >}}

- **Rail signal inside a roundabout:** The most common error. A rail signal inside a roundabout lets a train stop on the roundabout, blocking all other traffic. Use chain signals between each roundabout exit instead.
- **Missing signals on one side:** Two-way tracks need signals on BOTH sides. A rail signal on only one side of a two-way track lets trains pass in only one direction.
- **Forgeting to use signals in logistics stations:** A station with multiple loading/unloading bays needs chain signals on the bay entries. Without them, trains queue up inside the station and block the main line. See [How to Use Blueprints]({{< ref "/blueprints/how-to-use-blueprints" >}}) for station layout examples.
- **Too few blocks on long tracks:** A 500-tile straight track with one signal at each end means the entire track is one block. A single train on it blocks all other trains from using that track. Add signals every 1-2 train lengths to create more blocks.

{{< /section >}}

{{< section "Quick Reference" >}}

| Scenario | Entry Signal | Exit Signal |
|----------|:-----------:|:-----------:|
| Single intersection (T or 4-way) | Chain | Rail |
| Roundabout | Chain | Rail |
| Chain of intersections < train length | Chain | Chain (until final) |
| Merge lane (Y-shaped) | Chain | Rail |
| Unloading station with multiple bays | Chain | Rail |
| Two-way single track | Chain (both sides) | Chain (both sides) |

{{< /section >}}

{{< section "Bottom Line" >}}

Train signaling is the most common source of frustration in Factorio logistics, and it has one solution: chain signals before intersections, rail signals after. Build your intersections with this rule, and your rail network will never deadlock. The signal count for even complex intersections is always the same: N chain signals (entries) + N rail signals (exits).

{{< /section >}}

{{< section "Community Verification" >}}

- [Factorio Wiki: Railway signals](https://wiki.factorio.com/Railway/Signals) -- Official signal mechanics documentation
- [Factorio FFF: Space Age train improvements](https://factorio.com/blog/post/fff-422) -- Train changes in 2.0 (train groups, interrupt conditions)
