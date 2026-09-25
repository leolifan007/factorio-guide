---
title: "Factorio Gleba Spoilage Backup - How to Clear It Without Restarting"
description: "Gleba spoilage backup in Factorio Space Age - why your belts jam, the fastest way to clear an existing backlog, and the circuit fix that stops it coming back. Includes the nutrient-starve trap that makes it worse."
date: 2026-09-27
lastmod: 2026-09-27T14:23:00+08:00
tags: ["space-age", "gleba", "planets"]
draft: false
---

{{< callout "tip" >}}
**Short answer: your Gleba base is jammed because spoilage has nowhere to go and it is blocking the belt that feeds your nutrient production.** Clear it by inserting spoilage into a **heating tower** or **recycler** - never by manually deleting belts. Then stop it recurring by making spoilage a **filtered, dedicated output lane** rather than a byproduct mixed into your main bus. The trap: players cut nutrient production to "stop the spoilage," which kills the farms, which makes everything spoil faster. Keep nutrients flowing.
{{< /callout >}}

{{< section "Why Gleba Backs Up (And Why It Snowballs)" />}}

Every organic item on Gleba spoils on a timer. Spoilage itself does not spoil, so it **accumulates forever** unless something consumes or destroys it.

The snowball works like this:

| Step | What Happens | Result |
|:-----|:-------------|:-------|
| 1 | Fruit sits too long on the belt | Becomes spoilage |
| 2 | Spoilage has no output lane | Fills the belt |
| 3 | Belt jams | Fruit cannot reach the assembler |
| 4 | You cut nutrient production to stop it | Farms idle |
| 5 | Idle farms = more spoilage | **Jams harder** |

Step 4 is the fatal mistake. Cutting nutrients feels like it should slow spoilage, but nutrients are what keep the farms and the whole chain moving. Starve them and the entire base composts.

| Symptom | Actual Cause |
|:--------|:-------------|
| Belts full of spoilage, farms stopped | No spoilage sink |
| Nutrients keep running out | Spoilage blocking nutrient input |
| Science pack output at zero | Bioflux line jammed upstream |
| Base works, then dies every 10 min | Buffers too long, spoilage cycles |

{{< section "How to Clear an Existing Backlog (Fast)" />}}

Do not manually delete belt sections. That works for twelve seconds and then refills. You need a **sink** that runs continuously.

{{< diagram "diagrams/space-age/gleba-spoilage-sink.svg" "Gleba spoilage sink setup showing recycler and heating tower clearing jammed belts with filtered inserters" "760" >}}

**Three sinks, in order of preference:**

| Sink | Speed | Power | Best For |
|:-----|:------|:------|:---------|
| {{<material "recycler">}} Recycler | 1 item / 0.5s | 186 kW | Permanent solution, any scale |
| {{<material "heating-tower">}} Heating tower | Moderate | Produces heat | Dual purpose on cold builds |
| Burner / incinerator mod | Varies | Varies | Not vanilla - avoid |

**The fastest way to clear an existing jam:**

1. Place a recycler next to the jammed belt
2. Use a **filter inserter** set to spoilage only
3. Set the inserter condition to "spoilage > 0" so it never stops
4. Let it run - a single recycler eats a full belt of spoilage in a few minutes

If the jam is severe, drop **two recyclers** temporarily, clear it, then remove the second one.

{{< section "Why Spoilage Needs Its Own Lane" />}}

The root cause of recurring jams is that spoilage shares a belt with usable items. When the shared belt fills with spoilage, production stops.

| Design | Outcome |
|:-------|:--------|
| Spoilage mixed into main belt | Jams constantly - **this is the bug** |
| Spoilage on dedicated filtered lane | Self-clearing |
| Spoilage with priority splitter output | Self-clearing, better throughput |

**The fix:** use a splitter with a **filter set to spoilage** on every belt that carries organic items. Route the filtered spoilage output to your recycler. The main line stays clean.

This is the single change that converts a base that jams hourly into one that runs unattended.

{{< section "The Circuit That Stops It Coming Back" />}}

Once spoilage has a dedicated lane, wire the sink to a threshold so it self-regulates.

| Condition | Action |
|:----------|:-------|
| Spoilage > 100 | Run recycler continuously |
| Spoilage < 100 | Pause recycler to save power |
| Spoilage > 1000 | Something upstream is wrong - investigate |
| Nutrients = 0 | Alarm - this is the failure state |

Wire a chest or your logistic network to the inserter feeding the recycler. Enable on `spoilage > 100`.

**Do not** gate the recycler on `spoilage > 5000`. By then your belts are already jammed. Keep the threshold low so it clears continuously.

{{< section "The Nutrient Trap (Most Common Mistake)" />}}

When a base jams, the instinct is to reduce nutrient output because "nutrients cause spoilage." This is backwards.

| Action | Short-Term | Long-Term |
|:-------|:-----------|:----------|
| Cut nutrient production | Jams slow briefly | Farms idle, more spoilage |
| **Keep nutrients flowing** | Spoilage cleared by sink | Base stabilises |
| Add more nutrient buffers | Slight relief | Longer belts, more spoilage |

Nutrients are what drive fruit processing. **Fruit sitting on a belt spoils; fruit being processed does not.** Keep the chain moving and the spoilage problem is a throughput problem, which the recycler solves.

{{< section "Common Mistakes" />}}

| Mistake | Why It Fails |
|:--------|:-------------|
| Deleting belt sections by hand | Refills within minutes |
| Cutting nutrients | Kills farms, worsens spoilage |
| Building bigger spoilage chests | Fills, then jams anyway |
| Long belts with buffers | Every buffer is a spoilage factory |
| Ignoring it until science stops | By then the jam is deep |

The golden rule from the Gleba survival guide applies here: **short belts, no buffer chests**. Spoilage backup is usually a symptom of belts that are too long.

{{< section "Related Guides" />}}

- {{< ref "/space-age/gleba/gleba-survival-guide" >}} - core spoilage and nutrient mechanics
- {{< ref "/space-age/gleba/bioflux-production" >}} - the bioflux chain that feeds this system
- {{< ref "/space-age/aquilo/excess-ice" >}} - the same "surplus byproduct" problem on Aquilo

{{< section "Community Verification and Resources" />}}

- [Factorio Wiki: Spoilage](https://wiki.factorio.com/Spoilage) - official spoilage timer and conversion data
- [Reddit r/factorio: Gleba spoilage clogging belts](https://www.reddit.com/r/factorio/) - player-reported fixes for the recurring jam

*Last updated: 2026-09-27 | Verified against Factorio 2.0 / Space Age.*
