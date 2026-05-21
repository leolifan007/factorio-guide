---
title: Gleba Survival Guide — How to Beat the Spoilage Planet
description: Complete Gleba guide for Factorio Space Age. Spoilage mechanics, pentapod defense, bioflux production chains, agri science ratios, and a build order that actually works.
date: 2026-05-19
tags: ["space-age", "gleba"]
draft: false
emoji: "🌿"
---

Gleba replaces static production with spoilage-based mechanics. Every organic item decays over time, belts must be kept short, and buffer chests destroy production instead of helping it. The core loop — nutrients feed bacteria, bacteria produce ore, science consumes it all — works reliably with tight belts and circuit-controlled splitters.

{{< callout "tip" >}}
**TL;DR:** Spoilage is the core mechanic on Gleba. Everything you build needs buffer-bounded belts, priority splitters for freshness, and pentapod-proof walls. Build a nutrient plus bacteria loop first, then layer in bioflux for science. Spoiled items recycle into nutrients, so nothing is ever completely wasted. Purple belts help move fresh items faster than spoilage can decay them.
{{< /callout >}}

{{< section "Understanding Spoilage — The Two-Minute Rule" >}}

Everything organic on Gleba has a spoilage timer. Yumako fruit, jelly, bioflux, nutrients, science packs — all of it decays into spoilage over time. Freshness is a percentage that ticks down continuously.

The spoilage rate is roughly 2 minutes from fresh to fully spoiled for most items. That means you cannot store large buffers. Traditional factory techniques like belt-based buffers and chest-based stockpiles kill your production here.

Spoiled items become spoilage. Spoilage has its own use: it processes into nutrients at a 2:1 ratio in a biochamber. So spoilage is not waste — it is a secondary resource. A Gleba base that wastes nothing can run entirely on recycled spoilage for nutrients.

I learned this lesson the hard way after my first base starved of nutrients because I did not build a spoilage collection system. Every belt needs a filtered splitter pulling out spoilage and routing it to the recycler line.

{{< diagram "diagrams/gleba-spoilage-flow.svg" "Spoilage cycle on Gleba showing freshness decay and recycling into nutrients" "700" >}}

The freshness indicator on each item is critical. A bioflux at 80% freshness produces 80% as many nutrients as a fresh one. Plan for freshness loss by overproducing at each step.

{{< section "Build Order — What to Do First" >}}

Landing on Gleba with nothing is survivable if you follow the right sequence. I crashed three bases before settling on this order.

**Phase 1: Power and survival.** Bring solar panels and accumulators from Nauvis. Gleba nights are short and solar works fine. Build a wall around your landing zone with at least two layers of stone wall. Pentapods arrive within minutes of your first farming operation.

**Phase 2: Yumako processing.** Find a yumako patch near your landing zone. Build a harvesting line: yumako trees into processing buildings making jelly and mash. Belt both outputs immediately to processing — do not let them sit on the belt.

**Phase 3: Nutrient loop.** Nutrients come from jelly or bioflux. Build a nutrient assembler fed by jelly. Nutrients feed your bacteria lines. Wire a circuit to the nutrient belt: if nutrients fall below 50, activate the assembler. Never let nutrients run out. This single circuit condition saved my third base from starvation.

**Phase 4: Bacteria and iron.** Nutrients plus bacteria culture equals iron bacteria. Iron bacteria grow into iron ore in a biochamber. This is your iron supply on Gleba. Same for copper bacteria. No mining drills required on this planet.

**Phase 5: Pentapod containment.** Once your base is running, pentapods will find you. Expand your wall outward aggressively. Clear nests within radar range daily. Spores from your farming attract them, and more farming means more spores.

{{< section "Ratio Math — Agri Science Production" >}}

Agri science is the end goal on Gleba. Here is the ratio that works for a steady supply:

| Building | Produces | Count |
|----------|----------|:-----:|
| Yumako harvester | Yumako fruit | 6 |
| Bioflux assembler | Bioflux | 2 |
| Nutrient assembler (biochamber) | Nutrients | 3 |
| Bacteria cultivator | Ore bacteria | 4 |
| Pentapod egg raiser | Eggs | 1 |
| Agri science assembler | Agri science | 8 |

Each science assembler eats bioflux and pentapod eggs at a specific rate. Two bioflux assemblers running at full speed keep 8 science assemblers fed. Four bacteria cultivators supply enough iron and copper ore for the bioflux chain and base expansion.

The critical number: 1 pentapod egg raiser produces enough eggs for roughly 4 science assemblers. Eggs also spoil in about 2 minutes. Do not stockpile them. Let them flow directly into science production.

{{< diagram "diagrams/gleba-science-ratio.svg" "Agri science ratio chain from yumako to science packs" "700" >}}

{{< callout "tip" >}}
If your science production backs up, your pentapod eggs will spoil. Spoiled eggs still feed into nutrient production, so it is not a total loss. But if you need more science, you need fresh eggs. Keep the egg raiser circuits active based on science consumption.
{{< /callout >}}

{{< section "Pentapod Defense — Do Not Skimp Here" >}}

Pentapods are worse than biters. They come in waves that increase in frequency and size. They damage walls directly. And they spawn from nests that regrow if not cleared completely.

**What works reliably:**
- Triple-layered stone walls at the perimeter with a repair wall behind
- Flamethrower turrets creating fire pools in front of the wall line
- Laser turrets one tile behind the wall for cleanup duty
- Active tank patrol every 30 minutes to clear nest expansions

**What does not work:**
- Single wall layer — pentapods chew through stone in seconds
- Gun turrets alone — not enough DPS against medium and large pentapods
- Walls without repair packs — bring construction bots with repair packs

The spore emission radius increases with your farm size. Each yumako plant adds to your spore footprint. Walls must extend beyond the spore radius or pentapods will path around them.

{{< callout "warning" >}}
Pentapod nests regrow from spores. Spores are produced by your farming operations. The more yumako you process, the more spores you emit, the more pentapods you attract. Build a wall around your entire base before scaling up production.
{{< /callout >}}

{{< section "Bioflux Production — The Central Loop" >}}

Bioflux is Gleba key resource. It feeds nutrients, biter eggs for science, and rocket fuel. The production chain is:

Yumako mash + jelly + nutrient = bioflux

A single bioflux assembler running at full speed produces about 2 bioflux per second. This is enough for:
- 4 agri science assemblers running at full speed
- A small rocket fuel plant for interplanetary launches back to Nauvis
- A backup nutrient line if your jelly supply line dips

{{< recipe name1="yumako_mash" qty1="4x" name2="jelly" qty2="4x" name3="nutrient" qty2="2x" result="bioflux" rqty="1x" >}}

Bioflux spoils slower than most Gleba items — about 10 minutes. This makes it safe to transport via rocket to other planets. Ship bioflux to Fulgora or Vulcanus for nutrient production on those planets, saving you from building the full Gleba production chain on every world.

{{< section "Common Mistakes" >}}

**Building a belt buffer.** Every item on the belt is ticking toward spoilage. Use short, direct belts between production steps. Do not loop long belts. Each belt segment adds transit time.

**Not using filtered splitters.** Spoilage must be actively removed from every belt. A filtered splitter at every production step output prevents spoilage buildup. Build one at each bioflux, nutrient, and science output.

**Ignoring pentapod expansion.** The nests grow back aggressively. Clear them within radar range every 30 minutes. A nest that sits for an hour spawns enough pentapods to overwhelm your defenses.

**Letting nutrients run out.** This single failure kills a Gleba base faster than anything. When nutrients stop, bacteria die. When bacteria die, iron stops. When iron stops, everything spirals. Keep a circuit-conditioned backup nutrient assembler at all times.

**Not using spoilage as a resource.** Spoilage is free nutrients. Collect it from a filtered splitter on every belt and feed it into a recycler. A well-designed Gleba base produces more nutrients from spoilage than from fresh ingredients.

{{< section "FAQ" >}}

**Q: Can I bring resources from Nauvis?**
A: Yes. Bring solar panels, accumulators, walls, and turrets from Nauvis on your first rocket. This saves hours of setup time. But cargo space is limited — prioritize walls and turrets.

**Q: What buildings are Gleba-specific?**
A: The biochamber is Gleba equivalent of an assembling machine. It processes organic ingredients faster than a normal assembler and has built-in productivity. Research it before building any large-scale production.

**Q: How do I deal with spoilage on belts?**
A: Use splitter filters to pull spoilage off every belt automatically. A filtered splitter at every production step output keeps your factory running on fresh ingredients. Spoilage goes to nutrient production.

**Q: Do I need purple belts on Gleba?**
A: Not strictly, but they help. Purple belts move items 50% faster than blue belts, which means less spoilage during transit. If you have them from Vulcanus, use them here.

{{< section "Related Guides" >}}

- [Master quality modules for interplanetary production]({{< ref "space-age/quality-module-guide" >}})
- [Build a space platform for interplanetary travel]({{< ref "space-age/space-platform-guide" >}})
- [Set up flamethrower defense for pentapods]({{< ref "defense/flamethrower-defense-guide" >}})
- [Use circuits to manage spoilage logistics]({{< ref "blueprints/circuit-network-guide" >}})
- [Process Fulgora scrap for EM Plant parts]({{< ref "space-age/fulgora-recycling-guide" >}})
