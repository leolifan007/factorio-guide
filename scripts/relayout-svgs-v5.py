"""SVG relayout v5: line-by-line processing for zero collision risk."""
import os, re

DIR = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'
MIN_GAP = 120
PAD_L, PAD_R = 30, 30
FONT_MAP = {6:9, 7:10, 8:11, 9:12, 10:12, 11:13, 12:13, 13:13}

def stretch(v, lo, hi, nl, nh):
    if hi <= lo: return v
    return int(nl + max(0, min(1, (v-lo)/(hi-lo))) * (nh-nl))

def is_bg_or_dec(w, x, vbw):
    """Check if a rect is background (full canvas) or decorative (near full width)."""
    return w >= vbw - 2 or (w >= vbw * 0.8 and x <= 50)

for fname in sorted(os.listdir(DIR)):
    if not fname.endswith('.svg'): continue
    path = os.path.join(DIR, fname)
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')

    # Read first line for viewBox
    vb = re.search(r'viewBox="(\d+) (\d+) (\d+) (\d+)"', lines[0])
    if not vb: continue
    vbw, vbh = int(vb.group(3)), int(vb.group(4))
    new_vbh = int(vbh * 1.15)

    # --- Phase 1: collect all content x values ---
    all_xs = set()

    for ln in lines:
        # rect x
        for m in re.finditer(r'<rect[^>]*?x="(\d+)"[^>]*?width="(\d+)"', ln):
            x, w = int(m.group(1)), int(m.group(2))
            if not is_bg_or_dec(w, x, vbw):
                all_xs.add(x); all_xs.add(x + w)
        # text x
        for m in re.finditer(r'<text[^>]*?x="(\d+)"', ln):
            v = int(m.group(1))
            if 0 < v < vbw: all_xs.add(v)
        # line x1/x2
        for attr in ['x1', 'x2']:
            for m in re.finditer(f'{attr}="(\\d+)"', ln):
                v = int(m.group(1))
                if 5 < v < vbw: all_xs.add(v)
        # cx
        for m in re.finditer(r'cx="(\d+)"', ln):
            v = int(m.group(1))
            if 0 < v < vbw: all_xs.add(v)
        # transform rotate center
        for m in re.finditer(r'transform="rotate\((-?\d+),(\d+),(-?\d+)\)"', ln):
            v = int(m.group(2))
            if 0 < v < vbw: all_xs.add(v)

    if len(all_xs) < 3: continue
    old_min = min(all_xs); old_max = max(all_xs)
    gap = vbw - old_max
    do_stretch = gap >= MIN_GAP

    print(f'  {"STRETCH" if do_stretch else "fontbox":>8}  {fname:30s} gap={gap:3d}  [{old_min}..{old_max}]', end='')

    # --- Phase 2: process line by line ---
    out = []

    for ln in lines:
        nl = ln

        # Font size - per occurrence
        nl = re.sub(r'font-size="(\d+)"',
                    lambda m: f'font-size="{FONT_MAP.get(int(m.group(1)), int(m.group(1)))}"', nl)

        # Text x - per occurrence (no lookbehind, check context manually)
        for m in reversed(list(re.finditer(r'x="(\d+)"', nl))):
            val = int(m.group(1))
            # Only process if this x belongs to a <text> tag
            prefix = nl[max(0,m.start()-60):m.start()]
            if not ('<text' in prefix and ('>' not in prefix.split('<text')[0] if '<text' in prefix else True)):
                continue  # not inside a text tag
            new_val = stretch(val, old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else val
            if new_val != val:
                nl = nl[:m.start()] + f'x="{new_val}"' + nl[m.end():]

        # Rect: handle width & height (per rect per line)
        def fix_rect(m):
            full = m.group(0)
            x = int(m.group(1))
            w = int(m.group(2))
            h = int(m.group(3))
            if is_bg_or_dec(w, x, vbw):
                # background or decorative: only change height
                full = re.sub(r'height="\d+"', f'height="{new_vbh}"', full)
                return full
            else:
                # content box: stretch x, enlarge w/h
                new_x = stretch(x, old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else x
                new_w = int(w * 1.05)
                new_h = int(h * 1.25)
                full = re.sub(r'x="\d+"', f'x="{new_x}"', full)
                full = re.sub(r'width="\d+"', f'width="{new_w}"', full)
                full = re.sub(r'height="\d+"', f'height="{new_h}"', full)
                return full

        nl = re.sub(r'<rect[^>]*?x="(\d+)"[^>]*?width="(\d+)"[^>]*?height="(\d+)"', fix_rect, nl)

        # Line x1/x2 - find ALL attributes independently within each line, no order dependency
        is_line = '<line' in nl and '/>' in nl
        if is_line:
            def snap_and_stretch(val, is_x1):
                if do_stretch:
                    sv = stretch(val, old_min, old_max, PAD_L, vbw-PAD_R)
                else:
                    sv = val
                return sv
            x1m = re.search(r'x1="(\d+)"', nl)
            x2m = re.search(r'x2="(\d+)"', nl)
            if x1m:
                x1_val = int(x1m.group(1))
                nx1 = snap_and_stretch(x1_val, True)
                x2_val = int(x2m.group(1)) if x2m else 0
                nx2 = snap_and_stretch(x2_val, False) if x2m else 0
                # backward connector fix
                if x1_val > 30 and x2_val > 30 and nx1 > nx2 and nx1 - nx2 < 200:
                    nx1 = nx2
                # Skip structural full-width lines
                if not (x1_val == 0 and x2_val >= 800):
                    nl = nl.replace(f'x1="{x1_val}"', f'x1="{nx1}"', 1)
                    if x2m:
                        nl = nl.replace(f'x2="{x2_val}"', f'x2="{nx2}"', 1)

        # Circle cx (only if not inside a transform rotate)
        for m in reversed(list(re.finditer(r'cx="(\d+)"', nl))):
            val = int(m.group(1))
            # Check this cx is not inside a transform attribute
            prefix = nl[max(0,m.start()-40):m.start()]
            if 'transform="rotate' in prefix:
                continue  # skip cx inside rotate transform
            new_val = stretch(val, old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else val
            nl = nl[:m.start()] + f'cx="{new_val}"' + nl[m.end():]

        # Transform rotate centers
        def fix_rotate(m):
            angle, old_cx, old_cy = int(m.group(1)), int(m.group(2)), int(m.group(3))
            new_cx = stretch(old_cx, old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else old_cx
            return f'transform="rotate({angle},{new_cx},{old_cy})"'
        nl = re.sub(r'transform="rotate\((-?\d+),(\d+),(-?\d+)\)"', fix_rotate, nl)

        # Polygon points: stretch x coordinates (keep y)
        def fix_polygon(m):
            pts_str = m.group(1)
            pts = []
            for p in pts_str.split():
                parts = p.split(',')
                if len(parts) == 2:
                    try:
                        px = int(float(parts[0]))
                        py = int(float(parts[1]))
                        new_px = stretch(px, old_min, old_max, PAD_L, vbw-PAD_R) if do_stretch else px
                        pts.append(f'{new_px},{py}')
                    except:
                        pts.append(p)
                else:
                    pts.append(p)
            return f'points="{" ".join(pts)}"'
        nl = re.sub(r'points="([^"]+)"', fix_polygon, nl)

        # SVG tag: update height
        nl = re.sub(r'viewBox="0 0 \d+ \d+"', f'viewBox="0 0 {vbw} {new_vbh}"', nl)
        nl = re.sub(r'height="\d+"', f'height="{new_vbh}"', nl)

        out.append(nl)

    result = '\n'.join(out)
    if result != '\n'.join(lines):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(result)
        print('  ✓')
    else:
        print('  -')

print('Done')
