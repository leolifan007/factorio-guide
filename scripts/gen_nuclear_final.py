import sys, os

svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 1100" width="760" height="1100">
<defs><style>.lbl{font-family:"Segoe UI",Arial,sans-serif;}</style></defs>
<rect width="760" height="1100" fill="#12121f" rx="10"/>

<!-- TITLE -->
<rect x="0" y="0" width="760" height="48" fill="#0a1628" rx="10"/>
<text x="380" y="32" text-anchor="middle" class="lbl" font-size="14" font-weight="900" fill="#44ff88" letter-spacing="2">NUCLEAR POWER - 2x2 REACTOR LAYOUT</text>

<!-- SECTION 1: REACTORS (y 65-260) -->
<text x="380" y="80" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">1. REACTORS (4x) - Neighbor Bonus</text>

<!-- A (top-left) -->
<rect x="140" y="96" width="110" height="56" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
<text x="195" y="124" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">A</text>
<text x="195" y="142" text-anchor="middle" class="lbl" font-size="8" fill="#999999">1 nbr = 80 MW</text>

<!-- B (top-right) -->
<rect x="275" y="96" width="110" height="56" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
<text x="330" y="124" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">B</text>
<text x="330" y="142" text-anchor="middle" class="lbl" font-size="8" fill="#ffaa44">2 nbr = 160 MW</text>

<!-- C (bottom-left) -->
<rect x="140" y="166" width="110" height="56" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
<text x="195" y="194" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">C</text>
<text x="195" y="212" text-anchor="middle" class="lbl" font-size="8" fill="#999999">1 nbr = 80 MW</text>

<!-- D (bottom-right) -->
<rect x="275" y="166" width="110" height="56" rx="5" fill="#0d1b2a" stroke="#44ff88" stroke-width="2"/>
<text x="330" y="194" text-anchor="middle" class="lbl" font-size="12" fill="#44ff88" font-weight="700">D</text>
<text x="330" y="212" text-anchor="middle" class="lbl" font-size="8" fill="#ffaa44">2 nbr = 160 MW</text>

<!-- neighbor lines -->
<line x1="250" y1="118" x2="275" y2="118" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
<text x="262" y="114" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100pct</text>
<line x1="250" y1="188" x2="275" y2="188" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
<text x="262" y="184" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">+100pct</text>
<line x1="195" y1="152" x2="195" y2="166" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
<text x="205" y="162" class="lbl" font-size="7" fill="#44ff88">+100pct</text>
<line x1="330" y1="152" x2="330" y2="166" stroke="#44ff88" stroke-width="1.2" stroke-dasharray="4"/>
<text x="340" y="162" class="lbl" font-size="7" fill="#ffaa44">+300pct</text>

<!-- total -->
<rect x="140" y="240" width="245" height="22" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1"/>
<text x="262" y="255" text-anchor="middle" class="lbl" font-size="11" fill="#ffaa44" font-weight="700">TOTAL: 480 MW (4 reactors)</text>

<!-- DOWN ARROW -->
<line x1="380" y1="276" x2="380" y2="306" stroke="#444444" stroke-width="2"/>
<polygon points="376,300 380,308 384,300" fill="#444444"/>
<text x="394" y="294" class="lbl" font-size="8" fill="#666666">1000C heat out</text>

<!-- SECTION 2: HEAT FLOW (y 316-470) -->
<text x="380" y="332" text-anchor="middle" class="lbl" font-size="12" fill="#cccccc" font-weight="700">2. HEAT FLOW (left to right)</text>

<!-- Heat Pipes (left block) -->
<rect x="40" y="346" width="150" height="76" rx="5" fill="#1a0a04" stroke="#cc7733" stroke-width="1.5"/>
<text x="115" y="370" text-anchor="middle" class="lbl" font-size="10" fill="#cc7733" font-weight="700">HEAT PIPES</text>
<text x="115" y="386" text-anchor="middle" class="lbl" font-size="8" fill="#aa7744">3 parallel pipes</text>
<text x="115" y="401" text-anchor="middle" class="lbl" font-size="7" fill="#cc7733">1000C from reactor</text>
<text x="115" y="414" text-anchor="middle" class="lbl" font-size="7" fill="#aa7744">500C to exchanger</text>

<!-- arrow pipes to HX -->
<line x1="192" y1="383" x2="228" y2="383" stroke="#cc7733" stroke-width="2"/>
<polygon points="226,379 232,383 226,387" fill="#cc7733"/>

<!-- Heat Exchangers (center block) -->
<rect x="234" y="346" width="190" height="76" rx="5" fill="#1a0a0a" stroke="#ff6644" stroke-width="1.5"/>
<text x="329" y="370" text-anchor="middle" class="lbl" font-size="10" fill="#ff6644" font-weight="700">HEAT EXCHANGERS</text>
<text x="329" y="386" text-anchor="middle" class="lbl" font-size="8" fill="#ff6644">x48 (12 per reactor)</text>
<text x="329" y="401" text-anchor="middle" class="lbl" font-size="7" fill="#884422">In: 1000C heat</text>
<text x="329" y="414" text-anchor="middle" class="lbl" font-size="7" fill="#884422">Out: 500C steam</text>

<!-- arrow HX to turbines -->
<line x1="426" y1="383" x2="462" y2="383" stroke="#ff6644" stroke-width="2"/>
<polygon points="460,379 466,383 460,387" fill="#ff6644"/>

<!-- Steam Turbines (right block) -->
<rect x="468" y="346" width="180" height="76" rx="5" fill="#0a1028" stroke="#88ccff" stroke-width="1.5"/>
<text x="558" y="370" text-anchor="middle" class="lbl" font-size="10" fill="#88ccff" font-weight="700">STEAM TURBINES</text>
<text x="558" y="386" text-anchor="middle" class="lbl" font-size="8" fill="#88ccff">x84 (21 per reactor)</text>
<text x="558" y="401" text-anchor="middle" class="lbl" font-size="7" fill="#445566">In: 500C steam</text>
<text x="558" y="414" text-anchor="middle" class="lbl" font-size="7" fill="#445566">Out: 480 MW total</text>

<!-- water (far right) -->
<rect x="658" y="364" width="36" height="50" rx="4" fill="#0a1a2a" stroke="#44aaff" stroke-width="1.2"/>
<text x="676" y="393" text-anchor="middle" class="lbl" font-size="8" fill="#44aaff" font-weight="700">H2O</text>
<text x="676" y="407" text-anchor="middle" class="lbl" font-size="7" fill="#4488cc">4x pump</text>

<!-- water arrow (dashed) -->
<line x1="636" y1="389" x2="658" y2="389" stroke="#44aaff" stroke-width="1.2" stroke-dasharray="3"/>
<polygon points="656,385 662,389 656,393" fill="#44aaff"/>

<!-- DOWN ARROW to summary -->
<line x1="380" y1="442" x2="380" y2="472" stroke="#444444" stroke-width="2"/>
<polygon points="376,466 380,474 384,466" fill="#444444"/>

<!-- SECTION 3: SUMMARY BAR (y 480-573) -->
<rect x="40" y="480" width="680" height="93" rx="6" fill="#0a1628" stroke="#44ff88" stroke-width="1.5"/>
<text x="380" y="506" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="900">2x2 REACTOR = 480 MW TOTAL</text>
<line x1="40" y1="518" x2="720" y2="518" stroke="#1a3a1a" stroke-width="0.5"/>

<!-- 5 stat columns -->
<text x="118" y="536" text-anchor="middle" class="lbl" font-size="8" fill="#666666">REACTORS</text>
<text x="118" y="556" text-anchor="middle" class="lbl" font-size="13" fill="#44ff88" font-weight="700">4</text>
<text x="118" y="568" text-anchor="middle" class="lbl" font-size="7" fill="#444444">neighbor bonus</text>

<text x="264" y="536" text-anchor="middle" class="lbl" font-size="8" fill="#666666">HEAT EXCHANGERS</text>
<text x="264" y="556" text-anchor="middle" class="lbl" font-size="13" fill="#ff6644" font-weight="700">48</text>
<text x="264" y="568" text-anchor="middle" class="lbl" font-size="7" fill="#444444">12/rct</text>

<text x="410" y="536" text-anchor="middle" class="lbl" font-size="8" fill="#666666">TURBINES</text>
<text x="410" y="556" text-anchor="middle" class="lbl" font-size="13" fill="#88ccff" font-weight="700">84</text>
<text x="410" y="568" text-anchor="middle" class="lbl" font-size="7" fill="#444444">21/rct</text>

<text x="556" y="536" text-anchor="middle" class="lbl" font-size="8" fill="#666666">OFFSHORE PUMPS</text>
<text x="556" y="556" text-anchor="middle" class="lbl" font-size="13" fill="#44aaff" font-weight="700">4</text>
<text x="556" y="568" text-anchor="middle" class="lbl" font-size="7" fill="#444444">1 per 12 HX</text>

<text x="702" y="536" text-anchor="middle" class="lbl" font-size="8" fill="#666666">FUEL CELLS/HR</text>
<text x="702" y="556" text-anchor="middle" class="lbl" font-size="13" fill="#ffaa44" font-weight="700">~72</text>
<text x="702" y="568" text-anchor="middle" class="lbl" font-size="7" fill="#444444">18/rct</text>

<!-- DOWN ARROW to fuel cycle -->
<line x1="380" y1="579" x2="380" y2="609" stroke="#444444" stroke-width="1.5"/>
<polygon points="376,603 380,611 384,603" fill="#444444"/>

<!-- SECTION 4: FUEL CYCLE (y 619-690) -->
<text x="380" y="635" text-anchor="middle" class="lbl" font-size="12" fill="#aaaaaa" font-weight="700">3. FUEL CYCLE</text>

<!-- Node 1: Mining -->
<rect x="80" y="649" width="110" height="36" rx="4" fill="#1a1a2e" stroke="#555555" stroke-width="1"/>
<text x="135" y="666" text-anchor="middle" class="lbl" font-size="8" fill="#cccccc">Uranium Mining</text>
<text x="135" y="678" text-anchor="middle" class="lbl" font-size="7" fill="#555555">1 drill</text>

<!-- arrow 1-2 -->
<line x1="192" y1="667" x2="222" y2="667" stroke="#555555" stroke-width="1.5"/>
<polygon points="220,663 226,667 220,671" fill="#555555"/>

<!-- Node 2: Centrifuge -->
<rect x="228" y="649" width="110" height="36" rx="4" fill="#1a1a2e" stroke="#888888" stroke-width="1"/>
<text x="283" y="666" text-anchor="middle" class="lbl" font-size="8" fill="#cccccc">Centrifuge x5</text>
<text x="283" y="678" text-anchor="middle" class="lbl" font-size="7" fill="#555555">0.7pct U-235</text>

<!-- arrow 2-3 -->
<line x1="340" y1="667" x2="370" y2="667" stroke="#555555" stroke-width="1.5"/>
<polygon points="368,663 374,667 368,671" fill="#555555"/>

<!-- Node 3: Fuel Assembler -->
<rect x="376" y="649" width="120" height="36" rx="4" fill="#1a1a2e" stroke="#aa8800" stroke-width="1"/>
<text x="436" y="666" text-anchor="middle" class="lbl" font-size="8" fill="#cccccc">Fuel Assembler</text>
<text x="436" y="678" text-anchor="middle" class="lbl" font-size="7" fill="#aa8800">19 U-238 + 1 U-235</text>

<!-- arrow 3-4 -->
<line x1="498" y1="667" x2="528" y2="667" stroke="#555555" stroke-width="1.5"/>
<polygon points="526,663 532,667 526,671" fill="#555555"/>

<!-- Node 4: Reactor -->
<rect x="534" y="649" width="110" height="36" rx="4" fill="#0a1a2a" stroke="#44ff88" stroke-width="1.5"/>
<text x="589" y="666" text-anchor="middle" class="lbl" font-size="8" fill="#44ff88" font-weight="700">to Reactor</text>
<text x="589" y="678" text-anchor="middle" class="lbl" font-size="7" fill="#44ff88">200s per cell</text>

<!-- Kovarex note -->
<text x="670" y="662" class="lbl" font-size="7" fill="#ffaa44">Kovarex: 40 U-235</text>
<text x="670" y="674" class="lbl" font-size="7" fill="#ffaa44">then infinite fuel</text>

<!-- NOTES (y 710-750) -->
<rect x="40" y="710" width="680" height="32" rx="4" fill="#0a0a18" stroke="#222222" stroke-width="0.5"/>
<text x="50" y="728" class="lbl" font-size="7" fill="#555555">Notes: 1 offshore pump feeds 12 heat exchangers. 3 parallel heat pipes minimum for 2x2. 50+ steam tanks before circuit-controlled fuel. Touching reactors get +100pct each.</text>

</svg>'''

out = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\diagrams\nuclear-reactor-layout.svg'
with open(out, 'w', encoding='utf-8') as f:
    f.write(svg)
print(f'Written: {len(svg)} bytes to {out}')
