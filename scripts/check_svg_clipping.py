#!/usr/bin/env python3
"""Check SVGs for potential text clipping / overflow issues."""
import os, re

base = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\diagrams\space-age"

for f in sorted(os.listdir(base)):
    if not f.endswith('.svg'):
        continue
    path = os.path.join(base, f)
    with open(path, 'r', encoding='utf-8') as fp:
        content = fp.read()

    # Parse viewBox
    vb_match = re.search(r'viewBox="([^"]+)"', content)
    if vb_match:
        parts = vb_match.group(1).split()
        vb_w, vb_h = float(parts[2]), float(parts[3])
    else:
        vb_w, vb_h = None, None

    # Find the rightmost and bottom-most text coordinates
    text_xs = [float(x) for x in re.findall(r'<text[^>]*\bx="([\d.]+)"', content) if float(x) > 10]
    text_ys = [float(y) for y in re.findall(r'<text[^>]*\by="([\d.]+)"', content) if float(y) > 10]

    issues = []
    
    if vb_w and text_xs:
        max_tx = max(text_xs)
        # Check if text elements extend close to or beyond viewBox width
        if max_tx > vb_w - 15:
            issues.append(f"text at x={max_tx:.0f} near/over viewBox width {vb_w:.0f}")

    # Check rect elements that might clip text
    # Look for rect x+width vs text x
    rect_matches = re.findall(r'<rect[^>]*\sx="([\d.]+)"[^>]*\swidth="([\d.]+)"', content)
    for rx_str, rw_str in rect_matches:
        rx, rw = float(rx_str), float(rw_str)
        r_end = rx + rw
        # Find text elements inside this rect
        text_in_rect = re.findall(
            rf'<text[^>]*\bx="([\d.]+)"[^>]*\by="([\d.]+)"[^>]*>([^<]+)',
            content
        )
        for tx_str, ty_str, txt in text_in_rect:
            tx = float(tx_str)
            # Check if text is roughly within this rect's x range
            if rx - 5 <= tx <= r_end + 5:
                # Estimate text width (~7px per char at font-size 9)
                fs_match = re.search(r'font-size="([\d.]+)"', content[content.find(f'x="{tx_str}"'):])
                fs = float(fs_match.group(1)) if fs_match else 9
                est_width = len(txt) * fs * 0.6
                if tx + est_width > r_end + 5:
                    issues.append(f"text '{txt.strip()[:20]}' may overflow rect (x={rx:.0f}+w={rw:.0f}; text x={tx:.0f}, est. width={est_width:.0f})")

    status = "OK" if not issues else "ISSUES"
    print(f"\n== {f} [{status}] ==")
    print(f"  viewBox: {vb_w:.0f}x{vb_h:.0f}" if vb_w else "  viewBox: none")
    if text_xs:
        print(f"  text x range: {min(text_xs):.0f} to {max(text_xs):.0f} (viewBox width: {vb_w:.0f})")
    if issues:
        for iss in issues:
            print(f"  ! {iss}")
