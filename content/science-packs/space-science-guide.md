---
title: "Space Science Pack from Rocket Launch - Ratios and Setup for Factorio Space Age"
date: 2026-06-20
tags: ["science-packs", "space-age"]
draft: false
---

{{< callout "tip" >}}
**Space science at a glance:** Each rocket launch with a satellite produces 1000 space science packs in Space Age. One rocket silo running continuously at full speed produces roughly 1 rocket per 42 seconds, or about 85 space science packs per second. The bottleneck is never the silo -- it is producing 100 rocket parts worth of materials (red circuits, blue circuits, low density structures, and rocket fuel) fast enough.
{{< /callout >}}

{{< section "Recipe and Requirements" />}}

{{< recipe name1="rocket_part" qty1="100x" name2="satellite" qty2="1x" result="space_science" rqty="1000x" >}}

Space Science is unique among all science packs: you do not feed ingredients into an assembler. Instead, you build a rocket silo, fill it with 100 rocket parts, add a satellite, and launch. The satellite reaches your space platform and converts into 1000 space science packs per launch.

| Ingredient | Per Launch | Per 100 SPM (0.5 launches/min) | Per 200 SPM |
|-----------:|:----------:|:-----------------------------:|:-----------:|
| Rocket Parts | 100 | 50/min | 100/min |
| Red Circuits per part | 1 | 50/min | 100/min |
| Blue Circuits per part | 1 | 50/min | 100/min |
| Low Density Structures per part | 1 | 50/min | 100/min |
| Rocket Fuel per part | 1 | 50/min | 100/min |
| Satellite (Blueprint) | 1 | 0.5/min | 1/min |

Each launch also consumes: 1 rocket silo, ~42 seconds of crafting time, and enough belt throughput to keep the silo fed.



{{< section "Rocket Part Production Chain" />}}

Each rocket part needs 4 ingredients, all of which require significant mid-game production scale:

| Rocket Part Ingredient | Actual Items Needed | Intermediate Chain |
|-----------------------|-------------------|-------------------|
| Red Circuit (1) | 1 Plastic + 4 Copper Cable + 2 Green Circuit | Plastic from petroleum, Green from copper+iron |
| Blue Circuit (1) | 2 Green + 2 Red + 0.5 Sulfuric Acid | Acid from sulfur, sulfur from petroleum |
| Low Density Structure (1) | 10 Copper + 2 Steel + 5 Plastic | All from main bus materials |
| Rocket Fuel (1) | 10 Solid Fuel | Light oil -> solid fuel processing |

{{< callout "info" >}}
**Rocket silo speed:** The rocket silo has 4 module slots. Fill them with productivity modules immediately. Each level of productivity reduces the effective cost per part. At prod module 3 (4x +10%), you get 4 free rocket parts for every 10 crafted. This is the single best productivity investment in the entire factory because it directly multiplies science output.
{{< /callout >}}



{{< section "Rocket Silo Setup for 100 SPM" />}}

100 space science per minute is achievable with a single rocket silo and moderate production backing:

| Component | Machines | Produces | Notes |
|-----------|:--------:|:--------:|-------|
| Rocket Silo | 1 | 50 rocket parts/min | With 4 prod modules, no speed beacons |
| Red Circuit AM3 | 2 | ~60/min each | Standard circuit bus output |
| Blue Circuit AM3 | 2 | ~40/min each | Adjacent to acid pipe |
| LDS AM3 | 2 | ~60/min each | Steel + Copper + Plastic on belts |
| Solid Fuel Chem Plant | 3 | ~30/min each | Light oil from advanced refining |
| Green Circuit AM3 | 6 | ~90/min each | Shared with all other science packs |

{{< callout "warning" >}}
**The real space science bottleneck** is not the silo -- it is the material throughput. Each rocket launch consumes 100 blue circuits. At a moderate 100 SPM target, you need 50 blue circuits per minute just for the rocket silo -- on top of what [blue science]({{< ref "/science-packs/blue-science-guide" >}}) and other recipes consume. Plan your blue circuit production to handle double what you think you need.
{{< /callout >}}



{{< section "Production Flow" />}}

{{< diagram "diagrams/space-science-flow.svg" "Space science production chain from rocket silo on Nauvis through satellite launch to space platform and back to labs" "760" >}}

The space science loop has three stages:

1. **Ground production (Nauvis):** Rocket silo assembles 100 rocket parts. Each part needs materials from the main bus. The satellite is a separate blueprint item that needs to be inserted into the silo before launch.
2. **Launch:** Rocket launches automatically when the silo is full and a satellite is loaded. The satellite reaches your platform orbit.
3. **Space science generation:** The platform hub converts the satellite into 1000 space science packs. These can be returned to Nauvis via your platform's cargo landing system.

If you have already built a [space platform]({{< ref "/space-age/platform/space-platform-guide" >}}), making science return is automatic -- the platform hub sends science packs down with every rocket launch. You just need enough cargo capacity.



{{< section "Scaling with Multiple Silos" />}}

| SPM Target | Rocket Silos | Launches/min | Rocket Parts/min | Key Constraint |
|:----------:|:----------:|:------------:|:----------------:|---------------|
| 100 | 1 | 0.5 | 50 | Blue circuits |
| 200 | 1 | 1 | 100 | Blue + LDS line |
| 500 | 2-3 | 2.5 | 250 | Steel + Copper throughput |
| 1000 | 4-5 | 5 | 500 | Entire bus + train supply |

At 500+ SPM, a single silo cannot keep up due to the craft time. The rocket silo caps at roughly 1 rocket per 42 seconds (~1.4 launches/min at full prod modules). Beyond that, build parallel silos each with their own belt supply.

For high-throughput science bases, a [city block design]({{< ref "/base-design/city-block-guide" >}}) with a dedicated rocket block works well. Each silo becomes its own train stop: circuits in, science out by belt to labs.



{{< section "Common Mistakes" />}}

- **No productivity modules in the silo:** The rocket silo is the only building in the game where productivity modules do not slow down output (because the bottleneck is assembling rocket parts, not the final product). Always fill all 4 slots with productivity module 3s.
- **Forgetting the satellite:** A rocket launched without a satellite produces 0 space science. Build a dedicated satellite assembler next to the silo and use an inserter to load it into the rocket before launch.
- **Under-building solid fuel:** Rocket fuel production is often overlooked. At 50 rocket parts per minute, you need 500 solid fuel per minute. That is 1,000 light oil per minute -- a significant output from your refinery block. Check the [Oil Processing Guide]({{< ref "/production-ratios/oil-processing-guide" >}}) for the solid fuel yield ratios from advanced refining.



{{< section "Bottom Line" />}}

Space science is an exercise in production scaling. One rocket silo feeds a 100 SPM base with ease. Two silos handle 200 SPM. Beyond that, the challenge shifts from science production to raw material throughput -- expanded steel foundries, copper smelters, and circuit plants. Start with a single silo, productivity modules, and a satellite assembler. Then scale the belt-fed inputs until you hit the silo's 42-second cycle limit.



{{< section "Community Verification" />}}

- [Factorio Wiki: Space science pack](https://wiki.factorio.com/Space_science_pack) -- Science pack recipe and mechanics
- [Factorio Wiki: Rocket silo](https://wiki.factorio.com/Rocket_silo) -- Silo speed, module effects, and throughput data
- [Factorio FFF-419](https://factorio.com/blog/post/fff-419) -- Official Space Age science pack changes

