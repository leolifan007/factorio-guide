---
title: "Logistic Science Pack — Green Science Guide"
description: "Complete green science guide for Factorio: recipe, ratios, belt setup, and scaling tips for automating logistic science packs."
date: 2026-05-18
tags: ["getting-started", "science-packs"]
draft: false
---

<!-- Article Hero -->
<div class="article-hero-img" style="background:linear-gradient(135deg,#556b2f,#6abe30);height:200px;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;">
<span style="font-family:Orbitron,sans-serif;font-size:2rem;font-weight:900;color:#222;">LOGISTIC SCIENCE</span>
</div>

Green science is the wall that separates casual manual-crafting from real automation. Unlike red science (two ingredients, one assembler, done), green science forces you to think about sub-factories, belt balancing, and ratios. I've rebuilt this thing a dozen times across different playthroughs, and every time I find a cleaner way to lay it out.

{{< callout "tip" >}}
**TL;DR:** 1 inserter assembler + 1 belt assembler = enough to feed 10 green science assemblers. Build them in a line with belts running down the middle.
{{< /callout >}}

{{< section "Recipe" >}}

Each logistic science pack takes two items. Here's the exact recipe chain:

{{< recipe name1="inserter" qty1="1x" name2="transport_belt" qty2="1x" result="logistic_science" rqty="1x" >}}

The inserter recipe itself needs iron gears, green circuits, and iron plates. The belt recipe needs just one iron plate. So the full chain from raw materials is:

{{< recipe name1="iron_plate" qty1="3x" name2="circuit_green" qty2="1x" name3="iron_gear" qty3="2x" >}}

{{< section "Ratio Math — Getting the Numbers Right" >}}

Here's the math after crunching it:

| Machine | Output | Needed assemblers | Feeds how many science asm |
|---------|--------|:-----------------:|:--------------------------:|
| Green science assembler | 1 pack / 6s | 10 | — |
| Inserter assembler | 1 inserter / 0.5s | 1 | Up to 12 science assemblers |
| Belt assembler | 2 belts / 0.5s | 1 | Up to 24 science assemblers |
| Green circuit assembler | 1 circuit / 0.5s | 1 | Shared with red science |

The ratio is forgiving: one inserter assembler makes 2 inserters per second. Each science assembler eats 1 inserter every 6 seconds, so a single inserter assembler supports 12 science assemblers. Belt assemblers are even more efficient — 4 belts per second feeding 24 science assemblers.

**Bottom line:** Build 1 inserter assembler, 1 belt assembler, and 10 green science assemblers. It's a clean ratio that works from your first build through the mid-game.

{{< diagram "diagrams/green-science-flow.svg" "Green science production chain - inserter and belt assemblers feeding a 10-assembler science array" "760" >}}

{{< section "Layout That Works Every Time" >}}

I've tried a few layouts. The one that sticks is a straight-line double-sided build with components running down the middle:

<pre style="background:#1a1a1a;padding:0.75rem;border-radius:4px;border:1px solid #444;font-size:0.72rem;line-height:1.6;">
  Iron Plate Belt (top lane)   Green Circuit Belt (bottom lane)
  ─────────────────────────────────────────────────────────────
  [Ins][Bel][Ins][Bel][Ins][Bel][Ins][Bel]   ← sub-assembler row
    ║    ║    ║    ║    ║    ║    ║    ║
   [GS] [GS] [GS] [GS] [GS] [GS] [GS] [GS]  ← science assemblers
    ║    ║    ║    ║    ║    ║    ║    ║
  ─────────────────────────────────────────────
  Green science output belt → Labs
</pre>

Put inserter and belt assemblers in a row. Iron plates on one belt lane, green circuits on the other. Science packs go to a third belt feeding labs.

{{< callout "warning" >}}
**Watch out:** Your green science belt will back up if labs aren't consuming fast enough. I use a priority splitter: science output gets priority, excess goes to a buffer chest with circuit control.
{{< /callout >}}

{{< section "Integrating Into Your Factory" >}}

Green science is when you need a proper bus. Here's the minimum belt setup near labs:

1. **Iron plates** — one full belt lane
2. **Copper plates** — one lane for circuit production
3. **Green circuits** — already made for red science, just extend the belt
4. **Green science output** — dedicated belt feeding labs

Don't bother with a separate iron gear belt. A single gear assembler (steel furnace fed) handles everything up to blue science.

{{< section "Mistakes I Kept Making" >}}

**The belt backup trap.** I once spent an hour debugging why inserters weren't working. Turned out the green science belt was full — inserters couldn't place packs, which caused inserter production to back up. Solution: more labs or a buffer chest.

**Not enough copper wire.** One copper wire assembler feeds about 6 green circuit assemblers. If circuit production stalls, wire is almost always the culprit.

**Forgetting the output inserter.** Done this more times than I'd like to admit. Assembler fills up with science packs, no way out. Always put a fast inserter on output.

{{< section "Scaling for Early Game" >}}

Once you unlock Assembler 2 and fast belts, scaling is straightforward:

- Upgrade belts on the bus
- Switch science assemblers to Assembler 2
- Add a second inserter+belt assembler if pushing 30+ green SPM
- Red inserters speed up throughput

{{< callout "tip" >}}
Don't waste modules on green science production. The raw materials are cheap enough that productivity modules on circuit production give better returns.
{{< /callout >}}

{{< section "Bottom Line" >}}

Green science is the first test of real factory design. Get this ratio once, and you won't touch it again until megabase territory.

**Numbers to remember:**
- One inserter + one belt assembler feeds 10 green science assemblers
- One green circuit assembler handles both red and green at this scale
- One iron plate belt lane supports everything

**Next up:** The [Blue Science Guide]({{< ref "/science-packs/blue-science-guide" >}}) — oil processing is where Factorio really starts.