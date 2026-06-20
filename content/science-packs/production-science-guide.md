---
title: "Production Science Pack Ratios - Purple Science Setup for Space Age"
date: 2026-06-20
tags: ["science-packs", "production-ratios"]
draft: false
---

{{< callout "tip" >}}
**Purple science at a glance:** 5 assemblers need 9 steel furnaces, 2 engine assemblers, 2 electric engine assemblers, and 1 lubricant chemical plant. Total: about 15 machines running off a standard main bus. The key bottleneck is always electric engines -- most builds underestimate how many engine assemblers they need.
{{< /callout >}}

{{< section "Recipe and Requirements" >}}

{{< recipe name1="electric_engine" qty1="1x" name2="productivity_module_1" qty2="1x" name3="rail" qty3="1x" result="production_science" rqty="3x" >}}

The Production Science Pack (Purple) is the mid-game gate in Factorio Space Age. Each craft takes 10 seconds and produces 3 packs (up from 2 in Factorio 1.0). The three ingredients force you to scale up steel production, start lubricant-based manufacturing, and build your first module factory.

| Ingredient | Per Pack | For 5 SPM | Source |
|-----------|:--------:|:---------:|--------|
| Electric Engine Unit | 0.33/s | 1.67/s | Engine + Red Circuit + Lubricant |
| Productivity Module 1 | 0.33/s | 1.67/s | Red Circuit + Green Circuit |
| Rail | 0.33/s | 1.67/s | Steel + Stone |

If you are coming from [blue science]({{< ref "/science-packs/blue-science-guide" >}}), purple science is a different kind of challenge. Blue science tests your oil refining. Purple tests your raw resource scaling -- specifically steel throughput and circuit production.



{{< section "Optimal Ratios for 5 SPM" >}}

5 SPM is a comfortable mid-game target when first setting up purple science. It unlocks the main Space Age tech tree without forcing a megabase.

| Component | Machines | Input | Notes |
|-----------|:--------:|-------|------|
| Purple science assemblers | 5 | 3 ingredients each | Craft time 10s, output x3 |
| Electric engine assemblers | 2 | Engine + Red + Lube | 1 assembler feeds ~2.5 science assemblers |
| Engine unit assemblers | 2 | Steel + Gears + Pipes | AM2, direct feed to electric engines |
| Productivity module 1 assemblers | 1 | Red + Green circuits | One AM1 handles up to 10 SPM |
| Rail assemblers | 1 | Steel + Stone | One AM1 handles more than 5 SPM needs |
| Green circuit assemblers | 2-3 | Copper cable + Iron | Shared with other sciences |
| Red circuit assemblers | 1-2 | Plastic + Copper + Green | Shared with blue science |
| Lubricant chemical plant | 1 | Heavy oil | 1 plant at basic output is enough |
| Steel furnace (stone/steel) | 9 | Iron ore + Coal | Steel for rails + engine + modules |

{{< callout "warning" >}}
**Common ratio trap:** One engine unit assembler needs 1 steel/sec. Two engine assemblers need 2 steel/sec. Two rail assemblers need 5.4 steel/sec. Plus steel for the productivity module production chain. Your steel column should be at least twice what you think it needs. Check our [Smelting Ratios Guide]({{< ref "/production-ratios/smelting-ratios" >}}) for exact furnace counts.
{{< /callout >}}



{{< section "Lubricant Production" >}}

Purple science is the first point where you need lubricant. If you already have oil processing set up for blue science, adding lubricant is simple:

| Step | Machine | Input | Output |
|------|---------|-------|--------|
| Heavy oil extraction | Refinery (advanced) | Crude oil + Water | Heavy + Light + Petroleum |
| Heavy oil cracking | Chemical plant | Heavy oil | Light oil (optional) |
| Lubricant | Chemical plant | Heavy oil | Lubricant |

**The trick:** Do not crack all your heavy oil into light oil. Reserve at least one full pipe of heavy oil for lubricant production. Each electric engine unit needs 1 lubricant, and at 5 SPM you consume about 1.67 lubricant per second -- that is roughly 3 chemical plants worth of heavy oil cracking diverted to lube.

If you are using basic oil processing, a single refinery on crude oil produces 30 heavy oil per cycle. That feeds about 1.5 chemical plants making lubricant -- barely enough. Switch to [advanced oil processing]({{< ref "/production-ratios/oil-processing-guide" >}}) as soon as your blue science is stable. Advanced processing doubles heavy oil output per cycle.



{{< section "Layout -- Compact Purple Science Cell" >}}

{{< diagram "diagrams/purple-science-flow.svg" "Production science chain from steel and circuits through electric engines to purple science packs" "760" >}}

The optimal layout for purple science follows a straight line:

1. **North side:** Steel furnace column feeds into a splitter that sends steel to rail production, engine production, and productivity module assembly
2. **Middle row:** Engine assemblers feed into electric engine assemblers. Productivity module assemblers sit on the circuit bus
3. **South side:** Rail production on stone/steel input. Red and green circuits come from the main bus or a dedicated circuit sub-factory
4. **Output:** All three ingredients meet at the purple science assemblers. Belts merge using a 3-to-1 balancer

{{< callout "info" >}}
**Material routing:** Purple science is the first point where the [main bus]({{< ref "/base-design/main-bus-guide" >}}) becomes tight. You need steel, iron, copper, stone, plastic, and green circuits all flowing. Plan for 4 lanes of steel if you intend to scale past 15 SPM.
{{< /callout >}}



{{< section "Scaling Beyond 5 SPM" >}}

When you decide to push purple science higher, these are the bottlenecks to watch for:

| SPM Target | Purple Assemblers | Steel Furnaces | Electric Engine Assemblers | Key Constraint |
|:----------:|:----------------:|:-------------:|:-------------------------:|----------------|
| 5 | 5 | 9 | 2 | Steel throughput |
| 15 | 15 | 27 | 6 | Lubricant + Red circuits |
| 30 | 30 | 54 | 12 | Module factory space |
| 45 | 45 | 81 | 18 | Entire bus redesign needed |

**Scaling tip at 30+ SPM:** Switch electric engine assemblers to Assembling Machine 3 with speed module 1s. The recipe is slow (10s base), and speed modules directly increase purple science output per assembler without adding complexity to the ingredient belts.

A dedicated electric engine sub-factory becomes necessary around 30 SPM. You can use [circuit network control]({{< ref "/blueprints/circuit-network-guide" >}}) to balance lubricant between electric engine production and battery manufacturing for your other science packs.



{{< section "Common Mistakes" >}}

- **Underestimating steel:** Purple science consumes steel for rails, engine units, and productivity module component chains. A single yellow belt of steel (15/s) supports about 10 SPM of purple science only. Share with other sciences and you will run out quickly.
- **Neglecting module production:** Productivity module 1 requires 5 red circuits and 5 green circuits per unit. At 5 SPM, each minute you burn 50 red and 50 green circuits just on modules. That is comparable to the circuit consumption of blue science. Building a dedicated module assembler early saves you from circuit starvation later.
- **Not planning rail output:** One rail assembler at a full belt of steel produces 2 rails per second. That is enough for 5 SPM, but if you are also building rail networks for your factory expansion, the purple science demands will eat into your construction supply. Build a separate rail assembler just for science.



{{< section "Bottom Line" >}}

Purple science is where Factorio starts demanding real resource throughput. You need steel at scale, lubricant from your oil setup, and a small circuit factory running alongside everything else. Start at 5 SPM with 9 steel furnaces and 2 electric engine assemblers. Scale up in chunks rather than trying to build a 45 SPM setup from scratch -- the mid-game is about iteration, not perfection.

**Next step:** After purple science, the logical next milestone is setting up a space platform for [space science]({{< ref "/space-age/space-platform-guide" >}}). Or you can tackle utility science (yellow) to unlock logistic robots and upgrade your factory logistics.



{{< section "Community Verification" >}}

- [Factorio Wiki: Production science pack](https://wiki.factorio.com/Production_science_pack) -- Recipe reference and crafting times
- [Factorio FFF-419: Space Age science changes](https://factorio.com/blog/post/fff-419) -- Official changes to purple science output from 2 to 3 per craft

