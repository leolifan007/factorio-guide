#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate nuclear-reactor-layout.svg - vertical stack, zero overlap."""
import textwrap

svg = textwrap.dedent(r'''\
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 920" width="760" height="920">
  <defs>
    <style>
      .lbl { font-family: "Segoe UI", Arial, sans-serif; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="760" height="920" fill="#12121f" rx="10"/>

  <!-- ========== TITLE BAR ========== -->
  <rect x="0" y="0" width="760" height="48" fill="#0a1628" rx="10"/>
  <text x="380" y="32" text-anchor="middle" class="lbl" font-size="14" font-weight="900" fill="#44ff88" letter-spacing="2">NUCLEAR POWER - 2x2 REACTOR LAYOUT</text>

  <!-- =================================================================== -->
  <!-- SECTION 1: REACTORS (y 65 - 238) -->
  <!-- =================================================================== -->
  <text x="380" y="80" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">1. REACTORS (4x) - Neighbor Bonus</text>

  <!-- Reactor A (top-left) -->
  <rect x="160" y="96" width="110" height="58" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="215" y="125" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">A</text>
  <text x="215" y="143" text-anchor="middle" class="lbl" font-size="8" fill="#999">1 nbr = 80 MW</text>

  <!-- Reactor B (top-right) -->
  <rect x="290" y="96" width="110" height="58" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="345" y="125" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">B</text>
  <text x="345" y="143" text-anchor="middle" class="lbl" font-size="8" fill="#ffaa44">2 nbr = 160 MW</text>

  <!-- Reactor C (bottom-left) -->
  <rect x="160" y="166" width="110" height="58" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="215" y="195" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">C</text>
  <text x="215" y="213" text-anchor="middle" class="lbl" font-size="8" fill="#999">1 nbr = 80 MW</text>

  <!-- Reactor D (bottom-right) -->
  <rect x="290" y="166" width="110" height="58" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="345" y="195" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">D</text>
  <text x="345" y="213" text-anchor="middle" class="lbl" font-size="8" fill="#ffaa44">2 nbr = 160 MW</text>

  <!-- Neighbor bonus: A-B (horizontal) -->
  <line x1="270" y1="118" x2="290" y2="118" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="280" y="114" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: C-D (horizontal) -->
  <line x1="270" y1="188" x2="290" y2="188" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="280" y="184" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: A-C (vertical) -->
  <line x1="215" y1="154" x2="215" y2="166" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="225" y="164" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: B-D (vertical) -->
  <line x1="345" y1="154" x2="345" y2="166" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="355" y="164" class="lbl" font-size="7" fill="#ffaa44">+300%</text>

  <!-- Total output -->
  <rect x="160" y="238" width="240" height="22" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1"/>
  <text x="280" y="253" text-anchor="middle" class="lbl" font-size="11" fill="#ffaa44" font-weight="700">Total: 480 MW (4 reactors)</text>

  <!-- =================================================================== -->
  <!-- ARROW: Reactors -> Heat System -->
  <!-- =================================================================== -->
  <line x1="380" y1="272" x2="380" y2="302" stroke="#888" stroke-width="2"/>
  <polygon points="376,296 380,304 384,296" fill="#888"/>
  <text x="394" y="290" class="lbl" font-size="8" fill="#888">1000C heat</text>

  <!-- =================================================================== -->
  <!-- SECTION 2: HEAT FLOW - horizontal left to right (y 308 - 470) -->
  <!-- =================================================================== -->
  <text x="380" y="324" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">2. HEAT FLOW (left to right)</text>

  <!-- Block 1: Heat Pipes -->
  <rect x="60" y="338" width="120" height="70" rx="5" fill="#1a0a04" stroke="#cc7733" stroke-width="1.5"/>
  <text x="120" y="358" text-anchor="middle" class="lbl" font-size="9" fill="#cc7733" font-weight="700">HEAT PIPES</text>
  <text x="120" y="373" text-anchor="middle" class="lbl" font-size="8" fill="#aa7744">3 parallel</text>
  <text x="120" y="388" text-anchor="middle" class="lbl" font-size="7" fill="#aa7744">1000C from reactor</text>
  <text x="120" y="401" text-anchor="middle" class="lbl" font-size="7" fill="#aa7744">500C to exchanger</text>

  <!-- Arrow 1 -> 2 -->
  <line x1="182" y1="373" x2="218" y2="373" stroke="#cc7733" stroke-width="2"/>
  <polygon points="216,369 222,373 216,377" fill="#cc7733"/>

  <!-- Block 2: Heat Exchangers -->
  <rect x="222" y="338" width="160" height="70" rx="5" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.5"/>
  <text x="302" y="358" text-anchor="middle" class="lbl" font-size="9" fill="#ff6644" font-weight="700">HEAT EXCHANGERS</text>
  <text x="302" y="373" text-anchor="middle" class="lbl" font-size="8" fill="#ff6644">x48 (12 per reactor)</text>
  <text x="302" y="388" text-anchor="middle" class="lbl" font-size="7" fill="#884422">Input: 1000C heat</text>
  <text x="302" y="401" text-anchor="middle" class="lbl" font-size="7" fill="#884422">Output: 500C steam</text>

  <!-- Arrow 2 -> 3 -->
  <line x1="384" y1="373" x2="420" y2="373" stroke="#ff6644" stroke-width="2"/>
  <polygon points="418,369" 424,373 418,377" fill="#ff6644"/>

  <!-- Block 3: Steam Turbines -->
  <rect x="424" y="338" width="160" height="70" rx="5" fill="#0a1028" stroke="#88ccff" stroke-width="1.5"/>
  <text x="504" y="358" text-anchor="middle" class="lbl" font-size="9" fill="#88ccff" font-weight="700">STEAM TURBINES</text>
  <text x="504" y="373" text-anchor="middle" class="lbl" font-size="8" fill="#88ccff">x84 (21 per reactor)</text>
  <text x="504" y="388" text-anchor="middle" class="lbl" font-size="7" fill="#445566">Input: 500C steam</text>
  <text x="504" y="401" text-anchor="middle" class="lbl" font-size="7" fill="#445566">Output: 480 MW total</text>

  <!-- Water label (above turbines) -->
  <text x="620" y="358" text-anchor="middle" class="lbl" font-size="8" fill="#44aaff">H2O</text>
  <rect x="608" y="346" width="28" height="54" rx="3" fill="#0a1a2a" stroke="#44aaff" stroke-width="1"/>
  <text x="622" y="375" text-anchor="middle" class="lbl" font-size="6" fill="#4488cc">4x</text>
  <text x="622" y="387" text-anchor="middle" class="lbl" font-size="6" fill="#4488cc">pump</text>

  <!-- Arrow: water -> HX (dashed, from right) -->
  <line x1="580" y1="380" x2="608" y2="380" stroke="#44aaff" stroke-width="1.2" stroke-dasharray="3"/>
  <polygon points="606,376 612,380 606,384" fill="#44aaff"/>

  <!-- =================================================================== -->
  <!-- ARROW: Heat System -> Summary -->
  <!-- =================================================================== -->
  <line x1="380" y1="420" x2="380" y2="450" stroke="#888" stroke-width="2"/>
  <polygon points="376,444 380,452 384,444" fill="#888"/>

  <!-- =================================================================== -->
  <!-- SECTION 3: SUMMARY BAR (y 456 - 549) -->
  <!-- =================================================================== -->
  <rect x="40" y="456" width="680" height="93" rx="6" fill="#0a1628" stroke="#44ff88" stroke-width="1.5"/>

  <text x="380" y="482" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="900">2x2 REACTOR = 480 MW TOTAL</text>

  <line x1="40" y1="494" x2="720" y2="494" stroke="#1a3a1a" stroke-width="0.5"/>

  <!-- 5 stat columns, evenly spaced: 40 + i*160 -->
  <text x="104" y="512" text-anchor="middle" class="lbl" font-size="8" fill="#666">REACTORS</text>
  <text x="104" y="532" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="700">4</text>
  <text x="104" y="544" text-anchor="middle" class="lbl" font-size="7" fill="#444">+bonus</text>

  <text x="232" y="512" text-anchor="middle" class="lbl" font-size="8" fill="#666">HEAT EXCHANGERS</text>
  <text x="232" y="532" text-anchor="middle" class="lbl" font-size="13" fill="#ff6644" font-weight="700">48</text>
  <text x="232" y="544" text-anchor="middle" class="lbl" font-size="7" fill="#444">12/rct</text>

  <text x="360" y="512" text-anchor="middle" class="lbl" font-size="8" fill="#666">TURBINES</text>
  <text x="360" y="532" text-anchor="middle" class="lbl" font-size="13" fill="#88ccff" font-weight="700">84</text>
  <text x="360" y="544" text-anchor="middle" class="lbl" font-size="7" fill="#444">21/rct</text>

  <text x="488" y="512" text-anchor="middle" class="lbl" font-size="8" fill="#666">OFFSHORE PUMPS</text>
  <text x="488" y="532" text-anchor="middle" class="lbl" font-size="13" fill="#44aaff" font-weight="700">4</text>
  <text x="488" y="544" text-anchor="middle" class="lbl" font-size="7" fill="#444">1/12 HX</text>

  <text x="616" y="512" text-anchor="middle" class="lbl" font-size="8" fill="#666">FUEL CELLS/HR</text>
  <text x="616" y="532" text-anchor="middle" class="lbl" font-size="13" fill="#ffaa44" font-weight="700">~72</text>
  <text x="616" y="544" text-anchor="middle" class="lbl" font-size="7" fill="#444">18/rct</text>

  <!-- =================================================================== -->
  <!-- ARROW: Summary -> Fuel Cycle -->
  <!-- =================================================================== -->
  <line x1="380" y1="555" x2="380" y2="585" stroke="#555" stroke-width="1.5"/>
  <polygon points="376,579 380,587 384,579" fill="#555"/>

  <!-- =================================================================== -->
  <!-- SECTION 4: FUEL CYCLE (y 591 - 655) -->
  <!-- =================================================================== -->
  <text x="380" y="607" text-anchor="middle" class="lbl" font-size="12" fill="#aaaaaa" font-weight="700">3. FUEL CYCLE</text>

  <!-- Node 1: Mining -->
  <rect x="100" y="621" width="110" height="34" rx="4" fill="#1a1a2e" stroke="#555" stroke-width="1"/>
  <text x="155" y="637" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Uranium Mining</text>
  <text x="155" y="649" text-anchor="middle" class="lbl" font-size="7" fill="#555">1 drill</text>

  <!-- Arrow 1->2 -->
  <line x1="212" y1="638" x2="244" y2="638" stroke="#555" stroke-width="1.5"/>
  <polygon points="242,634 248,638 242,642" fill="#555"/>

  <!-- Node 2: Centrifuge -->
  <rect x="250" y="621" width="110" height="34" rx="4" fill="#1a1a2e" stroke="#888" stroke-width="1"/>
  <text x="305" y="637" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Centrifuge x5</text>
  <text x="305" y="649" text-anchor="middle" class="lbl" font-size="7" fill="#555">0.7pct U-235</text>

  <!-- Arrow 2->3 -->
  <line x1="362" y1="638" x2="394" y2="638" stroke="#555" stroke-width="1.5"/>
  <polygon points="392,634 398,638 392,642" fill="#555"/>

  <!-- Node 3: Fuel Assembler -->
  <rect x="400" y="621" width="120" height="34" rx="4" fill="#1a1a2e" stroke="#aa8800" stroke-width="1"/>
  <text x="460" y="637" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Fuel Assembler</text>
  <text x="460" y="649" text-anchor="middle" class="lbl" font-size="7" fill="#aa8800">19 U-238 + 1 U-235</text>

  <!-- Arrow 3->4 -->
  <line x1="522" y1="638" x2="554" y2="638" stroke="#555" stroke-width="1.5"/>
  <polygon points="552,634 558,638 552,642" fill="#555"/>

  <!-- Node 4: Reactor -->
  <rect x="560" y="621" width="100" height="34" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1.5"/>
  <text x="610" y="637" text-anchor="middle" class="lbl" font-size="8" fill="#44ff88" font-weight="700">-&gt; Reactor</text>
  <text x="610" y="649" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">200s/cell</text>

  <!-- Kovarex note -->
  <text x="690" y="635" class="lbl" font-size="7" fill="#ffaa44">Kovarex:</text>
  <text x="690" y="647" class="lbl" font-size="7" fill="#ffaa44">40 U-235</text>
  <text x="690" y="659" class="lbl" font-size="7" fill="#ffaa44">then infinite</text>

  <!-- =================================================================== -->
  <!-- SECTION 5: NOTES (y 680 - 720) -->
  <!-- =================================================================== -->
  <rect x="40" y="680" width="680" height="32" rx="4" fill="#0a0a18" stroke="#222" stroke-width="0.5"/>
  <text x="50" y="698" class="lbl" font-size="7" fill="#555">Notes: 1 offshore pump feeds 12 heat exchangers. 3 parallel heat pipes minimum for 2x2. 50+ steam tanks before circuit-controlled fuel. Touching reactors get +100pct each.</text>

</svg>
''')

out = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\diagrams\nuclear-reactor-layout.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"SVG written: {out}")
print(f"Size: {len(svg)} bytes")
