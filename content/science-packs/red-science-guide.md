---
title: "Red Science Pack - Automation Science Guide"
description: "Red science pack in Factorio: exact recipe, assembler count per SPM, belt layout, and how to automate automation science so it never stops. Includes the gear ratio that saves you a whole assembler."
date: 2026-05-18
lastmod: 2026-09-26T11:18:00+08:00
tags: ["science-packs", "getting-started"]
draft: false
---

{{< callout "tip" >}}
**Short answer:** red science is 1 iron gear + 1 copper plate, and you need roughly **1 assembler per 1 SPM** if feeding from belts. For a standard 10 SPM target, use **10 assemblers making gears and 10 making science** - or 5 gear assemblers if you use speed modules. The mistake almost everyone makes is under-building gears: one gear assembler cannot feed even two science assemblers.
{{< /callout >}}

{{< section "Recipe (Automation Science Pack)" />}}

{{< recipe name1="iron_gear" qty1="1x" name2="copper_plate" qty2="1x" result="automation_science" rqty="1x" >}}

The recipe takes **1 second** to craft in an assembling machine 1. That single fact drives every ratio below.

{{< section "The Gear Ratio Most Players Get Wrong" />}}

Iron gears take **0.5 seconds** to craft. Red science takes **1 second**. So one gear assembler can theoretically feed two science assemblers - but only if belts never stall.

{{< diagram "diagrams/space-age/red-science-ratio.svg" "Red science pack production ratio showing gear assembler to science assembler counts and belt feeding layout" "760" >}}

| SPM Target | Gear Assemblers | Science Assemblers | Total |
|:-----------|:---------------:|:------------------:|:-----:|
| 5 SPM | 3 | 5 | 8 |
| 10 SPM | 5 | 10 | 15 |
| 20 SPM | 10 | 20 | 30 |
| 30 SPM | 15 | 30 | 45 |

**Always round gear assemblers up.** A stalled gear line is the single most common reason red science output drops.

| Setup | Gear Assemblers | Reality |
|:------|:---------------:|:--------|
| Exact math (2:1) | 5 for 10 SPM | Stalls whenever a belt backs up |
| **Safe (1.5:1)** | **7 for 10 SPM** | Runs continuously |
| Overkill | 10 for 10 SPM | Wastes power, never stalls |

{{< section "Material Cost Per Science Pack" />}}

| Item | Per Pack | For 10 SPM | Notes |
|:-----|:--------:|:----------:|:------|
| {{<material "iron-plate">}} Iron plate | 1 (+2 for gear) | 30/sec | Feeds the gear assemblers |
| {{<material "copper-plate">}} Copper plate | 1 | 10/sec | Direct into science assembler |
| {{<material "iron-gear">}} Iron gear | 1 | 10/sec | Crafted from iron plate |

Iron is the bottleneck. Red science eats roughly **3 iron plates per pack** once gear crafting is included.

{{< section "Belt Layout That Never Stalls" />}}

The cleanest early setup puts gears and science on one row with a shared iron feed.

1. Run **one iron belt** down the back of the assembler row
2. Inserters pull iron into the gear assemblers first
3. Gears go onto a short belt feeding the science assemblers
4. Copper arrives on its own belt from the other side
5. Inserters output science to a belt heading to your labs

{{< diagram "diagrams/space-age/red-science-layout.svg" "Compact red science belt layout showing iron feed, gear assemblers, and science output to labs" "760" >}}

| Common Layout Problem | Fix |
|:----------------------|:----|
| Gear assembler starved | Move it closer to the iron feed |
| Science backs up into assembler | Add a buffer chest or route to more labs |
| Copper and iron belts cross | Run copper underneath with a tunnel |
| Labs idle | Check lab has an inserter AND power |

{{< section "How to Automate" />}}

1. Belt **iron plates** into the gear assemblers
2. Belt **copper plates** directly into the science assemblers
3. Move **gears** from gear assemblers to science assemblers on a short belt
4. Pull **science packs** out with an inserter into a chest or straight to labs

{{< callout "warning" >}}
**Common mistake:** labs need *both* science packs AND power. If red science is piling up but research is not progressing, check that your lab has an inserter feeding it and is inside a powered electric network.
{{< /callout >}}

{{< section "Research Priority After Red Science" />}}

Red science unlocks the automation tree. Push these in order:

| Priority | Technology | Why |
|:--------:|:-----------|:----|
| 1 | Automation 2 | Electric mining drills - stops manual mining |
| 2 | Logistics | Unlocks green science |
| 3 | Steel processing | Steel plates for mid-game |
| 4 | Engine | Engine units, required for blue science |

Red science is cheap, so do not overthink the build. Ten assemblers is more than enough to reach [green science]({{< ref "/getting-started/green-science-guide" >}}).

{{< section "When to Expand Red Science" />}}

Red science stays cheap forever, but your SPM target should grow with your base.

| Base Stage | Red SPM Target | Why |
|:-----------|:--------------:|:----|
| First hour | 5 | Enough to unlock automation 2 |
| Early base | 10 | Feeds all six labs without waiting |
| Mid game | 20-30 | Keeps research moving while you build out |
| Megabase | 45+ | Scales with the rest of your science |

You do not need to rebuild when you expand. Just **add assemblers to the end of the row** and extend the iron belt. The layout above scales linearly up to about 45 SPM before belt throughput becomes the limit.

| Sign You Need More | What It Means |
|:-------------------|:--------------|
| Labs sitting idle with science in stock | Other science tiers are the bottleneck |
| Research queue empty, red science full | You are over-producing red, redirect iron |
| Gears constantly short | Gear assemblers are under-built |

{{< section "Related Guides" />}}

- {{< ref "/getting-started/green-science-guide" >}} - the second science tier
- {{< ref "/base-design/main-bus-guide" >}} - where red science sits on your bus
- {{< ref "/production-ratios/smelting-ratios" >}} - how many furnaces feed this line

{{< section "Community Verification and Resources" />}}

- [Factorio Wiki: Automation science pack](https://wiki.factorio.com/Automation_science_pack) - official recipe and crafting time
- [Factorio Cheat Sheet](https://factoriocheatsheet.com/) - community ratio tables for all science packs

*Last updated: 2026-09-26 | Verified against Factorio 2.0.*
