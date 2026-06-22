# Bulk fix: add tables + material icons to thin SA articles
$base = 'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\content\space-age'

function Append-Fix {
    param($rel, $tail)
    $fp = Join-Path $base $rel
    $c = [System.IO.File]::ReadAllText($fp, [System.Text.Encoding]::UTF8)
    if ($c -match '(?s)(.*?)({{<\s*/\s*callout\s*>}})(.*)') {
        $head = $matches[1] + $matches[2]
        $rest = $matches[3]
        $c = $head + $tail + $rest
    } else {
        $c = $c.TrimEnd() + "`r`n" + $tail.TrimStart()
    }
    [System.IO.File]::WriteAllText($fp, $c, [System.Text.UTF8Encoding]::new($false))
    Write-Host "Fixed: $rel"
}

$vulcanusTail = @'
## Quick Reference — Vulcanus

| Priority | Task | Key Building | Key Item |
|:---------|:-----|:--------|:-----|
| 1 | Land and build solar | {{<material "solar-panel">}} Solar panel | {{<material "steel-plate">}} Steel |
| 2 | Mine tungsten | {{<material "big-mining-drill">}} Big drill | Tungsten carbide |
| 3 | Build foundry | {{<material "foundry">}} Foundry | {{<material "calcite">}} Calcite |
| 4 | Lava pumping | {{<material "offshore-pump">}} Pump | Molten iron/copper |

| Resource | Recipe | Input | Output | Foundry Bonus |
|:---------|:-------|:------|:-------|:------------:|
| Molten iron | Smelting | Lava + Calcite | 500 fluid | +50% prod |
| Molten copper | Smelting | Lava + Calcite | 500 fluid | +50% prod |
| Iron gears | Casting | 100 molten iron | 20 gears | Direct craft |
| Copper wire | Casting | 100 molten copper | 40 wire | Direct craft |
'@

$fulgoraTail = @'
## Quick Reference — Fulgora Scrap

| Item | Probability | Use | Void Method |
|:-----|:-----------:|:----|:-----------|
| {{<material "iron-gear-wheel">}} Iron gear | 22.5% | Belts, assemblers | Recycler loop |
| {{<material "copper-cable">}} Copper wire | 22.5% | Circuits | Recycler loop |
| {{<material "iron-plate">}} Iron plate | 15.0% | General build | Shooting chest |
| {{<material "battery">}} Battery | 5.6% | Accumulators | Keep |
| {{<material "processing-unit">}} Blue circuit | 4.5% | High-tech | **Keep** |
| {{<material "holmium-ore">}} Holmium ore | 2.8% | EM science | **Keep** |

| Module Setup | Items Recycled | 25% Return | Output |
|:------------|:--------------:|:----------:|:------|
| No modules | 1 | 25% | Common only |
| 1 Quality 1 | 1 | 22.5% | Mixed |
| 4 Quality 3 | 1 | 8.5% | Up to epic |
| 4 Speed 3 | 1.5/s | 25% | Common only |
'@

$glebaTail = @'
## Quick Reference — Gleba

| Threat | Source | Countermeasure | Building |
|:-------|:-------|:--------------|:---------|
| Spoilage | All organic items | Timer flushing | {{<material "decider-combinator">}} Circuit |
| Pentapods | Spore clouds | Turret perimeter | {{<material "gun-turret">}} Turret |
| Starvation | Stalled farms | Backup energy | {{<material "heating-tower">}} Tower |
| Belt jam | Excess fruit | Priority splitter | {{<material "splitter">}} Splitter |

| Source | Input | Nutrient Output | Spoilage |
|:-------|:-----|:---------------:|:--------:|
| Bioflux | 1 bioflux | 50 nutrients | 2 min |
| Yumako mash | 50 mash | 10 nutrients | 5 min |
| Jelly | 50 jelly | 10 nutrients | 5 min |
| Spoilage | 200 spoilage | 10 nutrients | 1 min |
'@

$aquiloTail = @'
## Quick Reference — Aquilo

| Category | Must Bring | Alternative | Warning |
|:---------|:-----------|:------------|:--------|
| Power | Solar + accumulators | {{<material "heating-tower">}} Heating tower | Rocket fuel needed |
| Heating | {{<material "heat-pipe">}} Heat pipes | Nuclear reactor | Ice platform |
| Production | {{<material "chemical-plant">}} Chem plants | Foundry | No mining |
| Defense | {{<material "rocket-launcher">}} Rockets | Laser turrets | Power hungry |

| Heat Source | Tiles to 500 C | Tiles to 100 C | Max Range |
|:------------|:--------------:|:--------------:|:---------:|
| Heating tower (fuel) | 8 | 20 | 30 tiles |
| Nuclear reactor | 15 | 40 | 55 tiles |
| Heat exchanger chain | 20 | 50 | 80 tiles |
'@

$platformTail = @'
## Quick Reference — Platform Build

| Stage | Build | Key Component | Time |
|:------|:------|:----------|:----:|
| 1 | Hub + foundation | {{<material "stone-brick">}} 20 tiles | 2 min |
| 2 | Fuel production | {{<material "assembling-machine-3">}} Crusher + chem | 3 min |
| 3 | Ammo line | {{<material "piercing-rounds-magazine">}} Iron + copper | 2 min |
| 4 | Turrets | {{<material "gun-turret">}} 4 turrets | 1 min |
| 5 | Thrusters | {{<material "rocket-fuel">}} 2 thrusters | 2 min |

| Region | Rocky | Metallic | Carbon | Oxide |
|:-------|:-----:|:--------:|:------:|:----:|
| Nauvis orbit | High | Low | Low | None |
| Inner planets | Medium | Medium | Medium | None |
| Outer planets | Low | High | High | Low |
| Aquilo route | Very high | High | Low | Medium |
'@

$pentTail = @'
## Defense Summary

| Layer | Turret | Ammo | Range | Best Vs |
|:------|:-------|:-----|:-----:|:--------|
| Inner | {{<material "rocket-launcher">}} Rocket turret | Explosive | 36 | Large |
| Middle | {{<material "gun-turret">}} Gun turret | Uranium | 24 | Medium |
| Outer | {{<material "land-mine">}} Landmines | — | — | First wave |
'@

$shipTail = @'
## Ship Components

| Component | Function | Count | Weight | Fuel |
|:----------|:---------|:-----:|:------:|:----:|
| Hub | Core, storage | 1 | 10t | — |
| Thruster | Movement | 2-4 | 12t | {{<material "rocket-fuel">}} Fuel |
| Crusher | Asteroid | 4-6 | 4t | Power |
| Turret | Defense | 4-8 | 4t | {{<material "piercing-rounds-magazine">}} Ammo |
'@

$qlTail = @'
## Quality Module Comparison

| Tier | Quality Bonus | Prod Penalty | Best Use |
|:----|:------------:|:------------:|:---------|
| Quality 1 | +1% | -5% | Start-up |
| Quality 2 | +2% | -10% | Mid-game |
| Quality 3 | +2.5% | -15% | End-game |
| Legendary Q3 | +6.2% | -10% | Optimal |
'@

$fixes = @(
    @{rel='vulcanus\vulcanus-guide.md'; tail=$vulcanusTail},
    @{rel='fulgora\fulgora-recycling-guide.md'; tail=$fulgoraTail},
    @{rel='gleba\gleba-survival-guide.md'; tail=$glebaTail},
    @{rel='aquilo\aquilo-guide.md'; tail=$aquiloTail},
    @{rel='platform\space-platform-guide.md'; tail=$platformTail},
    @{rel='gleba\pentapod-defense.md'; tail=$pentTail},
    @{rel='platform\ship-design.md'; tail=$shipTail},
    @{rel='quality\upcycling-loop.md'; tail=$qlTail}
)

foreach ($f in $fixes) {
    Append-Fix $f.rel $f.tail
}

Write-Host "`nAll bulk fixes applied"
