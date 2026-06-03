---
title: "Kovarex Enrichment —Uranium Processing Loop"
description: "Kovarex enrichment guide for Factorio. The uranium processing loop that converts U-238 waste into U-235 fuel. Ratios, centrifuge placement, and the kickstart problem."
date: 2026-05-23
lastmod: 2026-06-03T22:40:00+08:00
publishDate: 2026-06-08T00:00:00+08:00
tags: ["production-ratios", "nuclear", "uranium"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

Kovarex enrichment is the uranium processing upgrade that turns waste into fuel. Without it, {{< material "uranium_ore" >}} uranium ore yields mostly U-238 —barely enough U-235 to keep a single reactor running.

{{< callout "tip" >}}
**TL;DR:** Kovarex centrifuges convert 40 U-238 + 40 U-235 鈫?41 U-238 + 1 U-235. Net: -40 U-238, +1 U-235 per cycle. Build 3 centrifuges per reactor. Kickstart requires 40 U-235 accumulated first.
{{< /callout >}}

{{< diagram "diagrams/kovarex-loop.svg" "Kovarex enrichment loop —uranium ore processing, enrichment centrifuge, and fuel cell production" "900" >}}

## The Enrichment Loop

Kovarex centrifuges run a different recipe from standard uranium processing:

**Input:** 40 U-238 脳 2 slots + 40 U-235 脳 1 slot  
**Output:** 41 U-238 + 1 U-235  
**Cycle time:** ~60 seconds  
**Net result:** -40 U-238, +1 U-235

This turns your U-238 stockpile (the waste product) into additional U-235 (the fuel). A factory running Kovarex enrichment produces 10脳 more reactor fuel from the same ore.

## The Kickstart Problem

Kovarex centrifuges need 40 U-235 to start. Standard uranium processing yields U-235 at 0.7% —roughly 1 per 143 ore processed.

**The math:** To get 40 U-235 from normal processing, you need ~5,700 uranium ore. At 1 ore/sec, that's 95 minutes of pure processing before your first Kovarex centrifuge can run.

**Strategy:** Build standard centrifuges first. Accumulate U-235. Only then add Kovarex centrifuges. Don't build them early —they'll sit idle.

## The Golden Ratio

Once running, Kovarex enrichment changes your factory ratios:

| Reactors | Kovarex Centrifuges | Standard Centrifuges |
|----------|---------------------|----------------------|
| 1 | 3 | 2-3 |
| 2 | 6 | 4-5 |
| 4 | 12 | 8-10 |

**Why 3:1?** One reactor consumes 1 U-235 every 200 seconds. One Kovarex centrifuge produces ~1 U-235 per 60 seconds. Three centrifuges = 3 U-235 per 60 seconds = 1 per 20 seconds = 10脳 reactor demand. The excess fuels expansion.

## Circuit Control Tips

Kovarex centrifuges should only run when you have excess U-238:

- Wire inserters to logistics network
- Enable when U-238 > 500
- Disable when U-238 < 200

This prevents draining your U-238 buffer below fuel cell production needs.

## What Veterans Learn the Hard Way

- **Don't rush Kovarex** —build it after you have 40+ U-235 stockpiled
- **Keep U-238 buffer** —Kovarex drains it fast. 500+ minimum.
- **Prioritize fuel cells** —Kovarex is bonus fuel, not primary. Fuel cells come first.
- **Expand centrifuges gradually** —3 per reactor is plenty until you're running 4+ reactors

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| Building Kovarex before 40 U-235 | Centrifuges idle for hours |
| No U-238 buffer | Kovarex drains stockpile, fuel cell production stops |
| Too many Kovarex centrifuges | Wasted resources, idle machines |
| Ignoring circuit control | U-238 crashes during peak demand |

## The Bottom Line

Kovarex enrichment is the uranium endgame. Accumulate 40 U-235 first, then build 3 centrifuges per reactor. Wire them to your logistics network. Turn U-238 waste into endless reactor fuel.

---

**Related:** [Nuclear Power Guide]({{< ref "/base-design/nuclear-power-guide" >}})