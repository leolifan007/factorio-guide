---
title: "Best Planet Order in Space Age - Which Planet to Visit First and Why"
date: 2026-06-20
tags: ["space-age", "planets", "strategy"]
draft: false
---

{{< callout "tip" >}}
**TL;DR: Vulcanus -> Fulgora -> Gleba -> Nauvis (scale up) -> Aquilo.** Visit Vulcanus first for the foundry -- it doubles your iron and steel production instantly. Fulgora second for the electromagnetic plant and quality module loop. Gleba third for bioflux and agricultural science. Save Aquilo for last when your other planets are producing consistently.
{{< /callout >}}

{{< section "Why Order Matters" >}}

Factorio Space Age has four inner planets you must visit (Vulcanus, Fulgora, Gleba) plus the final planet (Aquilo). Each planet unlocks a permanent factory upgrade that changes how you produce things on all planets. The order you visit determines how quickly your base scales up.

| Planet | Permanent Unlock | Impact on Production |
|--------|-----------------|:--------------------:|
| Vulcanus | Foundry + Big Drill | Iron/steel 2x output, LDS from fluid |
| Fulgora | EM Plant + Quality Modules | Circuit production +50%, quality loop |
| Gleba | Bioflux + Infusion | Nutrient-based production, infinite resource patches |
| Aquilo | Fusion power + Cryogenics | Endgame energy, final tech requirements |

The optimal order maximizes the amount of multiplicative growth per planet visit. Visiting Vulcanus first gives you the technology that makes every other planet cheaper and faster.

{{< /section >}}

{{< section "Phase 1: Nauvis Prep (Before Any Planet)" >}}

Before building your first space platform, you need a well-functioning Nauvis base:

| Milestone | Target | Checklist |
|-----------|--------|:---------:|
| Science production | 15-30 SPM | All 4 Nauvis sciences running (red, green, blue, gray, purple, yellow) |
| Main bus | 4 belts iron, 4 belts copper | Check our [main bus guide]({{< ref "/base-design/main-bus-guide" >}}) for proper lane management |
| Defense | Turret perimeter | Gun turrets and walls covering pollution cloud |
| Smelting | 48+ furnaces | Iron and copper covered by [smelting ratios]({{< ref "/production-ratios/smelting-ratios" >}}) |
| Oil processing | Advanced refining | Switch from basic to advanced; balanced outputs |
| Space platform | First platform in orbit | Check the [space platform guide]({{< ref "/space-age/space-platform-guide" >}}) for early design |

Do not rush to leave Nauvis. The most common mistake is launching to Vulcanus with only red and green science running, then struggling to build anything because you lack blue science upgrades (logistics, construction bots, advanced oil).

{{< /section >}}

{{< section "Phase 2: Vulcanus First (Lava Smelting)" >}}

**Why first:** The foundry is the single most impactful unlock in Space Age. It replaces all Nauvis smelting with direct-from-lava production.

| Benefit | Detail |
|---------|--------|
| Iron from lava | Foundry casts molten iron directly from lava. No ore mining needed on Vulcanus. |
| Steel from iron (fluid) | Foundry makes steel from molten iron -- no iron plate intermediate. 50% fewer steps. |
| LDS from fluid | Low density structures crafted from molten copper + plastic, bypassing plate step. |
| Big drill | +50% resource drain on ore patches. Extends patch life significantly. |

**What to do there:** Build a lava pumping station, set up a foundry, research metallurgic science, and ship the foundry blueprint back to Nauvis. Full details in the [Vulcanus guide]({{< ref "/space-age/vulcanus-guide" >}}).

{{< /section >}}

{{< section "Phase 3: Fulgora Second (Quality and EM Plant)" >}}

**Why second:** The electromagnetic plant gives +50% circuit production speed, and quality module technology lets you upgrade every building in your factory.

| Benefit | Detail |
|---------|--------|
| EM Plant | 50% crafting speed bonus for circuits/science/intermediates |
| Quality modules | Recycler loop on Fulgora scrap gives quality items for free |
| Scrap recycling | Infinite resource generation from scrap islands |

**What to do there:** Set up scrap processing, build the EM plant, and start the quality module chain. The scrap output is random, so use circuit network sorting. Full guide at [Fulgora recycling]({{< ref "/space-age/fulgora-recycling-guide" >}}).

{{< /section >}}

{{< section "Phase 4: Gleba Third (Bioflux)" >}}

**Why third:** Gleba introduces the most complex production chain (biology/spoilage), but the bioflux unlocks agricultural science and infinite resource generation.

| Benefit | Detail |
|---------|--------|
| Bioflux | Converts to nutrients, which inserters and assemblers can use without electricity |
| Agricultural towers | Infinite fruit/plant growth -- never runs out |
| Stack inserters | Unlocked from Gleba research, doubles inserter throughput |

**What to do there:** The spoilage mechanic is the main challenge. Build produce-to-consumer chains that are as short as possible. Ship bioflux back to Nauvis for egg-based production chains. Full guide at [Gleba survival]({{< ref "/space-age/gleba-survival-guide" >}}).

{{< /section >}}

{{< section "Phase 5: Return to Nauvis (Scale Up)" >}}

After visiting all three inner planets, return to Nauvis and integrate everything:

1. Replace Nauvis smelting with foundry-based casting
2. Build EM plants for circuit production (50% faster than assemblers)
3. Run quality modules in recycler loops for legendary equipment
4. Scale science production to 60+ SPM across all 6 sciences

This is the most efficient point to build your endgame base. You have all the tools but do not yet need Aquilo's complexity. Many players spend 10-20 hours here building rail networks, city blocks, and megabase infrastructure.

{{< /section >}}

{{< section "Phase 6: Aquilo Last (Fusion)" >}}

Aquilo requires massive import logistics (no local resources except frozen ammonia), a heat pipe network, and rocket/laser defense against strafers. Visit only when:

- All 6 sciences are producing 30+ SPM
- You have a reliable cargo rocket system
- Your space platform can survive Aquilo orbit transitions
- You have 1000+ rocket fuel in storage on Nauvis

Full Aquilo prep checklist in the [Aquilo guide]({{< ref "/space-age/aquilo-guide" >}}).

{{< /section >}}

{{< section "Can You Skip Visits?" >}}

| Planet | Can Skip? | Consequence |
|--------|:---------:|-------------|
| Vulcanus | No | Foundry and big drill are required for endgame |
| Fulgora | No | EM plant and quality system are required |
| Gleba | No | Agricultural science is required for victory |
| Aquilo | Partially | Aquilo science is needed for fusion power, but you can delay it |

You cannot win Space Age without establishing science production on all four inner planets. The order above minimizes the friction of each visit by ensuring you always have the upgrade from the previous planet.

{{< /section >}}

{{< section "Community Verification" >}}

- [Factorio Wiki: Planet order](https://wiki.factorio.com/Planetary_science) -- Planet-by-planet science requirements
- [Reddit: Best planet order discussion (Space Age)](https://www.reddit.com/r/factorio/comments/1gb28mp/what_is_the_best_planet_to_first_go_to/) -- Player experiences and alternative orders
- [Factorio FFF: Space Age planet design](https://factorio.com/blog/post/fff-419) -- Developer reasoning behind planet difficulty
