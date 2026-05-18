"""Debug: find all x values in SVG and check gap"""
import os, re

diagram_dir = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'

for fname in sorted(os.listdir(diagram_dir)):
    if not fname.endswith('.svg'):
        continue
    path = os.path.join(diagram_dir, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    vb_match = re.search(r'viewBox="(\d+) (\d+) (\d+) (\d+)"', content)
    if not vb_match:
        continue
    vb_w = int(vb_match.group(3))
    vb_h = int(vb_match.group(4))
    
    xs = set()
    # All x values from any element
    for m in re.finditer(r'x="(\d+)"', content):
        xs.add(int(m.group(1)))
    # x1/x2 from lines
    for m in re.finditer(r'x1="(\d+)"', content):
        xs.add(int(m.group(1)))
    for m in re.finditer(r'x2="(\d+)"', content):
        xs.add(int(m.group(1)))
    # cx from circles
    for m in re.finditer(r'cx="(\d+)"', content):
        xs.add(int(m.group(1)))
    # polygon points
    for m in re.finditer(r'points="([^"]+)"', content):
        pts = m.group(1).split()
        for p in pts:
            parts = p.split(',')
            if len(parts) == 2:
                try:
                    xs.add(int(float(parts[0])))
                except:
                    pass
    
    if xs:
        old_min = min(xs)
        old_max = max(xs)
        gap = vb_w - old_max
        status = "STRETCH" if gap >= 120 else "skip"
        print(f'{status:8s} {fname:30s} x=[{old_min:3d}..{old_max:3d}] vb_w={vb_w:3d} gap={gap:3d}')
    else:
        print(f'{"no-x":8s} {fname:30s}')
