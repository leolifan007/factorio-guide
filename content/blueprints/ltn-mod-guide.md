---
title: "LTN Guide — Logistics Train Network for Megabases"
description: "LTN (Logistics Train Network) mod guide for Factorio. How the 3-stop system works, provider and requester configuration, depot setup, and the exact circuit wiring that gets your megabase trains running without deadlocks."
date: 2026-05-23
lastmod: 2026-05-23T19:09:00+08:00
publishDate: 2026-05-28T08:11:00+08:00
tags: ["blueprints", "trains-logistics", "ltn", "circuit-network"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

You have 5 dedicated resource trains. Then 10. Then 20. Every junction is a deadlock. Trains wait for trains waiting for trains. LTN solves this by making **one train handle every resource** automatically.

{{< callout "tip" >}}
**TL;DR:** LTN uses three stop types — Provider (has items), Requester (needs items), Depot (idle home). Wire each stop to the circuit network. LTN dispatches empty trains from depot → provider → requester → depot automatically. **Always keep idle trains in the depot or nothing moves.**
{{< /callout >}}

{{< diagram "diagrams/ltn-3stop.svg" "LTN 3-stop system — provider stop, rail network, requester stop, and depot" "820" >}}

## Why Dedicated Trains Don't Scale

Every new resource pair needs a new train route. At 20 resources × 20 destinations = **400 potential routes**. Each route competes for shared junctions. The problem isn't signaling — it's dispatching.

LTN replaces fixed schedules with a virtual dispatcher. You tell stations what they **provide** and what they **request**. LTN handles routing.

## The Three Stop Types

### 1. Provider Stop — "I Have Items"

| Component | Configuration |
|-----------|---------------|
| Train stop | Named `Provider [Resource]` (e.g., `Provider Iron Ore`) |
| Chest | Storage or passive provider, filled with items |
| Wire | Green wire from chest → train stop |

LTN reads chest contents via circuit network. When items exceed threshold, provider is "active" and LTN dispatches an empty train to load.

### 2. Requester Stop — "I Need Items"

| Component | Configuration |
|-----------|---------------|
| Train stop | Named `Requester [Product]` (e.g., `Requester Iron Plates`) |
| Chest | Requester chest set to request amount |
| Wire | Green wire from chest → train stop |

LTN reads the request signal and sends a loaded train from a provider.

### 3. Depot Stop — "Train Home Base"

| Component | Configuration |
|-----------|---------------|
| Train stop | Named `LTN Depot` (exact name required) |
| Trains | Parked with **no schedule** |
| Minimum fleet | 2 trains (small), 10+ (megabase) |

**The depot is the most critical element.** If all trains are busy, LTN cannot dispatch new deliveries. Build as dead-end spurs with enough slots for your entire fleet.

## How Dispatching Works

```
Depot (idle train) → Provider (loads cargo) → Requester (unloads) → Depot
```

One train carries one resource type per trip. LTN prevents cargo mixing by design — a train carrying iron ore only travels to requesters requesting iron ore.

**Multi-stop delivery** (optional): one train visits multiple requesters in sequence before returning to depot. Common for science pack distribution.

## Circuit Wiring Step-by-Step

**Provider stop:**
1. Place storage chest with items (e.g., iron ore)
2. Red wire: chest → decider combinator
3. Combinator: `If [item] > 0 → output [item] signal`
4. Green wire: combinator → train stop
5. Name stop: `Provider Iron Ore`

**Requester stop:**
1. Place requester chest (set request quantity, e.g., 400 iron ore)
2. Green wire: chest → train stop
3. Name stop: `Requester Iron Plates`

Without wires, LTN is blind.

## The Gotchas That Break First Setups

| Gotcha | Symptom | Fix |
|--------|---------|-----|
| No depot trains | LTN shows 0 available, nothing moves | Park 2+ unscheduled trains at depot |
| Provider not wired | Items exist but no train dispatched | Connect chest → stop with green wire |
| Request too low | Partial loads, slow trips | Match request to consumption rate (~400 ore/delivery) |
| Train length mismatch | Underloading, station overflow | Set LTN min length to match actual train size |
| Phantom train | Train exists but invisible to LTN | Clear leftover vanilla schedule — LTN trains must have **no schedule** |

## LTN vs Vanilla Train Limits

| Use Case | Recommendation |
|----------|----------------|
| <20 trains, simple routes | Vanilla train limits (no mod dependency) |
| 20+ trains, multi-resource | **LTN** (automatic dispatch, one train per all resources) |
| 200+ extreme scale | Vanilla limits + circuit control (lower CPU overhead) |

## Performance Notes

- LTN has measurable CPU cost at 100+ trains
- For most megabases (20-100 trains), LTN is the clear winner
- Keep depot near network center to minimize empty travel distance

## Common Mistakes

| Mistake | Result |
|---------|--------|
| Only 1 train in depot | Network stalls whenever that train is en route |
| Mixing resource types on one train | LTN prevents this by design — but miswired stops cause confusion |
| Forgetting to name stops correctly | LTN can't match providers to requesters |
| Depot too far from main network | Empty trains waste time traveling to providers |

## The Bottom Line

LTN's 3-stop model — provider, requester, depot — is the entire mental model. Wire correctly, maintain idle depot trains, and your megabase logistics run themselves. Complexity is front-loaded; configured networks need almost no maintenance.
