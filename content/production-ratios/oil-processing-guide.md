---
title: "Factorio Oil Processing Guide - Refinery Ratios and Cracking Setup"
description: "Oil processing ratios for Factorio: exact refinery-to-cracking ratios, pipe throughput limits, circuit-controlled cracking, and the 8:1:7 setup that never deadlocks."
date: 2026-05-21
tags: ["production-ratios", "getting-started"]
draft: false
emoji: "🛢️"
---

Your refineries are flashing yellow again. Heavy oil backed up → no light oil → no petroleum → no plastic → no red circuits → no blue science → completely dead base. The fix isn't more refineries. It's three pumps, three circuit wires, and the 8:1:7 ratio that keeps everything flowing.

{{< callout "tip" >}}
**TL;DR:** For every 8 refineries, build 1 heavy→light cracker, 7 light→petroleum crackers. Wire each storage tank to a pump with a decider: output > 20000 → crack. This setup never deadlocks.
{{< /callout >}}

## The Mechanics Behind This Bottleneck

Refineries produce three outputs simultaneously. If heavy oil fills up, the refinery stops — stopping light oil and petroleum production too. The game doesn't prioritize outputs. It stalls everything.

The solution is controlled cracking: convert excess heavy to light, excess light to petroleum, and let petroleum run through to solid fuel or rocket fuel when backed up.

## The Proven Fix — Ratios First, Pipes Second

**Basic ratio: 8:1:7**

| Machine | Count | Purpose |
|:--------|:-----:|:--------|
| Oil refineries (basic) | 8 | Raw crude → heavy + light + petroleum |
| Heavy→light crackers | 1 | Converts excess heavy oil to light |
| Light→petroleum crackers | 7 | Converts excess light oil to petroleum |

**How the math works:**
- 8 refineries produce: 40 heavy + 40 light + 80 petroleum per 5-second cycle
- 1 heavy cracker consumes 40 heavy → 30 light per cycle (clears all heavy if needed)
- 7 light crackers consume 105 light → 70 petroleum per cycle

The system can handle any consumption pattern because the cracking ratios match the production ratios.

**Circuit control (prevents the deadlock):**

1. Run red wire from heavy oil storage tank to decider combinator
2. Decider: heavy_oil > 20000 → output H = 1
3. Connect H output to the pump feeding heavy→light crackers
4. Repeat for light oil: light_oil > 20000 → output L = 1 → light→petroleum pump
5. Set and forget

{{< callout type="warning" >}}
**Traps People Keep Falling Into:** If heavy oil backs up, check that your heavy→light cracking pump gets enough supply. A common slip: the heavy oil pipe between the refinery output and the cracker input is too long (over ~100 tiles) causing flow dropoff. Use underground pipes to reduce segment count.
{{< /callout >}}

## Understanding Pipe Throughput (The Hidden Limiter)

Pipes have throughput limits that change with length:
- 1 pipe segment: 1,200 fluid/sec
- 10 segments: ~1,000 fluid/sec
- 50 segments: ~400 fluid/sec
- 100 segments: ~80 fluid/sec

For oil processing, keep pipe runs under 30 segments (about 60 tiles). Beyond that, throughput becomes your bottleneck before refinery speed does.

**Underground pipes are your friend.** Each underground pipe section counts as 2 segments regardless of distance (up to 11 tiles). A 10-tile gap costs only 2 segments instead of 10. This is the single highest-impact optimization for oil pipe networks.

| Diameter (pipe) | Max length before needing a pump | Flow rate |
|:---------------:|:--------------------------------:|:---------:|
| 1 pipe wide | ~30 segments (60 tiles) | ~80% of max |
| 2 pipes wide | ~50 segments (100 tiles) | ~90% of max |
| 3 pipes wide | ~80 segments (160 tiles) | ~95% of max |

## Advanced Oil — Heavy Oil Management

Heavy oil is the most valuable fraction for flamethrower ammo and lubricant. If you crack all of it, you lose access to both:

- **Lubricant:** Needed for electric engines (purple science). Each engine unit uses 1 lubricant.
- **Flamethrower ammo:** Heavy oil-based ammo deals the highest damage.

**The optimal approach:**
- Use the 8:1:7 base ratio
- Before the heavy→light cracker, add a split: some heavy oil goes to a dedicated lubricant tank
- If lubricant tank is full (maybe you're not building electric engines yet), route heavy to cracking
- Circuit condition on the lubricant tank: heavy > 5000 → send to cracking

{{< callout type="info" >}}
**Quick Tip:** Before advanced oil processing (which gives you full control over output ratios), you're stuck with basic processing. Build the circuit cracking setup from day one of oil — you won't need it until you've researched advanced oil, but having it ready prevents long debugging sessions later.
{{< /callout >}}

## Scaling Up — Refinery Blocks at Megabase Scale

For 1,000+ SPM, you'll need multiple refinery blocks. The design scales linearly:

**100 SPM base:**
- 8 refineries
- 1 heavy cracker + 7 light crackers
- 2 chemical plants for sulfur (plastic + sulfuric acid)
- 1 chemical plant for batteries

**1,000 SPM base:**
- 80 refineries (10× 8-reactor modules)
- 10 heavy crackers + 70 light crackers
- Dedicated crude oil train station per module
- Circuit control per module (not shared — independent pipe networks)

The per-module design ensures your oil base scales predictably: copy the blueprint, connect a crude oil train stop, done.

---

## Community Verification & Resources

- [Official Wiki — Oil Processing](https://wiki.factorio.com/Oil_processing) — exact cracking ratios and fluid system mechanics
- [Factorio Forums — Fluid Mechanics & Pipe Throughput](https://forums.factorio.com/viewtopic.php?t=6926) — community testing on pipe diameters, lengths, and flow rates
- [FactorioLab Calculator](https://factoriolab.github.io/) — set SPM target, get exact refinery/building counts including cracking modules
- [Kirk McDonald's Calculator](https://kirkmcdonald.github.io/calc.html) — oil processing ratio calculator for any target configuration
