"""Check what the actual set_attr regex string is."""
import re

# Read the v6 script
with open(r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\scripts\relayout-svgs-v6.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show lines 19 (set_attr) and 23 (get_attr)
for i in [18, 19, 22, 23]:
    ln = lines[i]
    print(f'Line {i+1}: {repr(ln.rstrip())}')
print()

# Test the actual regex
tag = '<text x="620" y="30" font-size="8" fill="#555">test</text>'

# What the f-string produces
attr = 'x'
pattern = f'\\b{attr}="\\d+"'
print(f'Pattern with \\b: {repr(pattern)}')

result1 = re.sub(pattern, 'x="790"', tag)
print(f'With \\b: {result1}')

# What I think we need
pattern2 = f'\\\\b{attr}="\\\\d+"'
print(f'Pattern with \\\\b: {repr(pattern2)}')

result2 = re.sub(pattern2, 'x="790"', tag)
print(f'With \\\\b: {result2}')
