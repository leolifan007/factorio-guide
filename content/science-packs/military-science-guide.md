---
title: "Military Science Pack Setup - Gray Science Ratios for Factorio 2.0"
date: 2026-06-20
tags: ["science-packs", "defense"]
draft: false
---

{{< callout "tip" >}}
**Military science at a glance:** Each science assembler needs 1 piercing round + 1 grenade + 1 stone wall every 10 seconds. One assembler of each ingredient feeds roughly 8-10 science assemblers. Military science is the cheapest and simplest science pack -- a single Assembling Machine 1 making grenades can support your whole early-game military research.
{{< /callout >}}

{{< section "Recipe and Requirements" >}}

{{< recipe name1="piercing_rounds" qty1="1x" name2="grenade" qty2="1x" name3="stone_wall" qty3="1x" result="military_science" rqty="2x" >}}

Military Science (Gray) is optional in Factorio 2.0 -- you can reach Space Age without researching any military technologies. But if biters are near your pollution cloud, military science unlocks the turret upgrades and damage research that keep your factory safe.

| Ingredient | Per Pack | For 10 SPM | Source |
|-----------|:--------:|:---------:|--------|
| Piercing Round Magazine | 0.5/s | 5/s | 5 Copper Plate + 1 Steel Plate per 1 |
| Grenade | 0.5/s | 5/s | 5 Iron Plate + 1 Coal per 2 |
| Stone Wall | 0.5/s | 5/s | 5 Stone Brick per 1 |

Output is 2 packs per craft (same in 1.0 and Space Age). Craft time is 10 seconds in an Assembling Machine 2.

{{< /section >}}

{{< section "Optimal Ratios for 10 SPM" >}}

Military science ratios are unusually easy because each ingredient assembler produces far more than a single science assembler consumes. Build one of each and see how much output you actually need.

| Component | Machines | Input | Notes |
|-----------|:--------:|-------|-------|
| Military science assemblers | 10 | 3 ingredients each | One AM2 craft = 2 packs |
| Piercing round assemblers | 1 | Copper + Steel | One AM2 feeds ~10 science assemblers |
| Grenade assemblers | 1 | Iron + Coal | One AM1 feeds ~16 science assemblers |
| Stone wall assemblers | 1 | Stone brick | One AM1 feeds ~14 science assemblers |
| Steel furnace | 2-4 | Iron ore + Coal | Steel for piercing rounds only |

{{< callout "info" >}}
**Why military science is cheap:** Each science pack needs half a piercing round per second, half a grenade, and half a wall. The ingredient production rates are much higher than the consumption rate. You do not need to scale military science the way you scale [blue science]({{< ref "/science-packs/blue-science-guide" >}}) or [purple science]({{< ref "/science-packs/production-science-guide" >}}).
{{< /callout >}}

{{< /section >}}

{{< section "Production Flow" >}}

{{< diagram "diagrams/military-science-flow.svg" "Military science production chain from copper/steel/iron/stone through piercing rounds, grenades, and walls to gray science packs" "760" >}}

The production chain splits into three parallel branches:

1. **Piercing Rounds (Ammo branch):** Copper plates + Steel plates into an Assembling Machine. One assembler produces 1 piercing round per 1 second. Each science assembler consumes 0.5 rounds per second.
2. **Grenades (Explosive branch):** Iron plates + Coal into an Assembling Machine. One craft produces 2 grenades in 8 seconds (0.25/s). Each science assembler consumes 0.5 grenades per second -- one grenade assembler supports 5 at full speed, or more if you add modules.
3. **Stone Walls (Defense branch):** Stone bricks from your furnace setup. One Assembling Machine 1 turns 5 bricks into 1 wall per 0.5 seconds. Each science assembler consumes 0.5 walls per second.

If you need ammunition for your actual turrets, build a separate piercing round line. Do not share the science ammo line with your defense ammo -- the science line only works if the belt is full and uninterrupted.

{{< /section >}}

{{< section "Layout -- Minimalist Military Science" >}}

Military science needs almost no specialized infrastructure. Typical mid-game approach:

- Route copper plate and steel plate belts to a single assembling machine making piercing rounds
- Iron plate and coal to a shared assembler for grenades
- Stone bricks from your furnace array into a wall assembler
- Merge all three outputs onto a 3-to-1 belt going into 8-10 science assemblers

**Space Age bonus:** If you have unlocked the foundry on [Vulcanus]({{< ref "/production-ratios/smelting-ratios" >}}...), consider using foundries for steel production. The bonus productivity on steel plates directly reduces the iron ore cost of your military science.

Add your military science labs inline with your other sciences. Since [all science packs]({{< ref "/base-design/main-bus-guide" >}}) share labs, just add a fourth belt feeding gray science alongside red, green, and blue.

{{< /section >}}

{{< section "When to Build Military Science" >}}

| Scenario | Build Military Science? | Reason |
|----------|:----------------------:|--------|
| Peaceful mode / no biters | Skip entirely | No military tech needed |
| Biters far from pollution cloud | Skip early | Red+green+blue gives core tech first |
| Biters near pollution cloud | ASAP | Damage upgrades + turret tech |
| Death world / high biter settings | Rush immediately | Need grenades for nest clearing |
| Space Age endgame (gleba/aquilo) | Scale to 30+ SPM | Pentapod defense on Gleba needs military upgrades |

{{< callout "tip" >}}
**Defense priority order:** Before building military science, make sure you have at least basic [early game defense]({{< ref "/defense/early-game-defense" >}}) set up -- a few gun turrets around your pollution generators. Military science unlocks damage upgrades that make those turrets 2-3x more effective, but only if you have turrets to apply them to.
{{< /callout >}}

{{< /section >}}

{{< section "Common Mistakes" >}}

- **Overbuilding:** Military science ingredients are extremely fast to produce. Building 4 assembling machines for grenades does not make your science faster -- one machine is enough for 15+ SPM. The bottleneck is how many science assemblers you build, not the ingredient supply.
- **Ammo belt sharing:** If you pull piercing rounds from the same belt that feeds your turrets, a biter attack empties the belt and starves your science. Build a dedicated ammunition assembler for science.
- **Forgetting stone:** Stone is easy to overlook once your base grows past the starting patch. Military science needs stone bricks for walls. Add a stone furnace to your smelting line or route a dedicated stone belt.

{{< /section >}}

{{< section "Bottom Line" >}}

Military science is the lowest-maintenance science pack in Factorio. One assembler per ingredient supports 8-10 science assemblers, which is more than you will need for most of the game. Skip it if biters are not a problem. Build a small setup when they are. Do not overthink the ratios -- they favor you.

{{< /section >}}

{{< section "Community Verification" >}}

- [Factorio Wiki: Military science pack](https://wiki.factorio.com/Military_science_pack) -- Recipe reference and crafting data
- [Official Factorio blog: FFF-419](https://factorio.com/blog/post/fff-419) -- Science pack changes in Space Age
