"""
Smart SVG layout fix: moderate font bump, enlarged boxes.
Titles (14px) untouched. Body text gets sensible sizing.
Box heights +25%, background + viewBox follow.
"""
import os, re

diagram_dir = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'

FONT_MAP = {
    6: 9,
    7: 10,
    8: 11,
    9: 12,
    10: 12,
    11: 13,
    12: 13,
    13: 13,
    # 14 stays 14 (titles)
}

for fname in sorted(os.listdir(diagram_dir)):
    if not fname.endswith('.svg'):
        continue
    path = os.path.join(diagram_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse viewBox
    vb_match = re.search(r'viewBox="0 0 (\d+) (\d+)"', content)
    if not vb_match:
        print(f'  Skip {fname}')
        continue
    vb_w, vb_h = int(vb_match.group(1)), int(vb_match.group(2))
    new_vb_h = int(vb_h * 1.15)

    lines = content.split('\n')
    out = []
    for line in lines:
        nl = line

        # Font sizes: apply map
        nl = re.sub(r'font-size="(\d+)"',
            lambda m: f'font-size="{FONT_MAP.get(int(m.group(1)), int(m.group(1)))}"', nl)

        # Rect boxes: enlarge
        if '<rect ' in nl:
            is_bg = bool(re.match(r'\s*<rect\s+width="(8\d+)"', nl))
            if is_bg:
                nl = re.sub(r'height="(\d+)"', lambda m: f'height="{new_vb_h}"', nl)
            else:
                nl = re.sub(r'height="(\d+)"', lambda m: f'height="{int(int(m.group(1))*1.25)}"', nl)
                nl = re.sub(r'width="(\d+)"', lambda m: f'width="{int(int(m.group(1))*1.05)}"', nl)

        # SVG tag
        if '<svg ' in nl:
            nl = re.sub(r'viewBox="0 0 \d+ \d+"', f'viewBox="0 0 {vb_w} {new_vb_h}"', nl)
            nl = re.sub(r'height="(\d+)"', lambda m: f'height="{new_vb_h}"', nl)

        out.append(nl)

    new_content = '\n'.join(out)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'  Fixed {fname}')

print('Done')
