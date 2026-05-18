"""
Single-pass SVG relayout: read all old coords, compute all new coords at once,
then write them back. Handles font map, box enlarge, content stretch, and
connection repair.
"""
import os, re
from collections import defaultdict

DIR = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'
MIN_GAP = 120
PAD_L, PAD_R = 30, 30
FONT_MAP = {6:9, 7:10, 8:11, 9:12, 10:12, 11:13, 12:13, 13:13}

def stretch(v, lo, hi, nl, nh):
    if hi <= lo: return v
    return int(nl + max(0, min(1, (v - lo) / (hi - lo))) * (nh - nl))

for fname in sorted(os.listdir(DIR)):
    if not fname.endswith('.svg'): continue
    path = os.path.join(DIR, fname)
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()

    vb = re.search(r'viewBox="(\d+) (\d+) (\d+) (\d+)"', src)
    if not vb: continue
    vbw, vbh = int(vb.group(3)), int(vb.group(4))
    new_vbh = int(vbh * 1.15)

    # --- Phase 1: Collect old data ---
    # Rectangles: (old_x, old_w, old_h, is_bg)
    rects = []
    for m in re.finditer(r'<rect [^>]*?x="(\d+)"[^>]*?width="(\d+)"[^>]*?height="(\d+)"', src):
        x, w, h = int(m.group(1)), int(m.group(2)), int(m.group(3))
        # Background = fills full canvas width OR very wide (>80% canvas)
        is_bg = (w >= vbw - 2) or (w >= vbw * 0.8 and x <= 50)
        rects.append({'ox': x, 'ow': w, 'oh': h, 'bg': is_bg,
                       'or': x + w, 'nx': x, 'nw': w, 'nh': h, 'nr': x + w})

    # Lines: extract all tag positions, then parse attrs individually
    # Handle any attribute order: x1, x2, y1 can appear in any sequence
    lines = []
    for m in re.finditer(r'<line [^>]*?/>', src):
        tag = m.group(0)
        x1m = re.search(r'x1="(\d+)"', tag)
        x2m = re.search(r'x2="(\d+)"', tag)
        y1m = re.search(r'y1="(\d+)"', tag)
        if x1m and x2m and y1m:
            x1, x2, y1 = int(x1m.group(1)), int(x2m.group(1)), int(y1m.group(1))
            # Skip full-width structural lines
            if x1 == 0 and x2 >= 800: continue
            lines.append({'x1': x1, 'nx1': x1, 'x2': x2, 'nx2': x2, 'y1': y1,
                           'px1': m.start() + x1m.start(1), 'px2': m.start() + x2m.start(1)})

    # Polygons (arrowheads): points as list of (x,y) tuples
    polys = []
    for m in re.finditer(r'<polygon [^>]*?points="([^"]+)"', src):
        pts = []
        for p in m.group(1).split():
            parts = p.split(',')
            if len(parts) == 2:
                try: pts.append((int(float(parts[0])), int(float(parts[1]))))
                except: pass
        if pts:
            polys.append({'pts': pts, 'npts': [p for p in pts]})

    # Text elements
    texts = []
    for m in re.finditer(r'<text [^>]*?x="(\d+)"', src):
        texts.append({'ox': int(m.group(1)), 'pos': m.start(1)})

    # Circle cx
    circs = []
    for m in re.finditer(r'cx="(\d+)"', src):
        circs.append({'val': int(m.group(1)), 'pos': m.start(1)})

    # --- Phase 2: Compute stretch range ---
    all_xs = set()
    for r in rects:
        if not r['bg']:
            all_xs.add(r['ox'])
            all_xs.add(r['or'])
    for t in texts:
        if 0 < t['ox'] < vbw: all_xs.add(t['ox'])
    for l in lines:
        if 0 < l['x1'] < vbw: all_xs.add(l['x1'])
        if 0 < l['x2'] < vbw: all_xs.add(l['x2'])
    for c in circs:
        if 0 < c['val'] < vbw: all_xs.add(c['val'])
    for p in polys:
        for px, py in p['pts']:
            if 0 < px < vbw: all_xs.add(px)

    if len(all_xs) < 3: continue
    old_min = min(all_xs)
    old_max = max(all_xs)
    gap = vbw - old_max

    needs_stretch = gap >= MIN_GAP
    dl = '▶' if needs_stretch else '✓'
    print(f'  {dl}  {fname:30s} gap={gap:3d}px  {"x=" + str(old_min) + ".." + str(old_max) if needs_stretch else "font+box only"}')
    if not needs_stretch and gap < 10:
        pass  # no changes needed beyond font+box
    else:
        # --- Phase 3: Compute new positions ---

        # 3a. Rect new values
        for r in rects:
            if r['bg']:
                r['nh'] = new_vbh
            else:
                r['nx'] = stretch(r['ox'], old_min, old_max, PAD_L, vbw - PAD_R) if needs_stretch else r['ox']
                r['nw'] = int(r['ow'] * 1.05)
                r['nh'] = int(r['oh'] * 1.25)
                r['nr'] = r['nx'] + r['nw']

        # 3b. Build edge maps for connection repair
        right_edge_map = {}
        left_edge_map = {}
        for r in rects:
            if not r['bg']:
                right_edge_map[r['or']] = r['nr']
                left_edge_map[r['ox']] = r['nx']

        # 3c. Line new values with connection repair
        for l in lines:
            l['nx1'] = stretch(l['x1'], old_min, old_max, PAD_L, vbw - PAD_R) if needs_stretch else l['x1']
            l['nx2'] = stretch(l['x2'], old_min, old_max, PAD_L, vbw - PAD_R) if needs_stretch else l['x2']

            # Snap x1 to rect right edge
            for old_re, new_re in right_edge_map.items():
                if l['x1'] == old_re:
                    l['nx1'] = new_re
                    break
            # Snap x2 to rect right edge
            for old_re, new_re in right_edge_map.items():
                if l['x2'] == old_re:
                    l['nx2'] = new_re
                    break
            # Snap x1 to rect left edge
            for old_le, new_le in left_edge_map.items():
                if l['x1'] == old_le:
                    l['nx1'] = new_le
                    break
            # Snap x2 to rect left edge
            for old_le, new_le in left_edge_map.items():
                if l['x2'] == old_le:
                    l['nx2'] = new_le
                    break

        # 3d. Polygon new values - match to line endpoints
        for pi in polys:
            npts = []
            for px, py in pi['pts']:
                new_px = stretch(px, old_min, old_max, PAD_L, vbw - PAD_R) if needs_stretch else px

                # Check if this point is an arrowhead tip matching a line end
                for l in lines:
                    # If original polygon x matches original line x2 at same y
                    if px == l['x2'] and py == l['y1']:
                        delta = l['nx2'] - l['x2']
                        new_px = px + delta  # move by same delta as line endpoint
                        break
                    # If matches line x1
                    if px == l['x1'] and py == l['y1']:
                        delta = l['nx1'] - l['x1']
                        new_px = px + delta
                        break

                npts.append((new_px, py))
            pi['npts'] = npts

    # --- Phase 4: Apply ALL changes via string replacement ---

    # Build replacement table: (old_str, new_str)
    # We'll apply in reverse order (intersecting changes first? no, unique attrs)
    # Use simple attr="old" → attr="new" replacement

    replacements = []  # (old_substring, new_substring) - applied sequentially

    # Font sizes
    found_fonts = set()
    for m in re.finditer(r'font-size="(\d+)"', src):
        old_fs = int(m.group(1))
        if old_fs in FONT_MAP and old_fs not in found_fonts:
            found_fonts.add(old_fs)
            new_fs = FONT_MAP[old_fs]
            if new_fs != old_fs:
                replacements.append((f'font-size="{old_fs}"', f'font-size="{new_fs}"'))

    # Text x
    for t in texts:
        ox = t['ox']
        if needs_stretch:
            new_x = stretch(ox, old_min, old_max, PAD_L, vbw - PAD_R)
        else:
            new_x = ox
        if new_x != ox:
            replacements.append((f'x="{ox}"', f'x="{new_x}"'))

    # Rect x, width, height
    for r in rects:
        if r['nx'] != r['ox']:
            replacements.append((f'x="{r["ox"]}"', f'x="{r["nx"]}"'))
        if r['nw'] != r['ow']:
            replacements.append((f'width="{r["ow"]}"', f'width="{r["nw"]}"'))
        if r['nh'] != r['oh']:
            replacements.append((f'height="{r["oh"]}"', f'height="{r["nh"]}"'))

    # Line x1, x2
    for l in lines:
        if l['nx1'] != l['x1']:
            replacements.append((f'x1="{l["x1"]}"', f'x1="{l["nx1"]}"'))
        if l['nx2'] != l['x2']:
            replacements.append((f'x2="{l["x2"]}"', f'x2="{l["nx2"]}"'))

    # Circle cx
    for c in circs:
        if needs_stretch:
            new_cx = stretch(c['val'], old_min, old_max, PAD_L, vbw - PAD_R)
        else:
            new_cx = c['val']
        if new_cx != c['val']:
            replacements.append((f'cx="{c["val"]}"', f'cx="{new_cx}"'))

    # Transform rotate centers (rotated text labels)
    for m in re.finditer(r'transform="rotate\((-?\d+),(\d+),(-?\d+)\)"', src):
        angle, old_cx, old_cy = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if needs_stretch:
            new_cx = stretch(old_cx, old_min, old_max, PAD_L, vbw - PAD_R)
        else:
            new_cx = old_cx
        if new_cx != old_cx:
            old_str = f'rotate({angle},{old_cx},{old_cy})'
            new_str = f'rotate({angle},{new_cx},{old_cy})'
            replacements.append((old_str, new_str))

    # Polygon points
    for pi in polys:
        old_pts_str = ' '.join(f'{px},{py}' for px, py in pi['pts'])
        new_pts_str = ' '.join(f'{nx},{ny}' for nx, ny in pi['npts'])
        if old_pts_str != new_pts_str:
            replacements.append((f'points="{old_pts_str}"', f'points="{new_pts_str}"'))

    # SVG viewBox and height
    if new_vbh != vbh:
        replacements.append((f'viewBox="0 0 {vbw} {vbh}"', f'viewBox="0 0 {vbw} {new_vbh}"'))
        replacements.append((f'height="{vbh}"', f'height="{new_vbh}"'))

    # Apply replacements (sort by length descending to avoid partial replacements)
    replacements.sort(key=lambda x: -len(x[0]))
    result = src
    for old_str, new_str in replacements:
        result = result.replace(old_str, new_str)

    if result != src:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(result)

print('Done')
