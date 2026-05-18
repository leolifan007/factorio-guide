"""SVG relayout v7: process ALL SVGs (flowcharts + diagrams), always stretch to fill canvas."""
import os, re

DIRS = [
    r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams',
    r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\flowcharts',
]

PAD_L, PAD_R = 30, 30
# Extended font map covering all sizes used in both dirs
FONT_MAP = {
    6: 9, 7: 10, 8: 11, 9: 12,    # original small
    10: 12,                        # 10 -> same size
    11: 13,                        # 11 -> 13
    12: 13,                        # 12 -> 13
    13: 13,                        # keep
    14: 14,                        # keep
    16: 16,                        # keep
    18: 18,                        # keep
}

def stretch(v, lo, hi, nl, nh):
    if hi <= lo: return v
    ratio = max(0, min(1, (v - lo) / (hi - lo)))
    return int(nl + ratio * (nh - nl))

def is_dec_band(x, w, h, vbw):
    """Check if rect is a decorative band (belt lines, separators)."""
    if w >= vbw * 0.8 and x <= 50 and h <= 15:
        return True
    return False

def is_canvas_bg(x, w, vbw):
    return x is None and w >= vbw - 2

def set_attr(tag, attr, new_val):
    """Replace attribute value in tag string."""
    return re.sub(r'\b' + attr + r'="(\d+)"', lambda m: f'{attr}="{new_val}"', tag)

def get_attr(tag, attr):
    m = re.search(r'\b' + attr + r'="(\d+)"', tag)
    return int(m.group(1)) if m else None

def process_svg(fname, path, src):
    vb = re.search(r'viewBox="(\d+) (\d+) (\d+) (\d+)"', src.split('\n')[0])
    if not vb:
        return src
    vb_x, vb_y, vbw, vbh = int(vb.group(1)), int(vb.group(2)), int(vb.group(3)), int(vb.group(4))

    lines = src.split('\n')

    # Collect ALL content x-positions
    xs = set()
    for ln in lines:
        # Rect edges (exclude full-canvas background)
        for m in re.finditer(r'<rect[^>]*?x="(\d+)"[^>]*?width="(\d+)"', ln):
            x, w = int(m.group(1)), int(m.group(2))
            if w < vbw - 2:  # not full-canvas
                xs.add(x)
                xs.add(x + w)
        # Text x
        for m in re.finditer(r'<text[^>]*?x="(\d+)"', ln):
            v = int(m.group(1))
            if 5 < v < vbw:
                xs.add(v)
        # Line x1, x2 (skip structural lines at edges)
        for a in ('x1', 'x2'):
            for m in re.finditer(r'\b' + a + r'="(\d+)"', ln):
                v = int(m.group(1))
                if 5 < v < vbw:
                    xs.add(v)
        # Circle cx (non-rotate)
        for m in re.finditer(r'cx="(\d+)"', ln):
            v = int(m.group(1))
            if 5 < v < vbw and 'rotate' not in ln:
                xs.add(v)
        # Rotate center
        for m in re.finditer(r'transform="rotate\((-?\d+),(\d+),(-?\d+)\)"', ln):
            v = int(m.group(2))
            if 5 < v < vbw:
                xs.add(v)

    if len(xs) < 3:
        return src

    old_min, old_max = min(xs), max(xs)
    gap = vbw - old_max

    # Always stretch if right gap >= 50px
    doe = gap >= 50

    new_height = int(vbh * 1.15)
    out = []

    for ln in lines:
        # SVG tag — update viewBox height
        if ln.startswith('<svg'):
            ln = re.sub(r'viewBox="0 0 \d+ \d+"', f'viewBox="0 0 {vbw} {new_height}"', ln)
            ln = re.sub(r'height="\d+"', f'height="{new_height}"', ln)

        # <rect>
        elif '<rect' in ln:
            x = get_attr(ln, 'x')
            w = get_attr(ln, 'width')
            h = get_attr(ln, 'height')
            if h is not None and w is not None:
                if is_canvas_bg(x, w, vbw):
                    ln = set_attr(ln, 'height', new_height)
                elif x is not None and is_dec_band(x, w, h, vbw):
                    nx = stretch(x, old_min, old_max, PAD_L, vbw - PAD_R) if doe else x
                    ln = set_attr(ln, 'x', nx)
                elif x is not None:
                    # Content box
                    nx = stretch(x, old_min, old_max, PAD_L, vbw - PAD_R) if doe else x
                    nw = int(w * 1.05)
                    nh = int(h * 1.25)
                    ln = set_attr(set_attr(set_attr(ln, 'x', nx), 'width', nw), 'height', nh)

        # <line>
        elif '<line' in ln:
            x1 = get_attr(ln, 'x1')
            x2 = get_attr(ln, 'x2')
            if x1 is not None and x2 is not None:
                if x1 == 0 and x2 >= vbw - 20:
                    out.append(ln)
                    continue  # structural divider
                nx1 = stretch(x1, old_min, old_max, PAD_L, vbw - PAD_R) if doe else x1
                nx2 = stretch(x2, old_min, old_max, PAD_L, vbw - PAD_R) if doe else x2
                if nx1 > nx2 and nx1 - nx2 < 200:
                    nx1 = nx2  # fold backward arrow
                ln = set_attr(set_attr(ln, 'x1', nx1), 'x2', nx2)

        # <text>
        elif '<text' in ln:
            x = get_attr(ln, 'x')
            if x is not None and 5 < x < vbw:
                nx = stretch(x, old_min, old_max, PAD_L, vbw - PAD_R) if doe else x
                ln = set_attr(ln, 'x', nx)

        # <circle>
        elif '<circle' in ln:
            cx = get_attr(ln, 'cx')
            if cx is not None and 5 < cx < vbw:
                ncx = stretch(cx, old_min, old_max, PAD_L, vbw - PAD_R) if doe else cx
                ln = set_attr(ln, 'cx', ncx)

        # Font-size: apply to all elements
        ln = re.sub(r'font-size="(\d+)"',
                    lambda m: f'font-size="{FONT_MAP.get(int(m.group(1)), int(m.group(1)))}"', ln)

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


for DIR in DIRS:
    print(f'\n=== {os.path.basename(DIR)} ===')
    for fname in sorted(os.listdir(DIR)):
        if not fname.endswith('.svg'):
            continue
        path = os.path.join(DIR, fname)
        with open(path, 'r', encoding='utf-8') as f:
            src = f.read()
        result = process_svg(fname, path, src)
        if result != src:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(result)
            old_size = len(src)
            new_size = len(result)
            print(f'  ✓ {fname:30s} {old_size:>5}B -> {new_size:>5}B')
        else:
            print(f'  - {fname:30s} (no change)')

print('\nDone')
