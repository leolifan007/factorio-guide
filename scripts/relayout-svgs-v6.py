"""SVG relayout v6: parse tag attributes, modify, rebuild. Zero collision risk."""
import os, re

DIR = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'
MIN_GAP, PAD_L, PAD_R = 120, 30, 30
FONT_MAP = {6:9, 7:10, 8:11, 9:12, 10:12, 11:13, 12:13, 13:13}

def stretch(v, lo, hi, nl, nh):
    if hi <= lo: return v
    return int(nl + max(0, min(1, (v-lo)/(hi-lo))) * (nh-nl))

def is_bg_dec(x, w, h, vbw):
    """Check if rect is background (full canvas) or decorative band (near full width, thin)."""
    full_canvas = (w >= vbw - 2)  # x=0, width=820 -> background
    is_band = (w >= vbw * 0.8 and x <= 50 and h <= 15)  # e.g. bus belt lines
    return full_canvas or is_band

def set_attr(tag, attr, new_val):
    """Replace attribute value in tag string. Uses word-boundary to avoid partial matches (rx vs x)."""
    return re.sub(f'\\b{attr}="\\d+"', f'{attr}="{new_val}"', tag)

def get_attr(tag, attr):
    m = re.search(f'\\b{attr}="(\\d+)"', tag)
    return int(m.group(1)) if m else None

def process_svg(fname, path, src):
    vb = re.search(r'viewBox="(\d+) (\d+) (\d+) (\d+)"', src.split('\n')[0])
    if not vb: return src
    vbw, vbh = int(vb.group(3)), int(vb.group(4))

    lines = src.split('\n')

    # Collect all content X positions
    xs = set()
    for ln in lines:
        for m in re.finditer(r'(?:(?:<(?:rect|text|circle|polygon|line)[^>]*?)?)'
                             r'(?:x|width|cx|x1|x2)="(\d+)"(?:[^>]*?/?"?\.?\s*)', ln):
            pass  # placeholder, we use specific patterns below
        # Just collect all as per earlier approach
        # rect edges (skip full-canvas background)
        for m in re.finditer(r'<rect[^>]*?x="(\d+)"[^>]*?width="(\d+)"', ln):
            x, w = int(m.group(1)), int(m.group(2))
            if not (w >= vbw - 2):
                xs.add(x); xs.add(x + w)
        # text x
        for m in re.finditer(r'<text[^>]*?x="(\d+)"', ln):
            v = int(m.group(1))
            if 0 < v < vbw: xs.add(v)
        # line x1/x2
        for a in ['x1', 'x2']:
            for m in re.finditer(f'\\b{a}="(\\d+)"', ln):
                v = int(m.group(1))
                if 5 < v < vbw: xs.add(v)
        # cx (non-rotate)
        for m in re.finditer(r'cx="(\d+)"', ln):
            v = int(m.group(1))
            if 0 < v < vbw and 'rotate' not in ln: xs.add(v)
        # rotate center
        for m in re.finditer(r'transform="rotate\((-?\d+),(\d+),(-?\d+)\)"', ln):
            v = int(m.group(2))
            if 0 < v < vbw: xs.add(v)

    if len(xs) < 3: return src
    old_min, old_max = min(xs), max(xs)
    gap = vbw - old_max
    doe = gap >= MIN_GAP

    out = []

    for ln in lines:
        # SVG tag
        if ln.startswith('<svg'):
            ln = re.sub(r'viewBox="0 0 \d+ \d+"', f'viewBox="0 0 {vbw} {int(vbh*1.15)}"', ln)
            ln = re.sub(r'height="\d+"', f'height="{int(vbh*1.15)}"', ln)

        # <rect> - check type
        elif '<rect' in ln:
            x = get_attr(ln, 'x')
            w = get_attr(ln, 'width')
            h = get_attr(ln, 'height')
            if h is not None and w is not None:
                w_val = w; h_val = h
                canvas_bg = (x is None and w_val >= vbw - 2)  # full-canvas background
                dec_band = (x is not None and w_val >= vbw * 0.8 and x <= 50 and h_val <= 15)
                
                if canvas_bg:
                    ln = set_attr(ln, 'height', int(vbh * 1.15))
                elif dec_band:
                    # Decorative band: stretch x only, keep original w/h
                    nx = stretch(x, old_min, old_max, PAD_L, vbw-PAD_R) if doe else x
                    ln = set_attr(ln, 'x', nx)
                elif x is not None:
                    # Content box: stretch x, enlarge w/h
                    nx = stretch(x, old_min, old_max, PAD_L, vbw-PAD_R) if doe else x
                    nw = int(w_val * 1.05)
                    nh = int(h_val * 1.25)
                    ln = set_attr(set_attr(set_attr(ln, 'x', nx), 'width', nw), 'height', nh)

        # <line> - handle any attr order
        elif '<line' in ln:
            x1 = get_attr(ln, 'x1')
            x2 = get_attr(ln, 'x2')
            if x1 is not None and x2 is not None:
                if x1 == 0 and x2 >= 800:
                    out.append(ln); continue  # skip structural line
                nx1 = stretch(x1, old_min, old_max, PAD_L, vbw-PAD_R) if doe else x1
                nx2 = stretch(x2, old_min, old_max, PAD_L, vbw-PAD_R) if doe else x2
                if nx1 > nx2 and nx1 - nx2 < 200:
                    nx1 = nx2
                ln = set_attr(set_attr(ln, 'x1', nx1), 'x2', nx2)

        # <text> - stretch x
        elif '<text' in ln:
            x = get_attr(ln, 'x')
            if x is not None and 0 < x < vbw:
                nx = stretch(x, old_min, old_max, PAD_L, vbw-PAD_R) if doe else x
                ln = set_attr(ln, 'x', nx)

        # <circle> - stretch cx (only if not inside rotate transform)
        elif '<circle' in ln:
            cx = get_attr(ln, 'cx')
            if cx is not None and 0 < cx < vbw:
                ncx = stretch(cx, old_min, old_max, PAD_L, vbw-PAD_R) if doe else cx
                ln = set_attr(ln, 'cx', ncx)

        # Font-size (any element)
        ln = re.sub(r'font-size="(\d+)"',
                    lambda m: f'font-size="{FONT_MAP.get(int(m.group(1)), int(m.group(1)))}"', ln)

        # Polygon points - stretch x
        if 'points="' in ln:
            def fix_pts(m):
                pts = []
                for p in m.group(1).split():
                    parts = p.split(',')
                    if len(parts) == 2:
                        try:
                            px, py = int(float(parts[0])), int(float(parts[1]))
                            npx = stretch(px, old_min, old_max, PAD_L, vbw-PAD_R) if doe else px
                            pts.append(f'{npx},{py}')
                        except:
                            pts.append(p)
                    else:
                        pts.append(p)
                return f'points="{" ".join(pts)}"'
            ln = re.sub(r'points="([^"]+)"', fix_pts, ln)

        # Transform rotate center
        if 'transform="rotate(' in ln:
            def fix_rot(m):
                angle = int(m.group(1))
                old_cx = int(m.group(2))
                old_cy = int(m.group(3))
                new_cx = stretch(old_cx, old_min, old_max, PAD_L, vbw-PAD_R) if doe else old_cx
                return f'transform="rotate({angle},{new_cx},{old_cy})"'
            ln = re.sub(r'transform="rotate\((-?\d+),(\d+),(-?\d+)\)"', fix_rot, ln)

        out.append(ln)

    result = '\n'.join(out)
    return result

for fname in sorted(os.listdir(DIR)):
    if not fname.endswith('.svg'): continue
    path = os.path.join(DIR, fname)
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()

    result = process_svg(fname, path, src)
    if result != src:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f'  ✓  {fname:30s}')
    else:
        print(f'  -  {fname:30s} (no change)')

print('Done')
