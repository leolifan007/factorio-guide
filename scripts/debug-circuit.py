"""Debug circuit-control SVG handling."""
import os, re

DIR = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\diagrams'
path = os.path.join(DIR, 'circuit-control.svg')

with open(path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')

vb = re.search(r'viewBox="(\d+) (\d+) (\d+) (\d+)"', lines[0])
vbw, vbh = int(vb.group(3)), int(vb.group(4))

xs = set()
for ln in lines:
    for m in re.finditer(r'<text[^>]*?x="(\d+)"', ln):
        v = int(m.group(1))
        if 0 < v < vbw:
            xs.add(v)

print(f"Content xs: {sorted(xs)}")
print(f"old_min={min(xs)}, old_max={max(xs)}")
print(f"gap={vbw - max(xs)}")

from collections import Counter
line_vals = Counter()
for ln in lines:
    m = re.search(r'<text[^>]*?x="(\d+)"', ln)
    if m:
        x = int(m.group(1))
        if x == 620:
            # Test the regex on this line
            r1 = re.search(r'x="(\d+)"', ln)
            r2 = re.search(r'\bx="(\d+)"', ln)
            print(f"\nLine: {repr(ln[:60])}")
            print(f"  Without \\b: {r1 and r1.group(0)}")
            print(f"  With \\b:    {r2 and r2.group(0)}")

            # Try set_attr equivalent
            new_ln = re.sub(r'x="\d+"', f'x="790"', ln)
            new_ln_b = re.sub(r'\bx="\d+"', f'x="790"', ln)
            print(f"  No \\b:  {repr(new_ln[:60])}")
            print(f"  With \\b: {repr(new_ln_b[:60])}")
            break
