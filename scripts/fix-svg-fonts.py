"""Bump font sizes in SVG diagrams for readability"""
import os, re

diagram_dir = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'

# Scale mapping: old_size → new_size
FONT_SCALE = {
    6:  11,
    7:  12,
    8:  13,
    9:  14,
    10: 14,
    11: 15,
    12: 15,
    13: 15,
}

for fname in sorted(os.listdir(diagram_dir)):
    if not fname.endswith('.svg'):
        continue
    path = os.path.join(diagram_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def bump(m):
        old = int(m.group(1))
        new = FONT_SCALE.get(old, old)
        return f'font-size="{new}"'
    
    new_content = re.sub(r'font-size="(\d+)"', bump, content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'  Updated {fname}')
    else:
        print(f'  Skipped {fname}')

print('Done')
