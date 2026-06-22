---
title: "Cross-Planet Logistics — What to Ship Between Planets and Cargo Rocket Automation"
description: "Cross-planet logistics guide for Factorio Space Age. Cargo rocket automation, planet import/export lists, rocket silo setups, and interplanetary supply chain design."
date: 2026-06-20
tags: ["space-age", "space-platform", "strategy"]
draft: false
emoji: "🪐"
aliases:
  - /space-age/cross-planet-logistics/
---

The Factorio Space Age endgame is a five-planet interplanetary empire. Each planet produces unique resources that the others need, and the cargo rocket is your supply line. See {{< ref "/space-age/guide/planet-order-guide" >}} for which planet to visit when, and {{< ref "/space-age/platform/space-platform-guide" >}} for platform fundamentals. Get the logistics wrong and your Gleba science packs rot waiting for a ride, or your Aquilo platform starves because you forgot calcite.

This guide covers what to ship, where to ship it, and how to automate the whole operation with cargo rocket circuits and space platform buffers.

{{< callout "tip" >}}
**TL;DR:** Ship unique planetary resources to Nauvis for final science. Ship calcite to every planet. Ship building materials to new outposts. Automate with circuit-controlled rocket silos and a space platform logistics buffer. Pre-made rocket parts from Vulcanus save your Nauvis iron supply.
{{< /callout >}}

## The Planet Export/Import Matrix

Each planet produces materials that no other planet can. Here's the full matrix of what goes where:

| Planet | Exports (sell) | Imports (need) |
|:-------|:---------------|:---------------|
| **Nauvis** | Universal science, rocket parts, uranium, mall items | Calcite, unique science packs, bioflux |
| **Vulcanus** | **Calcite**, foundry, big miner, tungsten, artillery | Rocket parts (optional), nuclear fuel, quality modules |
| **Fulgora** | **EM science pack**, EM plant, superconducting wire, holmium | Calcite, bioflux, rocket fuel, building materials |
| **Gleba** | **Agricultural science pack**, bioflux, nutrients, stack inserter | Calcite, artillery shells, rocket fuel, uranium |
| **Aquilo** | **Cryogenic science pack**, fusion reactor, quantum processor | Everything — no natural resources at all |

### What to Ship FROM Each Planet

{{< material "calcite" >}} — **Vulcanus → everywhere.** Calcite is the single most important interplanetary resource. Drop it to Nauvis for productivity module 3 production and smelting. Drop it to Gleba for rocket fuel. Drop it to Fulgora for concrete. Drop it to Aquilo for heating tower fuel.

{{< material "foundry" >}} + {{< material "big-mining-drill" >}} — **Vulcanus → Nauvis.** Ship four foundries and a stack of big miners back as soon as you unlock them. These items are irreplaceable in the endgame.

{{< material "em-science" >}} — **Fulgora → Nauvis** (or wherever science is consumed). EM science is the second Space Age science pack and must be shipped off Fulgora to be used.

{{< material "electromagnetic-plant" >}} — **Fulgora → everywhere.** The EM plant is the best circuit assembler in the game. Ship a stack to Nauvis for green/red/blue circuit production, and to Vulcanus for everything electronic.

{{< material "bioflux" >}} — **Gleba → Nauvis/Fulgora.** Bioflux is essential for productivity module 3 production (requires biter eggs + bioflux) and for the best rocket fuel recipe. Always keep a steady stream flowing.

{{< material "agri-science" >}} — **Gleba → Nauvis.** Agricultural science has a 1-hour spoilage timer. Ship it immediately — don't let it sit on Gleba.

{{< material "cryogenic-science" >}} — **Aquilo → Nauvis.** Aquilo science is the final Space Age science. Ship it frozen or don't ship it at all — it doesn't spoil, but production is slow.

{{< material "fusion-generator" >}} — **Aquilo → everything.** Fusion power changes the game. Ship one back to Nauvis and never think about nuclear again.

### What to Ship TO Each Planet

| Destination | Critical imports |
|:------------|:-----------------|
| **Nauvis** | Calcite (always), bioflux, all unique science packs, foundry/big miners, EM plants |
| **Vulcanus** | Bioflux, uranium fuel cells, quality module 3s |
| **Fulgora** | Calcite, bioflux, rocket fuel, nuclear fuel |
| **Gleba** | Calcite, artillery shells, rocket fuel, uranium ammo |
| **Aquilo** | Everything—iron/copper/steel, calcite, fuel, ammo, modules, circuits, bioflux |

{{< callout type="info" >}}
**Aquilo imports matter most.** You can land on Aquilo with nothing and ship everything in by rocket. Plan for 10+ rocket silos on Nauvis dedicated to Aquilo supply. Every single factory input on Aquilo comes from space.
{{< /callout >}}

## Cargo Rocket Automation

The cargo rocket is your delivery vehicle. Unlike the space platform, rockets are one-shot: launch, land, repeat. Here's how to automate them so you never think about logistics again.

### Rocket Silo Setup

Each rocket silo needs:

- **Rocket parts:** 100 per launch. These are expensive (1000 iron + 100 LDS + 100 fuel per launch)
- **Cargo:** Up to 1,000 stack capacity. Stack size depends on the item.
- **Destination:** Set per-silo. Dedicate one silo per destination planet.
- **Launch trigger:** Manual, circuit signal, or automatic via the Space Logistics menu

{{< diagram "diagrams/space-age/planet-logistics-matrix.svg" "Planet import/export logistics matrix showing what goes where" "760" >}}

### Signal-Based Requesting

You have two approaches to automation:

**Approach 1 — Rocket Automation (from SA 2.0):** The simplest method. Open the rocket silo UI, set a destination planet, and click "Automatic requests." The game handles the rest — it watches logistic network stock and auto-launches when conditions are met. This works well for simple builds.

**Approach 2 — Circuit-Controlled Silos (advanced):** Use the circuit network to request specific items when a planet's buffer runs low.

Wire your rocket silo to a constant combinator on the destination planet (read via the signal network):

| Signal type | What it does |
|:------------|:------------|
| **Logistic signal** (chest icon) | Reads destination planet's logistic requests |
| **Circuit signal** (green wire) | Sends a launch trigger when conditions are met |
| **Trash slot signal** | Specifies items to unload from space platform storage |

**The standard circuit pattern:**

```
Constant combinator: Set request thresholds
    ↓
Arithmetic combinator: Subtract (requested - available)
    ↓
Rocket silo: Read negative values as "ship these"
    ↓
Launch when any signal > 0 with a timer (10s delay to batch)
```

### Rocket Part Production

Rocket parts are the big cost. Each launch costs roughly:

| Component | Cost per rocket | Where to make |
|:----------|:---------------|:--------------|
| Rocket part × 100 | 1,000 iron plates, 100 LDS, 100 rocket fuel | Nauvis or Vulcanus |
| Low density structure (LDS) | Copper + steel + plastic | Nauvis (best with foundry) |
| Rocket fuel | Light oil + solid fuel | Vulcanus (free oil) or Gleba (bioflux → rocket fuel) |

**The cheapest rocket fuel recipe is on Gleba:** bioflux → rocket fuel yields 50% more fuel per ingredient than light oil cracking. If you're shipping fuel to other planets, make it on Gleba.

**Pre-made rocket parts from Vulcanus:** Vulcanus has infinite iron (lava → iron plates) and infinite oil (carbon oil from calcite + lava). Ship pre-made rocket parts to Nauvis to conserve Nauvis's iron supply for science and malls.

## Space Platform as Logistics Buffer

Your space platform isn't just for travel — it's a logistics buffer between planets. Platform logistics work like this:

1. **Platform requests** items from a planet's logistic network (requested chest limit + 50% buffer)
2. **Platform holds** those items in transit
3. **Platform ships** them to the destination via cargo landing pad

**Key trick:** Use the platform to buffer ongoing supplies. A platform in Nauvis orbit can request bioflux, calcite, and science packs continuously. When a rocket launches to Nauvis, the platform unloads directly to the landing pad. This eliminates waiting — the platform is always stocked.

{{< callout "tip" >}}
**Buffer zone strategy:** Keep a dedicated cargo platform in orbit around each planet. Set it to request the planet's exports. That way, when a rocket arrives from another planet, it can pick up outgoing goods immediately instead of waiting for ground-side production.
{{< /callout >}}

### Platform Request vs Direct Rocket: Which to Use?

| Scenario | Best method | Why |
|:---------|:------------|:----|
| Initial base setup | Direct rocket | One-time shipment of building materials |
| Ongoing science supply | Platform request | Continuous, automatic, buffer absorbs delays |
| Emergency resupply | Direct rocket | Urgent — skip the buffer wait |
| Bulk materials (calcite) | Platform request | Low urgency, high volume, buffer works well |
| Spoiling items (agri science) | Direct rocket | Minimize time from production to consumption |

## Full Automation Workflow

Here's the complete flow for a self-sustaining interplanetary empire:

**Step 1 — Planet production:** Each planet produces its unique exports and stores them in provider chests near the rocket silo.

**Step 2 — Rocket loading:** The silo's requester chest pulls items from the logistic network based on circuit signals.

**Step 3 — Space platform buffer:** The orbital platform requests the items and stockpiles them.

**Step 4 — Delivery:** When the destination planet requests items (e.g., Nauvis needs bioflux), the platform launches or the destination silo requests the goods.

**Step 5 — Consumption:** The cargo landing pad distributes items to the planet's logistic network via requester chests and belts.

{{< callout type="info" >}}
**Nauvis is your logistics hub.** Run 8-10 rocket silos on Nauvis: one for each destination planet, plus two for high-volume routes (Aquilo supply). Use circuit-controlled inserters to balance rocket part usage across all silos.
{{< /callout >}}

## Common Logistics Mistakes

**Mistake 1: Over-shipping calcite.** Calcite stacks to 200 but is consumed slowly. A single rocket of calcite (200 stacks × 50 per stack = 10,000 calcite) lasts hours on Nauvis. Don't launch calcite every 5 minutes — set a 25,000 threshold before requesting more.

**Mistake 2: Mixing items in one rocket.** If each silo handles one destination, configure it for one item type per launch. Mixing bioflux and iron plates means either you run out of bioflux or you waste rocket capacity on iron.

**Mistake 3: No buffer on the destination planet.** If your rocket arrives and the landing pad is full, items spill into provider chests that you can't control. Always leave 50+ empty slots in the landing pad for incoming rockets.

**Mistake 4: Forgetting Aquilo.** Aquilo needs everything — literally everything. Set up a dedicated silo group (3-4 silos) just for Aquilo before you leave Nauvis. If you forget ice, your fusion plant shuts down and everyone dies of hypothermia.

## Summary

Cross-planet logistics is the real endgame of Factorio Space Age. Master these principles and your interplanetary factory runs itself:

- **Calcite from Vulcanus** feeds every planet's smelting
- **Bioflux from Gleba** powers module 3s and rocket fuel
- **EM plants from Fulgora** upgrade every circuit line
- **Pre-made rocket parts from Vulcanus** save Nauvis iron
- **Space platform buffers** eliminate interplanetary waiting
- **Circuit-controlled silos** automate the full supply chain

For more on building the rockets that ship these goods, see the [Space Platform Design Guide]({{< ref "/space-age/platform/space-platform-guide" >}}). For efficient ship builds that carry cargo between planets, check out [Ship Design Patterns]({{< ref "/space-age/platform/ship-design" >}}). And for how to set up a calcite supply chain from scratch, read the [Vulcanus Guide]({{< ref "/space-age/guide/vulcanus-guide" >}}).
