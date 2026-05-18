"""Download missing icons and fix SVG font sizes"""
import urllib.request, os

icon_dir = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\icon'

# Missing icons (local_name → wiki page name)
items = [
    ('uranium_fuel_cell', 'Uranium_fuel_cell'),
]

for name, wiki in items:
    dest = os.path.join(icon_dir, f'{name}.png')
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        print(f'  OK {name}.png (exists)')
        continue
    for url in [
        f'https://wiki.factorio.com/images/{wiki}.png',
        f'https://wiki.factorio.com/images/thumb/{wiki}.png/64px-{wiki}.png',
    ]:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as r:
                data = r.read()
                if len(data) >= 500:
                    with open(dest, 'wb') as f:
                        f.write(data)
                    print(f'  OK {name}.png ({len(data)//1024}KB)')
                    break
        except:
            pass
    else:
        print(f'  FAIL {name}.png')
