import re
html = open(r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\docs\index.html', encoding='utf-8').read()
opens = html.count('<div')
closes = html.count('</div>')
print(f'Div balance: {opens} opens, {closes} closes (diff: {opens-closes})')
m = re.search(r'<div class=home-content>', html)
if m:
    print('home-content found in output V')
    region = html[m.end():]
    for key in ['topic-grid', 'about-card', 'site-disclaimer', 'guide-card']:
        if key in region[:8000]:
            print(f'  {key} inside home-content V')
        else:
            print(f'  {key} NOT in home-content (searching larger region)')
            if key in region:
                print(f'  {key} inside home-content (further down) V')
            else:
                print(f'  {key} NOT found anywhere')
else:
    print('home-content NOT found')
    # Search with different quote patterns
    m2 = re.search(r'home-content', html)
    if m2:
        print('  but "home-content" text exists in output')

card_imgs = re.findall(r'/images/featured/[^"\']+\.jpg', html)
print(f'\nCard images: {len(card_imgs)}')
print('  First 3:', card_imgs[:3])
print('  Last 3:', card_imgs[-3:])
