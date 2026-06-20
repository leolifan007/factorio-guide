#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate nuclear-reactor-layout.svg with zero text overlap."""

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 820" width="1000" height="820">
  <defs>
    <style>
      .lbl { font-family: "Segoe UI", Arial, sans-serif; }
    </style>
  </defs>

  <!-- Background -->
  <rect width="1000" height="820" fill="#12121f" rx="10"/>

  <!-- ========== TITLE BAR ========== -->
  <rect x="0" y="0" width="1000" height="50" fill="#0a1628" rx="10"/>
  <text x="500" y="33" text-anchor="middle" class="lbl" font-size="15" font-weight="900" fill="#44ff88" letter-spacing="2">NUCLEAR POWER - 2x2 REACTOR LAYOUT</text>

  <!-- ============================================================= -->
  <!-- SECTION 1: REACTORS (y: 65 - 290) -->
  <!-- ============================================================= -->
  <text x="130" y="85" class="lbl" font-size="11" fill="#888" font-weight="700">1. REACTORS (4x)</text>

  <!-- Reactor A (top-left) -->
  <rect x="80" y="100" width="120" height="60" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="140" y="128" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">A</text>
  <text x="140" y="146" text-anchor="middle" class="lbl" font-size="8" fill="#999">1 neighbor / 80 MW</text>

  <!-- Reactor B (top-right) -->
  <rect x="220" y="100" width="120" height="60" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="280" y="128" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">B</text>
  <text x="280" y="146" text-anchor="middle" class="lbl" font-size="8" fill="#ffaa44">2 nbr / 160 MW</text>

  <!-- Reactor C (bottom-left) -->
  <rect x="80" y="172" width="120" height="60" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="140" y="200" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">C</text>
  <text x="140" y="218" text-anchor="middle" class="lbl" font-size="8" fill="#999">1 neighbor / 80 MW</text>

  <!-- Reactor D (bottom-right) -->
  <rect x="220" y="172" width="120" height="60" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
  <text x="280" y="200" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">D</text>
  <text x="280" y="218" text-anchor="middle" class="lbl" font-size="8" fill="#ffaa44">2 nbr / 160 MW</text>

  <!-- Neighbor bonus: A-B (horizontal) -->
  <line x1="200" y1="122" x2="220" y2="122" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="210" y="118" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: C-D (horizontal) -->
  <line x1="200" y1="194" x2="220" y2="194" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="210" y="190" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: A-C (vertical) -->
  <line x1="140" y1="160" x2="140" y2="172" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="150" y="168" class="lbl" font-size="7" fill="#44ff88">+100%</text>

  <!-- Neighbor bonus: B-D (vertical) -->
  <line x1="280" y1="160" x2="280" y2="172" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
  <text x="290" y="168" class="lbl" font-size="7" fill="#ffaa44">+300%</text>

  <!-- Total -->
  <text x="280" y="260" text-anchor="end" class="lbl" font-size="11" fill="#ffaa44" font-weight="700">4 reactors = 480 MW total</text>
  <text x="280" y="275" text-anchor="end" class="lbl" font-size="8" fill="#666">Touching reactors get +100% each. Layout matters.</text>

  <!-- Arrow: reactors -&gt; heat pipes -->
  <line x1="360" y1="155" x2="430" y2="155" stroke="#cc7733" stroke-width="2.5"/>
  <polygon points="428,151 434,155 428,159" fill="#cc7733"/>
  <text x="395" y="147" text-anchor="middle" class="lbl" font-size="8" fill="#cc7733">1000 C</text>

  <!-- ============================================================= -->
  <!-- SECTION 2: HEAT PIPES + HEAT EXCHANGERS + TURBINES (y: 65 - 320, right of reactors) -->
  <!-- ============================================================= -->
  <text x="550" y="85" class="lbl" font-size="11" fill="#cc7733" font-weight="700">2. HEAT PIPES (3x parallel)</text>

  <!-- 3 parallel heat pipes -->
  <rect x="470" y="100" width="14" height="140" rx="3" fill="#2a1a0a" stroke="#cc7733" stroke-width="1.2"/>
  <rect x="492" y="100" width="14" height="140" rx="3" fill="#2a1a0a" stroke="#cc7733" stroke-width="1.2"/>
  <rect x="514" y="100" width="14" height="140" rx="3" fill="#2a1a0a" stroke="#cc7733" stroke-width="1.2"/>
  <text x="492" y="148" text-anchor="middle" class="lbl" font-size="8" fill="#cc7733" font-weight="700">3x</text>
  <text x="492" y="162" text-anchor="middle" class="lbl" font-size="7" fill="#aa7744">1000 C in</text>
  <text x="492" y="175" text-anchor="middle" class="lbl" font-size="7" fill="#aa7744">500 C out</text>

  <!-- Arrow: heat pipes -&gt; exchangers -->
  <line x1="530" y1="155" x2="580" y2="155" stroke="#ff6644" stroke-width="2.5"/>
  <polygon points="578,151 584,155 578,159" fill="#ff6644"/>

  <!-- Heat Exchangers (right of pipes) -->
  <text x="750" y="85" class="lbl" font-size="11" fill="#ff6644" font-weight="700">3. HEAT EXCHANGERS x48</text>
  <text x="750" y="99" text-anchor="middle" class="lbl" font-size="8" fill="#884422">12 per reactor / output: 500 C steam</text>

  <rect x="590" y="110" width="220" height="22" rx="3" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.2"/>
  <text x="700" y="125" text-anchor="middle" class="lbl" font-size="9" fill="#ff6644">x12 - 500 C steam</text>

  <rect x="590" y="138" width="220" height="22" rx="3" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.2"/>
  <text x="700" y="153" text-anchor="middle" class="lbl" font-size="9" fill="#ff6644">x12 - 500 C steam</text>

  <rect x="590" y="166" width="220" height="22" rx="3" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.2"/>
  <text x="700" y="181" text-anchor="middle" class="lbl" font-size="9" fill="#ff6644">x12 - 500 C steam</text>

  <rect x="590" y="194" width="220" height="22" rx="3" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.2"/>
  <text x="700" y="209" text-anchor="middle" class="lbl" font-size="9" fill="#ff6644">x12 - 500 C steam</text>

  <!-- Arrow: exchangers -&gt; turbines -->
  <line x1="812" y1="195" x2="860" y2="195" stroke="#88ccff" stroke-width="2.5"/>
  <polygon points="858,191 864,195 858,199" fill="#88ccff"/>

  <!-- Steam Turbines (right of exchangers) -->
  <text x="920" y="85" class="lbl" font-size="11" fill="#88ccff" font-weight="700">4. TURBINES x84</text>
  <text x="920" y="99" text-anchor="middle" class="lbl" font-size="8" fill="#445566">21 per reactor / 5.8 MW each</text>

  <rect x="870" y="110" width="180" height="22" rx="3" fill="#0a1628" stroke="#88ccff" stroke-width="1.2"/>
  <text x="960" y="125" text-anchor="middle" class="lbl" font-size="9" fill="#88ccff">x21 - 121.8 MW</text>

  <rect x="870" y="138" width="180" height="22" rx="3" fill="#0a1628" stroke="#88ccff" stroke-width="1.2"/>
  <text x="960" y="153" text-anchor="middle" class="lbl" font-size="9" fill="#88ccff">x21 - 121.8 MW</text>

  <rect x="870" y="166" width="180" height="22" rx="3" fill="#0a1628" stroke="#88ccff" stroke-width="1.2"/>
  <text x="960" y="181" text-anchor="middle" class="lbl" font-size="9" fill="#88ccff">x21 - 121.8 MW</text>

  <rect x="870" y="194" width="180" height="22" rx="3" fill="#0a1628" stroke="#88ccff" stroke-width="1.2"/>
  <text x="960" y="209" text-anchor="middle" class="lbl" font-size="9" fill="#88ccff">x21 - 121.8 MW</text>

  <!-- Water supply (far right) -->
  <rect x="980" y="110" width="36" height="106" rx="4" fill="#0a1a2a" stroke="#44aaff" stroke-width="1.2"/>
  <text x="998" y="152" text-anchor="middle" class="lbl" font-size="9" fill="#44aaff" font-weight="700">H2O</text>
  <text x="998" y="168" text-anchor="middle" class="lbl" font-size="7" fill="#4488cc">4x</text>
  <text x="998" y="180" text-anchor="middle" class="lbl" font-size="7" fill="#4488cc">pumps</text>

  <!-- ============================================================= -->
  <!-- SEPARATOR -->
  <!-- ============================================================= -->
  <line x1="40" y1="310" x2="960" y2="310" stroke="#222" stroke-width="1"/>

  <!-- ============================================================= -->
  <!-- SUMMARY BAR (y: 322 - 415) -->
  <!-- ============================================================= -->
  <rect x="40" y="322" width="920" height="93" rx="6" fill="#0a1628" stroke="#44ff88" stroke-width="1.5"/>

  <text x="500" y="348" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="900">2x2 REACTOR = 480 MW TOTAL</text>

  <line x1="40" y1="360" x2="960" y2="360" stroke="#1a3a1a" stroke-width="0.5"/>

  <!-- 5 stat columns -->
  <text x="146" y="378" text-anchor="middle" class="lbl" font-size="8" fill="#666">REACTORS</text>
  <text x="146" y="398" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="700">4</text>
  <text x="146" y="410" text-anchor="middle" class="lbl" font-size="7" fill="#444">neighbor bonus</text>

  <text x="302" y="378" text-anchor="middle" class="lbl" font-size="8" fill="#666">HEAT EXCHANGERS</text>
  <text x="302" y="398" text-anchor="middle" class="lbl" font-size="13" fill="#ff6644" font-weight="700">48</text>
  <text x="302" y="410" text-anchor="middle" class="lbl" font-size="7" fill="#444">12 per reactor</text>

  <text x="458" y="378" text-anchor="middle" class="lbl" font-size="8" fill="#666">STEAM TURBINES</text>
  <text x="458" y="398" text-anchor="middle" class="lbl" font-size="13" fill="#88ccff" font-weight="700">84</text>
  <text x="458" y="410" text-anchor="middle" class="lbl" font-size="7" fill="#444">21 per reactor</text>

  <text x="614" y="378" text-anchor="middle" class="lbl" font-size="8" fill="#666">OFFSHORE PUMPS</text>
  <text x="614" y="398" text-anchor="middle" class="lbl" font-size="13" fill="#44aaff" font-weight="700">4</text>
  <text x="614" y="410" text-anchor="middle" class="lbl" font-size="7" fill="#444">1 per 12 HX</text>

  <text x="770" y="378" text-anchor="middle" class="lbl" font-size="8" fill="#666">FUEL CELLS / HR</text>
  <text x="770" y="398" text-anchor="middle" class="lbl" font-size="13" fill="#ffaa44" font-weight="700">~72</text>
  <text x="770" y="410" text-anchor="middle" class="lbl" font-size="7" fill="#444">18 per reactor</text>

  <!-- ============================================================= -->
  <!-- SEPARATOR -->
  <!-- ============================================================= -->
  <line x1="40" y1="430" x2="960" y2="430" stroke="#222" stroke-width="1"/>

  <!-- ============================================================= -->
  <!-- FUEL CYCLE (y: 442 - 510) -->
  <!-- ============================================================= -->
  <text x="500" y="458" text-anchor="middle" class="lbl" font-size="10" fill="#aaa" font-weight="700">FUEL CYCLE</text>

  <!-- Node 1: Mining -->
  <rect x="120" y="472" width="110" height="38" rx="4" fill="#1a1a2e" stroke="#555" stroke-width="1"/>
  <text x="175" y="489" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Uranium Mining</text>
  <text x="175" y="501" text-anchor="middle" class="lbl" font-size="7" fill="#555">1 drill</text>

  <!-- Arrow 1-&gt;2 -->
  <line x1="232" y1="491" x2="262" y2="491" stroke="#555" stroke-width="1.5"/>
  <polygon points="260,487 266,491 260,495" fill="#555"/>

  <!-- Node 2: Centrifuge -->
  <rect x="268" y="472" width="110" height="38" rx="4" fill="#1a1a2e" stroke="#888" stroke-width="1"/>
  <text x="323" y="489" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Centrifuge x5</text>
  <text x="323" y="501" text-anchor="middle" class="lbl" font-size="7" fill="#555">0.7% -&gt; U-235</text>

  <!-- Arrow 2-&gt;3 -->
  <line x1="380" y1="491" x2="410" y2="491" stroke="#555" stroke-width="1.5"/>
  <polygon points="408,487 414,491 408,495" fill="#555"/>

  <!-- Node 3: Fuel Assembler -->
  <rect x="416" y="472" width="120" height="38" rx="4" fill="#1a1a2e" stroke="#aa8800" stroke-width="1"/>
  <text x="476" y="489" text-anchor="middle" class="lbl" font-size="8" fill="#ccc">Fuel Assembler</text>
  <text x="476" y="501" text-anchor="middle" class="lbl" font-size="7" fill="#aa8800">19 U-238 + 1 U-235</text>

  <!-- Arrow 3-&gt;4 -->
  <line x1="538" y1="491" x2="568" y2="491" stroke="#555" stroke-width="1.5"/>
  <polygon points="566,487 572,491 566,495" fill="#555"/>

  <!-- Node 4: Reactor -->
  <rect x="574" y="472" width="110" height="38" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1.5"/>
  <text x="629" y="489" text-anchor="middle" class="lbl" font-size="8" fill="#44ff88" font-weight="700">-&gt; Reactor</text>
  <text x="629" y="501" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">200 s / cell</text>

  <!-- Kovarex note -->
  <text x="730" y="485" class="lbl" font-size="7" fill="#ffaa44">Kovarex: needs 40 U-235</text>
  <text x="730" y="497" class="lbl" font-size="7" fill="#ffaa44">then fuel is infinite</text>

  <!-- ============================================================= -->
  <!-- NOTES (bottom) -->
  <!-- ============================================================= -->
  <text x="500" y="550" text-anchor="middle" class="lbl" font-size="8" fill="#444">Notes: 1 offshore pump feeds 12 heat exchangers. 3 parallel heat pipes minimum for 2x2. Use 50+ steam tanks before circuit-controlled fuel.</text>

</svg>'''

with open(r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\diagrams\nuclear-reactor-layout.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("SVG written successfully")
