"""Check all SVGs for structural issues: overflow, backward connectors, layout problems."""
import os, re

DIR = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'

for fname in sorted(os.listdir(DIR)):
    if not fname.endswith('.svg'): continue
    path = os.path.join(DIR, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    vb = re.search(r'viewBox="(\d+) (\d+) (\d+) (\d+)"', content)
    if not vb:
        print(f'  ❌ {fname}: NO VIEWBOX')
        continue
    vbw, vbh = int(vb.group(3)), int(vb.group(4))

    issues = []

    # Collect all RHS values
    rhss = []

    # 1. Check rect overflow
    for m in re.finditer(r'<rect[^>]*?x="(\d+)"[^>]*?width="(\d+)"', content):
        x, w = int(m.group(1)), int(m.group(2))
        if w < vbw - 2 and x > 0:  # not background
            right = x + w
            rhss.append(right)
            if right > vbw:
                issues.append(f'rect overflow: x={x} w={w} right={right} > vbw={vbw}')

    # 2. Check text overflow
    for m in re.finditer(r'<text[^>]*?x="(\d+)"', content):
        x = int(m.group(1))
        rhss.append(x)
        if x > vbw:
            issues.append(f'text overflow: x={x} > vbw={vbw}')

    # 3. Check cx overflow
    for m in re.finditer(r'cx="(\d+)"', content):
        x = int(m.group(1))
        rhss.append(x)
        if x > vbw:
            issues.append(f'circle overflow: cx={x} > vbw={vbw}')

    # 4. Check line x2 overflow  
    for m in re.finditer(r'x2="(\d+)"', content):
        x2 = int(m.group(1))
        if 5 < x2 < 10000:
            rhss.append(x2)
            if x2 > vbw:
                issues.append(f'line x2={x2} > vbw={vbw}')

    # 5. Check backward connectors
    # Properly match each line tag, handle any attribute order
    for m in re.finditer(r'<line[^>]*?/>', content):
        tag = m.group(0)
        x1m = re.search(r'x1="(\d+)"', tag)
        x2m = re.search(r'x2="(\d+)"', tag)
        if x1m and x2m:
            x1, x2 = int(x1m.group(1)), int(x2m.group(1))
            if x1 > 30 and x2 > 30 and x1 > x2 + 5:  # significant backward
                issues.append(f'backward connector: x1={x1} → x2={x2} (Δ={x1-x2})')

    # Summary
    max_rhs = max(rhss) if rhss else 0
    gap = vbw - max_rhs

    if issues:
        print(f'  ⚠  {fname:30s} max={max_rhs:3d}/{vbw} gap={gap:3d}')
        for iss in issues:
            print(f'       {iss}')
    else:
        print(f'  ✓  {fname:30s} max={max_rhs:3d}/{vbw} gap={gap:3d}')
