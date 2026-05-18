"""Single-pass SVG relayout v3: font map + box enlarge + stretch + connection repair.
Fixes: bg-rect over-enlarge, backward connectors, transform center drift."""
import os, re

DIR = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'
MIN_GAP = 120
PAD_L, PAD_R = 30, 30
FONT_MAP = {6:9, 7:10, 8:11, 9:12, 10:12, 11:13, 12:13, 13:13}

def stretch(v, lo, hi, nl, nh):
    if hi <= lo: return v
    return int(nl + max(0, min(1, (v-lo)/(hi-lo))) * (nh-nl))

for fname in sorted(os.listdir(DIR)):
    if not fname.endswith('.svg'): continue
    path = os.path.join(DIR, fname)
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()

    vb = re.search(r'viewBox="(\d+) (\d+) (\d+) (\d+)"', src)
    if not vb: continue
    vbw, vbh = int(vb.group(3)), int(vb.group(4))
    new_vbh = int(vbh * 1.15)

    # --- Phase 1: collect old data ---
    rects = []
    for m in re.finditer(r'<rect [^>]*?x="(\d+)"[^>]*?width="(\d+)"[^>]*?height="(\d+)"', src):
        x, w, h = int(m.group(1)), int(m.group(2)), int(m.group(3))
        is_bg = (w >= vbw - 2) or (w >= vbw * 0.8 and x <= 50)
        rects.append(dict(ox=x, ow=w, oh=h, bg=is_bg, or_=x+w, nx=x, nw=w, nh=h, nr_=x+w))

    lines = []
    for m in re.finditer(r'<line[^>]*?/>', src):
        tag = m.group(0)
        x1m = re.search(r'x1="(\d+)"', tag)
        x2m = re.search(r'x2="(\d+)"', tag)
        y1m = re.search(r'y1="(\d+)"', tag)
        if x1m and x2m and y1m:
            x1, x2, y1 = int(x1m.group(1)), int(x2m.group(1)), int(y1m.group(1))
            if x1 == 0 and x2 >= 800: continue
            lines.append(dict(x1=x1, nx1=x1, x2=x2, nx2=x2, y1=y1))

    polys = []
    for m in re.finditer(r'<polygon [^>]*?points="([^"]+)"', src):
        pts = []
        for p in m.group(1).split():
            parts = p.split(',')
            if len(parts) == 2:
                try: pts.append((int(float(parts[0])), int(float(parts[1]))))
                except: pass
        if pts:
            polys.append(dict(pts=pts, npts=[p for p in pts]))

    texts = []
    for m in re.finditer(r'<text [^>]*?x="(\d+)"', src):
        texts.append(dict(ox=int(m.group(1))))

    circs = []
    for m in re.finditer(r'cx="(\d+)"', src):
        circs.append(dict(val=int(m.group(1))))

    # --- Phase 2: stretch range ---
    all_xs = set()
    for r in rects:
        if not r['bg']:
            all_xs.add(r['ox']); all_xs.add(r['or_'])
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
    # Also check transform rotation centers
    for m in re.finditer(r'transform="rotate\((-?\d+),(\d+),(-?\d+)\)"', src):
        cx_val = int(m.group(2))
        if 0 < cx_val < vbw: all_xs.add(cx_val)

    if len(all_xs) < 3: continue
    old_min = min(all_xs); old_max = max(all_xs)
    gap = vbw - old_max
    do_stretch = gap >= MIN_GAP
    dl = 'STRETCH' if do_stretch else 'fontbox'
    print(f'  {dl:8s}  {fname:30s} gap={gap:3d}  range=[{old_min}..{old_max}]')

    # --- Phase 3: compute new positions ---
    for r in rects:
        if r['bg']:
            r['nh'] = new_vbh
            # Keep original width for bg rects
        else:
            r['nx'] = stretch(r['ox'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else r['ox']
            r['nw'] = int(r['ow'] * 1.05)
            r['nh'] = int(r['oh'] * 1.25)
            r['nr_'] = r['nx'] + r['nw']

    # Edge maps for connection repair
    right_edge_map = {}
    left_edge_map = {}
    for r in rects:
        if not r['bg']:
            right_edge_map[r['or_']] = r['nr_']
            left_edge_map[r['ox']] = r['nx']

    for l in lines:
        l['nx1'] = stretch(l['x1'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else l['x1']
        l['nx2'] = stretch(l['x2'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else l['x2']
        # Snap x1 to box edges
        for old_re, new_re in right_edge_map.items():
            if l['x1'] == old_re: l['nx1'] = new_re; break
        for old_le, new_le in left_edge_map.items():
            if l['x1'] == old_le: l['nx1'] = new_le; break
        for old_re, new_re in right_edge_map.items():
            if l['x2'] == old_re: l['nx2'] = new_re; break
        for old_le, new_le in left_edge_map.items():
            if l['x2'] == old_le: l['nx2'] = new_le; break
        # Fix backward connectors
        if l['nx1'] > l['nx2'] and l['nx1'] - l['nx2'] < 200:
            l['nx1'] = l['nx2']

    # Arrowheads - snap to connected line endpoints
    for pi in polys:
        npts = []
        for px, py in pi['pts']:
            new_px = stretch(px, old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else px
            for l in lines:
                if px == l['x2'] and py == l['y1']:
                    new_px = px + (l['nx2'] - l['x2'])
                    break
                if px == l['x1'] and py == l['y1']:
                    new_px = px + (l['nx1'] - l['x1'])
                    break
            npts.append((new_px, py))
        pi['npts'] = npts

    # --- Phase 4: string replacement ---
    replacements = []

    # Font
    seen = set()
    for m in re.finditer(r'font-size="(\d+)"', src):
        fs = int(m.group(1))
        if fs in FONT_MAP and fs not in seen:
            seen.add(fs)
            to = FONT_MAP[fs]
            if to != fs: replacements.append((f'font-size="{fs}"', f'font-size="{to}"'))

    # Text x
    for t in texts:
        new_x = stretch(t['ox'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else t['ox']
        if new_x != t['ox']: replacements.append((f'x="{t["ox"]}"', f'x="{new_x}"'))

    # Rect x, w, h
    for r in rects:
        if r['nx'] != r['ox']: replacements.append((f'x="{r["ox"]}"', f'x="{r["nx"]}"'))
        if r['nw'] != r['ow']: replacements.append((f'width="{r["ow"]}"', f'width="{r["nw"]}"'))
        if r['nh'] != r['oh']: replacements.append((f'height="{r["oh"]}"', f'height="{r["nh"]}"'))

    # Line x1, x2
    for l in lines:
        if l['nx1'] != l['x1']: replacements.append((f'x1="{l["x1"]}"', f'x1="{l["nx1"]}"'))
        if l['nx2'] != l['x2']: replacements.append((f'x2="{l["x2"]}"', f'x2="{l["nx2"]}"'))

    # Circle cx
    for c in circs:
        new_cx = stretch(c['val'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else c['val']
        if new_cx != c['val']: replacements.append((f'cx="{c["val"]}"', f'cx="{new_cx}"'))

    # Transform rotate centers
    for m in re.finditer(r'transform="rotate\((-?\d+),(\d+),(-?\d+)\)"', src):
        angle, old_cx, old_cy = int(m.group(1)), int(m.group(2)), int(m.group(3))
        new_cx = stretch(old_cx, old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else old_cx
        if new_cx != old_cx:
            replacements.append((f'rotate({angle},{old_cx},{old_cy})', f'rotate({angle},{new_cx},{old_cy})'))

    # Polygon points
    for pi in polys:
        old_s = ' '.join(f'{px},{py}' for px, py in pi['pts'])
        new_s = ' '.join(f'{nx},{ny}' for nx, ny in pi['npts'])
        if old_s != new_s: replacements.append((f'points="{old_s}"', f'points="{new_s}"'))

    # Viewbox and height
    if new_vbh != vbh:
        replacements.append((f'viewBox="0 0 {vbw} {vbh}"', f'viewBox="0 0 {vbw} {new_vbh}"'))
        replacements.append((f'height="{vbh}"', f'height="{new_vbh}"'))

    replacements.sort(key=lambda x: -len(x[0]))
    result = src
    for old_str, new_str in replacements:
        result = result.replace(old_str, new_str)

    if result != src:
        diff_lines = len(result.split('\n')) - len(src.split('\n'))
        with open(path, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f'         ✓ written ({abs(diff_lines)} line change)')

print('Done')
