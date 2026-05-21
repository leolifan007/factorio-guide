---
title: "Gleba Survival Guide — Spoilage, Nutrients, and Science"
description: "Gleba guide for Factorio Space Age. Spoilage mechanics, nutrient production, bioflux loop, and the belt setup that prevents spoilage from stalling your base."
date: 2026-05-21
tags: ["space-age", "gleba"]
draft: false
emoji: "🌿"
---

Gleba is the only planet where your factory actively works against you. Belt buffers that help on Nauvis rot here. Chests filled with spare parts turn into chests of spoilage. Assemblers that back up kill their own inputs. The fix isn't better production — it's controlled destruction. If something isn't moving, destroy it.

{{< callout "tip" >}}
**TL;DR:** Every organic item on Gleba has a spoilage timer. Short belts (under 20 tiles), no buffer chests, circuit-controlled splitters that burn excess items before they rot. Bioflux → nutrients → bacteria → ore → science. Any backup kills your entire production chain.
{{< /callout >}}

## The Mechanics Behind This Bottleneck

Every organic item on Gleba (and items derived from them) spoils over time:

| Item | Spoilage timer | What it spoils into |
|:-----|:--------------:|:-------------------|
| Yumako fruit | 1 hour | Spoilage |
| Jellynut | 1 hour | Spoilage |
| Bioflux | 30 min | Spoilage |
| Nutrients | 5 min | Spoilage |
| Bacteria | 2 min | Spoilage (no, you can't stop this) |
| Science packs | 1 hour | Spoilage |

The key insight: **nutrients** are the bottleneck. Nutrients spoil in 5 minutes. Every assembler that needs nutrients must be within belt distance of the nutrient source. If nutrients travel more than ~20 tiles on a yellow belt before reaching an assembler, they expire en route.

## The Proven Fix — Short Belts, Circuit Control, Burn Everything

**Stage 1 — Nutrient production, local to every consumer.**

Don't build a central nutrient factory and belt it everywhere. Each production cluster needs its own nutrient source:

- **Near fruit processing:** nutrients from bioflux (lasts 30 min, more stable)
- **Near bacteria vats:** nutrients directly from spoilage (1 nutrient per spoilage, fast but short lifespan)
- **Near science:** nutrients fed directly from a local bioflux producer

Distance rule: **keep any belt carrying nutrients under 15 tiles.** After that, use a separate nutrient maker.

{{< diagram "diagrams/gleba-nutrient-grid.svg" "Gleba nutrient production zones — local bioflux-to-nutrient assemblies within 15 tiles of each consumer cluster" "760" >}}

**Stage 2 — Bioflux the backbone.**

Bioflux (from yumako + jellynut mash) has a 30-minute timer — your most stable intermediate. Build bioflux production in bulk and let it supplement nutrients locally.

Each bioflux → 10 nutrients. 10 nutrients run one bacteria vat for roughly 2 minutes. Keep a bioflux chest buffer near each consumer cluster and convert on-demand.

**Stage 3 — Burn what you can't use.**

Circuit-controlled splitters are mandatory on Gleba. Set each output splitter to:

- Enable if item < threshold (e.g., iron bacteria < 500)
- If disabled: route to a heating tower for destruction

Without this, any production line that backs up (say you have enough iron) will let bacteria spoil on the belt, filling everything with spoilage.

{{< callout type="info" >}}
**Quick Tip:** Spoilage is useful. It feeds nutrient production (1 spoilage → 1 nutrient in a biochamber). It feeds heating towers for power. It makes fertilizer for more fruit production. The only "bad" spoilage is spoilage sitting on a belt blocking production. If it can't be used: heating tower.
{{< /callout >}}

## The Production Chain — What Goes Where

**Yumako → Yumako mash → Bioflux:**
- 1 yumako → 3 mash (in biochamber)
- 1 mash + 1 jellynut mash → 1 bioflux
- Bioflux preserved: 30 minutes

**Bioflux → Nutrients:**
- 1 bioflux → 10 nutrients (in biochamber)
- Nutrients preserved: 5 minutes
- Feed this to bacteria vats directly — minimal belt travel

**Bacteria → Ore:**
- Nutrients + bioflux + water → iron/copper bacteria
- Bacteria spoil: 2 minutes
- Bacteria in assembler → iron/copper ore
- Ore does NOT spoil (thank goodness)

**Fruit → Seeds → More fruit:**
- Processing fruit has a 50% chance of returning seeds
- Seeds let you plant more trees
- Without seeds, your fruit inputs eventually run out
- Burn excess yumako/jellynut that would rot to avoid stalling

{{< callout type="warning" >}}
**Traps People Keep Falling Into:** Don't belt fruit directly to your base. Process fruit into mash inside the farm area. Raw fruit spoils in 1 hour and fills belt space. Mash spoils in 30 minutes — still not great, but you can at least process it into bioflux (30 min) which is workable.
{{< /callout >}}

## Power — Heating Towers and Spoilage

Gleba's power comes from burning things. Heating towers burn any fuel at 250% efficiency. Spoilage burns. Seeds burn. Excess fruit burns.

**Power targets:**
- Early base: 5 heating towers, fed by excess spoilage
- Mid base: 10 towers, supplemented by rocket fuel from jellynut processing
- Late base: 20 towers, grid-tied across the base

**The fuel priority chain:**
1. First priority: active production (nutrients, bioflux to assemblers)
2. Second priority: spoilage → heating towers
3. Third priority: excess seeds → heating towers
4. Last resort: dedicated yumako/jellynut planting for fuel

Note: Heating towers produce 250% of the heat value vs. normal burners. A heating tower with rocket fuel produces ~40 MW. Run the math before building large solar fields — Gleba's swamp/marsh reduces solar to ~20% of Nauvis output.

## Where Most Players Mess This Up

**Everything on one belt.** A single belt carrying fruit, nutrients, and bioflux to different consumers creates a spoilage logjam the moment any consumer stalls. Separate belts per product type.

**No spoilage overflow.** The heating tower needs a circuit condition: if spoilage on the return belt > 100, burn to prevent belt clog. Without this, spoilage silently accumulates and eventually jams your nutrient production.

**One-direction waste.** In a designed system, every belt eventually terminates at a heating tower or a recycler. No belt dead-ends on Gleba. If a belt has no consumer, objects on it rot and block everything.

---

## Community Verification & Resources

- [Official Wiki — Gleba](https://wiki.factorio.com/Gleba) — spoilage timers, nutrient production rates, and biochamber mechanics
- [Factorio Forums — Space Age Discussion](https://forums.factorio.com/viewforum.php?f=69) — community feedback on optimal Gleba routes and common pitfalls
- [Steam Guide — Gleba First Hour](https://steamcommunity.com/sharedfiles/filedetails/?id=3278846547) — tested starting guide for the Gleba landing
- [Alt-F4 Blog — Gleba Deep Dive](https://alt-f4.blog/) — engineering analysis of spoilage mechanics and belt throughput
