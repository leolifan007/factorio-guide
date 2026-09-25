---
title: "How to Use Blueprints - Complete Guide"
description: "How to copy, import, export, and organize blueprints in Factorio 2.0. Blueprint string tutorial, blueprint book naming, upgrade planner, and the parameter system that saves hours of rebuilding."
date: 2026-05-18
lastmod: 2026-09-26T16:32:00+08:00
tags: ["blueprints", "tutorial", "beginner"]
draft: false
---

{{< callout "tip" >}}
**Short answer:** press **G** to grab the blueprint tool, drag a box over any build, and it lands in your inventory. To share it, select the blueprint and click **Export** - you get a string that anyone can paste with **Ctrl+V**. The three things beginners miss: (1) **Shift + scroll** rotates and mirrors a held blueprint, (2) the **Upgrade Planner** upgrades a whole base in one drag, (3) **blueprint parameters** let one book adapt to any recipe instead of making ten copies.
{{< /callout >}}

{{< section "What Blueprints Actually Do" />}}

A blueprint copies a design. A **blueprint book** stores many designs. Together they turn your factory from a hand-built thing into something you can reproduce anywhere.

| Tool | Shortcut | Purpose |
|:-----|:---------|:--------|
| Blueprint | **G** | Copy a design |
| Blueprint book | In inventory | Organise many blueprints |
| Upgrade planner | In inventory | Swap buildings across an area |
| Deconstruction planner | In inventory | Mark things for removal |

{{< section "Copy a Design" />}}

1. Press **G** (blueprint tool)
2. Drag a rectangle around the area you want to copy
3. The blueprint appears on your cursor - click your inventory to store it

{{< diagram "diagrams/space-age/blueprint-workflow.svg" "Factorio blueprint workflow showing copy, save to book, and paste steps with keyboard shortcuts" "760" >}}

| Action | How |
|:-------|:----|
| Copy a build | G, drag box |
| Rotate held blueprint | R |
| Mirror held blueprint | Shift + scroll |
| Place (no tiles) | Shift + click |
| Cancel | Q |

**Shift + click places the blueprint without its floor tiles** (concrete, stone brick). This is the fastest way to reuse a design on a different surface.

{{< section "Save to a Blueprint Book" />}}

1. Open your inventory
2. Click the blueprint
3. Click **Save** and choose a **blueprint book**
4. Give it a clear name

{{< callout "info" >}}
**Naming convention:** use `[Category] Description`, for example `[Smelting] Iron 12x Furnace`. Future you will thank present you.
{{< /callout >}}

{{< section "Import and Export Strings" />}}

Blueprint strings are how designs travel between players and from websites.

| Task | Steps |
|:-----|:------|
| **Import** | Copy the string, press **Ctrl+V** with the blueprint tool active |
| **Export** | Select blueprint, click the **export** button top-right, **Ctrl+C** |

{{< diagram "diagrams/space-age/blueprint-string-flow.svg" "Blueprint string import and export flow showing where strings come from and how to share them" "760" >}}

| String Source | Reliability |
|:--------------|:------------|
| Factorio Prints / community sites | Good - check version |
| A friend in-game | Perfect |
| Old forum posts | Risky - may predate 2.0 |
| Random screenshots | **Not a string** - cannot import |

Strings encode the whole design including modules and circuit settings. An old string may reference items that no longer exist in 2.0 - if import fails, that is usually why.

{{< section "Organising a Blueprint Book" />}}

A good book structure saves hours of searching later.

| Book | Contents |
|:-----|:---------|
| Production | Smelting, circuits, science packs |
| Defense | Walls, turrets, artillery outposts |
| Trains | Stations, loaders, unloaders |
| Modules | Beaconed builds, speed/prod setups |
| Circuit networks | Combinators, smart stations - see the [circuit network guide]({{< ref "/blueprints/circuit-network-guide" >}}) |
| Mall | Inserters, belts, chests (self-building factory) |

Keep books **under 20 entries each**. A book with 80 blueprints is slower to use than no book at all.

{{< section "Blueprint Parameters (The Feature You Are Not Using)" />}}

Parameters let a single blueprint **ask you for a recipe** instead of hard-coding one.

| Without Parameters | With Parameters |
|:-------------------|:----------------|
| One blueprint per recipe | One blueprint, any recipe |
| 10 assembler builds for 10 items | 1 parameterised build |
| Editing means rebuilding | Set recipe on paste |

**How to set it up:**

1. Place an assembler with **no recipe** in your build
2. Create the blueprint
3. When you paste it, the game prompts you to pick the recipe
4. Save that as your parameterised blueprint

This is how megabase builders ship a single "generic assembler" design that works for every product.

{{< section "Upgrade Planner" />}}

The upgrade planner swaps every building in an area to a better tier in one drag.

| Upgrade Path | Common Use |
|:-------------|:-----------|
| Stone furnace -> Steel -> Electric | Smelting expansion |
| Basic belt -> Fast -> Express | Throughput boost |
| Assembler 1 -> 2 -> 3 | Crafting speed |
| Yellow inserter -> Stack inserter | Gleba unlock |

**Pro tip:** apply the upgrade planner *before* pasting a blueprint to bring it up to your current technology level in one step.

{{< section "Deconstruction Planner" />}}

Removes buildings in an area.

1. Select the deconstruction planner
2. Drag over the target area
3. Construction robots remove the buildings

{{< callout "warning" >}}
Deconstructing **destroys** the building - you do not get it back automatically unless a storage chest is in range of construction robots. Use **Shift + deconstruction planner** to filter which items are kept.
{{< /callout >}}

{{< section "Related Guides" />}}

- {{< ref "/blueprints/circuit-network-guide" >}} - wiring the circuits inside your blueprints
- {{< ref "/production-ratios/beacon-module-guide" >}} - the beaconed builds worth blue printing
- {{< ref "/trains-logistics/construction-robot-guide" >}} - robots that place your blueprints

{{< section "Community Verification and Resources" />}}

- [Factorio Wiki: Blueprint](https://wiki.factorio.com/Blueprint) - official blueprint and string format docs
- [Factorio Prints](https://factorioprints.com/) - community blueprint library

*Last updated: 2026-09-26 | Verified against Factorio 2.0.*
