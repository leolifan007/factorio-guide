"""
Smart SVG stretch: stretch content then re-connect box edges to lines.
After basic linear stretch, snaps line endpoints to box right-edges.
"""
import os, re

diagram_dir = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'
MIN_GAP = 120
PAD_L = 30
PAD_R = 30

def get_vb(content):
    m = re.search(r'viewBox="(\d+) (\d+) (\d+) (\d+)"', content)
    if not m: return None, None
    return int(m.group(3)), int(m.group(4))

def parse_before(content):
    """Parse original rect positions and line connections for later fixing."""
    rects = []  # [(x, w, right_edge)]
    for m in re.finditer(r'<rect [^>]*?x="(\d+)"[^>]*width="(\d+)"', content):
        x = int(m.group(1)); w = int(m.group(2))
        if w < 750:  # not background
            rects.append((x, w, x + w))

    lines = []  # [(x1, x2, y)]
    for m in re.finditer(r'<line [^>]*x1="(\d+)"[^>]*x2="(\d+)"[^>]*y1="(\d+)"', content):
        lines.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))
    for m in re.finditer(r'<line [^>]*x2="(\d+)"[^>]*x1="(\d+)"[^>]*y1="(\d+)"', content):
        if (int(m.group(2)), int(m.group(1)), int(m.group(3))) not in lines:
            lines.append((int(m.group(2)), int(m.group(1)), int(m.group(3))))

    polys = []  # [(x_coords, y, type)]
    for m in re.finditer(r'<polygon [^>]*points="([^"]+)"', content):
        pts = m.group(1).split()
        coords = []
        for p in pts:
            parts = p.split(',')
            if len(parts) == 2:
                try: coords.append((int(float(parts[0])), int(float(parts[1]))))
                except: pass
        if coords:
            polys.append(coords)

    return rects, lines, polys

def collect_stretch_xs(content, vb_w):
    """Collect content x positions to determine stretch range."""
    xs = set()
    # Text x
    for m in re.finditer(r'<text [^>]*x="(\d+)"', content):
        v = int(m.group(1))
        if 0 < v < vb_w: xs.add(v)
    # Rect x (not background)
    for m in re.finditer(r'<rect [^>]*x="(\d+)"', content):
        tag = m.group(0)
        wm = re.search(r'width="(\d+)"', tag)
        if wm and int(wm.group(1)) >= vb_w - 2: continue
        v = int(m.group(1))
        if 0 < v < vb_w: xs.add(v)
    # Line x1/x2 (not full-width)
    for m in re.finditer(r'x1="(\d+)"', content):
        v = int(m.group(1))
        if 0 < v < vb_w: xs.add(v)
    for m in re.finditer(r'x2="(\d+)"', content):
        v = int(m.group(1))
        if 0 < v < vb_w: xs.add(v)
    # Circle cx
    for m in re.finditer(r'cx="(\d+)"', content):
        v = int(m.group(1))
        if 0 < v < vb_w: xs.add(v)
    # Polygon x
    for m in re.finditer(r'points="([^"]+)"', content):
        for p in m.group(1).split():
            parts = p.split(',')
            if len(parts) == 2:
                try:
                    v = int(float(parts[0]))
                    if 0 < v < vb_w: xs.add(v)
                except: pass
    return sorted(xs)

def stretch(x, old_min, old_max, new_min, new_max):
    """Linear interpolation, clamped."""
    if old_max <= old_min: return x
    r = max(0, min(1, (x - old_min) / (old_max - old_min)))
    return int(new_min + r * (new_max - new_min))

def fix_line_connections(content, old_rects, old_lines, old_polys, 
                         old_min, old_max, new_min, new_max):
    """Snap lines that connected to box edges in original layout."""
    
    # For each original rect, compute its stretched version
    rect_map = []  # [(old_right_edge, new_right_edge)]
    for x, w, re_ in old_rects:
        stretched_x = stretch(x, old_min, old_max, new_min, new_max)
        stretched_w = int(w * 1.05)  # from fix-svg-layout: width * 1.05, but already applied
        rect_map.append((re_, stretched_x + stretched_w))

    # For each line, if x1 connected to a rect right-edge, snap
    replacements = {}  # {(old_val, attr) -> new_val}
    for x1, x2, y in old_lines:
        sx1 = stretch(x1, old_min, old_max, new_min, new_max)
        sx2 = stretch(x2, old_min, old_max, new_min, new_max)
        
        # Check if x1 matched a rect right edge
        for old_re, new_re in rect_map:
            if abs(x1 - old_re) <= 2 and abs(sx1 - new_re) > 3:
                # Snap x1 to new right edge
                replacements[(x1, 'x1')] = new_re
                break
        
        # Check if x2 matched a rect left edge or something connected
        for old_re, new_re in rect_map:
            # Check if x2 is near a rect right edge (arriving arrow)
            if abs(x2 - old_re) <= 2 and abs(sx2 - new_re) > 3:
                replacements[(x2, 'x2')] = new_re
                break
    
    # For polygons, check if any x is near a line's x2 at same y
    # First check if poly points match line endpoints
    for poly_coords in old_polys:
        stretch_pts = []
        for cx, cy in poly_coords:
            scx = stretch(cx, old_min, old_max, new_min, new_max)
            scy = cy  # y not stretched
            stretch_pts.append((scx, scy, cx, cy))
        
        # Check if middle/tip point matches a line end
        for i, (scx, scy, ocx, ocy) in enumerate(stretch_pts):
            for old_x1, old_x2, old_y in old_lines:
                if abs(ocy - old_y) <= 5:
                    # Check if this poly point corresponds to line x2
                    if abs(ocx - old_x2) <= 3:
                        sn = stretch(old_x2, old_min, old_max, new_min, new_max)
                        # Check if line x2 was also snapped
                        srckey = (old_x2, 'x2')
                        if srckey in replacements:
                            sn = replacements[srckey]
                        replacements[(ocx, f'poly_{i}x')] = sn
    
    # Apply replacements
    lines = content.split('\n')
    out_lines = []
    for line in lines:
        nl = line
        for (old_val, attr), new_val in replacements.items():
            if attr.startswith('poly_'):
                idx = int(attr.split('_')[1])
                # Replace in polygon points
                nl = re.sub(
                    r'points="([^"]*)"',
                    lambda m: fix_poly_point(m, old_val, new_val, idx),
                    nl
                )
            else:
                nl = nl.replace(f'{attr}="{old_val}"', f'{attr}="{new_val}"')
        out_lines.append(nl)
    return '\n'.join(out_lines)

def fix_poly_point(m, old_val, new_val, idx):
    pts_str = m.group(1)
    parts = pts_str.split()
    count = 0
    new_parts = []
    for p in parts:
        coords = p.split(',')
        if len(coords) == 2:
            try:
                cx = int(float(coords[0]))
                if cx == old_val:
                    if count == idx:
                        new_parts.append(f'{new_val},{coords[1]}')
                        count += 1
                        continue
                    count += 1
            except:
                pass
        new_parts.append(p)
    return f'points="{" ".join(new_parts)}"'

# Main
for fname in sorted(os.listdir(diagram_dir)):
    if not fname.endswith('.svg'): continue
    path = os.path.join(diagram_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    vb_w, _ = get_vb(content)
    if not vb_w: continue
    
    xs = collect_stretch_xs(content, vb_w)
    if len(xs) < 3: continue
    
    old_min = min(xs)
    old_max = max(xs)
    gap = vb_w - old_max
    
    if gap < MIN_GAP:
        print(f'  ─  {fname:30s} gap={gap}px')
        continue
    
    print(f'  ▶  {fname:30s} gap={gap}px  [{old_min}..{old_max}]→[{PAD_L}..{vb_w-PAD_R}]')
    
    # Parse original connections
    old_rects, old_lines, old_polys = parse_before(content)
    old_content = content
    
    # Basic stretch
    def do_stretch(m, attr):
        tag = m.group(0)
        old = int(m.group(1))
        new = stretch(old, old_min, old_max, PAD_L, vb_w - PAD_R)
        return tag.replace(f'{attr}="{old}"', f'{attr}="{new}"')
    
    # Text x
    content = re.sub(r'<text [^>]*x="(\d+)"', lambda m: do_stretch(m, 'x'), content)
    # Rect x (skip bg)
    def stretch_rect_x(m):
        tag = m.group(0)
        wm = re.search(r'width="(\d+)"', tag)
        if wm and int(wm.group(1)) >= vb_w - 2: return tag
        old = int(m.group(1))
        new = stretch(old, old_min, old_max, PAD_L, vb_w - PAD_R)
        return tag.replace(f'x="{old}"', f'x="{new}"')
    content = re.sub(r'<rect [^>]*x="(\d+)"', stretch_rect_x, content)
    # Lines
    content = re.sub(r'x1="(\d+)"', lambda m: do_stretch(m, 'x1'), content)
    content = re.sub(r'x2="(\d+)"', lambda m: do_stretch(m, 'x2'), content)
    # Circle cx
    content = re.sub(r'cx="(\d+)"', lambda m: do_stretch(m, 'cx'), content)
    # Polygon points
    def stretch_points(m):
        pts = m.group(1).split()
        new_pts = []
        for p in pts:
            parts = p.split(',')
            if len(parts) == 2:
                try:
                    nx = stretch(int(float(parts[0])), old_min, old_max, PAD_L, vb_w - PAD_R)
                    new_pts.append(f'{nx},{parts[1]}')
                except:
                    new_pts.append(p)
            else:
                new_pts.append(p)
        return f'points="{" ".join(new_pts)}"'
    content = re.sub(r'points="([^"]+)"', stretch_points, content)
    
    # Fix connections
    content = fix_line_connections(content, old_rects, old_lines, old_polys,
                                   old_min, old_max, PAD_L, vb_w - PAD_R)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done')
