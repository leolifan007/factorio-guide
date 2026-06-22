---
title: "Fulgora Scrap Overflow — How to Void Excess Items and Keep Production Running"
description: "Fulgora scrap overflow solutions for Factorio Space Age. Sorter designs, voiding strategies, holmium processing, and the recycler loop that never deadlocks."
date: 2026-06-20
tags: ["space-age", "fulgora", "production"]
draft: false
emoji: "⚡"
aliases:
  - /space-age/fulgora-scrap-overflow/
---

You set up scrap recycling on Fulgora and your belts are already jammed. Not with one item — with twelve. Blue circuits pile up next to concrete next to gears next to holmium ore. The recyclers stop because the output belt has nowhere to put more gears. And since the recyclers stopped, you're not getting holmium anymore. The entire base is deadlocked because one belt segment filled with iron gears. See {{< ref "/space-age/fulgora/fulgora-recycling-guide" >}} for the Fulgora landing setup before diving into overflow control.

This is the scrap overflow problem. Here's how to design a sorter that never jams.

{{< callout "tip" >}}
**TL;DR:** Every scrap output needs a dedicated path — to storage, to a consumer assembler, or to a recycler loop that voids it. Build filter splitters for high-value items first, then route everything excess through a recycler chain. A sushi belt + priority splitter layout handles all 12 scrap outputs without deadlock.
{{< /callout >}}

## Why Fulgora's Recycling Is Different

On Nauvis, you control what your factory produces. If iron plate backs up, the miners stop and the belt idles. No problem.

On Fulgora, recycling scrap produces random outputs. A single recycler cycling scrap pulls from this weighted pool:

| Item | Weight | Probability | Primary Use |
|:-----|:------:|:-----------:|:-----------|
| {{< material "iron_gear" >}} Iron gear wheel | 8.0 | 22.9% | Mall items, recycle to steel |
| {{< material "ice" >}} Ice | 4.5 | 12.9% | Water → steam → power |
| {{< material "stone" >}} Stone | 4.0 | 11.4% | Walls, rails, concrete |
| {{< material "concrete" >}} Concrete | 3.0 | 8.6% | Foundations, landfill |
| {{< material "iron_plate" >}} Iron plate | 3.0 | 8.6% | General construction |
| {{< material "copper_plate" >}} Copper plate | 3.0 | 8.6% | General construction |
| {{< material "steel_plate" >}} Steel plate | 2.5 | 7.1% | Advanced items, structures |
| {{< material "battery" >}} Battery | 2.0 | 5.7% | Accumulators, science |
| {{< material "circuit_blue" >}} Blue circuit | 2.0 | 5.7% | Science, modules |
| {{< material "holmium_ore" >}} Holmium ore | 1.5 | 4.3% | **Science — the reason you're here** |
| {{< material "solid_fuel" >}} Solid fuel | 1.5 | 4.3% | Boiler fuel, rocket fuel |

Every item type needs an output path. If **any one** of these has no path, your entire recycling line stops. This is the fundamental constraint of Fulgora design.

{{< callout type="info" >}}
**Quick Tip:** Track your scrap overflow with the circuit network before it becomes a problem. Wire a constant combinator to each filter inserter output and read belt contents through the hub. When an item type exceeds 1,000 on belts, the circuit can trigger an alarm or auto-route to void.
{{< /callout >}}

## The Priority Sorter — Two Designs

### Design A: Belt-Only Priority Sorter (No Circuits)

The simplest approach uses filter splitters in priority order:

```
[Scrap Recyclers row] → Sushi belt
                           ↓
                     Filter Splitter #1: Holmium Ore → Holmium processing
                     Filter Splitter #2: Blue Circuits → Chest buffer → Science
                     Filter Splitter #3: Batteries → Chest buffer → Science/Accumulators
                     Filter Splitter #4: Steel Plate → Chest buffer → Mall
                     Filter Splitter #5: Copper Plate → Chest buffer → Mall
                     Filter Splitter #6: Iron Plate → Chest buffer → Mall
                     Filter Splitter #7: Iron Gears → Recycler (void loop)
                     Filter Splitter #8: Concrete → Recycler (void loop)
                     Filter Splitter #9: Stone → Recycler (void loop)
                     Filter Splitter #10: Ice → Recycler (void loop)
                     Filter Splitter #11: Solid Fuel → Recycler (void loop)

                     → End of belt: everything remaining → Recycler loop
```

Each filter splitter pulls one item type off the main sushi belt onto a dedicated lane. The remaining items continue down the belt to the next splitter. Put high-value items (holmium, blue circuits) first so they get priority access.

### Design B: Circuit-Controlled Sorter

For tighter control, wire each output inserter to a decider combinator:

1. Read the entire sushi belt's contents via a red wire connected to the belt
2. For each output lane, set a constant combinator with the item type and threshold
3. The decider enables the filter inserter when `item count < threshold`
4. When the threshold is met, items back up on the sushi belt and eventually reach the void recycler

The circuit approach is more responsive and lets you change thresholds without rebuilding belts. Our [Circuit Network Guide]({{< ref "/blueprints/circuit-network-guide" >}}) has the wiring patterns.

{{< diagram "diagrams/space-age/scrap-overflow-sorter.svg" "Priority sorter station with scrap belt, filter splitter tree, and recycler void loops" "760" >}}

## The Recycler Loop — Voiding Without Deadlock

The items you can't use (excess concrete, stone, gears, ice, solid fuel) need to disappear. Place a row of recyclers at the end of your sorter:

**Single-pass recycler loop:**
```
Excess items → Recycler → 75% voided, 25% returned
                           ↓
                    Items come back mixed → back to sushi belt or second recycler
```

Each recycler cycle destroys 75% of input items (returning their base materials at 25% rate). A 3-recycler chain reduces any pile to near zero:

| Pass | Items Voided | Remaining |
|:----:|:-----------:|:---------:|
| 1 | 75% | 25% |
| 2 | 93.75% | 6.25% |
| 3 | 98.44% | 1.56% |

**Design it as a dead-end loop:**

1. Place 3-4 recyclers in a line
2. The first recycler outputs back onto the input belt
3. A splitter prioritizes fresh overflow over recycler output
4. After 3-4 cycles, most items are gone

{{< callout type="info" >}}
**Quick Tip:** Don't mix quality items into your void loop. A rare steel plate fed to a recycler yields rare iron ore — which can jam your normal-quality belt if you don't filter it. Either filter quality items with a quality-check inserter before voiding, or have separate void lines per quality tier. See our [Quality Module Guide]({{< ref "/space-age/quality/quality-module-guide" >}}) for quality sorting logic.
{{< /callout >}}

### Shooting Chests: The Old Way

Before recyclers were available at scale, players built "shooting chests" — steel chests with an inserter feeding them and a turret shooting them. Each turret shot destroys one item. The turret targets the chest, not the items inside — the chest takes damage and items eventually break.

**Throughput comparison:**

| Method | Items Voided per Second | Setup Cost |
|:-------|:------------------------:|:----------:|
| Recycler (green modules) | 4-6 items/s | High (recycler + power) |
| Recycler (no modules) | 2-3 items/s | Medium |
| Shooting chest (pistol) | 0.3 items/s | Very low |
| Shooting chest (SMG) | 0.8 items/s | Low |
| Shooting chest (turret, red ammo) | 2.0 items/s | Low |

For early Fulgora, a shooting chest handles overflow of one or two item types. For a full scrap processing line with hundreds of items per minute, use recycler loops.

## The Holmium Processing Chain

Holmium ore is the primary reason to visit Fulgora. The full chain:

```
Scrap → Recycler → Holmium ore (4.3% chance per cycle)
                    ↓
           Holmium plate (in chemical plant, requires sulfuric acid)
                    ↓
           ┌────────┴────────┐
           ↓                 ↓
  Electromagnetic science   Superconductor → Quality modules
```

**Critical ratios:**

| Stage | Input | Output | Machines for 60 SPM |
|:------|:------|:------:|:-------------------:|
| Scrap recycling | 1 scrap/sec | ~0.04 holmium/sec | ~40 recyclers |
| Holmium plate | 5 ore + 15 acid | 1 plate | 5 chemical plants |
| EM science | 1 plate + circuits | 2 science | 3 EM assemblers |
| Superconductor | 1 plate + copper | 2 superconductor | 1 foundry |

You need roughly **40 scrap recyclers running at full speed** to sustain 60 SPM of electromagnetic science. Your scrap sorter must handle the output of all 40 — that's a lot of iron gears, concrete, and stone heading to void.

## Planet-Specific Considerations

**Space platforms** make interplanetary shipping viable. The [Space Platform Guide]({{< ref "/space-age/platform/space-platform-guide" >}}) covers how to build a ship that ferries holmium plate and EM science back to Nauvis. You don't need to build all EM science on Fulgora — ship holmium plate to Nauvis if you prefer.

**Key Fulgora-specific tips:**

- **Ice is water.** Melting ice gives you water for sulfuric acid — build the ice melting setup early and run pipes to your holmium processing.
- **Concrete is everywhere.** You'll have more concrete than you need. Use it for foundation tiles (prevents scrap patch depletion on small islands) and void the rest.
- **Speed vs. quality modules.** Speed modules in scrap recyclers increase throughput (more scrap processed = more holmium). Quality modules give better holmium quality but lower overall quantity. Early game: speed. End game: quality for legendary holmium.

## Common Failure Modes

**Sushi belt too short for splitters.** Each filter splitter needs 2 tiles of belt space. With 11 item types, that's 22 tiles of belt minimum. Make it 30 tiles to leave room.

**No power for voiding.** Void recyclers and inserters consume power. If your lightning power cuts out during a storm lull, items pile up. Buffer 100+ accumulators per 10 recyclers.

**One cycler void loop.** A single recycler handling concrete will process ~25 items/s but only destroy 75%. The remaining 25% spills back onto the belt. Use 3 recyclers in series for reliable voiding at megabase scale.

**High-value items mixed into void.** Don't let holmium ore or blue circuits reach the void recyclers. Filter them out first with dedicated splitters. A single blue circuit costs 20 red circuits + 4 green circuits — voiding it is painful.

---

## Community Verification & Resources

- [Official Wiki — Scrap](https://wiki.factorio.com/Scrap) — exact scrap recycling weights and output probabilities
- [Factorio Forums — Fulgora Sorter Designs](https://forums.factorio.com/viewforum.php?f=69) — community sorter blueprints and circuit designs
- [Reddit r/factorio — Fulgora Megabase](https://www.reddit.com/r/factorio/) — compact recycler layouts and 300+ SPM Fulgora builds
- [Alt-F4 Blog — Fulgora Deep Dive](https://alt-f4.blog/) — analysis of scrap recycling ratios and megabase throughput
