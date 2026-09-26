---
title: "Factorio Aquilo Heat Pipe Not Working - 5 Causes and Fixes"
description: "Your Aquilo heat pipe looks connected but your machines keep freezing. The adjacency rule, the real heat drain table (per entity kW), how many heating towers you actually need, and how to bootstrap power without dying cold."
date: 2026-09-26
lastmod: 2026-09-26T00:47:00+08:00
tags: ["space-age", "aquilo", "planets"]
draft: false
---

{{< callout "tip" >}}
**Short answer: a building only stays warm if it physically touches a heated tile.** Heat does not radiate outward, it does not travel along normal fluid pipes, and it does not care how close buildings are. Three checks fix 90% of broken Aquilo heat networks: (1) every machine orthogonally or diagonally adjacent to a heat pipe, (2) the source sitting above 30 degrees C, and (3) total consumer drain below what your heating towers can supply. Warm note: {{<material "heating-tower">}} heating towers burn solid fuel, and Aquilo has {{<material "crude_oil">}} crude oil, so the fix is usually local once you break the cold start.
{{< /callout >}}

If your chemical plants are blinking frozen on Aquilo, it is not a power problem. Aquilo electricity runs fine while your factory is a block of ice. **Heating and electricity are two separate networks**, and almost every "heat pipe not working" complaint is actually a geometry mistake.

{{< section "Cause 1: The Machine Is Not Touching The Heat Pipe" />}}

This is the one that gets everyone. **Adjacency means orthogonally or diagonally adjacent - one tile.** Not two tiles, not "in the same row", not "within beacon range".

{{< diagram "diagrams/space-age/aquilo-heat-adjacency.svg" "Aquilo heat pipe adjacency rule showing which machines stay warm and which freeze" "760" >}}

Common versions of this mistake:

| What you built | Why it freezes |
|:---------------|:---------------|
| Heat pipe running parallel, one empty tile of gap | Heat does not radiate through the floor |
| Heat pipe under underground belts only | The belt entrance and exit are not heated tiles |
| Row of machines with heat pipe on one end | Only the machine touching the pipe survives |
| Beaconed layout copied from Nauvis | Beacons are the {{<material "beacon">}} single largest heat drain at 400 kW |

The fix is boring: **run the heat pipe directly alongside the machine row**, so every machine shares a border with a heated tile. Do not leave spacing for future expansion the way you would on Nauvis.

{{< section "Cause 2: Demand Exceeds What One Heating Tower Can Supply" />}}

Heat pipes never leak heat into the environment. They only lose it to entities that need to stay warm. So if your network goes cold, **something on that network is eating more kW than you are generating.**

{{< diagram "diagrams/space-age/aquilo-heat-budget.svg" "Aquilo heat budget per entity in kilowatts with heating tower, heat pipes and consumers" "760" >}}

| Entity | Heat drain |
|:-------|:-----------|
| {{<material "beacon">}} Beacon | 400 kW |
| {{<material "oil_refinery">}} Oil refinery | 200 kW |
| Turbo underground belt | 200 kW |
| {{<material "chemical-plant">}} Chemical plant, {{<material "assembling-machine-3">}} assembling machine, {{<material "recycler">}} recycler, {{<material "cryogenic_plant">}} cryogenic plant | 100 kW |
| Storage tank, selector combinator | 100 kW |
| Pipe to ground | 150 kW |
| Fast / express underground belt | 100 / 150 kW |
| Splitter | 40 kW |
| {{<material "inserter">}} Inserter, pump, {{<material "gun_turret">}} turret | 30 kW |
| Transport belt | 10 kW |
| Normal {{<material "pipe">}} pipe | 1 kW |

Read that list again, because two entries explain most failures. **Underground belts cost five to twenty times what the surface belt costs**, so a belt-heavy bus that crosses itself underground will out-drain your heat supply without looking any bigger. Same for pipe to ground at 150 kW against 1 kW for a surface pipe.

**Practical rule:** one {{<material "heating-tower">}} heating tower covers a compact production block, not a base. If you have more than roughly 20 machines plus their belts and undergrounds on one network, split it into separate heated zones with their own tower. If you are planning the wider layout, {{< ref "/space-age/aquilo/aquilo-guide" >}} covers how much space to reserve per zone before you commit.

{{< section "Cause 3: The Heating Tower Has Nothing To Burn" />}}

Cold start problem: your refinery needs heat before it can make solid fuel, and it needs solid fuel before it can make heat.

Break the loop with imported fuel. Bring {{<material "solid_fuel">}} solid fuel or {{<material "rocket-fuel">}} rocket fuel with your landing cargo, use it to run the first tower, then switch to locally refined fuel from the {{<material "crude_oil">}} crude oil pumpjacks once the chain is warm. Aquilo genuinely has oil, so this is a one-time bootstrap rather than a permanent import dependency. The exact fuel count to pack is listed in {{< ref "/space-age/aquilo/what-to-bring" >}}, and getting that number wrong is why so many first landings freeze before minute ten.

Worth knowing if the tower is missing from your build menu entirely: **heating towers are unlocked on Gleba, not on Nauvis.** If you jumped straight to Aquilo, {{< ref "/space-age/gleba/gleba-survival-guide" >}} covers the Gleba chain that hands you both the tower and the heat exchanger you need here.

| Stage | Fuel source | Notes |
|:------|:------------|:------|
| Landing | Imported solid / rocket fuel | Enough for the first 20 minutes |
| Bootstrap | Local crude oil to solid fuel | Refinery itself needs heat |
| Stable | Solid fuel loop with buffer chest | Chests are freeze-immune |

Note the useful exception: **chests do not freeze.** Chests, electric poles, {{<material "solar-panel">}} solar panels, {{<material "accumulator">}} accumulators, lamps, {{<material "wall">}} walls, {{<material "tesla_turret">}} tesla turrets and rails are all immune. That means you can safely buffer solid fuel in an unheated area right next to the tower.

{{< section "Cause 4: You Confused Fluid Pipes With Heat Pipes" />}}

Regular {{<material "pipe">}} pipes move fluids. Heat pipes move heat. They are different entities and they do not substitute for each other. A belt of machines wired together with normal pipes will freeze even if those pipes sit directly on top of a working heating tower.

Also worth knowing: **heat does not pass through machines.** Heat pipes chain to each other, and every machine touching the chain gets warm, but a machine never relays heat to its neighbour. Put one heat pipe tile between two machines in a row and only those two survive.

{{< section "Cause 5: Robot Power, Not Heat" />}}

This one is not heat at all, it just looks identical. On Aquilo the ratio of gravity to atmospheric pressure is five times higher than elsewhere, so construction and logistic robots consume proportionally more energy. Players blame freezing when the actual fault is that bots cannot finish the build before the network browns out.

The symptom difference: **frozen machines are already built and idle; starved bots leave half-finished ghosts.** If you see ghosts that never complete, add power, not heat.

{{< section "The 60-Second Diagnostic" />}}

| Symptom | Most likely cause | First fix |
|:--------|:------------------|:----------|
| One machine frozen, neighbours fine | Not touching the heated tile | Move it one tile toward the pipe |
| Whole row freezes a few minutes after start-up | Demand above supply | Add a second heating tower, split the zone |
| Everything freezes during expansion | New block never got its own tower | Zone heating, do not daisy-chain |
| Freezes when you add undergrounds | 150 to 200 kW per underground | Replace with surface belts inside heated area |
| Nothing works right after landing | No fuel in the first tower | Refine local crude oil or import solid fuel |
| Ghosts never finish building | Bot power drain, not heat | Add generation, not heating |

{{< section "What NOT To Do" />}}

| Bad idea | Why it fails |
|:---------|:-------------|
| Waiting for electricity to warm things | Power and heat are separate networks |
| Building one giant heated base | Total drain quietly exceeds one tower |
| Scaling with underground belts | Cheapest-looking option, worst heat cost |
| Assuming wiki Nauvis layouts transfer | Every tile here needs a heat budget |
| Ignoring the freezing icon | It tells you the exact problem for free |

Once the network holds temperature, Aquilo flips to the opposite problem: ice. Ammonia separation and electrolysis hand you far more ice than your base consumes, and a full ice buffer stalls production just as hard as a frozen machine does. {{< ref "/space-age/aquilo/excess-ice" >}} covers the voiding setups that stop it backing up into the block you just finished heating.

{{< section "Community Verification and Resources" />}}

- [Factorio Wiki: Aquilo](https://wiki.factorio.com/Aquilo) - freezing mechanics and the official per-entity heat drain table
- [Factorio Wiki: Heat pipe](https://wiki.factorio.com/Heat_pipe) - heat throughput limits and connection rules
- [Reddit r/factorio](https://www.reddit.com/r/factorio/) - player-reported cold-start routes and zone layouts

*Last updated: 2026-09-26 | Verified against Factorio 2.0 / Space Age.*
