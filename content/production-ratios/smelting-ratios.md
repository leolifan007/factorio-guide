---
title: "Smelting Ratios — How Many Furnaces Per Belt"
description: "Exact smelting ratios for iron, copper, steel, and stone. Never waste furnaces or belt capacity again."
date: 2026-05-18
tags: ["production-ratios", "smelting", "belts"]
---

## The Core Concept

A **transport belt** carries 7.5 items/second (15 items/second for fast belt, 22.5 for express belt).

A **stone furnace** smelts 1 plate per 3.2 seconds = **0.3125 plates/second**.
An **electric furnace** smelts 1 plate per 1.6 seconds = **0.625 plates/second**.

## Iron and Copper Smelting

| Belt Type | Plates/sec | Stone Furnaces | Electric Furnaces |
|-----------|-------------|-----------------|-------------------|
| Basic belt (half) | 3.75 | 12 | 6 |
| Basic belt (full) | 7.5 | 24 | 12 |
| Fast belt | 15 | 48 | 24 |
| Express belt | 22.5 | 72 | 36 |

<div class="tip-box">
<strong>Rule of thumb:</strong> 1 full basic belt of iron ore needs exactly <strong>24 stone furnaces</strong> (or 12 electric furnaces) to consume it entirely.
</div>

## Steel Smelting

Steel needs **5 iron plates** and takes **17.5 seconds** in a stone furnace.

| Setup | Steel plates/sec | Furnaces needed |
|-------|------------------|-----------------|
| Basic | 0.28 | 1 furnace = 1 steel at a time |
| Optimized | 1.0 | 6 electric furnaces + beacon setup |

> **Pro tip:** Steel is slow. Don't try to make large amounts of steel with stone furnaces. Electric furnaces or **steel furnaces** are highly recommended.

## Visual Layout

A proper smelting column (simplified description):

Iron ore belt arrow Furnace Furnace Furnace... arrow Plate output belt arrow Chest or next assembler

> **Design principle:** Always leave space to **upgrade** from stone to steel to electric furnaces without rebuilding the entire column.

## Beaconed Smelting (Megabase)

With **speed module 3** in furnaces plus **speed beacons**:

| Setup | Plates/sec per furnace | Furnaces for 1 belt |
|-------|------------------------|----------------------|
| Beaconed electric | ~2.5 | 3 furnaces per half-belt |

**Next:** [Production Ratio Reference]({{< ref "/production-ratios/" >}}) — all ratios in one table.
