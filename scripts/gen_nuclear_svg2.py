#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate nuclear-reactor-layout.svg - narrow vertical, zero overlap."""
import textwrap

svg = textwrap.dedent(r'''\
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 980" width="760" height="980">
  <defs>
    <style>
      .lbl { font-family: "Segoe UI", Arial, sans-serif; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="760" height="980" fill="#12121f" rx="10"/>

  <!-- ========== TITLE BAR ========== -->
  <rect x="0" y="0" width="760" height="48" fill="#0a1628" rx="10"/>
  <text x="380" y="32" text-anchor="middle" class="lbl" font-size="14" font-weight="900" fill="#44ff88" letter-spacing="2">NUCLEAR POWER - 2x2 REACTOR LAYOUT</text>

  <!-- ============================================================= -->
  <!-- SECTION 1: REACTORS (y: 65 - 260) -->
  <!-- ============================================================= -->
  <text x="380" y="80" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">1. REACTORS (4x) - neighbor bonus math</text>

  <!-- Reactor A (top-left) -->
  <rect x="150" y="96" width="100" height="52" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="200" y="120" text-anchor="middle" class="lbl" font-size="11" fill="#44ff88" font-weight="700">A</text>
  <text x="200" y="136" text-anchor="middle" class="lbl" font-size="7" fill="#999">1 neighbor = 80 MW</text>

  <!-- Reactor B (top-right) -->
  <rect x="280" y="96" width="100" height="52" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="330" y="120" text-anchor="middle" class="lbl" font-size="11" fill="#44ff88" font-weight="700">B</text>
  <text x="330" y="136" text-anchor="middle" class="lbl" font-size="7" fill="#ffaa44">2 nbr = 160 MW</text>

  <!-- Reactor C (bottom-left) -->
  <rect x="150" y="164" width="100" height="52" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="200" y="188" text-anchor="middle" class="lbl" font-size="11" fill="#44ff88" font-weight="700">C</text>
  <text x="200" y="204" text-anchor="middle" class="lbl" font-size="7" fill="#999">1 neighbor = 80 MW</text>

  <!-- Reactor D (bottom-right) -->
  <rect x="280" y="164" width="100" height="52" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="330" y="188" text-anchor="middle" class="lbl" font-size="11" fill="#44ff88" font-weight="700">D</text>
  <text x="330" y="204" text-anchor="middle" class="lbl" font-size="7" fill="#ffaa44">2 nbr = 160 MW</text>

  <!-- Neighbor bonus: A-B (horizontal) -->
  <line x1="250" y1="115" x2="280" y2="115" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="265" y="111" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: C-D (horizontal) -->
  <line x1="250" y1="183" x2="280" y2="183" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="265" y="179" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: A-C (vertical) -->
  <line x1="200" y1="148" x2="200" y2="164" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="210" y="160" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: B-D (vertical) -->
  <line x1="330" y1="148" x2="330" y2="164" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="340" y="160" class="lbl" font-size="7" fill="#ffaa44">+300%</text>

  <!-- Total output -->
  <rect x="150" y="232" width="230" height="24" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1"/>
  <text x="265" y="248" text-anchor="middle" class="lbl" font-size="11" fill="#ffaa44" font-weight="700">TOTAL: 480 MW (4 reactors)</text>

  <!-- ============================================================= -->
  <!-- SECTION 2: HEAT PIPES + HEAT EXCHANGERS + TURBINES (y: 275 - 620) -->
  <!-- Horizontal flow: Pipes -> HX -> Turbines -> Water -->
  <!-- ============================================================= -->
  <text x="380" y="295" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">2. HEAT FLOW (left to right)</text>

  <!-- (a) Heat Pipes - left -->
  <text x="110" y="320" text-anchor="middle" class="lbl" font-size="9" fill="#cc7733" font-weight="700">Heat Pipes</text>
  <text x="110" y="333" text-anchor="middle" class="lbl" font-size="7" fill="#aa7744">3 parallel</text>
  <rect x="80" y="342" width="16" height="110" rx="3" fill="#2a1a0a" stroke="#cc7733" stroke-width="1.2"/>
  <rect x="102" y="342" width="16" height="110" rx="3" fill="#2a1a0a" stroke="#cc7733" stroke-width="1.2"/>
  <rect x="124" y="342" width="16" height="110" rx="3" fill="#2a1a0a" stroke="#cc7733" stroke-width="1.2"/>
  <text x="110" y="380" text-anchor="middle" class="lbl" font-size="7" fill="#cc7733">1000C</text>
  <text x="110" y="393" text-anchor="middle" class="lbl" font-size="7" fill="#aa7744">to</text>
  <text x="110" y="405" text-anchor="middle" class="lbl" font-size="7" fill="#aa7744">500C</text>

  <!-- Arrow: pipes -> HX -->
  <line x1="142" y1="395" x2="195" y2="395" stroke="#ff6644" stroke-width="2"/>
  <polygon points="193,391 199,395 193,399" fill="#ff6644"/>

  <!-- (b) Heat Exchangers - center left -->
  <text x="330" y="320" text-anchor="middle" class="lbl" font-size="9" fill="#ff6644" font-weight="700">Heat Exchangers x48</text>
  <text x="330" y="333" text-anchor="middle" class="lbl" font-size="7" fill="#884422">12 per reactor / 500C steam out</text>

  <rect x="210" y="357" width="200" height="18" rx="3" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.2"/>
  <text x="310" y="370" text-anchor="middle" class="lbl" font-size="8" fill="#ff6644">x12  -  500C steam</text>

  <rect x="210" y="381" width="200" height="18" rx="3" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.2"/>
  <text x="310" y="394" text-anchor="middle" class="lbl" font-size="8" fill="#ff6644">x12  -  500C steam</text>

  <rect x="210" y="405" width="200" height="18" rx="3" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.2"/>
  <text x="310" y="418" text-anchor="middle" class="lbl" font-size="8" fill="#ff6644">x12  -  500C steam</text>

  <rect x="210" y="429" width="200" height="18" rx="3" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.2"/>
  <text x="310" y="442" text-anchor="middle" class="lbl" font-size="8" fill="#ff6644">x12  -  500C steam</text>

  <!-- Arrow: HX -> Turbines -->
  <line x1="412" y1="410" x2="455" y2="410" stroke="#88ccff" stroke-width="2"/>
  <polygon points="453,406 459,410 453,414" fill="#88ccff"/>

  <!-- (c) Steam Turbines - center right -->
  <text x="570" y="320" text-anchor="middle" class="lbl" font-size="9" fill="#88ccff" font-weight="700">Steam Turbines x84</text>
  <text x="570" y="333" text-anchor="middle" class="lbl" font-size="7" fill="#445566">21 per reactor / 5.8 MW each</text>

  <rect x="470" y="357" width="180" height="18" rx="3" fill="#0a1628" stroke="#88ccff" stroke-width="1.2"/>
  <text x="560" y="370" text-anchor="middle" class="lbl" font-size="8" fill="#88ccff">x21  -  121.8 MW</text>

  <rect x="470" y="381" width="180" height="18" rx="3" fill="#0a1628" stroke="#88ccff" stroke-width="1.2"/>
  <text x="560" y="394" text-anchor="middle" class="lbl" font-size="8" fill="#88ccff">x21  -  121.8 MW</text>

  <rect x="470" y="405" width="180" height="18" rx="3" fill="#0a1628" stroke="#88ccff" stroke-width="1.2"/>
  <text x="560" y="418" text-anchor="middle" class="lbl" font-size="8" fill="#88ccff">x21  -  121.8 MW</text>

  <rect x="470" y="429" width="180" height="18" rx="3" fill="#0a1628" stroke="#88ccff" stroke-width="1.2"/>
  <text x="560" y="442" text-anchor="middle" class="lbl" font-size="8" fill="#88ccff">x21  -  121.8 MW</text>

  <!-- Arrow: Water -> HX (from right) -->
  <line x1="660" y1="410" x2="690" y2="410" stroke="#44aaff" stroke-width="1.5" stroke-dasharray="3"/>
  <polygon points="690,406 696,410 690,414" fill="#44aaff"/>

  <!-- (d) Water supply - far right -->
  <rect x="700" y="357" width="36" height="90" rx="4" fill="#0a1a2a" stroke="#44aaff" stroke-width="1.2"/>
  <text x="718" y="390" text-anchor="middle" class="lbl" font-size="8" fill="#44aaff" font-weight="700">H2O</text>
  <text x="718" y="405" text-anchor="middle" class="lbl" font-size="7" fill="#4488cc">4x</text>
  <text x="718" y="417" text-anchor="middle" class="lbl" font-size="6" fill="#4488cc">pumps</text>

  <!-- ============================================================= -->
  <!-- SECTION 3: SUMMARY BAR (y: 500 - 595) -->
  <!-- ============================================================= -->
  <rect x="40" y="508" width="680" height="87" rx="6" fill="#0a1628" stroke="#44ff88" stroke-width="1.5"/>

  <text x="380" y="534" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="900">2x2 REACTOR = 480 MW TOTAL</text>

  <line x1="40" y1="546" x2="720" y2="546" stroke="#1a3a1a" stroke-width="0.5"/>

  <!-- 5 stat columns, evenly spaced: 40 + n*160 -->
  <text x="104" y="564" text-anchor="middle" class="lbl" font-size="7" fill="#666">REACTORS</text>
  <text x="104" y="584" text-anchor="middle" class="lbl" font-size="11" fill="#44ff88" font-weight="700">4</text>
  <text x="104" y="596" text-anchor="middle" class="lbl" font-size="6" fill="#444">+bonus</text>

  <text x="232" y="564" text-anchor="middle" class="lbl" font-size="7" fill="#666">HEAT EXCHANGERS</text>
  <text x="232" y="584" text-anchor="middle" class="lbl" font-size="11" fill="#ff6644" font-weight="700">48</text>
  <text x="232" y="596" text-anchor="middle" class="lbl" font-size="6" fill="#444">12/rct</text>

  <text x="360" y="564" text-anchor="middle" class="lbl" font-size="7" fill="#666">TURBINES</text>
  <text x="360" y="584" text-anchor="middle" class="lbl" font-size="11" fill="#88ccff" font-weight="700">84</text>
  <text x="360" y="596" text-anchor="middle" class="lbl" font-size="6" fill="#444">21/rct</text>

  <text x="488" y="564" text-anchor="middle" class="lbl" font-size="7" fill="#666">OFFSHORE PUMPS</text>
  <text x="488" y="584" text-anchor="middle" class="lbl" font-size="11" fill="#44aaff" font-weight="700">4</text>
  <text x="488" y="596" text-anchor="middle" class="lbl" font-size="6" fill="#444">1/12HX</text>

  <text x="616" y="564" text-anchor="middle" class="lbl" font-size="7" fill="#666">FUEL CELLS/HR</text>
  <text x="616" y="584" text-anchor="middle" class="lbl" font-size="11" fill="#ffaa44" font-weight="700">~72</text>
  <text x="616" y="596" text-anchor="middle" class="lbl" font-size="6" fill="#444">18/rct</text>

  <!-- ============================================================= -->
  <!-- SECTION 4: FUEL CYCLE (y: 615 - 690) -->
  <!-- ============================================================= -->
  <text x="380" y="633" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">3. FUEL CYCLE</text>

  <!-- Node 1: Mining -->
  <rect x="100" y="648" width="100" height="34" rx="4" fill="#1a1a2e" stroke="#555" stroke-width="1"/>
  <text x="150" y="663" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Uranium Mining</text>
  <text x="150" y="675" text-anchor="middle" class="lbl" font-size="7" fill="#555">1 drill</text>

  <!-- Arrow 1->2 -->
  <line x1="202" y1="665" x2="232" y2="665" stroke="#555" stroke-width="1.5"/>
  <polygon points="230,661 236,665 230,669" fill="#555"/>

  <!-- Node 2: Centrifuge -->
  <rect x="238" y="648" width="100" height="34" rx="4" fill="#1a1a2e" stroke="#888" stroke-width="1"/>
  <text x="288" y="663" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Centrifuge x5</text>
  <text x="288" y="675" text-anchor="middle" class="lbl" font-size="7" fill="#555">0.7pct U-235</text>

  <!-- Arrow 2->3 -->
  <line x1="340" y1="665" x2="370" y2="665" stroke="#555" stroke-width="1.5"/>
  <polygon points="368,661 374,665 368,669" fill="#555"/>

  <!-- Node 3: Fuel Assembler -->
  <rect x="376" y="648" width="110" height="34" rx="4" fill="#1a1a2e" stroke="#aa8800" stroke-width="1"/>
  <text x="431" y="663" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Fuel Assembler</text>
  <text x="431" y="675" text-anchor="middle" class="lbl" font-size="7" fill="#aa8800">19 U-238 + 1 U-235</text>

  <!-- Arrow 3->4 -->
  <line x1="488" y1="665" x2="518" y2="665" stroke="#555" stroke-width="1.5"/>
  <polygon points="516,661 522,665 516,669" fill="#555"/>

  <!-- Node 4: Reactor -->
  <rect x="524" y="648" width="100" height="34" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1.5"/>
  <text x="574" y="663" text-anchor="middle" class="lbl" font-size="8" fill="#44ff88" font-weight="700">-&gt; Reactor</text>
  <text x="574" y="675" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">200s/cell</text>

  <!-- Kovarex -->
  <text x="660" y="660" class="lbl" font-size="7" fill="#ffaa44">Kovarex: 40 U-235</text>
  <text x="660" y="672" class="lbl" font-size="7" fill="#ffaa44">then infinite fuel</text>

  <!-- ============================================================= -->
  <!-- NOTES (y: 710 - 740) -->
  <!-- ============================================================= -->
  <rect x="40" y="710" width="680" height="36" rx="4" fill="#0a0a18" stroke="#222" stroke-width="0.5"/>
  <text x="50" y="728" class="lbl" font-size="7" fill="#555">Notes: 1 offshore pump feeds 12 heat exchangers. 3 parallel heat pipes minimum. 50+ steam tanks before circuit-controlled fuel. Neighbor bonus: each touching reactor adds +100pct output.</text>

</svg>
''')

out = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\diagrams\nuclear-reactor-layout.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"SVG written: {out}")
print(f"Size: {len(svg)} bytes")
