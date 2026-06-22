#!/usr/bin/env python3
"""Check SVGs for text near viewBox edges (potential clipping)."""
import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

base = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\diagrams\space-age"

for f in sorted(os.listdir(base)):
    if not f.endswith('.svg'):
        continue
    path = os.path.join(base, f)
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()

    vb_match = re.search(r'viewBox="([^"]+)"', content)
    if not vb_match:
        continue
    parts = vb_match.group(1).split()
    vb_w, vb_h = float(parts[2]), float(parts[3])

    # Find all text elements with x,y,content
    text_pattern = re.compile(r'<text[^>]*x="([\d.]+)"[^>]*y="([\d.]+)"[^>]*>([^<]+)')
    edge_texts = []
    for m in text_pattern.finditer(content):
        tx, ty, txt = float(m.group(1)), float(m.group(2)), m.group(3).strip()
        # Check text near right edge of viewBox
        gap_right = vb_w - tx
        # Estimate text width based on character count
        est_w = len(txt) * 7.5  # rough estimate at ~10px font
        if tx + est_w > vb_w - 5:
            edge_texts.append((tx, ty, txt, gap_right, est_w))
        # Check text near bottom
        gap_bottom = vb_h - ty
        if gap_bottom < 5 and gap_bottom > -5:
            edge_texts.append((tx, ty, txt, gap_right, 'bottom'))

    if edge_texts:
        print(f"\n== {f} ==")
        for tx, ty, txt, gap, est in edge_texts:
            if isinstance(est, str):
                print(f"  Bottom edge: x={tx:.0f} y={ty:.0f} '{txt[:30]}' gap={gap:.0f}")
            else:
                print(f"  Right edge: x={tx:.0f} y={ty:.0f} '{txt[:30]}' gap_right={gap:.0f} est_w={est:.0f}")
    else:
        print(f"{f}: OK")
