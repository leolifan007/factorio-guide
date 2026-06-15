#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate nuclear-reactor-layout.svg - vertical stack, strictly no overlap."""
import textwrap

svg = textwrap.dedent(r'''\
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 1300" width="760" height="1300">
  <defs>
    <style>
      .lbl { font-family: "Segoe UI", Arial, sans-serif; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="760" height="1300" fill="#12121f" rx="10"/>

  <!-- ========== TITLE BAR ========== -->
  <rect x="0" y="0" width="760" height="50" fill="#0a1628" rx="10"/>
  <text x="380" y="33" text-anchor="middle" class="lbl" font-size="15" font-weight="900" fill="#44ff88" letter-spacing="2">NUCLEAR POWER - 2x2 REACTOR LAYOUT</text>

  <!-- ==================================================================================== -->
  <!-- SECTION 1: REACTORS (y 65 - 270) -->
  <!-- ==================================================================================== -->
  <text x="380" y="82" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">1. REACTORS (4x) - Neighbor Bonus Math</text>

  <!-- Reactor A (top-left) -->
  <rect x="140" y="100" width="100" height="58" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="190" y="128" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">A</text>
  <text x="190" y="146" text-anchor="middle" class="lbl" font-size="8" fill="#999999">1 nbr = 80 MW</text>

  <!-- Reactor B (top-right) -->
  <rect x="260" y="100" width="100" height="58" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="310" y="128" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">B</text>
  <text x="310" y="146" text-anchor="middle" class="lbl" font-size="8" fill="#ffaa44">2 nbr = 160 MW</text>

  <!-- Reactor C (bottom-left) -->
  <rect x="140" y="170" width="100" height="58" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="190" y="198" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">C</text>
  <text x="190" y="216" text-anchor="middle" class="lbl" font-size="8" fill="#999999">1 nbr = 80 MW</text>

  <!-- Reactor D (bottom-right) -->
  <rect x="260" y="170" width="100" height="58" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="310" y="198" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">D</text>
  <text x="310" y="216" text-anchor="middle" class="lbl" font-size="8" fill="#ffaa44">2 nbr = 160 MW</text>

  <!-- Neighbor bonus: A-B (horizontal) -->
  <line x1="240" y1="120" x2="260" y2="120" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="250" y="116" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: C-D (horizontal) -->
  <line x1="240" y1="190" x2="260" y2="190" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="250" y="186" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: A-C (vertical) -->
  <line x1="190" y1="158" x2="190" y2="170" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="200" y="168" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: B-D (vertical) -->
  <line x1="310" y1="158" x2="310" y2="170" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="320" y="168" class="lbl" font-size="7" fill="#ffaa44">+300%</text>

  <!-- Total output -->
  <rect x="140" y="244" width="220" height="24" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1"/>
  <text x="250" y="260" text-anchor="middle" class="lbl" font-size="11" fill="#ffaa44" font-weight="700">TOTAL: 480 MW (4 reactors)</text>

  <!-- Down arrow to next section -->
  <line x1="380" y1="276" x2="380" y2="306" stroke="#444444" stroke-width="2"/>
  <polygon points="376,300 380,308 384,300" fill="#444444"/>
  <text x="394" y="294" class="lbl" font-size="8" fill="#666666">1000C heat out</text>

  <!-- ==================================================================================== -->
  <!-- SECTION 2: HEAT FLOW - horizontal left to right (y 316 - 530) -->
  <!-- Each block is on its OWN horizontal band, no vertical overlap -->
  <!-- ==================================================================================== -->
  <text x="380" y="332" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">2. HEAT FLOW (left to right)</text>

  <!-- Block 1: Heat Pipes (left) -->
  <rect x="40" y="348" width="140" height="80" rx="5" fill="#1a0a04" stroke="#cc7733" stroke-width="1.5"/>
  <text x="110" y="372" text-anchor="middle" class="lbl" font-size="10" fill="#cc7733" font-weight="700">HEAT PIPES</text>
  <text x="110" y="388" text-anchor="middle" class="lbl" font-size="8" fill="#aa7744">3 parallel</text>
  <text x="110" y="403" text-anchor="middle" class="lbl" font-size="7" fill="#cc7733">1000C from reactor</text>
  <text x="110" y="418" text-anchor="middle" class="lbl" font-size="7" fill="#aa7744">500C to exchanger</text>

  <!-- Arrow: Pipes -> HX -->
  <line x1="182" y1="388" x2="218" y2="388" stroke="#cc7733" stroke-width="2"/>
  <polygon points="216,384 222,388 216,392" fill="#cc7733"/>

  <!-- Block 2: Heat Exchangers (center) -->
  <rect x="224" y="348" width="200" height="80" rx="5" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.5"/>
  <text x="324" y="372" text-anchor="middle" class="lbl" font-size="10" fill="#ff6644" font-weight="700">HEAT EXCHANGERS</text>
  <text x="324" y="388" text-anchor="middle" class="lbl" font-size="8" fill="#ff6644">x48 (12 per reactor)</text>
  <text x="324" y="403" text-anchor="middle" class="lbl" font-size="7" fill="#884422">Input: 1000C heat</text>
  <text x="324" y="418" text-anchor="middle" class="lbl" font-size="7" fill="#884422">Output: 500C steam</text>

  <!-- Arrow: HX -> Turbines -->
  <line x1="426" y1="388" x2="462" y2="388" stroke="#ff6644" stroke-width="2"/>
  <polygon points="460,384 466,388 460,392" fill="#ff6644"/>

  <!-- Block 3: Steam Turbines (right) -->
  <rect x="468" y="348" width="180" height="80" rx="5" fill="#0a1028" stroke="#88ccff" stroke-width="1.5"/>
  <text x="558" y="372" text-anchor="middle" class="lbl" font-size="10" fill="#88ccff" font-weight="700">STEAM TURBINES</text>
  <text x="558" y="388" text-anchor="middle" class="lbl" font-size="8" fill="#88ccff">x84 (21 per reactor)</text>
  <text x="558" y="403" text-anchor="middle" class="lbl" font-size="7" fill="#445566">Input: 500C steam</text>
  <text x="558" y="418" text-anchor="middle" class="lbl" font-size="7" fill="#445566">Output: 480 MW total</text>

  <!-- Water (far right, above turbines) -->
  <rect x="660" y="368" width="36" height="50" rx="4" fill="#0a1a2a" stroke="#44aaff" stroke-width="1.2"/>
  <text x="678" y="393" text-anchor="middle" class="lbl" font-size="8" fill="#44aaff" font-weight="700">H2O</text>
  <text x="678" y="407" text-anchor="middle" class="lbl" font-size="7" fill="#4488cc">4x</text>
  <text x="678" y="419" text-anchor="middle" class="lbl" font-size="6" fill="#4488cc">pumps</text>

  <!-- Water arrow (dashed) -->
  <line x1="648" y1="393" x2="660" y2="393" stroke="#44aaff" stroke-width="1.2" stroke-dasharray="3"/>
  <polygon points="658,389 664,393 658,397" fill="#44aaff"/>

  <!-- Down arrow to summary -->
  <line x1="380" y1="442" x2="380" y2="472" stroke="#444444" stroke-width="2"/>
  <polygon points="376,466 380,474 384,466" fill="#444444"/>

  <!-- ==================================================================================== -->
  <!-- SECTION 3: SUMMARY BAR (y 480 - 573) -->
  <!-- ==================================================================================== -->
  <rect x="40" y="480" width="680" height="93" rx="6" fill="#0a1628" stroke="#44ff88" stroke-width="1.5"/>

  <text x="380" y="506" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="900">2x2 REACTOR = 480 MW TOTAL</text>

  <line x1="40" y1="518" x2="720" y2="518" stroke="#1a3a1a" stroke-width="0.5"/>

  <!-- 5 stat columns, evenly spaced: 40 + i*160 -->
  <text x="104" y="536" text-anchor="middle" class="lbl" font-size="8" fill="#666666">REACTORS</text>
  <text x="104" y="556" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="700">4</text>
  <text x="104" y="568" text-anchor="middle" class="lbl" font-size="7" fill="#444444">neighbor bonus</text>

  <text x="264" y="536" text-anchor="middle" class="lbl" font-size="8" fill="#666666">HEAT EXCHANGERS</text>
  <text x="264" y="556" text-anchor="middle" class="lbl" font-size="13" fill="#ff6644" font-weight="700">48</text>
  <text x="264" y="568" text-anchor="middle" class="lbl" font-size="7" fill="#444444">12 per rct</text>

  <text x="424" y="536" text-anchor="middle" class="lbl" font-size="8" fill="#666666">STEAM TURBINES</text>
  <text x="424" y="556" text-anchor="middle" class="lbl" font-size="13" fill="#88ccff" font-weight="700">84</text>
  <text x="424" y="568" text-anchor="middle" class="lbl" font-size="7" fill="#444444">21 per rct</text>

  <text x="584" y="536" text-anchor="middle" class="lbl" font-size="8" fill="#666666">OFFSHORE PUMPS</text>
  <text x="584" y="556" text-anchor="middle" class="lbl" font-size="13" fill="#44aaff" font-weight="700">4</text>
  <text x="584" y="568" text-anchor="middle" class="lbl" font-size="7" fill="#444444">1 per 12 HX</text>

  <text x="720" y="536" text-anchor="middle" class="lbl" font-size="8" fill="#666666">FUEL CELLS/HR</text>
  <text x="720" y="556" text-anchor="middle" class="lbl" font-size="13" fill="#ffaa44" font-weight="700">~72</text>
  <text x="720" y="568" text-anchor="middle" class="lbl" font-size="7" fill="#444444">18 per rct</text>

  <!-- Down arrow to fuel cycle -->
  <line x1="380" y1="579" x2="380" y2="609" stroke="#444444" stroke-width="1.5"/>
  <polygon points="376,603 380,611 384,603" fill="#444444"/>

  <!-- ==================================================================================== -->
  <!-- SECTION 4: FUEL CYCLE (y 619 - 690) -->
  <!-- ==================================================================================== -->
  <text x="380" y="635" text-anchor="middle" class="lbl" font-size="12" fill="#aaaaaa" font-weight="700">3. FUEL CYCLE</text>

  <!-- Node 1: Mining -->
  <rect x="80" y="649" width="110" height="38" rx="4" fill="#1a1a2e" stroke="#555555" stroke-width="1"/>
  <text x="135" y="666" text-anchor="middle" class="lbl" font-size="8" fill="#cccccc">Uranium Mining</text>
  <text x="135" y="678" text-anchor="middle" class="lbl" font-size="7" fill="#555555">1 drill</text>

  <!-- Arrow 1->2 -->
  <line x1="192" y1="668" x2="222" y2="668" stroke="#555555" stroke-width="1.5"/>
  <polygon points="220,664 226,668 220,672" fill="#555555"/>

  <!-- Node 2: Centrifuge -->
  <rect x="228" y="649" width="110" height="38" rx="4" fill="#1a1a2e" stroke="#888888" stroke-width="1"/>
  <text x="283" y="666" text-anchor="middle" class="lbl" font-size="8" fill="#cccccc">Centrifuge x5</text>
  <text x="283" y="678" text-anchor="middle" class="lbl" font-size="7" fill="#555555">0.7pct to U-235</text>

  <!-- Arrow 2->3 -->
  <line x1="340" y1="668" x2="370" y2="668" stroke="#555555" stroke-width="1.5"/>
  <polygon points="368,664 374,668 368,672" fill="#555555"/>

  <!-- Node 3: Fuel Assembler -->
  <rect x="376" y="649" width="120" height="38" rx="4" fill="#1a1a2e" stroke="#aa8800" stroke-width="1"/>
  <text x="436" y="666" text-anchor="middle" class="lbl" font-size="8" fill="#cccccc">Fuel Assembler</text>
  <text x="436" y="678" text-anchor="middle" class="lbl" font-size="7" fill="#aa8800">19 U-238 + 1 U-235</text>

  <!-- Arrow 3->4 -->
  <line x1="498" y1="668" x2="528" y2="668" stroke="#555555" stroke-width="1.5"/>
  <polygon points="526,664 532,668 526,672" fill="#555555"/>

  <!-- Node 4: Reactor -->
  <rect x="534" y="649" width="110" height="38" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1.5"/>
  <text x="589" y="666" text-anchor="middle" class="lbl" font-size="8" fill="#44ff88" font-weight="700">-&gt; Reactor</text>
  <text x="589" y="678" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">200s per cell</text>

  <!-- Kovarex note (right of fuel cycle) -->
  <text x="680" y="662" class="lbl" font-size="7" fill="#ffaa44">Kovarex:</text>
  <text x="680" y="674" class="lbl" font-size="7" fill="#ffaa44">needs 40 U-235</text>
  <text x="680" y="686" class="lbl" font-size="7" fill="#ffaa44">then infinite fuel</text>

  <!-- ==================================================================================== -->
  <!-- SECTION 5: NOTES (y 710 - 750) -->
  <!-- ==================================================================================== -->
  <rect x="40" y="710" width="680" height="36" rx="4" fill="#0a0a18" stroke="#222222" stroke-width="0.5"/>
  <text x="50" y="728" class="lbl" font-size="7" fill="#555555">Notes: 1 offshore pump feeds 12 heat exchangers. 3 parallel heat pipes minimum for 2x2. 50+ steam tanks before circuit-controlled fuel. Touching reactors get +100pct each. Brownout if steam &lt; 50 tanks.</text>

</svg>
''')

out = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\diagrams\nuclear-reactor-layout.svg"
with open(out, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"SVG written: {out}")
print(f"Size: {len(svg)} bytes")
# Verify no XML parsing errors
import xml.etree.ElementTree as ET
try:
    ET.fromstring(svg)
    print("XML validation: OK")
except Exception as e:
    print(f"XML validation FAILED: {e}")
