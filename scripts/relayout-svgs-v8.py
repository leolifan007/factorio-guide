"""SVG relayout v8: NO font size changes. Only stretch horizontally and enlarge viewBox."""
import os, re

DIAGRAM_DIR = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'
PAD_L, PAD_R = 30, 30

def stretch(v, lo, hi, nl, nh):
    if hi <= lo: return v
    ratio = max(0, min(1, (v - lo) / (hi - lo)))
    return int(nl + ratio * (nh - nl))

def set_attr(tag, attr, new_val):
    return re.sub(r'\b' + attr + r'="(\d+)"', lambda m: f'{attr}="{new_val}"', tag)

def get_attr(tag, attr):
    m = re.search(r'\b' + attr + r'="(\d+)"', tag)
    return int(m.group(1)) if m else None

def process_svg(fname, path, src):
    vb = re.search(r'viewBox="(\d+) (\d+) (\d+) (\d+)"', src.split('\n')[0])
    if not vb: return src
    vb_x, vb_y, vbw, vbh = int(vb.group(1)), int(vb.group(2)), int(vb.group(3)), int(vb.group(4))

    lines = src.split('\n')

    # Collect content x positions
    xs = set()
    for ln in lines:
        # Rect edges (skip background canvas)
        for m in re.finditer(r'<rect[^>]*?x="(\d+)"[^>]*?width="(\d+)"', ln):
            x, w = int(m.group(1)), int(m.group(2))
            if w < vbw - 2:
                xs.add(x); xs.add(x + w)
        # Text x
        for m in re.finditer(r'<text[^>]*?x="(\d+)"', ln):
            v = int(m.group(1))
            if 5 < v < vbw: xs.add(v)
        # Line x1/x2 (skip structural edge lines)
        for a in ('x1', 'x2'):
            for m in re.finditer(r'\b' + a + r'="(\d+)"', ln):
                v = int(m.group(1))
                if 5 < v < vbw: xs.add(v)
        # Circle cx (non-rotate)
        for m in re.finditer(r'cx="(\d+)"', ln):
            v = int(m.group(1))
            if 5 < v < vbw and 'rotate' not in ln: xs.add(v)

    if len(xs) < 3: return src
    old_min, old_max = min(xs), max(xs)
    gap = vbw - old_max

    # Only stretch if there's a meaningful right gap
    doe = gap >= 80

    if not doe and gap >= 30:
        # Even if not enough to stretch, just enlarge viewBox slightly
        new_h = int(vbh * 1.10)
        out = []
        for ln in lines:
            if ln.startswith('<svg'):
                ln = re.sub(r'viewBox="0 0 \d+ \d+"', f'viewBox="0 0 {vbw} {new_h}"', ln)
                ln = re.sub(r'height="\d+"', f'height="{new_h}"', ln)
            elif '<rect' in ln:
                x = get_attr(ln, 'x')
                w = get_attr(ln, 'width')
                h = get_attr(ln, 'height')
                if h is not None and w is not None and x is None and w >= vbw - 2:
                    # Background rect - extend height
                    ln = set_attr(ln, 'height', new_h)
            out.append(ln)
        return '\n'.join(out)

    new_h = int(vbh * 1.15)
    out = []
    for ln in lines:
        # SVG tag
        if ln.startswith('<svg'):
            ln = re.sub(r'viewBox="0 0 \d+ \d+"', f'viewBox="0 0 {vbw} {new_h}"', ln)
            ln = re.sub(r'height="\d+"', f'height="{new_h}"', ln)

        # <rect>
        elif '<rect' in ln:
            x = get_attr(ln, 'x')
            w = get_attr(ln, 'width')
            h = get_attr(ln, 'height')
            if h is not None and w is not None:
                # Background
                if x is None and w >= vbw - 2:
                    ln = set_attr(ln, 'height', new_h)
                # Decorative band (belt lines)
                elif x is not None and 0 <= x <= 50 and w >= vbw * 0.8 and h <= 15:
                    nx = stretch(x, old_min, old_max, PAD_L, vbw - PAD_R) if doe else x
                    ln = set_attr(ln, 'x', nx)
                # Content rect: stretch x, slightly enlarge
                elif x is not None:
                    nx = stretch(x, old_min, old_max, PAD_L, vbw - PAD_R) if doe else x
                    nw = int(w * 1.05)
                    nh = int(h * 1.15)
                    ln = set_attr(set_attr(set_attr(ln, 'x', nx), 'width', nw), 'height', nh)

        # <line>
        elif '<line' in ln:
            x1 = get_attr(ln, 'x1')
            x2 = get_attr(ln, 'x2')
            if x1 is not None and x2 is not None:
                if x1 == 0 and x2 >= vbw - 20:
                    out.append(ln); continue
                nx1 = stretch(x1, old_min, old_max, PAD_L, vbw - PAD_R) if doe else x1
                nx2 = stretch(x2, old_min, old_max, PAD_L, vbw - PAD_R) if doe else x2
                if nx1 > nx2 and nx1 - nx2 < 200:
                    nx1 = nx2
                ln = set_attr(set_attr(ln, 'x1', nx1), 'x2', nx2)

        # <text> — stretch x, KEEP font-size
        elif '<text' in ln:
            x = get_attr(ln, 'x')
            if x is not None and 5 < x < vbw:
                nx = stretch(x, old_min, old_max, PAD_L, vbw - PAD_R) if doe else x
                ln = set_attr(ln, 'x', nx)

        # <circle> — stretch cx
        elif '<circle' in ln:
            cx = get_attr(ln, 'cx')
            if cx is not None and 5 < cx < vbw:
                ncx = stretch(cx, old_min, old_max, PAD_L, vbw - PAD_R) if doe else cx
                ln = set_attr(ln, 'cx', ncx)

        # Polygon points — stretch x
        if 'points="' in ln:
            def fix_pts(m):
                pts = []
                for p in m.group(1).split():
                    parts = p.split(',')
                    if len(parts) == 2:
                        try:
                            px = int(float(parts[0]))
                            py = int(float(parts[1]))
                            npx = stretch(px, old_min, old_max, PAD_L, vbw - PAD_R) if doe else px
                            pts.append(f'{npx},{py}')
                        except ValueError:
                            pts.append(p)
                    else:
                        pts.append(p)
                return f'points="{" ".join(pts)}"'
            ln = re.sub(r'points="([^"]+)"', fix_pts, ln)

        # Transform rotate
        if 'transform="rotate(' in ln:
            def fix_rot(m):
                angle = int(m.group(1))
                old_cx = int(m.group(2))
                old_cy = int(m.group(3))
                new_cx = stretch(old_cx, old_min, old_max, PAD_L, vbw - PAD_R) if doe else old_cx
                return f'transform="rotate({angle},{new_cx},{old_cy})"'
            ln = re.sub(r'transform="rotate\((-?\d+),(\d+),(-?\d+)\)"', fix_rot, ln)

        out.append(ln)
    return '\n'.join(out)


for fname in sorted(os.listdir(DIAGRAM_DIR)):
    if not fname.endswith('.svg'): continue
    path = os.path.join(DIAGRAM_DIR, fname)
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    result = process_svg(fname, path, src)
    if result != src:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f'  OK {fname:30s} {len(src):>5}B -> {len(result):>5}B')
    else:
        print(f'  -- {fname:30s} (no change)')

print('Done')
