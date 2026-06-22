# Task Artifact: Factorio Space Age Guide — 2 Articles + 2 SVG Diagrams

## Objective
Create 2 Factorio Space Age guide articles with matching SVG diagrams, write them to the existing Hugo guide repository at `C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide`.

## Files Created

### Article 1 — Vulcanus Lava Processing
- **Path:** `content/space-age/vulcanus/lava-processing.md` (12,436 bytes)
- **Alias:** `/space-age/vulcanus-lava-processing/`
- Covers: lava pumping, foundry recipes, calcite logistics, casting throughput tables, Nauvis export ratios
- Shortcodes: `{{< material >}}`, `{{< callout >}}`, `{{< ref >}}`, `{{< diagram >}}`

### Article 2 — Quality Module Upcycling Loop
- **Path:** `content/space-age/quality/upcycling-loop.md` (15,435 bytes)
- **Alias:** `/space-age/quality-module-upcycling/`
- Covers: upcycling loop design, quality probability matrix, tier strategy, item selection, legendary equipment ROI
- Shortcodes: `{{< material >}}`, `{{< callout >}}`, `{{< ref >}}`, `{{< diagram >}}`

### SVG Diagram 1 — Lava Processing Flow
- **Path:** `static/images/diagrams/space-age/lava-processing-flow.svg` (16,325 bytes)
- 760×480px, dark theme (#1a1a2e bg, #e8941c accent)
- Flow: Lava Pump → Foundry → Molten Iron/Copper → Casting + LDS
- Throughput table at bottom

### SVG Diagram 2 — Quality Upcycling Loop
- **Path:** `static/images/diagrams/space-age/quality-upcycling-loop.svg` (17,820 bytes)
- 760×500px, dark theme (#1a1a2e bg)
- Flow: Common Input → Assembler (with quality modules) → Filter → Recycler → Feedback loop
- Quality filter arrows (uncommon/rare/epic/legendary) + Probability Matrix table

## Pre-existing Fixes Applied
Fixed 2 unclosed `{{< callout >}}` shortcodes (should be `{{< /callout >}}`) in:
- `content/space-age/gleba/bioflux-production.md`
- `content/space-age/platform/cross-planet-logistics.md`

## Build Result
`hugo --quiet` → exit 0 ✅ (132 pages, 244 static files)
