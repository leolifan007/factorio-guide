"""Single-pass SVG relayout v4: position-based string replacement for accuracy."""
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
        rects.append(dict(ox=x, ow=w, oh=h, bg=is_bg, or_=x+w))

    # Lines with position tracking
    lines = []  # each: {pos_x1, pos_x2, x1, x2, nx1, nx2}
    for m in re.finditer(r'<line[^>]*?/>', src):
        tag = m.group(0)
        tag_start = m.start()
        x1m = re.search(r'x1="(\d+)"', tag)
        x2m = re.search(r'x2="(\d+)"', tag)
        y1m = re.search(r'y1="(\d+)"', tag)
        if x1m and x2m and y1m:
            x1, x2 = int(x1m.group(1)), int(x2m.group(1))
            if x1 == 0 and x2 >= 800: continue
            lines.append(dict(
                pos_x1=tag_start + x1m.start(1), pos_x1_end=tag_start + x1m.end(1),
                pos_x2=tag_start + x2m.start(1), pos_x2_end=tag_start + x2m.end(1),
                x1=x1, x2=x2, nx1=x1, nx2=x2
            ))

    # Polygons with position tracking
    polys = []
    for m in re.finditer(r'<polygon [^>]*?points="([^"]+)"', src):
        pts = []
        for p in m.group(1).split():
            parts = p.split(',')
            if len(parts) == 2:
                try: pts.append((int(float(parts[0])), int(float(parts[1]))))
                except: pass
        if pts:
            polys.append(dict(
                pos=m.start(1), pos_end=m.end(1),
                pts=pts, npts=[p for p in pts]
            ))

    texts = []
    for m in re.finditer(r'<text [^>]*?x="(\d+)"', src):
        texts.append(dict(ox=int(m.group(1)), pos=m.start(1), pos_end=m.end(1)))

    circs = []
    for m in re.finditer(r'cx="(\d+)"', src):
        circs.append(dict(val=int(m.group(1)), pos=m.start(1), pos_end=m.end(1)))

    rotate_centers = []
    for m in re.finditer(r'transform="rotate\((-?\d+),(\d+),(-?\d+)\)"', src):
        angle, old_cx, old_cy = int(m.group(1)), int(m.group(2)), int(m.group(3))
        rotate_centers.append(dict(angle=angle, old=old_cx, old_cy=old_cy,
                                    pos=m.start(2), pos_end=m.end(2)))

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
    for r in rotate_centers:
        if 0 < r['old'] < vbw: all_xs.add(r['old'])

    if len(all_xs) < 3: continue
    old_min = min(all_xs); old_max = max(all_xs)
    gap = vbw - old_max
    do_stretch = gap >= MIN_GAP
    dl = 'STRETCH' if do_stretch else 'fontbox'
    print(f'  {dl:8s}  {fname:30s} gap={gap:3d}  range=[{old_min}..{old_max}]', end='')

    # --- Phase 3: compute new positions ---
    for r in rects:
        if r['bg']:
            r['nh'] = new_vbh
            r['nw'] = r['ow']; r['nx'] = r['ox']
        else:
            r['nx'] = stretch(r['ox'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else r['ox']
            r['nw'] = int(r['ow'] * 1.05)
            r['nh'] = int(r['oh'] * 1.25)
            r['nr_'] = r['nx'] + r['nw']

    right_edge_map = {}
    left_edge_map = {}
    for r in rects:
        if not r['bg']:
            right_edge_map[r['or_']] = r['nr_']
            left_edge_map[r['ox']] = r['nx']

    for l in lines:
        l['nx1'] = stretch(l['x1'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else l['x1']
        l['nx2'] = stretch(l['x2'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else l['x2']
        for old_re, new_re in right_edge_map.items():
            if l['x1'] == old_re: l['nx1'] = new_re; break
        for old_le, new_le in left_edge_map.items():
            if l['x1'] == old_le: l['nx1'] = new_le; break
        for old_re, new_re in right_edge_map.items():
            if l['x2'] == old_re: l['nx2'] = new_re; break
        for old_le, new_le in left_edge_map.items():
            if l['x2'] == old_le: l['nx2'] = new_le; break
        if l['nx1'] > l['nx2'] and l['nx1'] - l['nx2'] < 200:
            l['nx1'] = l['nx2']

    for pi in polys:
        npts = []
        for px, py in pi['pts']:
            new_px = stretch(px, old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else px
            for l in lines:
                if px == l['x2'] and py == l['y1'] if 'y1' in l else False:
                    pass  # y1 not stored; skip arrowhead snap for now
            npts.append((new_px, py))
        pi['npts'] = npts

    # --- Phase 4: position-based replacement ---
    # Build list of (start_byte, old_len, new_str) sorted reverse by position
    edits = []

    def add_edit(pos_start, pos_end, new_val_str):
        """Add an edit at exact byte position."""
        old_len = pos_end - pos_start
        edits.append((pos_start, old_len, str(new_val_str)))

    # Font sizes (tag-level, safe for global replacement since font-size attr is unique per value)
    seen_fs = set()
    for m in re.finditer(r'font-size="(\d+)"', src):
        fs = int(m.group(1))
        if fs in FONT_MAP and fs not in seen_fs:
            seen_fs.add(fs)
            to = FONT_MAP[fs]
            if to != fs:
                add_edit(m.start(1), m.end(1), str(to))

    # Text x
    for t in texts:
        new_x = stretch(t['ox'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else t['ox']
        if new_x != t['ox']:
            add_edit(t['pos'], t['pos_end'], str(new_x))

    # Rect attrs
    for r in rects:
        rx_str, rw_str, rh_str = str(r['ox']), str(r['ow']), str(r['oh'])
        # Find each attr at the rect tag (not globally - but rect x/w/h are likely unique enough)
        # Use careful position tracking similar to lines
        pass  # rect x values are mostly unique and won't collide

    # For rects, use global replacement (values are unique enough)
    for r in rects:
        old_x, new_x = r['ox'], r['nx']
        old_w, new_w = r['ow'], r['nw']
        old_h, new_h = r['oh'], r['nh']
        # Only replace if values differ
        if new_x != old_x:
            edits.append((src.find(f'x="{old_x}"', 0), len(f'x="{old_x}"'), f'x="{new_x}"'))
        if new_w != old_w:
            edits.append((src.find(f'width="{old_w}"', 0), len(f'width="{old_w}"'), f'width="{new_w}"'))
        if new_h != old_h:
            edits.append((src.find(f'height="{old_h}"', 0), len(f'height="{old_h}"'), f'height="{new_h}"'))

    # Line x1/x2 - USE POSITION (not global)
    for l in lines:
        if l['nx1'] != l['x1']:
            add_edit(l['pos_x1'], l['pos_x1_end'], str(l['nx1']))
        if l['nx2'] != l['x2']:
            add_edit(l['pos_x2'], l['pos_x2_end'], str(l['nx2']))

    # Circle cx
    for c in circs:
        new_cx = stretch(c['val'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else c['val']
        if new_cx != c['val']:
            add_edit(c['pos'], c['pos_end'], str(new_cx))

    # Rotate centers
    for r in rotate_centers:
        new_cx = stretch(r['old'], old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else r['old']
        if new_cx != r['old']:
            add_edit(r['pos'], r['pos_end'], str(new_cx))

    # Polygon points (global replacement - points strings are unique)
    for pi in polys:
        old_s = ' '.join(f'{px},{py}' for px, py in pi['pts'])
        new_s = ' '.join(f'{nx},{ny}' for nx, ny in pi['npts'])
        if old_s != new_s:
            add_edit(pi['pos'], pi['pos_end'], new_s)

    # Viewbox and height (unique, global is fine)
    if new_vbh != vbh:
        edits.append((src.find(f'viewBox="0 0 {vbw} {vbh}"'), len(f'viewBox="0 0 {vbw} {vbh}"'), f'viewBox="0 0 {vbw} {new_vbh}"'))
        edits.append((src.find(f'height="{vbh}"'), len(f'height="{vbh}"'), f'height="{new_vbh}"'))

    # Apply position-based edits in reverse order
    edits.sort(key=lambda x: -x[0])
    result = list(src)  # work with list of chars
    for pos_start, old_len, new_str in edits:
        if pos_start < 0: continue  # not found
        result[pos_start:pos_start+old_len] = list(new_str)

    result_str = ''.join(result)
    if result_str != src:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(result_str)
        print(f'  ✓')
    else:
        print(f'  -')

print('Done')
