---
title: "Trains and Logistics Guide"
description: "Rail signals, train schedules, deadlock prevention, LTN, and logistic robot networks — build reliable transport at any scale."
date: 2026-05-18
---

<!-- Section: Trains and Logistics Overview -->
<div class="section-card orange">
<p>Factorios transport system scales from a single locomotive to continent-spanning rail networks carrying thousands of items per minute.</p>
<blockquote><p><strong>Design principle:</strong> Build your rail network <em>before</em> you need it. Retrofitting rails into a built-out base is painful.</p></blockquote>
</div>

## Rail Signal Basics

| Signal | Purpose |
|--------|---------|
| Rail signal | Marks end of a block (placed after intersections) |
| Chain signal | Extends block (placed before intersections) |
| Train stop | Destination for a train schedule |

> **Golden rule:** A train can only enter a block if the exit is also clear. Chain signals propagate this check through intersections.

## Deadlock Prevention

Deadlocks happen when two trains each occupy a block the other needs.

<div class="check-row">
<div class="check-item"><span class="check-icon"></span><div><strong>Rule 1:</strong> Never have two trains share the same single-track segment in opposite directions.</div></div>
<div class="check-item"><span class="check-icon"></span><div><strong>Rule 2:</strong> Use chain signals at all intersection entrances.</div></div>
<div class="check-item"><span class="check-icon"></span><div><strong>Rule 3:</strong> Keep train station lanes separate (dedicated in/out tracks).</div></div>
</div>

## Logistics Robots vs Belts

| Task | Belts | Logistics robots |
|------|-------|-------------------|
| High volume | Best | Warning limited by roboport coverage |
| Long distance | Warning Complex | Excellent (via roboport network) |
| Setup cost | Low | High (roboports plus robots) |
| UPS cost | Low | High (late-game impact) |

> **Rule of thumb:** Belts for bulk production (iron, copper, plates). Robots for low-volume, high-flexibility tasks (modules, blueprints, repair packs).
