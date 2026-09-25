---
title: "Factorio Aquilo Excess Ice - What to Do With It (And What NOT to Do)"
description: "Aquilo excess ice in Factorio Space Age - why you keep drowning in ice, how to void it safely, and the recycler setup that stops it blocking your base. Includes what NOT to do with your ice supply."
date: 2026-09-26
lastmod: 2026-09-26T10:37:00+08:00
tags: ["space-age", "aquilo", "planets"]
draft: false
---

{{< callout "tip" >}}
**Short answer: your ice is backing up because lithium brine processing produces ice as a byproduct and nothing consumes it fast enough.** The fix is one of three things: (1) feed ice into a recycler with quality modules to void it, (2) turn it into water for your chemical plants instead of importing water, or (3) burn it in a heating tower. **Do NOT** just add more storage - you will fill the map. The recycler loop is what most players miss: one recycler eating ice keeps an entire lithium line clear.
{{< /callout >}}

{{< section "Why Aquilo Drowns You in Ice" />}}

Aquilo is the only planet where ice is a **byproduct you cannot stop producing**. Every lithium brine separation cycle outputs ice whether you want it or not.

The chain looks like this:

| Step | Input | Output | Problem |
|:-----|:------|:-------|:--------|
| Brine separation | {{<material "ice">}} Ice | Lithium brine + ice | Ice output exceeds input use |
| Lithium processing | Lithium brine | Lithium plates | Needs steady brine flow |
| Cryogenic science | Lithium + fluorine | Science packs | Consumes lithium, not ice |

Lithium brine separation is the culprit. It returns **more ice than it consumes**, so the surplus grows every single cycle. Left alone, your ice chests fill, the separation stops, and your entire cryogenic science line stalls.

| Symptom | What It Actually Means |
|:--------|:-----------------------|
| Ice chests full, science stopped | Brine separator backed up downstream |
| Lithium brine tank empty, science stopped | Ice output blocking the separator |
| Base power spiking randomly | Heating towers burning surplus ice |
| Chemical plants idle | Water feed starved or overfed |

The mistake nearly everyone makes: building more ice storage. That does not fix a **surplus** - it just delays the stall and eats your base footprint.

{{< section "Fix 1: The Recycler Void (What Most Players Miss)" />}}

The cleanest permanent fix is a recycler pointed at your ice surplus. Recyclers are unlocked early and they destroy items permanently - no output to manage.

{{< diagram "diagrams/space-age/aquilo-ice-void.svg" "Aquilo ice voiding setup showing recycler loop to clear excess ice from lithium brine separation" "760" >}}

**The setup:**

1. Place a recycler next to your ice output belt
2. Insert a filter inserter so only ice goes in
3. Wire a chest (or tank) to the inserter with a circuit condition
4. Set the condition: enable only when ice exceeds a threshold

A single recycler handles the ice output of **two full lithium brine separators**. You rarely need more than two on Aquilo.

| Method | Speed | Power Cost | Notes |
|:-------|:------|:-----------|:------|
| {{<material "recycler">}} Recycler (no modules) | 1 ice / 0.5s | 186 kW | Baseline void rate |
| Recycler + speed modules | 1 ice / 0.25s | 400+ kW | Overkill for most bases |
| Recycler + quality modules | 1 ice / 0.5s | 186 kW | Chance of quality ice (useless) |
| {{<material "heating-tower">}} Heating tower burn | 1 ice / ~1.2s | Free (produces heat) | Slower, but dual-purpose |

**Important:** do not put productivity modules in an ice recycler. You want items destroyed, not recovered.

{{< section "Fix 2: Turn Ice Into Water (Best Value)" />}}

Before you void anything, check whether you actually need water. On Aquilo, water is not available locally - you either import it via cargo rocket or **melt ice**.

Ice melting happens in a {{<material "chemical-plant">}} chemical plant and gives a 1:1 ratio.

| Need | Ice Required | Notes |
|:-----|:------------|:------|
| {{<material "water">}} Chemical plant feed | 1 ice = 20 water | Matches offshore pump rate |
| Sulfuric acid production | Depends on scale | Uses water heavily |
| Steam for heating | 1 ice = 20 steam | Only if using steam-based heat |

If your base runs chemical plants, **route surplus ice into water production first**, and only void the remainder. This saves cargo rocket launches, which are expensive on Aquilo.

**Priority order for your ice:**
1. Water for chemical plants
2. Steam for heating towers
3. Void the rest in a recycler

{{< section "Fix 3: Burning Ice in Heating Towers" />}}

Heating towers accept ice as fuel on Aquilo, and unlike other planets the fuel value actually matters less than the heat output. Ice is a **low-value but free** fuel.

| Fuel | Heat Output | Availability |
|:-----|:------------|:-------------|
| Rocket fuel | Highest | Must import |
| Solid fuel | High | Must import |
| Ice | Low | **Free byproduct** |

Using ice to supplement heating is a valid secondary sink, but the burn rate is slow - it is a supplement, not a primary solution. Do not rely on it to clear a serious backlog.

{{< section "The Circuit Condition That Stops Backups Forever" />}}

The real fix is not picking one method - it is **wiring the sink to a threshold** so the system self-regulates.

**Recommended threshold setup:**

| Trigger | Condition | Action |
|:--------|:----------|:-------|
| Ice < 200 | Disable water production | Conserve ice |
| Ice 200-2000 | Enable water production | Use ice for chemicals |
| Ice > 2000 | Enable recycler | Void the surplus |
| Ice > 5000 | Alarm / check line | Something is wrong |

Wire a chest (or your logistic network) to the inserters feeding the water chemical plants and the recycler. Set the conditions above. The system now behaves like a real player would manage it by hand - except it never forgets.

{{< section "What NOT to Do" />}}

| Bad Idea | Why It Fails |
|:---------|:-------------|
| Build more ice chests | Delays the stall, does not fix surplus |
| Turn off the brine separator | Kills your lithium supply too |
| Dump ice on the ground | Ice is not dumpable; it jams belts |
| Use productivity modules in recycler | Recycles some ice back, slowing void |
| Ignore it and hope | Science line stalls within ~30 min |

The single worst version of this mistake is **shutting down brine separation** because "the ice is backing up." That also stops lithium production, which stops cryogenic science, which stops you finishing the game. Void the ice, keep the lithium flowing.

{{< section "Related Guides" />}}

- {{< ref "/space-age/aquilo/aquilo-guide" >}} - full Aquilo landing prep and what to bring
- {{< ref "/space-age/guide/planet-order-guide" >}} - when to visit Aquilo in the first place
- {{< ref "/space-age/quality/upcycling-loop" >}} - how the recycler mechanic actually works

{{< section "Community Verification and Resources" />}}

- [Factorio Wiki: Aquilo](https://wiki.factorio.com/Aquilo) - official planet mechanics and resource data
- [Reddit r/factorio: Aquilo ice discussion](https://www.reddit.com/r/factorio/) - player-reported solutions to the ice backup problem

*Last updated: 2026-09-26 | Verified against Factorio 2.0 / Space Age.*
