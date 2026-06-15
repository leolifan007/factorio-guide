---
title: "How to Use Blueprints in Factorio - Complete Guide"
description: "How to copy, import, export, and organize blueprints in Factorio. Includes blueprint string tutorial, blueprint library, and how to use community blueprints."
date: 2026-05-18
lastmod: 2026-06-15T13:42:00+08:00
tags: ["blueprints", "tutorial", "beginner"]
draft: false
---

You found a perfect smelting blueprint on Reddit. Twelve hours later you're still trying to paste it into your game and the belts look wrong. I wasted an entire evening on my first blueprint import because nobody told me how the upgrade planner works. Here's the 5-minute setup that actually works.

{{< callout "tip" >}}
**TL;DR:** Press G for blueprint tool. Drag to copy. Ctrl+V to paste from string. Save to blueprint book with format [Category] Description. Use upgrade planner (red arrow icon in inventory) to auto-upgrade buildings when pasting old blueprints.
{{< /callout >}}

## What Blueprints Actually Are

A blueprint is a copy of a factory section that you can save and reuse. It stores every building, belt, inserter, and wire -- but not the modules inside buildings or items in chests. After 200 hours I'd collected 50 blueprints across 8 books. Without organization, finding the right one took longer than building it from scratch.

Here's what you can blueprint:

| What works | What doesn't save |
|-----------|------------------|
| Belt paths and splitters | Modules inside assemblers |
| Building positions | Circuit network wire colors (just the connections) |
| Inserter positions and filters | Items in chests/trains |
| Train stop names | Train schedules |
| Wire connections | Tile entities like concrete |
| Tile (ghost) entities | Roboport logistics zones |

I learned the module thing the hard way when I pasted a beaconed smelting array and all 48 furnaces came with no modules. Now I use the upgrade planner trick (see below) to fix this.

## The Workflow I Actually Use

**Step 1 -- Copy.** Press G (blueprint tool). Drag over the area. The blueprint appears on your cursor. Place it in your inventory (default key Q to clear cursor).

**Step 2 -- Name it.** Right-click the blueprint in inventory. Name format I use: `[Smelting] Iron 12x Stone`. The category in brackets lets me sort alphabetically. Without this, you end up with "Blueprint" x30 and no way to find the right one.

**Step 3 -- Save to book.** Drag the blueprint onto a blueprint book. I organize books by category:

| Book name | Contents |
|:----------|:---------|
| Smelting | Stone/steel/electric furnace arrays, beaconed setups |
| Science | Each science pack tier as a tileable module |
| Defense | Wall sections, flame turret layouts, artillery outposts |
| Trains | Loading/unloading stations, stacker designs, intersections |
| Mall | Belt/inserter/assembler production (self-feeding) |

**Step 4 -- Import community blueprints.** Copy a blueprint string from the web. Select the blueprint tool (G). Press Ctrl+V. The blueprint appears in your inventory ready to use.

**Step 5 -- Export.** Right-click a blueprint in inventory, click the export button (top-right), Ctrl+C to copy the string. Paste it into a text file or share it.

{{< callout "warning" >}}
Blueprint strings are long -- like 2,000 characters long for a medium build. Don't try to remember them. I save mine to a dedicated blueprint folder in my projects. If you lose your blueprint library and don't have backups, you rebuild everything by hand.
{{< /callout >}}

## The Upgrade Planner -- Why I Use It Every Session

The upgrade planner sits in your inventory (looks like a red arrow icon). It auto-upgrades buildings inside a selected area:

| Before | After |
|:-------|:------|
| Stone furnace | Steel furnace or Electric furnace |
| Yellow belt | Red belt or Blue belt |
| Assembler 1 | Assembler 2 or Assembler 3 |
| Burner inserter | Normal inserter or Fast inserter |

My workflow when I find a blueprint designed for assembler 1s: paste the blueprint, then drag the upgrade planner over the whole area set to assembler 3. Every assembler upgrades at once. The same approach works for belts -- paste an old blueprint and upgrade belts in one click.

## The Deconstruction Planner -- Undo Without Pain

The deconstruction planner removes buildings. Select it in inventory (looks like a red X), drag over the area. Construction bots handle the removal. The mistake I made: I didn't know about the filter option.

Shift-right-click the deconstruction planner to set filters. I use this to remove only belts without touching buildings, or remove only power poles without affecting assemblers. Without filters, one drag deletes everything.

{{< callout type="info" >}}
**Quick Tip:** When you deconstruct a building, items go to storage chests. If you don't have a logistics network, dropped items stay on the ground and expire. Always deconstruct within roboport range. I lost 400 belts this way.
{{< /callout >}}

## What I Wish Someone Told Me

**Blueprint books are not folders.** You can nest books inside books. I organize mine as: Main Book > Planet-specific sub-books (Nauvis, Vulcanus, Fulgora). A single blueprint string can hold an entire book of blueprints.

**Copy from map view.** Press M to open the map and use the blueprint tool there. This lets you copy large sections without zooming in. I design megabase smelting arrays entirely in map view.

**Blueprints survive updates.** Blueprint strings from Factorio 1.1 work in 2.0 / Space Age. The format is backward compatible. Old belt-based blueprints paste as ghost entities that assemblers auto-fill.

---

## Community Verification & Resources

- [Official Factorio Wiki -- Blueprint System](https://wiki.factorio.com/Blueprint) -- blueprint syntax, upgrade planner filters, and deconstruction planner controls
- [Factorio Prints](https://factorioprints.com/) -- community blueprint library with 10,000+ designs sorted by category
- [Factorio Blueprint Library (Reddit)](https://www.reddit.com/r/factorio/) -- weekly blueprint sharing threads for beginners and megabase builders

**Related:** [Circuit Network Guide]({{< ref "/blueprints/circuit-network-guide" >}}) | [Your First Factory]({{< ref "/getting-started/your-first-factory" >}}) | [Main Bus Guide]({{< ref "/base-design/main-bus-guide" >}})
