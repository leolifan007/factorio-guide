---
title: "Gleba Bioflux Production — Fruit Ratio, Nutrients Loop, and Spoilage Control"
description: "Gleba bioflux production guide for Factorio Space Age. Yumako/jellynut processing ratios, nutrient loops, spoilage timing, and full bioflux automation."
date: 2026-06-20
tags: ["space-age", "gleba", "production"]
draft: false
emoji: "🌿"
aliases:
  - /space-age/gleba-bioflux-production/
---

Bioflux is the single most important intermediate on Gleba. It feeds nutrients, which feed bacteria, which produce your iron and copper ore. Without steady bioflux, your Gleba base starves. The challenge: yumako and jellynut have a 1-hour spoilage timer, nutrients spoil in 5 minutes, and any backup in the chain defaults everything to spoilage. Here's the ratio and loop design that keeps bioflux flowing. For a complete Gleba walkthrough, see {{< ref "/space-age/gleba/gleba-survival-guide" >}}.

{{< callout "tip" >}}
**TL;DR:** Process fruit into mash immediately at the farm. The correct ratio: 1 yumako → 3 mash, 1 jelly → 5 jelly. Combine 1 mash + 1 jellynut jelly = 2 bioflux. Each bioflux makes 10 nutrients. Keep nutrient belts under 15 tiles. Circuit-control every output to burn excess before it spoils.
{{< /callout >}}

## Yumako vs Jellynut — What Each Fruit Produces

Fruit on Gleba isn't interchangeable. Each type produces a different intermediate needed for the bioflux chain:

| Fruit | Processing Output | Amount | Spoilage Timer | Primary Use |
|:------|:-----------------:|:------:|:--------------:|:-----------|
| {{< material "yumako" >}} Yumako | Yumako mash | 3 per fruit | 30 min | Bioflux base, nutrients |
| {{< material "jellynut" >}} Jellynut | Jellynut jelly | 5 per fruit | 30 min | Bioflux catalyst, fuel |
| — | Spoilage | 0-1 per fruit | — | Nutrient alternative, fuel |

**The key ratios in a biochamber:**

| Recipe | Input A | Input B | Output | Biochambers for 60 SPM |
|:-------|:-------:|:-------:|:------:|:----------------------:|
| Yumako mash | 1 yumako | — | 3 mash | 12 |
| Jellynut jelly | 1 jellynut | — | 5 jelly | 8 |
| Bioflux | 1 mash | 1 jelly | 2 bioflux | 6 |
| Nutrients (from bioflux) | 1 bioflux | — | 10 nutrients | 4 |
| Nutrients (from spoilage) | 1 spoilage | — | 1 nutrient | 12 |

{{< callout type="info" >}}
**Quick Tip:** Jellynut is more efficient than yumako for bulk processing. One jellynut produces 5 jelly, while one yumako produces 3 mash. The bioflux recipe needs 1:1 mash-to-jelly, meaning you need roughly 1.7 yumako trees for every 1 jellynut tree. Adjust your planting accordingly.
{{< /callout >}}

## The Mash → Jelly → Bioflux Chain

The full production chain from fruit to science:

```
┌────────────────────────────────────────────────────────┐
│                    FRUIT FARMS                          │
│  Yumako groves ──→ Agricultural towers                 │
│  Jellynut groves ──→ Agricultural towers                │
└────────────────────┬───────────────────────────────────┘
                     ↓
┌────────────────────┴───────────────────────────────────┐
│               FRUIT PROCESSING (local)                  │
│  Yumako ──→ Biochamber ──→ Yumako mash (3 per fruit)   │
│  Jellynut ──→ Biochamber ──→ Jellynut jelly (5 per)    │
└────────────────────┬───────────────────────────────────┘
                     ↓
┌────────────────────┴───────────────────────────────────┐
│                BIOFLUX MANUFACTURING                    │
│  1 mash + 1 jelly → Biochamber → 2 bioflux             │
│  Bioflux spoils in 30 minutes — stable intermediate     │
└────────────────────┬───────────────────────────────────┘
                     ↓
┌────────────────────┴───────────────────────────────────┐
│          NUTRIENT & BACTERIA PRODUCTION                 │
│  Bioflux → Biochamber → 10 nutrients (5 min spoilage)  │
│  Nutrients + bioflux + water → Bacteria vat → Ore      │
│  Ore does NOT spoil ✓                                   │
└────────────────────┬───────────────────────────────────┘
                     ↓
┌────────────────────┴───────────────────────────────────┐
│                   SCIENCE                               │
│  Agricultural science = bioflux + biter eggs + ore      │
└────────────────────────────────────────────────────────┘
```

**The math for a continuous 60 SPM base:**

| Required | Quantity | Notes |
|:---------|:--------:|:------|
| Yumako fruit per minute | ~120 | From ~6 yumako trees with speed modules |
| Jellynut per minute | ~70 | From ~4 jellynut trees |
| Biochambers making mash | 12 | Each handles 10 fruit/min with speed modules |
| Biochambers making jelly | 8 | Each handles ~9 fruit/min |
| Biochambers making bioflux | 6 | Each produces ~20 bioflux/min |
| Bioflux per minute | 120 | Core throughput measure |
| Nutrients per minute | 600 | From 60 bioflux/min (half for bacteria, half for science) |

{{< diagram "diagrams/space-age/bioflux-chain.svg" "Gleba bioflux production chain from fruit to science" "760" >}}

## Nutrient Loop Design — Don't Let It Stall

Nutrients spoil in **5 minutes**. That's the tightest constraint in the entire Gleba chain. Here's the loop design that prevents stalling:

### The Local Nutrient Rule

**Never belt nutrients more than 15 tiles.** Build a nutrient maker (biochamber converting bioflux → nutrients) within 15 tiles of each consumer cluster:

- **Bacteria vat cluster:** Dedicated nutrient maker, direct inserter from bioflux chest → nutrient maker → bacteria vat. Belt only if absolutely necessary (and keep under 10 tiles).
- **Science cluster:** Separate nutrient maker fed by an independent bioflux supply. If science backs up, nutrients spoil — which is fine because spoilage feeds the heating tower.
- **Fruit processing:** These biochambers can self-feed on the fruit they process (nutrients from yumako mash directly). No external nutrient belt needed.

### The Spoilage Belt

Every nutrient consumer outputs spoilage. Route spoilage on a dedicated belt back to a central collection point:

1. Spoilage belt runs past every biochamber
2. Each biochamber outputs spoilage via a filtered inserter
3. Central spoilage collector feeds:
   - Heating towers for power (priority 1)
   - Nutrient production from spoilage (1:1 ratio, emergency only)
   - Fertilizer production for fruit farms

{{< callout type="info" >}}
**Quick Tip:** Use a circuit-controlled splitter on the nutrient belt. Read the belt contents. If nutrients exceed 50 on the belt segment, route excess through a recycler or to a heating tower. This prevents nutrient spoilage from blocking new nutrient production.
{{< /callout >}}

## Spoilage Timing Mechanics and Circuit-Controlled Flushing

### The Spoilage Timer

Each Gleba organic item has a built-in spoilage timer measured in seconds:

| Item | Base Timer | Effective Working Time |
|:-----|:----------:|:---------------------:|
| {{< material "yumako" >}} Yumako fruit | 3,600 s (1 h) | ~50 min on belt + processing time |
| {{< material "jellynut" >}} Jellynut | 3,600 s (1 h) | ~50 min on belt |
| {{< material "bioflux" >}} Bioflux | 1,800 s (30 min) | ~25 min usable |
| {{< material "nutrients" >}} Nutrients | 300 s (5 min) | ~4 min usable before quality drops |
| {{< material "spoilage" >}} Spoilage | — | Indefinite (the final form) |
| {{< material "biter_egg" >}} Biter eggs | 3,600 s (1 h) | Spoiled eggs hatch into biters! |
| Agricultural science | 3,600 s (1 h) | Must reach lab before expiry |

**Breaking the spoilage problem:**

1. **Process fruit at the farm.** Build biochambers processing yumako and jellynut directly next to the agricultural towers. Belt mash (30 min) instead of fruit (60 min) — you've already doubled your window.
2. **Turn mash into bioflux immediately.** Bioflux also lasts 30 minutes, but 1 bioflux = 10 nutrients vs 1 mash = a fraction of a nutrient. You're compressing value.
3. **Convert bioflux → nutrients on-demand.** Use circuit control: only make nutrients when bacteria vats need them. A chest buffer of 50 bioflux gives you 500 nutrients worth of emergency reserve.

### Circuit-Controlled Flushing

The circuit system on Gleba isn't optional — it's mandatory. Here's the control logic:

**Per-production-line controller:**
```
[Decider combinator]
Input: Read belt contents (item count)
Condition: IF [item] > [threshold] → Output [item] = 1

[Filter inserter at end of belt]
Enable: IF [item] = 1 → Route to heating tower line
```

Set thresholds conservatively:
- Mash: threshold 200 (higher = more buffer, higher = more spoilage risk)
- Jelly: threshold 150
- Bioflux chest: threshold 100
- Nutrients on belt: threshold 50
- Bacteria on belt: threshold 30 (2-minute spoilage — flush aggressively)

Your [Quality Module Guide]({{< ref "/space-age/quality/quality-module-guide" >}}) covers the combinator patterns for item counting on belts.

## Bioflux → Biter Egg → Science Pipeline

Agricultural science requires bioflux, biter eggs, and ore:

```
Bioflux + Nutrients → Biter egg incubator → Biter eggs (1 h spoil)
Bioflux + Biter eggs + Ore → Agricultural science (1 h spoil)
                                        ↓
                               Biolabs on Nauvis (or Gleba)
```

The biter egg pipeline is the most dangerous because **spoiled biter eggs hatch into live biters**. If your bioflux supply stutters and eggs spoil inside your base, you get a breach:

1. **Keep biter egg production isolated.** Wall off the egg incubators with a 2-tile gap. Pave the floor with concrete. Turrets on the perimeter.
2. **Auto-flush spoiled eggs.** Any egg that hits 10% spoilage time remaining gets routed to a heating tower via circuit-controlled inserter.
3. **Buffer bioflux for eggs.** Always keep 30+ bioflux in a chest next to the egg incubator. If the main bioflux belt stops, the inserter feeds from the buffer while you fix the upstream problem.

{{< callout "tip" >}}
**TL;DR for Biter Eggs:** Keep a dedicated bioflux buffer chest next to every egg incubator cluster. If bioflux stops, eggs spoil and hatch. Don't let this happen — it's the #1 Gleba base killer.
{{< /callout >}}

## Defense Considerations

Pentapods attack your Gleba base — particularly your fruit farms. A single agricultural tower making noise attracts them. Common pitfall: focusing so much on bioflux ratios that you forget to wall off the perimeter.

Our [Pentapod Defense Guide]({{< ref "/space-age/gleba/pentapod-defense" >}}) covers the turret layout and patrol patterns. The short version: rocket turrets with explosive rockets are the most efficient pentapod killer. Tesla towers also work well against the medium stompers. Land mines are surprisingly effective against small pentapods.

## Common Failure Modes

**Fruit processed too far from farms.** Belt raw yumako across half your base → half of it spoils before processing. Result: -50% throughput, constant shortages. Fix: process fruit inside the farm area.

**One central bioflux maker.** When the belt breaks (and it will, because Gleba belts break), all nutrient production stops. Fix: 2-3 distributed bioflux makers, each feeding their local nutrient cluster.

**No emergency nutrient path.** The bioflux → nutrient path breaks. Bacteria vats starve. Iron and copper stop. Everything cascades. Fix: build a spoilage → nutrient biochamber as a backup. Wire it to activate via circuit when main nutrient supply drops below 10.

**Belting nutrients through the main base.** 50-tile nutrient belt = 95% spoilage before reaching the end. Fix: local nutrient production only, max 15 tiles.

---

## Community Verification & Resources

- [Official Wiki — Bioflux](https://wiki.factorio.com/Bioflux) — exact processing ratios, spoilage times, and biochamber mechanics
- [Factorio Forums — Gleba Science](https://forums.factorio.com/viewforum.php?f=69) — community bioflux layouts and circuit designs
- [Steam Guide — Gleba First Hour](https://steamcommunity.com/sharedfiles/filedetails/?id=3278846547) — tested starting guide for the Gleba landing
- [Alt-F4 Blog — Gleba Spoilage Mechanics](https://alt-f4.blog/) — deep analysis of spoilage timers and production chain optimization
