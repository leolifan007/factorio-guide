---
title: "Production Ratios — Factorio Ratio Reference"
description: "Exact production ratios for every item in Factorio. Furnace ratios, circuit ratios, science ratios — optimized for any factory scale."
date: "2026-05-17"
---

## Production Ratios

The **Production Ratios** section is your reference guide for Factorio's math. Every recipe has a precise input/output ratio. Understanding these ratios lets you build factories that run at exactly the throughput you need — no overproduction, no starvation.

---

## Why Ratios Matter

Factorio's production chain is a system of ratios. If assemblers run faster than their upstream suppliers, they starve. If they run slower, you waste potential.

For example: **1 Green Circuit** requires **3 Iron Plates worth of copper cable**. If your iron plate supply is 60 items/min but your copper cable supply is only 30 items/min, your green circuit production is limited by copper cable — not iron.

Knowing ratios lets you **balance your factory on paper before you build it**.

---

## Core Smelting Ratios

### Furnace Ratio
Stone furnace vs. steel furnace, ore to plate conversion rate:
- **1 Stone Furnace** smelts ore at 0.3125 plates/second
- **1 Steel Furnace** smelts ore at 0.5 plates/second (60% faster)
- **1 Electric Furnace** smelts ore at 0.5 plates/second (same speed, no fuel needed)

### Steel Ratio
- **1 Steel Plate** requires **5 Iron Plates** (in a steel furnace)
- **Ratio:** For every 1 steel plate/minute, you need 5 iron ore/minute dedicated to steel.

---

## Circuit Ratios

### Copper Cable Ratio
- **1 Electronic Circuit** requires **2 Copper Cable**
- **1 Copper Plate** makes **2 Copper Cable**
- **Effective ratio:** 1 copper plate → 2 cables → 1 circuit (uses 0.5 copper plate per circuit)

**Bottleneck:** Cable production is often the hidden chokepoint in green circuit production.

### Green Circuit Ratio
- **1 Electronic Circuit** = 1 Green Circuit
- Input: 2 Copper Cable + 3 Iron Plates (as cable input) — wait, no.
- **Actual recipe:** 1 Electronic Circuit = 3 Iron Plates + 2 Copper Cable
- **The cable ratio:** 2 cable requires 1 copper plate. So: 1 green circuit = 3 iron plates + 1 copper plate.

**Standard balanced ratio:** 3 green circuit assemblers needs ~1.5 belt of iron, ~1 belt of copper.

### Red Circuit Ratio (Advanced Circuit)
- **1 Advanced Circuit** = 2 Electronic Circuits + 3 Copper Cable + 0.5 (productivity bonus)  
- **Practical ratio:** ~2.5 red circuits per 1 green circuit belt input
- This is the #1 bottleneck for blue science packs

### Blue Circuit Ratio (Processing Unit)
- **1 Processing Unit** = 2 Advanced Circuits + 2 Electronic Circuits
- Very high copper and circuit demand — often the limiting factor for purple/yellow science

---

## Science Pack Ratios

### Red Science Ratio
- **1:1:1 ratio** — 1 inserter, 1 gear, 1 red pack. Dead simple.

### Green Science Ratio
- 1 Green Circuit → 1 Green Science Pack
- Need ~3x more green circuit capacity than any other ingredient

### Blue Science Ratio
- 1 Advanced Circuit + 1 Engine Unit → 1 Blue Science Pack
- **Bottleneck:** Advanced circuit production

---

## Module & Beacon Ratios

### Speed Module Ratio
Speed modules increase assembler speed. The effective ratio changes based on beacon count:
- **Speed Module 1:** +20% speed. 6 beacons with speed 1 = +120% speed bonus.
- **Net result:** 1 assembler with 6 speed beacons does the work of 2.2 unaugmented assemblers.

### Productivity Module Ratio
Productivity modules reduce total packs needed:
- **Productivity Module 3:** +30% productivity. Each pack requires 30% fewer intermediate products.
- **Critical for:** Rocket parts, satellite — where the intermediate product cost is enormous.

### Beacon Setup
The optimal beacon density is **8 beacons per assembler** (each beacon covering 2 sides).
- With 8 speed 3 beacons: assembler runs at 700% base speed
- **Tradeoff:** Beaconed assemblers produce faster but consume more resources per item

---

## Quick Reference Table

| Item | Recipe | Key Ratio |
|------|--------|-----------|
| Iron Plate | 1 Iron Ore | 1:1 |
| Copper Plate | 1 Copper Ore | 1:1 |
| Steel Plate | 5 Iron Plate | 5:1 |
| Copper Cable | 1 Copper Plate | 2:1 |
| Green Circuit | 3 Iron + 2 Copper Cable | — |
| Red Circuit | 2 Green + 3 Copper Cable | — |
| Blue Circuit | 2 Red + 2 Green | — |
| Engine Unit | 1 Steel + 1 Iron Plate | — |
| Battery | 1 Sulfuric Acid + 1 Iron Plate | — |
| Rocket Fuel | 10 Rocket Parts | — |
| Low Density Structure | 1 Steel + 2 Copper Plate | — |

---

## Related Sections

- **[Getting Started](/getting-started/)** — Use these ratios in context
- **[Base Design](/base-design/)** — Layout your factory around these ratios
