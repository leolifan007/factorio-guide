---
title: "Base Design — factorio Layout & Architecture"
description: "Main bus, city blocks, beacon setups, nuclear reactors, and megabase layouts. Every factory architecture explained with diagrams."
date: "2026-05-17"
---

## Base Design in Factorio

A great factory isn't just about producing items — it's about producing them **in a way that's organized, expandable, and repairable**. Base design is the art of organizing production chains spatially.

---

## Main Bus Architecture

The **main bus** is the most popular mid-game factory architecture. A set of parallel bus lanes runs down the center of the factory, and each production line pulls from the bus.

### What Goes on the Main Bus (in order)
1. **Iron plates** — 2 to 4 lanes
2. **Copper plates** — 1 to 2 lanes
3. **Gears** — 1 lane
4. **Electronic circuits (green)** — 1 lane
5. **Steel plates** — 1 lane
6. **Advanced circuits (red)** — 1 lane
7. **Plastic bars** — 1 lane

### Bus Width Recommendations
- **Iron:** 4 lanes minimum (you'll need it for green circuits + gears + blue science)
- **Copper:** 2 lanes minimum (green circuits + red circuits)
- **Gears:** 1 lane (very low total consumption)
- **Green circuits:** 1 lane (high consumption, but compact)

### When NOT to Use a Main Bus
- When you need to ship items **backward** up the factory (bus only works for forward flow)
- When you want absolute UPS efficiency (bus architectures have dead walking sections)
- When playing **Space Age** — Gleba and Fulgora require completely different layouts

---

## City Block Design

**City blocks** are the gold standard for large and megabase builds. Each block is a uniform square (e.g., 64x64 tiles), and every production facility fits inside a block.

### Advantages of City Blocks
- Uniform layout = easy to expand
- Trains can navigate using the same intersections
- Simple to copy/paste with blueprints
- Easy to calculate throughput per block

### Standard Block Sizes
- **64x64** — popular for vanilla megabases
- **48x48** — tighter, more compact
- **32x32** — for tighter resource areas

### Main Bus + City Block Hybrid
Many players use a main bus for early/mid game, then transition to city blocks for late game megabase builds.

---

## Smelting Setups

### Stone vs. Steel vs. Electric Furnaces
| Type | Speed | Fuel | Best For |
|------|-------|------|----------|
| Stone | 0.3125/s | Coal | Very early game |
| Steel | 0.5/s | Coal | Early to mid game |
| Electric | 0.5/s | None | Mid to late game |

### Smelting Array Ratios
- **12 steel furnaces** on a full yellow belt of ore = 1 full yellow belt of plates
- **12 electric furnaces** = same output, zero fuel management
- **24 electric furnaces** = 2 full belts of plates

---

## Nuclear Power Layouts

Nuclear is more complex than steam but produces 25x more power per building.

### Basic Nuclear Setup
- 1 Reactor produces **40 MW** of heat
- Reactors can be adjacent — each neighbor adds 100% bonus heat exchange
- **2-reactor adjacent** = 120 MW total (each reactor 60 MW effective)
- **N-reactor row:** `(N × 40) + ((N-1) × 40)` MW effective

### Kovarex Enrichment
A single Kovarex loop (2 centrifuges with 5% productivity) sustains unlimited nuclear fuel once started.

---

## Beacon & Module Setups

### Speed Beacon Layout
- **8 beacons** per assembler (optimal) — beacons on all 8 adjacent tiles
- Speed Module 3 in both beacons and assembler: 700% base speed
- 1 beaconed blue circuit assembler = ~10 unbeaconed assemblers in terms of output

### Productivity Beacon Layout
- **8 beacons** with Productivity Module 3
- Reduces total packs needed by 30% per tier
- Essential for reducing the scale of high-tier science (purple, yellow, space)

### Mixed Setup (Speed + Productivity)
- Beacons have 2 module slots — can mix Speed 3 + Productivity 3
- **Most efficient late-game setup:** 4 Speed 3 + 4 Productivity 3 per beacon

---

## Megabase Layouts

A **megabase** produces 1,000+ SPM (science per minute). The architecture matters enormously for UPS (updates per second).

### UPS-Friendly Designs
- **Beacon-strip layouts:** Production lines in rows with beacons between
- **Balancer-based** city blocks with train throughput matching production
- **Bot-based megabases:** Less UPS-efficient but simpler to build

### SPM Calculation
- 1 SPM = 1 of each science pack per minute
- **1,000 SPM** requires roughly 5,000 assembling machine 3s (unbeaconed)
- With heavy beaconing: 1,000 SPM can be achieved with ~500 assemblers

---

## Expandable Base Guide

**The number one rule:** Design your first factory assuming you'll want to expand it.

Signs your base is getting cramped:
- Green circuit production can't keep up with demand
- Your bus has more splitters than lanes
- You can't find space to add a new production line

**When to rebuild:**
- Once your first green circuit line is full, plan a second before adding blue science
- The moment biters start eating your production lines, redesign the defense

---

## Related Guides

- **[Main Bus Guide](/base-design/factorio-main-bus-guide/)** — Full bus architecture walkthrough
- **[Beacon Setup Guide](/base-design/factorio-beacon-setup/)** — Module and beacon math
- **[City Block Guide](/base-design/factorio-city-block-guide/)** — Uniform megabase tiles
- **[Nuclear Setup Layout](/base-design/factorio-nuclear-setup-layout/)** — Full reactor blueprints
