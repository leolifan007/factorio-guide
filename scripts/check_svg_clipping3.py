#!/usr/bin/env python3
"""Check pentapod SVG viewBox and y=724 text."""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

base = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\diagrams\space-age"

for f in ['pentapod-defense-layout.svg', 'quality-upcycling-loop.svg', 'ship-layout-templates.svg']:
    path = os.path.join(base, f)
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()

    vb = re.search(r'viewBox="([^"]+)"', content)
    if vb:
        parts = vb.group(1).split()
        print(f"\n== {f} ==")
        print(f"  viewBox: {parts[0]} {parts[1]} {parts[2]} {parts[3]}")

        vb_w, vb_h = float(parts[2]), float(parts[3])

        # Check all near-bottom text (y near viewBox height)
        for m in re.finditer(r'<text[^>]*y="([\d.]+)"[^>]*x="([\d.]+)"[^>]*>([^<]+)', content):
            y = float(m.group(1))
            x = float(m.group(2))
            txt = m.group(3).strip()
            if y > vb_h - 20:
                print(f"  NEAR BOTTOM: x={x:.0f} y={y:.0f} '{txt[:50]}'")
            if x > vb_w - 50:
                # Check font size
                context_before = content[:m.start()]
                fs = None
                fs_match = re.search(r'font-size="([\d.]+)"', context_before[context_before.rfind('<text'):])
                if fs_match:
                    fs = float(fs_match.group(1))
                est_w = len(txt) * (fs or 10) * 0.6
                if x + est_w > vb_w:
                    print(f"  OVERFLOW RIGHT: x={x:.0f} y={y:.0f} font={fs or '?'} '{txt[:50]}' est_overflow={x+est_w-vb_w:.0f}px")
