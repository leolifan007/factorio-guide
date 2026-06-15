---
title: "Factorio LTN Mod Guide (Logistic Train Network)"
description: "How to use the Logistic Train Network (LTN) mod for Factorio: setup, depot design, station naming, requester/provider stations, and common LTN circuit configurations."
date: 2026-05-18
lastmod: 2026-06-15T13:46:00+08:00
tags: ["blueprints", "mods", "trains"]
draft: false
---

You've got 50 trains running across a megabase and every one of them is either waiting at a full station or blocking an intersection. Vanilla train limits work for small bases, but I hit the wall around 30 trains. LTN (Logistic Train Network) is the mod that automates train dispatch. Here's how I set it up without the head-scratching.

{{< callout "tip" >}}
**TL;DR:** LTN works like a logistics network but for trains. Build a depot of waiting trains. Build requester stations (need items) and provider stations (have items). LTN dispatches a train when a requester's threshold is met. Key settings: train limit = 1 per station, stack threshold = at least 1 trainload, network ID filtering for separated grids.
{{< /callout >}}

## How LTN Is Different From Vanilla

In vanilla Factorio, you set a train schedule manually (Station A > Station B). If Station B is full, the train waits. If a new outpost opens, you add a new schedule. This works for 5 trains. At 30 trains, you spend more time editing schedules than building factories.

LTN replaces this with an automated dispatcher. You define stations as providers or requesters. The depot holds idle trains. When a requester station signals "I need 2,000 iron plates," LTN finds a provider with iron, dispatches the nearest idle train, and the train does the trip automatically.

The magic is one-way only: providers and requesters are separate. A train picks up from a provider, drops at a requester, returns to depot. No complex schedules to maintain.

{{< callout type="info" >}}
**Quick Tip:** Start with one depot and 3 trains. Add more trains as you add stations. A good rule: 1 train per 3 requester stations. With stack threshold set to 1 trainload, a single train can serve iron outpost > iron requester > steel outpost > steel requester in a single trip.
{{< /callout >}}

## The Setup (Blueprint Ready)

| Component | What it does | Signal needed |
|:----------|:------------|:-------------|
| Depot | Holds idle trains, refuels them | None |
| Provider | Has items and reports them to LTN | Green wire from chest > constant combinator > lamp pole |
| Requester | Needs items and requests a delivery | Green wire from chest > constant combinator > lamp pole |
| LTN Combinator | Box at the station entrance, sets train load size | Red wire to lamp pole |

**Depot layout:** 4 stations in a row, each with a refueling inserter. Fuel belt runs behind all 4. Train limit = 1 per station (depot always wants empty trains).

**Provider station:** 6 steel chests unload by stack inserter into a single belt that feeds the train. Circuit: green wire from a chest reads item count > constant combinator has the item icon with a negative value (-2000) > combined signal on green wire goes to the lamp pole. LTN sees negative combined signal = "I have items available."

**Requester station:** Same circuit but positive. Chest reads item count > constant combinator positive value (2000) > combined signal = "I need this many more."

## Common Mistakes I Made

**Stack threshold too low.** Default is 1. I set it to 10% of a trainload, and LTN dispatched a train for 200 iron plates. The train traveled 2 minutes for 1 second of unloading. Set stack threshold to 1 trainload minimum.

**No network ID filtering.** In a megabase with separate train networks (smelting grid, science grid), LTN will route a science-provider train to an iron-requester station in the wrong grid. Set network ID on each station to separate them.

**Depot too small.** Two depot tracks isn't enough for 20 requesters. I use 8 depot stations and let excess trains wait at their last station instead. Rule of thumb: depot capacity = total trains / 3.

---

## Community Verification & Resources

- [LTN Mod Page (Factorio Mods)](https://mods.factorio.com/mod/LogisticTrainNetwork) -- official mod download, changelog, and documentation
- [Reddit -- LTN Guide](https://www.reddit.com/r/factorio/) -- community circuit setups and station blueprints
- [LTN Documentation (GitHub)](https://github.com/Optera/LogisticTrainNetwork/wiki) -- full circuit logic, depot sizing, and network ID documentation

**Related:** [How to Use Blueprints]({{< ref "/blueprints/how-to-use-blueprints" >}}) | [Basic Rail Network]({{< ref "/trains-logistics/basic-rail-network" >}}) | [Circuit Network Guide]({{< ref "/blueprints/circuit-network-guide" >}})
