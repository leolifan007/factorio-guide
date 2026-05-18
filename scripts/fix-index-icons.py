"""Replace SVG icon references with real PNG icons in _index.md files."""
import os, re

FILES = [
    (r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\content\getting-started\_index.md',
     {
         'red-science': 'automation_science.png',
         'green-science': 'logistic_science.png',
         'furnace': 'stone_furnace.png',
         'assembler': 'assembling_machine_1.png',
         'inserter': 'inserter.png',
         'transport-belt': 'transport_belt.png',
     }),
    (r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\content\science-packs\_index.md',
     {
         'red-science': 'automation_science.png',
         'green-science': 'logistic_science.png',
         'military-science': 'military_science.png',
         'blue-science': 'chemical_science.png',
         'purple-science': 'production_science.png',
         'yellow-science': 'utility_science.png',
         'space-science': 'space_science.png',
     })
]

for fpath, mapping in FILES:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    count = 0
    for svg_name, png_name in mapping.items():
        old = f'/factorio-guide/images/icons/{svg_name}.svg'
        new = f'/factorio-guide/images/icon/{png_name}'
        if old in content:
            content = content.replace(old, new)
            count += 1
            print(f'  {svg_name}.svg -> {png_name}  ({os.path.basename(fpath)})')
    
    # Also remove the onerror fallback for cleanliness
    # Pattern: onerror="..." without changing the rest
    content = re.sub(r'\s+onerror="[^"]*"', '', content)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  -> Updated {count} references in {os.path.basename(fpath)}\n')
