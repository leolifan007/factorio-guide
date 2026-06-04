---
title: "LTN Mod Guide - Logistic Train Network Setup for Factorio"
description: "LTN (Logistic Train Network) mod guide for Factorio. Provider stops, requester stops, depot configuration, and the 3-stop system that automates your entire rail network."
date: 2026-05-23
lastmod: 2026-06-03T22:40:00+08:00
publishDate: 2026-06-04T00:00:00+08:00
tags: ["blueprints", "trains", "logistics"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

LTN (Logistic Train Network) turns trains into logistic bots. {{< material "rail" >}} Trains automatically travel from providers to requesters based on supply and demand —no schedules needed.

{{< callout "tip" >}}
**TL;DR:** Build a depot for idle trains. Place provider stops where items are produced. Place requester stops where items are needed. LTN assigns trains automatically. Wire every stop to chests.
{{< /callout >}}

{{< diagram "diagrams/ltn-3stop.svg" "LTN 3-stop system —depot, provider stop, and requester stop with train flow" "900" >}}

## The 3-Stop System

LTN requires three stop types:

| Stop Type | Purpose | Circuit Connection |
|-----------|---------|-------------------|
| **Depot** | Idle trains wait here | None (LTN manages) |
| **Provider** | Items available for pickup | Storage chest 鈫?stop |
| **Requester** | Items needed for delivery | Requester chest 鈫?stop |

**How it works:**
1. Provider signals available items to LTN
2. Requester signals needed items to LTN
3. LTN dispatches idle train from depot
4. Train loads at provider, unloads at requester
5. Empty train returns to depot

## Depot Setup

The depot is where idle trains park. Critical rules:

- **Minimum 2 trains** —one loading/unloading, one waiting
- **No schedule** —LTN assigns temporary schedules
- **Fuel station** —trains refuel at depot automatically

Place depots centrally on your rail network. Every train should reach a depot within 30 seconds of emptying.

## Provider Stops

Provider stops announce available items:

1. Place stop next to production
2. Wire storage chests to stop
3. Set "provide threshold" (e.g., provide iron plates when >1000)

**Best practice:** Use passive provider chests. LTN will dispatch trains when stock exceeds threshold.

## Requester Stops

Requester stops announce demand:

1. Place stop next to consumption
2. Wire requester chests to stop
3. Set "request threshold" (e.g., request iron plates when <200)

**Best practice:** Use requester chests with high request counts. LTN batches deliveries to minimize train trips.

## What Veterans Learn the Hard Way

- **Depot trains must be empty** —LTN can't assign a train carrying cargo
- **Wire every stop** —unwired stops break the network
- **Thresholds matter** —too low = train spam; too high = stockouts
- **One item type per provider** —mixed providers confuse LTN

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| Single train depot | Network stalls when train is busy |
| Unwired stops | LTN doesn't see supply/demand |
| Mixed provider chests | Trains load wrong items |
| No fuel at depot | Trains strand mid-network |

## The Bottom Line

LTN automates train logistics. Build depots with 2+ trains. Wire providers to storage chests. Wire requesters to requester chests. Set thresholds. Let LTN handle the rest.

---

**Related:** [Basic Rail Network]({{< ref "/trains-logistics/basic-rail-network" >}}) | [Circuit Network Guide]({{< ref "/blueprints/circuit-network-guide" >}})