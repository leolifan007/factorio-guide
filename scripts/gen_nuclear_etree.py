#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate nuclear-reactor-layout.svg using ElementTree (guaranteed valid XML)."""
import xml.etree.ElementTree as ET
import os

NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)

def S(parent, tag, **attrs):
    """Create subelement with attributes."""
    e = ET.SubElement(parent, tag)
    for k, v in attrs.items():
        e.set(k, str(v))
    return e

def T(parent, text):
    """Set text content (auto-escapes < > &)."""
    parent.text = text
    return parent

# Root
root = ET.Element("{" + NS + "}svg")
root.set("xmlns", NS)
root.set("viewBox", "0 0 760 1500")
root.set("width", "760")
root.set("height", "1500")

# defs / style
defs = S(root, "{" + NS + "}defs")
style = S(defs, "{" + NS + "}style")
style.text = ".lbl { font-family: 'Segoe UI', Arial, sans-serif; }"

# Background
S(root, "{" + NS + "}rect", width=760, height=1500, fill="#12121f", rx=10)

# Title bar
S(root, "{" + NS + "}rect", x=0, y=0, width=760, height=54, fill="#0a1628", rx=10)
t = S(root, "{" + NS + "}text", x=380, y=35, fill="#44ff88",
      **{"text-anchor": "middle", "font-size": "16", "font-weight": "900", "letter-spacing": "2", "class": "lbl"})
T(t, "NUCLEAR POWER - 2x2 REACTOR LAYOUT")

# ============================================================
# SECTION 1: REACTORS (y 70 - 320)
# ============================================================
t1 = S(root, "{" + NS + "}text", x=380, y=90, fill="#cccccc",
       **{"text-anchor": "middle", "font-size": "13", "font-weight": "700", "class": "lbl"})
T(t1, "1. REACTORS (4x) - Neighbor Bonus Math")

note1 = S(root, "{" + NS + "}text", x=380, y=108, fill="#888888",
           **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(note1, "Touching reactors get +100% power per neighbor. Layout: 2x2 square.")

# Reactor A
S(root, "{" + NS + "}rect", x=140, y=125, width=120, height=65, rx=6, fill="#0d1b2a", stroke="#44ff88", **{"stroke-width": "2.5"})
ta = S(root, "{" + NS + "}text", x=200, y=158, fill="#44ff88",
       **{"text-anchor": "middle", "font-size": "14", "font-weight": "700", "class": "lbl"})
T(ta, "A")
ta2 = S(root, "{" + NS + "}text", x=200, y=178, fill="#aaaaaa",
        **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(ta2, "1 neighbor = 80 MW")

# Reactor B
S(root, "{" + NS + "}rect", x=290, y=125, width=120, height=65, rx=6, fill="#0d1b2a", stroke="#44ff88", **{"stroke-width": "2.5"})
tb = S(root, "{" + NS + "}text", x=350, y=158, fill="#44ff88",
       **{"text-anchor": "middle", "font-size": "14", "font-weight": "700", "class": "lbl"})
T(tb, "B")
tb2 = S(root, "{" + NS + "}text", x=350, y=178, fill="#ffaa44",
        **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(tb2, "2 nbr = 160 MW")

# Reactor C
S(root, "{" + NS + "}rect", x=140, y=210, width=120, height=65, rx=6, fill="#0d1b2a", stroke="#44ff88", **{"stroke-width": "2.5"})
tc = S(root, "{" + NS + "}text", x=200, y=243, fill="#44ff88",
       **{"text-anchor": "middle", "font-size": "14", "font-weight": "700", "class": "lbl"})
T(tc, "C")
tc2 = S(root, "{" + NS + "}text", x=200, y=263, fill="#aaaaaa",
        **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(tc2, "1 neighbor = 80 MW")

# Reactor D
S(root, "{" + NS + "}rect", x=290, y=210, width=120, height=65, rx=6, fill="#0d1b2a", stroke="#44ff88", **{"stroke-width": "2.5"})
td = S(root, "{" + NS + "}text", x=350, y=243, fill="#44ff88",
       **{"text-anchor": "middle", "font-size": "14", "font-weight": "700", "class": "lbl"})
T(td, "D")
td2 = S(root, "{" + NS + "}text", x=350, y=263, fill="#ffaa44",
        **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(td2, "2 nbr = 160 MW")

# Neighbor lines
S(root, "{" + NS + "}line", x1=260, y1=145, x2=290, y2=145, stroke="#44ff88",
   **{"stroke-width": "1.5", "stroke-dasharray": "5"})
lab_ab = S(root, "{" + NS + "}text", x=275, y=140, fill="#44ff88",
            **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(lab_ab, "+100%")

S(root, "{" + NS + "}line", x1=260, y1=230, x2=290, y2=230, stroke="#44ff88",
   **{"stroke-width": "1.5", "stroke-dasharray": "5"})
lab_cd = S(root, "{" + NS + "}text", x=275, y=225, fill="#44ff88",
            **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(lab_cd, "+100%")

S(root, "{" + NS + "}line", x1=200, y1=190, x2=200, y2=210, stroke="#44ff88",
   **{"stroke-width": "1.5", "stroke-dasharray": "5"})
lab_ac = S(root, "{" + NS + "}text", x=212, y=203, fill="#44ff88",
            **{"font-size": "8", "class": "lbl"})
T(lab_ac, "+100%")

S(root, "{" + NS + "}line", x1=350, y1=190, x2=350, y2=210, stroke="#44ff88",
   **{"stroke-width": "1.5", "stroke-dasharray": "5"})
lab_bd = S(root, "{" + NS + "}text", x=362, y=203, fill="#ffaa44",
            **{"font-size": "8", "class": "lbl"})
T(lab_bd, "+300%")

# Total output
S(root, "{" + NS + "}rect", x=140, y=290, width=270, height=28, rx=5, fill="#0a1a2a", stroke="#44ff88", **{"stroke-width": "1.5"})
total = S(root, "{" + NS + "}text", x=275, y=309, fill="#ffaa44",
          **{"text-anchor": "middle", "font-size": "13", "font-weight": "700", "class": "lbl"})
T(total, "TOTAL: 480 MW (4 reactors, 2x2)")

# Down arrow
S(root, "{" + NS + "}line", x1=380, y1=328, x2=380, y2=368, stroke="#555555", **{"stroke-width": "2.5"})
S(root, "{" + NS + "}polygon", points="376,362 380,370 384,362", fill="#555555")
arr_txt = S(root, "{" + NS + "}text", x=396, y=352, fill="#888888", **{"font-size": "9", "class": "lbl"})
T(arr_txt, "1000C heat output")

# ============================================================
# SECTION 2: HEAT FLOW (y 380 - 620)
# ============================================================
t2 = S(root, "{" + NS + "}text", x=380, y=398, fill="#cccccc",
       **{"text-anchor": "middle", "font-size": "13", "font-weight": "700", "class": "lbl"})
T(t2, "2. HEAT FLOW (left to right)")

# Heat Pipes block
S(root, "{" + NS + "}rect", x=40, y=418, width=160, height=90, rx=6, fill="#1a0a04", stroke="#cc7733", **{"stroke-width": "2"})
hp_title = S(root, "{" + NS + "}text", x=120, y=445, fill="#cc7733",
             **{"text-anchor": "middle", "font-size": "11", "font-weight": "700", "class": "lbl"})
T(hp_title, "HEAT PIPES")
hp1 = S(root, "{" + NS + "}text", x=120, y=463, fill="#aa7744",
         **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(hp1, "3 parallel pipes")
hp2 = S(root, "{" + NS + "}text", x=120, y=480, fill="#cc7733",
         **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(hp2, "Input: 1000C from reactor")
hp3 = S(root, "{" + NS + "}text", x=120, y=497, fill="#aa7744",
         **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(hp3, "Output: 500C to exchanger")

# Arrow Pipes -> HX
S(root, "{" + NS + "}line", x1=202, y1=463, x2=242, y2=463, stroke="#cc7733", **{"stroke-width": "2.5"})
S(root, "{" + NS + "}polygon", points="240,459 246,463 240,467", fill="#cc7733")

# Heat Exchangers block
S(root, "{" + NS + "}rect", x=248, y=418, width=200, height=90, rx=6, fill="#1a0a0a", stroke="#ff6644", **{"stroke-width": "2"})
hx_title = S(root, "{" + NS + "}text", x=348, y=445, fill="#ff6644",
             **{"text-anchor": "middle", "font-size": "11", "font-weight": "700", "class": "lbl"})
T(hx_title, "HEAT EXCHANGERS")
hx1 = S(root, "{" + NS + "}text", x=348, y=463, fill="#ff6644",
         **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(hx1, "x48 total (12 per reactor)")
hx2 = S(root, "{" + NS + "}text", x=348, y=480, fill="#884422",
         **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(hx2, "Input: 1000C heat from pipes")
hx3 = S(root, "{" + NS + "}text", x=348, y=497, fill="#884422",
         **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(hx3, "Output: 500C steam to turbines")

# Arrow HX -> Turbines
S(root, "{" + NS + "}line", x1=450, y1=463, x2=492, y2=463, stroke="#ff6644", **{"stroke-width": "2.5"})
S(root, "{" + NS + "}polygon", points="490,459 496,463 490,467", fill="#ff6644")

# Steam Turbines block
S(root, "{" + NS + "}rect", x=498, y=418, width=180, height=90, rx=6, fill="#0a1028", stroke="#88ccff", **{"stroke-width": "2"})
tb_title = S(root, "{" + NS + "}text", x=588, y=445, fill="#88ccff",
             **{"text-anchor": "middle", "font-size": "11", "font-weight": "700", "class": "lbl"})
T(tb_title, "STEAM TURBINES")
tb1 = S(root, "{" + NS + "}text", x=588, y=463, fill="#88ccff",
         **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(tb1, "x84 total (21 per reactor)")
tb2 = S(root, "{" + NS + "}text", x=588, y=480, fill="#445566",
         **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(tb2, "Input: 500C steam")
tb3 = S(root, "{" + NS + "}text", x=588, y=497, fill="#445566",
         **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(tb3, "Output: 480 MW total")

# Water supply (far right)
S(root, "{" + NS + "}rect", x=692, y=438, width=40, height=50, rx=5, fill="#0a1a2a", stroke="#44aaff", **{"stroke-width": "1.5"})
water = S(root, "{" + NS + "}text", x=712, y=465, fill="#44aaff",
          **{"text-anchor": "middle", "font-weight": "700", "font-size": "9", "class": "lbl"})
T(water, "H2O")
wp = S(root, "{" + NS + "}text", x=712, y=480, fill="#4488cc",
       **{"text-anchor": "middle", "font-size": "7", "class": "lbl"})
T(wp, "4x pumps")

# Water arrow (dashed)
S(root, "{" + NS + "}line", x1=668, y1=463, x2=692, y2=463, stroke="#44aaff",
   **{"stroke-width": "1.5", "stroke-dasharray": "4"})
S(root, "{" + NS + "}polygon", points="690,459 696,463 690,467", fill="#44aaff")

# Down arrow to summary
S(root, "{" + NS + "}line", x1=380, y1=520, x2=380, y2=560, stroke="#555555", **{"stroke-width": "2.5"})
S(root, "{" + NS + "}polygon", points="376,554 380,562 384,554", fill="#555555")

# ============================================================
# SECTION 3: SUMMARY BAR (y 570 - 673)
# ============================================================
S(root, "{" + NS + "}rect", x=40, y=570, width=680, height=103, rx=8, fill="#0a1628", stroke="#44ff88", **{"stroke-width": "2"})

summary = S(root, "{" + NS + "}text", x=380, y=600, fill="#44ff88",
            **{"text-anchor": "middle", "font-size": "15", "font-weight": "900", "class": "lbl"})
T(summary, "2x2 REACTOR = 480 MW TOTAL")

S(root, "{" + NS + "}line", x1=40, y1=618, x2=720, y2=618, stroke="#1a3a1a", **{"stroke-width": "0.8"})

# 5 columns
cols = [118, 272, 426, 580, 706]
labels = ["REACTORS", "HEAT EXCHANGERS", "STEAM TURBINES", "OFFSHORE PUMPS", "FUEL CELLS/HR"]
values = ["4", "48", "84", "4", "~72"]
sublabels = ["+neighbor bonus", "12/rct", "21/rct", "1 per 12 HX", "18/rct"]
val_fills = ["#44ff88", "#ff6644", "#88ccff", "#44aaff", "#ffaa44"]

for i in range(5):
    x = cols[i]
    l1 = S(root, "{" + NS + "}text", x=x, y=638, fill="#888888",
            **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
    T(l1, labels[i])
    v = S(root, "{" + NS + "}text", x=x, y=660, fill=val_fills[i],
          **{"text-anchor": "middle", "font-size": "15", "font-weight": "700", "class": "lbl"})
    T(v, values[i])
    s = S(root, "{" + NS + "}text", x=x, y=674, fill="#555555",
          **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
    T(s, sublabels[i])

# Down arrow to fuel cycle
S(root, "{" + NS + "}line", x1=380, y1=682, x2=380, y2=722, stroke="#555555", **{"stroke-width": "2"})
S(root, "{" + NS + "}polygon", points="376,716 380,724 384,716", fill="#555555")

# ============================================================
# SECTION 4: FUEL CYCLE (y 732 - 820)
# ============================================================
t3 = S(root, "{" + NS + "}text", x=380, y=750, fill="#aaaaaa",
       **{"text-anchor": "middle", "font-size": "13", "font-weight": "700", "class": "lbl"})
T(t3, "3. FUEL CYCLE")

# Node 1: Mining
S(root, "{" + NS + "}rect", x=80, y=764, width=120, height=42, rx=5, fill="#1a1a2e", stroke="#666666", **{"stroke-width": "1.2"})
m1 = S(root, "{" + NS + "}text", x=140, y=785, fill="#cccccc",
        **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(m1, "Uranium Mining")
m2 = S(root, "{" + NS + "}text", x=140, y=800, fill="#888888",
        **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(m2, "1 drill (enough)")

# Arrow 1->2
S(root, "{" + NS + "}line", x1=202, y1=785, x2=238, y2=785, stroke="#888888", **{"stroke-width": "2"})
S(root, "{" + NS + "}polygon", points="236,781 242,785 236,789", fill="#888888")

# Node 2: Centrifuge
S(root, "{" + NS + "}rect", x=244, y=764, width=120, height=42, rx=5, fill="#1a1a2e", stroke="#888888", **{"stroke-width": "1.2"})
c1 = S(root, "{" + NS + "}text", x=304, y=785, fill="#cccccc",
        **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(c1, "Centrifuge x5")
c2 = S(root, "{" + NS + "}text", x=304, y=800, fill="#888888",
        **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(c2, "0.7% -> U-235")

# Arrow 2->3
S(root, "{" + NS + "}line", x1=366, y1=785, x2=402, y2=785, stroke="#888888", **{"stroke-width": "2"})
S(root, "{" + NS + "}polygon", points="400,781 406,785 400,789", fill="#888888")

# Node 3: Fuel Assembler
S(root, "{" + NS + "}rect", x=408, y=764, width=130, height=42, rx=5, fill="#1a1a2e", stroke="#aa8800", **{"stroke-width": "1.2"})
f1 = S(root, "{" + NS + "}text", x=473, y=785, fill="#cccccc",
        **{"text-anchor": "middle", "font-size": "9", "class": "lbl"})
T(f1, "Fuel Assembler")
f2 = S(root, "{" + NS + "}text", x=473, y=800, fill="#aa8800",
        **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(f2, "19 U-238 + 1 U-235")

# Arrow 3->4
S(root, "{" + NS + "}line", x1=540, y1=785, x2=576, y2=785, stroke="#888888", **{"stroke-width": "2"})
S(root, "{" + NS + "}polygon", points="574,781 580,785 574,789", fill="#888888")

# Node 4: Reactor
S(root, "{" + NS + "}rect", x=582, y=764, width=110, height=42, rx=5, fill="#0a1a2a", stroke="#44ff88", **{"stroke-width": "2"})
r1 = S(root, "{" + NS + "}text", x=637, y=785, fill="#44ff88",
        **{"text-anchor": "middle", "font-weight": "700", "font-size": "9", "class": "lbl"})
T(r1, "-> Reactor")
r2 = S(root, "{" + NS + "}text", x=637, y=800, fill="#44ff88",
        **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(r2, "200s per cell")

# Kovarex note
k1 = S(root, "{" + NS + "}text", x=720, y=780, fill="#ffaa44", **{"font-size": "8", "class": "lbl"})
T(k1, "Kovarex:")
k2 = S(root, "{" + NS + "}text", x=720, y=794, fill="#ffaa44", **{"font-size": "8", "class": "lbl"})
T(k2, "needs 40 U-235")
k3 = S(root, "{" + NS + "}text", x=720, y=808, fill="#ffaa44", **{"font-size": "8", "class": "lbl"})
T(k3, "then infinite fuel")

# ============================================================
# NOTES (y 840 - 890)
# ============================================================
S(root, "{" + NS + "}rect", x=40, y=840, width=680, height=42, rx=5, fill="#0a0a18", stroke="#333333", **{"stroke-width": "0.8"})
# IMPORTANT: use ElementTree which auto-escapes < > &
notes_txt = S(root, "{" + NS + "}text", x=50, y=865, fill="#666666", **{"font-size": "9", "class": "lbl"})
# The < and > will be auto-escaped by ElementTree
T(notes_txt, "Notes: 1 offshore pump feeds 12 heat exchangers. 3 parallel heat pipes minimum for 2x2. 50+ steam tanks before circuit-controlled fuel. Touching reactors get +100% each. Brownout if steam < 50 tanks.")

# Footer
footer = S(root, "{" + NS + "}text", x=380, y=920, fill="#444444",
           **{"text-anchor": "middle", "font-size": "8", "class": "lbl"})
T(footer, "FactorioGuides.com - Nuclear Power Guide")

# ============================================================
# Write output
# ============================================================
out = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\diagrams\nuclear-reactor-layout.svg"
os.makedirs(os.path.dirname(out), exist_ok=True)

# Use ET.tostring (no minidom, to avoid duplicate attr error)
from xml.etree.ElementTree import tostring
svg_bytes = tostring(root, encoding="UTF-8")
svg_str = '<?xml version="1.0" encoding="UTF-8"?>\n' + svg_bytes.decode("utf-8")

with open(out, "w", encoding="utf-8") as f:
    f.write(svg_str)

print(f"SVG written: {out}")
print(f"Size: {os.path.getsize(out)} bytes")

# Validate
try:
    ET.parse(out)
    print("XML validation: OK")
except Exception as e:
    print(f"XML validation FAILED: {e}")
