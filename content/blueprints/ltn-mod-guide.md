---
title: "LTN Guide — Logistics Train Network for Megabases"
description: "LTN (Logistics Train Network) mod guide for Factorio. How the 3-stop system works, provider and requester configuration, depot setup, and the exact circuit wiring that gets your megabase trains running without deadlocks."
date: 2026-05-23
lastmod: 2026-05-23T17:56:00+08:00
publishDate: 2026-05-28T08:11:00+08:00
tags: ["blueprints", "trains-logistics", "ltn", "circuit-network"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

You built a beautiful train network. Five dedicated resource trains, each running iron, copper, coal, or stone on its own route. Then you added ten more. Now every junction is a deadlock. Trains are waiting for other trains. Your ore patches are running full but your smelters are starving. You've spent 8 hours manually fixing train schedules and the gridlock is worse than when you started.

This is the fundamental scaling problem of dedicated train networks. Every new resource pair needs a new train pair. At 20 resources and 20 destinations, you need 400 train routes. That's not a train network — that's a part-time job. LTN (Logistics Train Network) solves this by making one train handle every resource automatically.

Your factory has 40 trains and zero deadlocks. Here's how.

{{< callout "tip" >}}
**TL;DR:** LTN replaces fixed train schedules with a virtual dispatcher. You build three types of stops: providers (has items), requesters (needs items), and depots (train home base). LTN automatically sends empty trains from depots to providers, loads them, and delivers to requesters. One train handles every resource. The depot must always have idle trains or nothing moves.
{{< /callout >}}

## Why Your Train Network Is Always Gridlocked

The problem is not your signaling. Your signaling is fine. The problem is that your train network is a collection of individual point-to-point routes, and every point-to-point route competes for the same junctions.

Train A wants to go from Iron Patch 1 to the Iron Smelters. Train B wants to go from Iron Patch 2 to the Iron Smelters. Both trains must traverse the shared junction at Smelter Row. When the junction is occupied by Train A, Train B waits. When Train C from Copper Patch 3 needs to cross that same junction to reach the Copper Smelters, everyone waits.

At 5 trains, this is manageable. At 20, it's a system-wide freeze. The solution is not better signaling — it's better dispatching.

## LTN in a Nutshell: One Train, Every Resource

LTN adds a virtual train dispatcher to the game. Instead of programming each train with a fixed route, you tell each station what it PROVIDES and what it REQUESTS. LTN's central dispatcher manages the rest.

The mental model shift: instead of "train A goes from Iron Mine to Iron Smelter," you think in terms of "iron ore exists at Iron Mine and is needed at Iron Smelter." LTN handles the routing.

**What LTN adds:**
- A new train schedule system (replaces vanilla schedules)
- A dispatcher GUI for managing the network
- Station types: provider, requester, depot
- Automatic routing and pathfinding for trains

**What LTN does not change:**
- Rail signals (still use vanilla signaling)
- Train locomotives and wagons (standard trains)
- The physical rail network

## The Stop Setup That Makes Everything Work

Every LTN network has exactly three types of stops. Get these right and your network runs perfectly. Get any one wrong and nothing moves.

**Type 1: Provider Stop**
A provider stop has items available for pickup. LTN dispatches an empty train here to load items.

Configuration:
- Place a train stop named "Provider [resource name]" (e.g., "Provider Iron Ore")
- Connect a logistic chest (storage or passive provider) to the train stop via green wire
- The chest contents are what LTN reads — it knows how much of each item is available
- Alternatively: wire the train stop directly to a combinator reading the logistic network

The combinator setup: place a constant combinator outputting the resource signal you want (e.g., signal I for iron ore). Set the threshold. When the logistic network has > threshold amount of iron ore, the provider is "active" and LTN will dispatch a train.

**Type 2: Requester Stop**
A requester stop needs items delivered. LTN sends a loaded train here.

Configuration:
- Place a train stop named "Requester [resource name]" (e.g., "Requester Iron Plates")
- Attach a requester chest requesting the resource
- Wire the requester chest to the train stop via green wire
- LTN reads the chest's requests and dispatches a train

**Type 3: Depot Stop**
The depot is where empty trains wait between jobs. LTN dispatches trains from here to providers and back here when done.

Configuration:
- Place a train stop named "LTN Depot" (exact name matters)
- Place trains at the depot with no schedule
- LTN automatically assigns schedules to depot trains
- Minimum requirement: 2 trains per depot (one en route, one available)

The depot is the most critical element. If all depot trains are busy, LTN cannot dispatch new deliveries. Always maintain at least one idle train at the depot.

## Configuring the Depot — Your Trains' Home Base

The depot is not just a train stop — it's an idle fleet management system.

**Depot configuration rules:**
1. All trains in the depot must have no schedule set
2. Trains must be stopped at the depot stop (not just in the depot area)
3. The depot stop should be in a location with no pathfinding conflicts
4. Minimum fleet: 2 trains for a small network, 10+ for a megabase

**LTN depot settings (in the LTN dispatcher GUI):**
- Minimum trains in depot: 2 (never let the depot go below this)
- Depot warning time: 600 seconds (alert you if a train has been idle too long)
- Max train wait time at stop: 600 seconds (prevent trains from waiting forever)

**The depot layout:**
Build the depot as a dead-end spur with enough slots for all your trains. Each slot is a train stop. Trains park, wait for assignment, leave when dispatched.

## Handling Multiple Resources Without Train Crashes

One train handling multiple resources sounds like a recipe for mixing ores. It isn't — if you wire it correctly.

**The key principle: one train, one cargo.**

When a train arrives at a provider stop, it loads until the provider is empty (or the train is full). It then travels to the requester stop and unloads. The train's cargo manifest is locked during travel.

LTN prevents cargo mixing by design: a train carrying iron ore will only travel to a requester stop that requests iron ore. The dispatcher matches cargo type to request type.

**Multi-stop delivery (optional advanced feature):**
A train can deliver to multiple requesters in sequence. Configure this in LTN's route management. A common pattern: one train delivers to multiple science pack requesters, visiting each in sequence before returning to the depot.

**Resource priority:**
If multiple requesters request the same resource, LTN prioritizes by proximity. The closest requester gets the delivery first. This is automatic — you don't configure it.

## The Gotchas That Break LTN on First Setup

LTN is powerful but has sharp edges. These are the mistakes that break most first-time setups:

**Gotcha 1: No depot trains.**
Symptom: LTN shows 0 available trains. Nothing moves.
Fix: Ensure at least 2 trains are parked at depot stops with no schedule set.

**Gotcha 2: Provider stops not wired.**
Symptom: LTN shows items available but no train dispatches.
Fix: Wire the logistic chest to the train stop. The stop must receive the item signal via circuit network.

**Gotcha 3: Requester stops requesting too little.**
Symptom: Trains arrive with partial loads, trips take forever.
Fix: Set request amounts to match your consumption rate. A train carries ~200 stacks. If your factory consumes 400 iron ore per minute, request at least 400 ore per delivery.

**Gotcha 4: Train length mismatch.**
Symptom: Trains don't load fully, or can't fit in stations.
Fix: Set LTN's minimum train length to match your actual train length. If you use 2-8 trains (2 locomotives + 8 wagons), set minimum length to 10.

**Gotcha 5: The "phantom train" problem.**
Symptom: A train appears to exist but doesn't show up in LTN.
Fix: The train has a leftover schedule. Clear its schedule manually. LTN trains must have no schedule to be managed.

## LTN vs Vanilla Train Limits: Which to Use

Factorio 0.17+ introduced vanilla train limits — a built-in version of LTN's station slot system. The question: should you use LTN or vanilla train limits?

**Use vanilla train limits when:**
- You have fewer than 20 trains
- You want to avoid mod dependencies
- Your network is simple (one resource type per route)
- You prefer visual simplicity over maximum flexibility

**Use LTN when:**
- You have 20+ trains
- You want one train to handle multiple resources
- You need complex multi-stop delivery routes
- You want automatic load balancing across multiple providers

**Performance note:**
LTN has a CPU cost. At extreme scale (200+ trains), vanilla train limits with circuit-controlled schedules can match LTN performance with less overhead. For most megabases, LTN is the better choice up to ~100 trains.

## The Circuit Wire Setup: Step by Step

For a working LTN provider stop:
```
1. Place a storage chest with iron ore
2. Place a red wire from the chest to a decider combinator
3. Set decider combinator: if [iron ore] > 0 → output [iron ore] signal
4. Place a green wire from the combinator to the train stop
5. Name the train stop "Provider Iron Ore"
```

For a working LTN requester stop:
```
1. Place a requester chest requesting 400 iron ore
2. Wire the requester chest to the train stop via green wire
3. Name the train stop "Requester Iron Ore"
```

The circuit wires tell LTN what the network contains and what it needs. Without the wires, LTN is blind.

## The Bottom Line

LTN is the difference between a train network that scales and one that collapses under its own weight. The 3-stop system is the entire mental model — providers, requesters, depot. Wire correctly, maintain depot idle trains, and your megabase's logistics run themselves. The complexity is front-loaded. Once configured, LTN networks require almost no maintenance.
