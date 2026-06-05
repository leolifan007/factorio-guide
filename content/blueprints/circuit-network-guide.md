---
title: "Factorio Circuit Network Guide - Wires, Combinators and SR Latch"
description: "Learn Factorio circuit network from scratch: red/green wires, decider combinator, arithmetic combinator, SR latch, and automated oil cracking control."
date: 2026-05-21
tags: ["blueprints", "circuit-network"]
draft: false
emoji: "🔧"
---

Your refineries are stuck on heavy oil again. The belts backed up last night and your entire base stalled because petroleum backed up — and nobody noticed for three hours. The fix isn't more storage tanks. It's a single red wire, a decider combinator, and 30 seconds of configuration.

{{< callout "tip" >}}
**TL;DR:** Connect a storage tank to a pump with red wire. Decider combinator: petroleum > 20000 → output P = 1. Connect to pump. Done — automated cracking solves 90% of your fluid problems.
{{< /callout >}}

## The Root Cause — Why Fluids Stall Without Circuits

Refineries produce heavy oil, light oil, and petroleum simultaneously. If any of the three outputs fills up, the refinery stops all production. No petroleum means no plastic. No plastic means no red circuits. No red circuits means your entire factory crawls to a halt.

The solution is circuit-controlled cracking: convert excess heavy to light, excess light to petroleum. Three pumps, three decider combinators, zero deadlocks.

## How to Solve It Properly — Three Patterns That Handle Everything

You only need three circuit patterns. Everything else is a variation.

**Pattern 1 — Fluid cracking automation.** This is the one that fixes refinery deadlocks.

What you need: red wire, decider combinator, pump per fluid type.

{{< diagram "diagrams/circuit-wires.svg" "Red wire and green wire circuit network — red for production control, green for train/logistics" "760" >}}

1. Run red wire from a heavy oil tank to a decider combinator
2. Set decider: heavy_oil > 20000 → output P = 1
3. Connect decider output to the pump feeding heavy→light cracking
4. Repeat: light oil tank → decider (light_oil > 20000) → pump for light→petroleum
5. Skip petroleum → solid fuel. Petroleum backs up? Crack less. This handles itself.

A red wire carries signal. A green wire is a separate network. If one wire shorts it doesn't corrupt the other. Convention: red for production, green for train control.

**Pattern 2 — SR latch for power control.** Insert fuel cells only when steam tanks are low.

- Wire all steam tanks to a decider combinator
- Set: steam < 10000 → output S = 1 (set condition)
- Set another: steam > 24000 → output S = 0 (reset condition)
- Connect both to a single decider in SR latch mode
- Output drives the fuel inserter

Result: fuel insertion only triggers when steam drops below threshold, stops when full. Cuts fuel consumption by 50-80%.

**Pattern 3 — Belt item counting for balanced output.**

- Place a red wire on a belt segment with read-hold mode
- Wire to an arithmetic combinator: each * -1 → each
- Wire output back to a constant combinator with your target values
- Sum gives you actual demand minus supply

Common use: keep exactly 200 green circuits on the belt to the mall. Insert more when count drops below 200.

{{< callout type="info" >}}
**Quick Tip:** Constant combinators let you set fixed values. Use them as lookup tables: wire a constant with "iron_plate = 500" to a requester chest, and bots maintain exactly 500 iron plates in that chest. No fiddling with stack limits.
{{< /callout >}}

## Where Most Players Mess This Up

**Wire colors aren't decorative.** Red and green are electrically isolated networks. If you run both on the same pole, they stay separate — the pole carries them as independent signals. This is useful: run red for level sensors and green for demand signals on the same power pole.

**Output not connected.** The most common bug: the combinator is configured correctly but its output port is unconnected. The output is on the right side of the combinator (small triangle), input on the left.

**Everything on one wire.** A single circuit network can carry every item signal simultaneously — each item type is a separate channel. A belt full of 20 item types produces 20 independent signals on one wire, not interference.

## Pushing It Further — Circuit Networks at Megabase Scale

Once you've mastered the three patterns, circuit networks scale to:

- **Train station limits** — wire all chests at a station, compute total storage, broadcast station capacity. Trains only go where they're needed.
- **Solar accumulator ratios** — circuit-controlled power switch that disconnects accumulators from the grid at a set charge level.
- **Kovarex smart centrifuge** — only output U-235 when you have enough to sustain the reactor block.
- **Mall demand system** — wire requester chests to constant combinators. Set chest to request exact counts. Bots deliver only what's needed.

---

## Community Verification & Resources

- [Official Factorio Wiki — Circuit Network](https://wiki.factorio.com/Circuit_network) — complete combinator reference with all signal types
- [Reddit r/factorio — Circuit Tutorials](https://www.reddit.com/r/factorio/) — community blueprints for advanced contraptions
- [Factorio Blueprint Library](https://factorioprints.com/) — ready-to-use SR latch and fluid control blueprints
