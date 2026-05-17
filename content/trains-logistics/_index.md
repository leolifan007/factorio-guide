---
title: "Trains & Logistics — Factorio Rail Network Guide"
description: "Factorio train signals, deadlock prevention, LTN mod, logistic bots, and requester chest setups. Build reliable rail networks from scratch."
date: "2026-05-17"
---

## Trains & Logistics in Factorio

Trains and logistic robots are Factorio's two primary late-game logistics systems. Trains move bulk goods between distant locations; logistic robots move items to and from requester and provider chests within a logistic network.

---

## Train Basics

### Why Use Trains?
- Trains can move enormous quantities of ore across the map
- Trains are more UPS-efficient than belts over long distances
- A single rail network supports unlimited trains
- Trains are the only practical way to supply a megabase with ore

### Train Anatomy
- **Locomotive** — provides forward power (requires fuel)
- **Cargo Wagon** — holds items (stacks of 2000 for raw ore)
- **Fluid Wagon** — holds fluids (sulfuric acid, petroleum, etc.)
- **Train Stop** — tells a train where to go
- **Rail** — the track itself

---

## Rail Signals — Chain vs. Rail

This is the most confusing mechanic in Factorio. Here's the rule:

### Rail Signals
Place a **rail signal** when a track branches or intersects. Rail signals divide the track into **blocks**. A train won't enter a block if another train is already in it.

### Chain Signals
Place a **chain signal** at the **entrance** of intersections. Chain signals propagate the signal state from all downstream signals. A train won't enter a chain signal unless **every path through the intersection is clear**.

### The Golden Rule
> **"Chain signal at entrance, rail signal at exit"**

Every intersection follows this rule:
1. **Chain signal** at the start of the intersection (from each approach direction)
2. **Rail signal** at the end of the intersection (exit onto the main track)

---

## Train Deadlock Prevention

Deadlocks occur when two trains block each other's paths. Common causes:

### Cause 1: Bidirectional Trains on Single Tracks
**Fix:** Use one-way rail loops wherever possible. If you must use bidirectional tracks, ensure each direction has its own dedicated lane.

### Cause 2: Insufficient Waiting Space
**Fix:** Build **stackers** — holding lanes before a station where trains wait in queue. A stacker should have at least 2-3 waiting slots.

### Cause 3: No Train Limit Set
**Fix:** Set train limits on stations (Factorio 1.1+). A station limit of 1 means only 1 train parks there at a time.

### Cause 4: Trains Waiting on the Main Line
**Fix:** All trains must wait at stations or stackers, never on the main line. Design your network so the main line has no stopping points.

---

## Train Station Design

### Basic Pickup Station
- Train stop named for the resource ("Iron Ore" / "Copper Ore")
- Provider chests connected to the train stop
- Set train schedule: Iron Ore Station → Unload at Main Base → return to Iron Ore Station

### Basic Delivery Station
- Train stop with requester chests
- Inserters pull from cargo wagons into requester chests
- Set train limit to match unloading speed

### Train Refueling
- Create a dedicated refueling station called "Fuel" with a logistic request for nuclear fuel (or rocket fuel)
- Trains visiting the refueling station automatically refuel from the provider chest

---

## LTN (Logistic Train Network) Mod

The **LTN** mod replaces Factorio's default train system with a smarter dispatcher:
- You set provider stations and requester stations
- LTN automatically assigns trains to routes
- Trains are reused across multiple routes

**When to use LTN:** For megabases with 10+ trains. Default Factorio trains work fine for smaller setups.

---

## Logistic Robots

Logistic robots are the second major logistics system. They require:
- **Roboports** — recharge and house the robots
- **Construction robots** — build and repair (from personal logistics)
- **Logistic robots** — move items between chests

### Chest Types

| Chest | Function |
|-------|----------|
| Passive Provider | Always available to robots |
| Active Provider | Sends items to network immediately |
| Storage | Default item storage |
| Requester | Requests specific items from network |
| Buffer | Like requester + storage combined |

### Requester Chest Ratio
- 1 requester chest with 10 slots can request 10 different items
- Robots fly at ~90 tiles/second — sufficient for small-to-medium networks
- For megabase logistics, use **train-based** item delivery instead

---

## Bots vs. Belts

**Short answer:** Both are good. Use belts for throughput, bots for flexibility.

| Factor | Belts | Logistic Bots |
|--------|-------|--------------|
| Throughput | High (60-120 items/s) | Medium (50-80 items/s per bot) |
| Setup cost | Moderate | High (roboports are expensive) |
| Flexibility | Fixed routes | Anywhere in logistic network |
| UPS efficiency | Excellent | Poor at megabase scale |
| Best for | Main production | Mall, late-game supply |

---

## Rail Intersection Blueprints

The most important intersections to have as blueprints:

1. **4-way intersection** — main crossing
2. **3-way intersection** — T-junction
3. **Double-track roundabout** — simple and reliable
4. **High-throughput 4-way** — for busy rail networks

**Key design principle:** Longer intersections = higher throughput. A 6-tile-long intersection handles more trains per minute than a 2-tile one.

---

## Related Guides

- **[Train Signals Guide](/trains-logistics/factorio-train-signals-guide/)** — Chain vs. rail signals
- **[Train Deadlock Fix](/trains-logistics/factorio-train-deadlock-fix/)** — Prevention checklist
- **[Rail Intersection Blueprint](/trains-logistics/factorio-rail-intersection-blueprint/)** — Ready-to-use designs
- **[Logistic Network Guide](/trains-logistics/factorio-logistic-network-guide/)** — Bot network setup
