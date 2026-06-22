---
title: "Utility Science Pack Setup - Yellow Science Ratios for Space Age"
date: 2026-06-20
tags: ["science-packs", "production-ratios"]
draft: false
---

{{< callout "tip" >}}
**Yellow science at a glance:** 5 assemblers need 10 steel furnaces, 1 flying robot frame assembler, 1 blue circuit assembler, and 1 low density structure assembler. The output is 3 packs per craft (Space Age). Blue circuits (processing units) are the bottleneck -- one blue circuit assembler needs 20 green circuits and 2 red circuits per second at full tilt.
{{< /callout >}}

{{< section "Recipe and Requirements" >}}

{{< recipe name1="processing_unit" qty1="1x" name2="flying_robot_frame" qty2="1x" name3="low_density_structure" qty3="1x" result="utility_science" rqty="3x" >}}

Utility Science (Yellow) is the most complex pre-Space science pack. While [blue science]({{< ref "/science-packs/blue-science-guide" >}}) introduces oil and [purple science]({{< ref "/science-packs/production-science-guide" >}}) tests your steel throughput, yellow science demands production depth: you need blue circuits (which bring sulfuric acid into the mix), flying robot frames (which chain through electric engines), and low density structures (plastic + copper + steel).

| Ingredient | Per Yellow Science Pack | For 5 SPM | How to Make |
|-----------|:----------------------:|:---------:|------------|
| Processing Unit (Blue Circuit) | 0.33/s | 1.67/s | Red Circuit + Green Circuit + Sulfuric Acid |
| Flying Robot Frame | 0.33/s | 1.67/s | Engine + Electric Engine + Battery + 2 Green + 3 Steel |
| Low Density Structure | 0.33/s | 1.67/s | Copper + Steel + Plastic |

Each craft in Space Age produces 3 utility science packs (up from 2 in 1.0). The craft time is 21 seconds base, or about 29 seconds in an Assembling Machine 2.

{{< /section >}}

{{< section "Optimal Ratios for 5 SPM" >}}

| Component | Machines | Input | Notes |
|-----------|:--------:|-------|-------|
| Yellow science assemblers | 5 | Blue + Frame + LDS | AM2, 29 sec craft time |
| Flying robot frame assemblers | 1 | Engine + Elec + Bat + Green + Steel | AM2, feeds 2 science assemblers |
| Electric engine assemblers | 2 | Engine + Red + Lube | Shared with purple science chain |
| Engine unit assemblers | 2 | Steel + Gear + Pipe | Pulls from main bus |
| Blue circuit assemblers | 1 | 20 Green + 2 Red + Acid | AM3 recommended for speed |
| Red circuit assemblers | 2 | Plastic + Copper + Green | Shared with blue and purple science |
| Green circuit assemblers | 4 | Copper cable + Iron | Yellow science is circuit-hungry |
| Low density structure assemblers | 1 | Copper + Steel + Plastic | One AM2 output beats 5 SPM needs |
| Battery chemical plants | 1 | Sulfuric Acid + Iron | One plant handles multiple sciences |
| Steel furnace (stone/steel) | 10 | Iron ore + Coal | Steel for frames, LDS, gears |
| Sulfuric acid chemical plants | 1 | Sulfur + Water + Iron | Feeds blue circuits and batteries |

{{< callout "warning" >}}
**The blue circuit tax:** Each blue circuit needs 20 green circuits and 2 red circuits. At 5 SPM, your circuit factory must produce roughly 33 green circuits and 3.3 red circuits per second just for yellow science -- plus blue science, purple science, and whatever else you are building. Build at least 4 green circuit assemblers and route them before anything else.
{{< /callout >}}

{{< /section >}}

{{< section "Low Density Structure Production" >}}

Low density structures (LDS) are straightforward but material-heavy. Each unit needs 10 copper plates, 2 steel plates, and 5 plastic bars. At 5 SPM you need roughly 17 copper plates per second just for LDS.

| SPM | LDS/sec | Copper/sec | Steel/sec | Plastic/sec |
|:---:|:-------:|:----------:|:---------:|:----------:|
| 5 | 1.67 | 16.7 | 3.3 | 8.3 |
| 15 | 5.0 | 50.0 | 10.0 | 25.0 |
| 30 | 10.0 | 100.0 | 20.0 | 50.0 |

Your furnace columns need to handle this. Check [smelting ratios]({{< ref "/production-ratios/smelting-ratios" >}}) to calculate steel furnace upgrades. At 30 SPM you should be switching to electric furnaces and beaconed setups.

{{< /section >}}

{{< section "Production Flow" >}}

{{< diagram "diagrams/yellow-science-flow.svg" "Utility science production chain from basic materials through flying robot frames to yellow science packs" "760" >}}

The production chain for yellow science splits into three parallel branches:

1. **Flying Robot Frame branch:** Steel + Gear + Pipe -> Engine. Engine + Red Circuit + Lube -> Electric Engine. Then combine Engine + Electric Engine + Battery + Green Circuits + Steel to make the frame.
2. **Blue Circuit branch:** Green Circuit + Plastic -> Red Circuit. Then Red Circuit + Green Circuit + Sulfuric Acid -> Blue Circuit.
3. **Low Density Structure branch:** Copper Plate + Steel Plate + Plastic -> LDS. Dead simple but copper-intensive.

All three branches converge at the yellow science assemblers. The flying robot frame is the slowest of the three ingredients to produce, so build its assembler first and let the other two branches match its output.

If your oil processing is still on basic refining, now is the time to switch. Plastic for LDS and red circuits, plus sulfur for sulfuric acid -- both come from petroleum. Our [Oil Processing Guide]({{< ref "/production-ratios/oil-processing-guide" >}}) covers the advanced refining ratios that keep all three outputs balanced.

{{< /section >}}

{{< section "Scaling Beyond 5 SPM" >}}

| SPM Target | Yellow Assemblers | Blue Circuit AMs | Flying Robot AMs | Key Constraint |
|:----------:|:----------------:|:----------------:|:----------------:|---------------|
| 5 | 5 | 1 | 1 | Circuit production |
| 15 | 15 | 3 | 3 | Acid throughput |
| 30 | 30 | 6 | 6 | Steel + Power |
| 45 | 45 | 9 | 9 | Entire bus width |

At 30+ SPM, the main bus becomes the primary bottleneck. You need dedicated circuit sub-factories rather than pulling circuits off the main bus. A [city block design]({{< ref "/base-design/city-block-guide" >}}) with train-supplied circuit production is the standard solution for this stage.

**Module tip:** Productivity modules in blue circuit assemblers are the highest-ROI investment in the yellow science chain. Each prod module saves 10% of the massive green circuit input. Speed modules in flying robot frame assemblers also help since the craft time is long.

{{< /section >}}

{{< section "Common Mistakes" >}}

- **Not enough green circuits:** A blue circuit assembler running at full speed consumes 20 green circuits per second. That is one full yellow belt. Most players build two green circuit assemblers thinking it is enough, then wonder why all their science packs are starved.
- **Sulfuric acid delivery:** Pipes have throughput limits. If you pipe sulfuric acid across half your base, the flow rate drops below what blue circuit assemblers need. Either build acid production close to the circuit area or use barrels with bots.
- **Neglecting batter:** Battery production needs sulfuric acid too. A single battery chemical plant running off the same acid line can starve the blue circuit assembler. Build a separate acid plant or split the output with pumps.

{{< /section >}}

{{< section "Bottom Line" >}}

Utility science is the throughput exam in Factorio. It forces you to build a proper circuit factory with dedicated green circuit production, scale up steel and copper simultaneously, and integrate sulfuric acid into your base logistics. Start with 5 SPM using the ratios above. Scale by doubling entire production blocks rather than adding single machines -- the ratios are designed to scale linearly.

{{< /section >}}

{{< section "Community Verification" >}}

- [Factorio Wiki: Utility science pack](https://wiki.factorio.com/Utility_science_pack) -- Recipe reference and crafting times
- [Factorio FFF-419: Space Age science changes](https://factorio.com/blog/post/fff-419) -- Official changes to yellow science output per craft

{{< /section >}}