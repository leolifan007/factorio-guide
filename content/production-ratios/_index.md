---
title: "Production Ratios — Factorio Ratio Reference"
description: "Exact production ratios for every item in Factorio. Furnace ratios, circuit ratios, science ratios — optimized for any factory scale."
date: "2026-05-21"
---

## Production Ratios

The **Production Ratios** section is your reference guide for Factorio's math. Every recipe has a precise input/output ratio. Understanding these ratios lets you build factories that run at exactly the throughput you need — no overproduction, no starvation.

---

## Why Ratios Matter

Factorio's production chain is a system of ratios. If assemblers run faster than their upstream suppliers, they starve. If they run slower, you waste potential.

For example: **1 Green Circuit** requires **3 Iron Plates + 2 Copper Cable** (made from 1 Copper Plate). If your iron supply is 60 items/min but your copper output is only enough for 30 items/min, green circuit production caps at copper throughput.

Knowing ratios lets you **balance your factory on paper before you build it**.

---

## Core Smelting Ratios

### Furnace Ratio
Stone furnace vs. steel furnace, ore to plate conversion rate:
- **1 Stone Furnace** smelts ore at 0.3125 plates/second
- **1 Steel Furnace** smelts ore at 0.5 plates/second (60% faster)
- **1 Electric Furnace** smelts ore at 0.5 plates/second (same speed, no fuel needed)

### Steel Ratio
- **1 Steel Plate** requires **5 Iron Plates**
- **Ratio:** For every 1 steel plate/second, you need 5 iron plates/second dedicated to steel.

---

## Circuit Ratios

### Copper Cable Ratio
- **1 Copper Plate** makes **2 Copper Cable**
- **1 Electronic Circuit** requires **2 Copper Cable**
- **Net:** 1 copper plate feeds 1 green circuit assembler

### Green Circuit Ratio
- **1 Electronic Circuit** = 3 Iron Plates + 2 Copper Cable
- The 2 copper cables come from 1 copper plate
- **Standard ratio:** 3 green circuit assemblers need ~1.5 belts of iron and ~1 belt of copper supply

### Red Circuit Ratio (Advanced Circuit)
- **1 Advanced Circuit** = 2 Electronic Circuits + 2 Copper Cable + 1 Plastic Bar
- **Supply chain:** 3 red circuit assemblers consume roughly 1 full belt of green circuits

### Blue Circuit Ratio (Processing Unit)
- **1 Processing Unit** = 2 Advanced Circuits + 20 Electronic Circuits
- **Total raw:** 1 blue circuit needs ~40 iron plates + ~30 copper plates worth of intermediates
- Very high demand — always build dedicated blue circuit sub-factories

---

## Science Pack Ratios

### Red Science Ratio
- 1 Iron Gear + 1 Copper Plate → 1 Red Science Pack
- 5 assemblers = ~1 red science per second

### Green Science Ratio
- 1 Inserter + 1 Transport Belt → 1 Green Science Pack
- 1 inserter assembler feeds ~12 science assemblers; 1 belt assembler feeds ~24

### Blue Science Ratio
- 1 Advanced Circuit + 1 Engine Unit → 1 Blue Science Pack
- **Bottleneck:** Engine unit production (needs steel + pipes + gears)

---

## Module & Beacon Ratios

### Speed Module Effect
Speed modules increase assembler speed multiplicatively:
- **Speed Module 1:** +20% speed per module
- With 8 speed beacons (Speed 3): assembler runs at ~700% base speed

### Productivity Module Effect
Productivity modules reduce total raw material cost:
- **Productivity Module 3:** +10% productivity per module
- **Critical for:** Rocket parts, blue circuits, science packs with high intermediate costs

### Beacon Density (2.0 update)
In Factorio 2.0, the maximum beacons affecting a single machine is reduced compared to 1.1. Plan for **6-8 beacons** per machine for late-game layouts, not the old 12-beacon standard.

---

## Quick Reference Table

| Item | Recipe | Key Ratio |
|------|--------|-----------|
| Iron Plate | 1 Iron Ore | 1:1 |
| Copper Plate | 1 Copper Ore | 1:1 |
| Steel Plate | 5 Iron Plate | 5:1 |
| Copper Cable | 1 Copper Plate | 2:1 |
| Green Circuit | 3 Iron + 2 Copper Cable | — |
| Red Circuit | 2 Green + 2 Cable + 1 Plastic | — |
| Blue Circuit | 2 Red + 20 Green | — |
| Engine Unit | 1 Steel + 1 Iron Gear + 1 Pipe | — |
| Battery | 1 Sulfuric Acid + 1 Iron Plate | — |
| Low Density Structure | 1 Steel + 2 Copper Plate | — |

---

## Related Sections

- **[Getting Started](/getting-started/)** — Use these ratios in context
- **[Base Design](/base-design/)** — Layout your factory around these ratios
