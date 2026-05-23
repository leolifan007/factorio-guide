---
title: "Aquilo — The Frozen Planet Survival and Research Guide"
description: "Aquilo guide for Factorio Space Age. Ice power mechanics, heat management systems, lithium supply chains, cryogenic science packs, and the strategy that keeps your base alive on the coldest planet."
date: 2026-05-23
lastmod: 2026-05-23T17:55:00+08:00
publishDate: 2026-05-27T16:52:00+08:00
tags: ["space-age", "aquilo", "space-platform"]
draft: false
hidden: true
emoji: ""
version: "2.0"
---

Aquilo is where Factorio Space Age stops being a factory game and starts being a survival game. You land and your solar panels produce nothing. The temperature is below zero. Your steam engines are frozen solid. Your roboports are dark. Every building on Aquilo is either generating heat or dying of cold. There is no water for steam power. There is no coal for burner power. There are no ore patches to build a traditional base. And you need lithium — but you can't mine enough of it here.

The cold kills your power grid. The lack of resources kills your factory. The loneliness of being on the most remote planet in the game kills your patience. Here is the exact order of operations to not just survive on Aquilo — but to extract the unique research it provides.

{{< callout "tip" >}}
**TL;DR:** Aquilo power comes from burning ice. Ice burned in smelter arrays produces heat and steam. Build a centralized heat distribution network first. Lithium is rare here — import from Gleba. Aquilo is not meant to be self-sufficient. Build only what Aquilo uniquely provides: cryogenic science packs. Import everything else.
{{< /callout >}}

## The Coldest Place in the Factorio Universe

Aquilo is a frozen moon. The surface temperature is below the freezing point of water. This is not cosmetic — it is a mechanical constraint that governs every aspect of gameplay.

In Factorio, buildings have a heat tolerance. Below a certain temperature, they stop functioning. On Aquilo, the ambient temperature is below this threshold for most buildings.

The mechanics:
- Every building on Aquilo has a minimum operating temperature
- Electric buildings (assemblers, smelters, inserters) need ambient heat or a heat pipe connection
- Steam engines need water above 15°C to produce power
- The solution: burn ice to generate heat

Ice is Aquilo's primary resource. Ice exists in dense patches across the surface. Burn it, and you get heat + water vapor. The water vapor drives steam turbines. The heat warms nearby buildings.

## Why Ice Changes Everything About Power

Ice on Aquilo is not just a resource — it is the entire power infrastructure.

**Ice as fuel:**
- Burner mining drills on ice patches produce ice chunks
- Ice chunks fed into smelters produce heat + steam
- Steam drives steam turbines → electricity
- Heat from the smelter warms nearby buildings through heat pipes

The math for 1 MW of power from ice:
- 1 smelter burning ice produces ~500 kW of heat
- 2 smelters = 1 MW of heat output
- Steam turbines convert heat to electricity at ~25% efficiency
- Net: 2 ice-burning smelters + 1 steam turbine = ~500 kW of power

This is significantly less efficient than solar or nuclear. Aquilo power is expensive. This is by design.

**The heating network:**
Smelters burning ice radiate heat through heat pipes. Heat pipes connect to:
- Nearby smelters (chain heating)
- Assembler machines (prevent freezing)
- Power substations (keep the grid warm)
- Roboports (prevent logistic network shutdown)

The heating network must cover your entire factory footprint. If any building is outside the heat radius, it freezes.

## The Lithium Problem: You Need It But Cannot Make It Here

Lithium is the key resource on Aquilo. It is used for:
- Lithium batteries (long-duration energy storage)
- Cryogenic science packs (the Aquilo-unique science tier)
- Quality module 5 components (the absolute endgame modules)

The problem: Aquilo has very few lithium ore deposits. Surface lithium patches are rare and small. Asteroid mining can supplement, but the surface deposits alone won't sustain a large science operation.

**The real lithium source: Gleba.**
Lithium is a common byproduct on Gleba — it appears in the bio-processing chain. If you've built a functional Gleba setup, you can export lithium ore to Aquilo via space platform.

**If you don't have Gleba running yet:**
Aquilo lithium patches exist, but they're not obvious. Look for the pale green ore patches with a different texture from iron/copper. They appear in clusters of 3-5 nodes. Mine them carefully — you'll need everything you get.

## Building a Heat Management System

The heating network is the make-or-break system on Aquilo. Build it wrong and your factory freezes. Build it right and it runs indefinitely.

**The standard Aquilo heat layout:**
```
[Ice Mining Drills] → [Ice Smelter Array] → [Heat Pipe Network] → [Factory Area]
                        ↑
                  6-8 burners
                  per smelter
```

**Critical rules for heat distribution:**
- Smelters must be adjacent to ice patches (burner drills feed directly)
- Heat pipes radiate 4 tiles per pipe. Use underground heat pipes to cover large areas.
- The heat network must be continuous. Any gap = freeze point.
- Smelter arrays at the center of your factory provide the most even heat distribution

**The power plant:**
Dedicate a specific area to ice-burning smelters that run at full power 24/7. This is your heat plant. Route heat pipes from here to every part of the factory. Keep the heat plant running regardless of power demand — if it shuts down, everything freezes.

**Redundancy:** Build 50% more heat capacity than you need. If a smelter goes offline for maintenance, the others cover the gap. An ice smelter that runs dry is a factory-freeze emergency.

## What Veterans Wish They Knew Before Landing

The learning curve on Aquilo is brutal. These are the lessons most players learn the hard way:

**Lesson 1: Solar panels are dead.**
Solar panels produce power but no heat. On Aquilo, you need heat more than you need power. Every building that needs power also needs heat. Solar + battery banks solve power, not heat. You still need the ice smelter array.

**Lesson 2: The factory shrinks.**
Because heat distribution is expensive and complex, you cannot build the sprawling factories Aquilo has conditioned you to build. Compact layouts are mandatory. Every tile of heat pipe costs smelter output. Every spread-out assembly line is a heat distribution problem.

**Lesson 3: Import everything you can.**
Aquilo is not meant to be a self-sufficient planet. It is a specialized research facility on ice. Import construction bots, backup power (nuclear fuel cells), spare parts, and lithium from Gleba. Export cryogenic science and advanced products. This is the sustainable Aquilo strategy.

**Lesson 4: Roboports freeze.**
Logistic robots need their roboports to stay above freezing. If the roboport freezes, your logistic network shuts down and construction bots return to their nests. Always heat roboports with dedicated heat pipe connections, not just proximity to a warm building.

## The Aquilo Research Chain — What Stays, What Goes

Aquilo has its own science tree. Most Nauvis research is unavailable here — you can't research nuclear or military on Aquilo. You can only research what Aquilo uniquely enables:

**Available on Aquilo:**
- Cryogenic science packs (the Aquilo science tier)
- Advanced quality modules (quality module 5 — the highest tier)
- Space platform improvements (the Aquilo space platform is a hub for interplanetary logistics)
- Energy storage upgrades (battery technology that far exceeds Nauvis)

**Not available on Aquilo:**
- Military research (no biter enemies here)
- Nuclear research (no uranium on Aquilo)
- most production technologies (best researched on Nauvis/Vulcanus)

**The cryogenic science chain:**
1. Mine ice → power the factory
2. Mine lithium → produce batteries
3. Produce cryogenic science packs: lithium battery + ice + advanced circuits → cryogenic science pack
4. Research: quality module 5, advanced space platform components, ultimate energy storage

Quality Module 5 is the capstone Aquilo research. It provides productivity bonuses that exceed module 4. A rocket silo with 4 Quality Module 5s produces 50%+ more rockets per resource than with module 4s.

## The Aquilo Space Platform — The Interplanetary Hub

Aquilo's space platform serves as the hub for space logistics between planets. Because Aquilo has no local resources (beyond ice and trace lithium), the platform must shuttle materials between Gleba, Vulcanus, Fulgora, and Aquilo.

**The Aquilo platform's role:**
- Import: lithium from Gleba, tungsten carbide from Vulcanus, quality materials from Fulgora
- Export: cryogenic science to Nauvis, advanced modules to wherever needed
- Hub: intermediate refueling stop for long-haul space routes

The Aquilo platform is smaller than a dedicated Vulcanus or Gleba platform. It doesn't need to produce anything — it needs to transfer and store materials. Build a large cargo bay and a modest thruster section.

## The Bottom Line

Aquilo is the endgame of Factorio Space Age. It demands everything you've learned from Fulgora, Gleba, and Vulcanus — and then asks you to solve the heat equation on top of it. The strategy is: import aggressively, build compactly, heat continuously, and extract the irreplaceable cryogenic science and quality module 5 research. Everything else on Aquilo is in service of that goal.
