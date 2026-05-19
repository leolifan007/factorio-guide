---
title: City Block Design Guide — Modular Megabase Layout
description: City block guide for Factorio. Block sizes, train grid design, intersection types, resource distribution, UPS impact, and Space Age building integration for scalable megabases.
date: 2026-05-19
tags: ["base-design", "city-block"]
draft: false
---

The main bus carries you to blue science. After that, your factory grows wider, not taller. Trains replace belts. Outposts multiply. And then you hit the big question: how do you organize a base that spans the entire map?

City blocks are the answer. A grid of standardized squares connected by trains. Each block is a self-contained factory cell. You stamp them wherever you need more iron plates, more circuits, more of anything. I have built five megabases with this approach across different versions of Factorio. The pattern that works best is simpler than you might expect.

{{< callout "tip" >}}
**TL;DR:** The best city block size is 4-chunk (128x128 tiles) with a rail loop around each block. Use roundabout intersections for throughput under 30 trains per minute. Use stacker intersections for higher traffic. Leave space for roboports and logistics chests at every block corner. City blocks in Space Age still work great — just update your internal builds to fit Foundries and EM Plants.
{{< /callout >}}

{{< section "Block Size — The Critical Decision" >}}

Three sizes dominate the megabase community. Each has tradeoffs:

| Block size | Chunks | Internal space | Best for |
|-----------|:------:|:--------------:|----------|
| 3-chunk | 96x96 | 60x60 usable | Outposts, small refineries |
| 4-chunk | 128x128 | 90x90 usable | Standard production (most common) |
| 6-chunk | 192x192 | 150x150 usable | Massive builds, module production |

I recommend 4-chunk blocks for a first megabase. They are spacious enough for a full smelting column or a green circuit array, but tight enough that trains can service them without long internal rail paths. The 90x90 tile internal space fits beaconed rows of furnaces and provides room for roboports at every corner.

{{< diagram "diagrams/city-block-sizes.svg" "Comparison of 3-chunk, 4-chunk, and 6-chunk city block sizes with usable space highlighted" "700" >}}

{{< section "The Rail Grid — Your Base Highway" >}}

The rail grid surrounds each block with a bidirectional path. Trains enter on one side, drop off or pick up cargo, and exit on the opposite side. The grid uses a two-track system: one direction on each side of the block.

**Key specifications for a 4-chunk grid:**
- Track spacing: 4 rails wide total (2 in each direction)
- Train stop slots: 6 tiles deep inside the block entrance
- Fuel distribution: one refueling station per 8 blocks
- Signaling rule: chain signal before every intersection, rail signal after

Do not worry about dedicated fuel trains for your first megabase. Belt fuel to a network of refueling stations placed at grid intersections. You can switch to a fuel train network when the base exceeds 500 trains.

{{< callout "tip" >}}
Use chain signals before every rail intersection and rail signals after every exit. This single rule prevents 95% of deadlocks. If a train cannot clear the entire intersection, the chain signal holds it back until the path is clear.
{{< /callout >}}

Build your rail grid on a blueprint book. A single 4-chunk block blueprint with rail perimeter and roboport corner saves hours of manual placement.

{{< section "Intersection Design — Where Deadlocks Happen" >}}

The intersection is where city blocks live or die. A single bad intersection causes a deadlock that paralyzes your entire base.

**Roundabout intersections (good enough):**
- Single lane roundabout at each block corner
- Chain signals at each entrance to the roundabout
- Rail signals at each exit from the roundabout
- Throughput cap: roughly 25-30 trains per minute
- Compact and easy to tile across the grid

**Stacker intersections (better performance):**
- Dedicated turn lanes for left and right
- No crossing paths — each train path is independent
- Separate entry lanes for each direction
- Throughput cap: 60-plus trains per minute

Start with roundabouts. They are compact and easy to build across a large grid. Upgrade to stacker intersections at bottlenecks — typically the main iron and copper arteries where traffic is heaviest.

{{< diagram "diagrams/city-block-intersection.svg" "Comparison of roundabout and stacker intersection layouts for city block rail grids" "700" >}}

**How to detect a bottleneck:** Watch the rail map. If trains are stopped at a chain signal before an intersection for more than 10 seconds, that intersection is overloaded. Build a stacker bypass parallel to it.

For high-traffic blocks, add a second exit. A block producing green circuits needs two output stations. Two stations mean two exit paths from the block, halving the load on the nearest intersection.

{{< section "Power Distribution Across the Grid" >}}

Powering a city block base requires careful planning. Each block draws significant power from furnaces, modules, and beacons.

**Power strategy for city blocks:**
- Build a dedicated nuclear power block (2x2 reactor layout)
- Route power poles along the rail perimeter of each block
- Each block needs medium power poles on all 4 sides
- 1 nuclear block (2x2) powers about 15-20 production blocks at full load
- Add solar panels on block rooftops to supplement power

I run a separate 2x2 nuclear station for every 15 blocks. This keeps power loss across long distance low.

{{< section "Blueprint Management" >}}

City blocks are useless without a good blueprint organization system.

**My blueprint book structure:**
- Book 1: Rail grid (4 templates for the 4 rotation variants)
- Book 2: Smelting block templates (iron, copper, steel, stone)
- Book 3: Circuit block templates (green, red, blue)
- Book 4: Science block templates (each science type)
- Book 5: Utility blocks (oil, nuclear, module production)

Each template includes the train stations with circuit conditions and requester chest settings. This lets me stamp a block and have it running in 5 minutes.

{{< section "Inside the Block — Production Templates" >}}

Each block is a template you can stamp down anywhere. Here are the templates I use most often:

**Smelting block (4-chunk)**
- Input: 2 train stations (iron ore and copper ore)
- Output: 2 train stations (iron plates and copper plates)
- 48 electric furnaces arranged in 12 beaconed rows
- 125,000 iron plates per minute at full production with speed modules

**Circuit block (4-chunk)**
- Input: iron plates, copper plates, plastic (3 stations)
- Output: green circuits (2 stations)
- 20 assembler 3s with speed beacons in a compact row layout
- 4 cable assemblers nearby with direct insertion to circuit assemblers

**Science block (4-chunk)**
- Input: all 7 science packs via dedicated stations on each side
- Output: none (consumed by labs)
- 60 labs arranged with 12 beacon modules for maximum research speed
- Belt-fed lab output that feeds the next lab row

{{< section "Space Age Updates — Foundries and EM Plants" >}}

City blocks work perfectly in Space Age with updated internal templates.

**Foundry block.** The Foundry replaces electric furnaces for smelting. It is faster and has built-in productivity. A single Foundry block at 4-chunk produces as much as 2.5 smelting blocks from the base game. This frees up enormous amounts of space.

**EM Plant block.** The Electromagnetic Plant replaces assemblers for circuit production. It quadruples circuit output per block compared to assembler 3s. Use EM Plant templates for all green, red, and blue circuit production.

**Cryo Plant block.** The Cryogenic Plant processes advanced Space Age recipes that require low temperatures. These are planet-specific and need their own blocks near the interplanetary logistics hub.

{{< callout "warning" >}}
Foundries and EM Plants are physically larger than standard buildings. A 3-chunk block might not fit them comfortably. Stick to 4-chunk or larger blocks for Space Age production templates.
{{< /callout >}}

{{< section "Common Mistakes" >}}

**Blocks too small.** Saving space makes blocks harder to build in. The rail perimeter eats more room than you expect. Start with 4-chunk.

**No roboport coverage.** Every block corner needs a roboport with logistics coverage reaching into neighboring blocks. Construction bots connect block to block. Without roboports, every build is manual.

**Single train station per resource.** High-volume resources like iron plates need multiple stations. Plan for 2-4 stations per input to avoid train queueing.

**Deadlock chains.** One deadlocked intersection spreads to every intersection behind it. If a train blocks an intersection, the entire rail network in that direction locks up. Mitigate with stacker bypasses at critical junctions.

**Forgetting refueling.** Trains run out of fuel. If they stop in the middle of an intersection, the whole grid locks. Place refueling stations at regular intervals.

{{< section "FAQ" >}}

**Q: How many blocks do I need for a 1k SPM base?**
A: Approximately 30-40 blocks depending on beacon usage and module tier. Each block produces roughly 25-35 SPM of its assigned science.

**Q: Can I mix block sizes in the same grid?**
A: Yes. Use 4-chunk for the main production grid and 2-chunk blocks for mining outposts and small deposits.

**Q: Do city blocks work with belts inside them?**
A: Yes. Belts within each block are fine. Only inter-block transport should use trains exclusively.

**Q: How do power poles work across blocks?**
A: The rail perimeter carries power poles connecting each block. Place poles at regular intervals along the perimeter path.

{{< section "Related Guides" >}}

- [Design a main bus as an alternative early-game layout]({{< ref "base-design/main-bus-guide" >}})
- [Master train signaling for the rail grid]({{< ref "trains-logistics/basic-rail-network" >}})
- [Optimize smelting ratios for block templates]({{< ref "production-ratios/smelting-ratios" >}})
- [Use circuits to manage block-level logistics]({{< ref "blueprints/circuit-network-guide" >}})
- [Set up nuclear power for block energy needs]({{< ref "base-design/nuclear-power-guide" >}})
