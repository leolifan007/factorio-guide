import re
for name in ['baseof.html', 'home.html', 'latest-articles.html']:
    path = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\layouts\_default\\' + name
    text = open(path, encoding='utf-8').read()
    opens = len(re.findall(r'<div[\s>]', text))
    closes = text.count('</div>')
    if name != 'baseof.html' and not path.endswith('latest-articles.html'):
        path = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\layouts\\' + ('partials\\' if name == 'latest-articles.html' else '_default\\') + name
        text = open(path, encoding='utf-8').read()
        opens = len(re.findall(r'<div[\s>]', text))
        closes = text.count('</div>')
    print(f'{name:25s}  <div: {opens:3d}  </div>: {closes:3d}  diff: {opens-closes:+3d}')
