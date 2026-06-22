html = open(r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\docs\index.html', encoding='utf-8').read()
opens = html.count('<div')
closes = html.count('</div>')
if opens == closes:
    print(f'div balance OK: {opens} opens, {closes} closes')
else:
    print(f'div MISMATCH: {opens} opens, {closes} closes (diff: {opens - closes})')

# Check for home-content wrapping
import re
home_opens = list(re.finditer('<div[^>]*class="[^"]*home-content', html))
home_closes = []
# Find home-content closing - look for </div> after the home-content open
print(f'home-content opens: {len(home_opens)}')
if home_opens:
    idx = home_opens[0].start()
    # Find enough context
    snippet_start = max(0, html.rfind('<div', 0, idx) - 200)
    # Look at region after home-content for closing
    region = html[idx:idx+2000]
    print(f'Home-content wrap check: home-content present')

# Check featured images referenced in cards
card_imgs = re.findall(r'<img[^>]*src="([^"]*)"', html)
print(f'\nCard images found: {len(card_imgs)}')
for img in card_imgs[:5]:
    print(f'  {img}')
print('  ...' if len(card_imgs) > 5 else '')
