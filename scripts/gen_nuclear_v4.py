#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate nuclear-reactor-layout.svg - pure vertical stack, zero overlap."""
import textwrap

svg = textwrap.dedent('''\
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 1200" width="760" height="1200">
  <defs>
    <style>
      .lbl { font-family: "Segoe UI", Arial, sans-serif; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="760" height="1200" fill="#12121f" rx="10"/>

  <!-- ========== TITLE BAR ========== -->
  <rect x="0" y="0" width="760" height="48" fill="#0a1628" rx="10"/>
  <text x="380" y="32" text-anchor="middle" class="lbl" font-size="14" font-weight="900" fill="#44ff88" letter-spacing="2">NUCLEAR POWER - 2x2 REACTOR LAYOUT</text>

  <!-- =================================================================== -->
  <!-- SECTION 1: REACTORS (y 65 - 270) -->
  <!-- =================================================================== -->
  <text x="380" y="80" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">1. REACTORS (4x) - Neighbor Bonus Math</text>

  <!-- Reactor A (row 1, col 1) -->
  <rect x="120" y="96" width="120" height="56" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="180" y="124" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">A</text>
  <text x="180" y="142" text-anchor="middle" class="lbl" font-size="8" fill="#999">1 nbr = 80 MW</text>

  <!-- Reactor B (row 1, col 2) -->
  <rect x="270" y="96" width="120" height="56" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="330" y="124" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">B</text>
  <text x="330" y="142" text-anchor="middle" class="lbl" font-size="8" fill="#ffaa44">2 nbr = 160 MW</text>

  <!-- Reactor C (row 2, col 1) -->
  <rect x="120" y="168" width="120" height="56" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="180" y="196" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">C</text>
  <text x="180" y="214" text-anchor="middle" class="lbl" font-size="8" fill="#999">1 nbr = 80 MW</text>

  <!-- Reactor D (row 2, col 2) -->
  <rect x="270" y="168" width="120" height="56" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="330" y="196" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">D</text>
  <text x="330" y="214" text-anchor="middle" class="lbl" font-size="8" fill="#ffaa44">2 nbr = 160 MW</text>

  <!-- Neighbor bonus: A-B (horizontal) -->
  <line x1="240" y1="118" x2="270" y2="118" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="255" y="114" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: C-D (horizontal) -->
  <line x1="240" y1="190" x2="270" y2="190" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="255" y="186" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: A-C (vertical) -->
  <line x1="180" y1="152" x2="180" y2="168" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="190" y="162" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: B-D (vertical) -->
  <line x1="330" y1="152" x2="330" y2="168" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="340" y="162" class="lbl" font-size="7" fill="#ffaa44">+300%</text>

  <!-- Total output -->
  <rect x="120" y="240" width="270" height="24" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1"/>
  <text x="255" y="256" text-anchor="middle" class="lbl" font-size="11" fill="#ffaa44" font-weight="700">TOTAL: 480 MW (4 reactors)</text>

  <!-- Down-arrow to next section -->
  <line x1="380" y1="272" x2="380" y2="302" stroke="#444" stroke-width="2"/>
  <polygon points="376,296 380,304 384,296" fill="#444"/>
  <text x="394" y="290" class="lbl" font-size="8" fill="#666">1000C heat out</text>

  <!-- =================================================================== -->
  <!-- SECTION 2: HEAT FLOW - horizontal left to right (y 310 - 510) -->
  <!-- Each block stacks vertically below reactors, no horizontal split -->
  <!-- =================================================================== -->
  <text x="380" y="326" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">2. HEAT FLOW (Left to Right)</text>

  <!-- Block 1: Heat Pipes (left) -->
  <rect x="40" y="340" width="160" height="70" rx="5" fill="#1a0a04" stroke="#cc7733" stroke-width="1.5"/>
  <text x="120" y="362" text-anchor="middle" class="lbl" font-size="10" fill="#cc7733" font-weight="700">HEAT PIPES</text>
  <text x="120" y="378" text-anchor="middle" class="lbl" font-size="8" fill="#aa7744">3 parallel pipes</text>
  <text x="120" y="393" text-anchor="middle" class="lbl" font-size="7" fill="#cc7733">1000C from reactor</text>
  <text x="120" y="405" text-anchor="middle" class="lbl" font-size="7" fill="#aa7744">500C to exchanger</text>

  <!-- Arrow 1 -> 2 -->
  <line x1="202" y1="375" x2="238" y2="375" stroke="#cc7733" stroke-width="2"/>
  <polygon points="236,371 242,375 236,379" fill="#cc7733"/>

  <!-- Block 2: Heat Exchangers (center) -->
  <rect x="244" y="340" width="200" height="70" rx="5" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.5"/>
  <text x="344" y="362" text-anchor="middle" class="lbl" font-size="10" fill="#ff6644" font-weight="700">HEAT EXCHANGERS</text>
  <text x="344" y="378" text-anchor="middle" class="lbl" font-size="8" fill="#ff6644">x48 (12 per reactor)</text>
  <text x="344" y="393" text-anchor="middle" class="lbl" font-size="7" fill="#884422">In: 1000C heat</text>
  <text x="344" y="405" text-anchor="middle" class="lbl" font-size="7" fill="#884422">Out: 500C steam</text>

  <!-- Arrow 2 -> 3 -->
  <line x1="446" y1="375" x2="482" y2="375" stroke="#ff6644" stroke-width="2"/>
  <polygon points="480,371 486,375 480,379" fill="#ff6644"/>

  <!-- Block 3: Steam Turbines (right) -->
  <rect x="488" y="340" width="180" height="70" rx="5" fill="#0a1028" stroke="#88ccff" stroke-width="1.5"/>
  <text x="578" y="362" text-anchor="middle" class="lbl" font-size="10" fill="#88ccff" font-weight="700">STEAM TURBINES</text>
  <text x="578" y="378" text-anchor="middle" class="lbl" font-size="8" fill="#88ccff">x84 (21 per reactor)</text>
  <text x="578" y="393" text-anchor="middle" class="lbl" font-size="7" fill="#445566">In: 500C steam</text>
  <text x="578" y="405" text-anchor="middle" class="lbl" font-size="7" fill="#445566">Out: 480 MW total</text>

  <!-- Water supply (right of turbines) -->
  <rect x="680" y="355" width="36" height="40" rx="4" fill="#0a1a2a" stroke="#44aaff" stroke-width="1.2"/>
  <text x="698" y="372" text-anchor="middle" class="lbl" font-size="7" fill="#44aaff" font-weight="700">H2O</text>
  <text x="698" y="385" text-anchor="middle" class="lbl" font-size="6" fill="#4488cc">4x</text>
  <text x="698" y="397" text-anchor="middle" class="lbl" font-size="6" fill="#4488cc">pump</text>

  <!-- Water arrow (dashed) -->
  <line x1="656" y1="375" x2="680" y2="375" stroke="#44aaff" stroke-width="1.2" stroke-dasharray="3"/>
  <polygon points="678,371 684,375 678,379" fill="#44aaff"/>

  <!-- Down-arrow to summary -->
  <line x1="380" y1="435" x2="380" y2="465" stroke="#444" stroke-width="2"/>
  <polygon points="376,459 380,467 384,459" fill="#444"/>

  <!-- =================================================================== -->
  <!-- SECTION 3: SUMMARY BAR (y 473 - 566) -->
  <!-- =================================================================== -->
  <rect x="40" y="473" width="680" height="93" rx="6" fill="#0a1628" stroke="#44ff88" stroke-width="1.5"/>

  <text x="380" y="499" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="900">2x2 REACTOR = 480 MW TOTAL</text>

  <line x1="40" y1="511" x2="720" y2="511" stroke="#1a3a1a" stroke-width="0.5"/>

  <!-- 5 stat columns, evenly spaced -->
  <text x="118" y="529" text-anchor="middle" class="lbl" font-size="8" fill="#666">REACTORS</text>
  <text x="118" y="549" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="700">4</text>
  <text x="118" y="561" text-anchor="middle" class="lbl" font-size="7" fill="#444">+bonus</text>

  <text x="264" y="529" text-anchor="middle" class="lbl" font-size="8" fill="#666">HEAT EXCHANGERS</text>
  <text x="264" y="549" text-anchor="middle" class="lbl" font-size="13" fill="#ff6644" font-weight="700">48</text>
  <text x="264" y="561" text-anchor="middle" class="lbl" font-size="7" fill="#444">12/rct</text>

  <text x="410" y="529" text-anchor="middle" class="lbl" font-size="8" fill="#666">TURBINES</text>
  <text x="410" y="549" text-anchor="middle" class="lbl" font-size="13" fill="#88ccff" font-weight="700">84</text>
  <text x="410" y="561" text-anchor="middle" class="lbl" font-size="7" fill="#444">21/rct</text>

  <text x="556" y="529" text-anchor="middle" class="lbl" font-size="8" fill="#666">OFFSHORE PUMPS</text>
  <text x="556" y="549" text-anchor="middle" class="lbl" font-size="13" fill="#44aaff" font-weight="700">4</text>
  <text x="556" y="561" text-anchor="middle" class="lbl" font-size="7" fill="#444">1/12HX</text>

  <text x="702" y="529" text-anchor="middle" class="lbl" font-size="8" fill="#666">FUEL CELLS/HR</text>
  <text x="702" y="549" text-anchor="middle" class="lbl" font-size="13" fill="#ffaa44" font-weight="700">~72</text>
  <text x="702" y="561" text-anchor="middle" class="lbl" font-size="7" fill="#444">18/rct</text>

  <!-- Down-arrow to fuel cycle -->
  <line x1="380" y1="574" x2="380" y2="604" stroke="#444" stroke-width="2"/>
  <polygon points="376,598 380,606 384,598" fill="#444"/>

  <!-- =================================================================== -->
  <!-- SECTION 4: FUEL CYCLE (y 612 - 680) -->
  <!-- =================================================================== -->
  <text x="380" y="628" text-anchor="middle" class="lbl" font-size="12" fill="#aaaaaa" font-weight="700">3. FUEL CYCLE</text>

  <!-- Node 1: Mining -->
  <rect x="80" y="644" width="120" height="36" rx="4" fill="#1a1a2e" stroke="#555" stroke-width="1"/>
  <text x="140" y="661" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Uranium Mining</text>
  <text x="140" y="673" text-anchor="middle" class="lbl" font-size="7" fill="#555">1 drill</text>

  <!-- Arrow 1 -> 2 -->
  <line x1="202" y1="662" x2="236" y2="662" stroke="#555" stroke-width="1.5"/>
  <polygon points="234,658 240,662 234,666" fill="#555"/>

  <!-- Node 2: Centrifuge -->
  <rect x="242" y="644" width="120" height="36" rx="4" fill="#1a1a2e" stroke="#888" stroke-width="1"/>
  <text x="302" y="661" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Centrifuge x5</text>
  <text x="302" y="673" text-anchor="middle" class="lbl" font-size="7" fill="#555">0.7pct U-235</text>

  <!-- Arrow 2 -> 3 -->
  <line x1="364" y1="662" x2="398" y2="662" stroke="#555" stroke-width="1.5"/>
  <polygon points="396,658 402,662 396,666" fill="#555"/>

  <!-- Node 3: Fuel Assembler -->
  <rect x="404" y="644" width="130" height="36" rx="4" fill="#1a1a2e" stroke="#aa8800" stroke-width="1"/>
  <text x="469" y="661" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Fuel Assembler</text>
  <text x="469" y="673" text-anchor="middle" class="lbl" font-size="7" fill="#aa8800">19 U-238 + 1 U-235</text>

  <!-- Arrow 3 -> 4 -->
  <line x1="536" y1="662" x2="570" y2="662" stroke="#555" stroke-width="1.5"/>
  <polygon points="568,658 574,662 568,666" fill="#555"/>

  <!-- Node 4: Reactor -->
  <rect x="576" y="644" width="110" height="36" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1.5"/>
  <text x="631" y="661" text-anchor="middle" class="lbl" font-size="8" fill="#44ff88" font-weight="700">-&gt; Reactor</text>
  <text x="631" y="673" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">200s/cell</text>

  <!-- Kovarex note -->
  <text x="720" y="658" class="lbl" font-size="7" fill="#ffaa44">Kovarex:</text>
  <text x="720" y="670" class="lbl" font-size="7" fill="#ffaa44">40 U-235</text>
  <text x="720" y="682" class="lbl" font-size="7" fill="#ffaa44">then infinite</text>

  <!-- =================================================================== -->
  <!-- SECTION 5: NOTES (y 700 - 740) -->
  <!-- =================================================================== -->
  <rect x="40" y="700" width="680" height="32" rx="4" fill="#0a0a18" stroke="#222" stroke-width="0.5"/>
  <text x="50" y="718" class="lbl" font-size="7" fill="#555">Notes: 1 offshore pump feeds 12 heat exchangers. 3 parallel heat pipes min for 2x2. 50+ steam tanks before circuit-controlled fuel. Touching reactors get +100pct each.</text>

</svg>
''')

out = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\diagrams\nuclear-reactor-layout.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"SVG written: {out}")
print(f"Size: {len(svg)} bytes")
print(f"viewBox height: 1200")
