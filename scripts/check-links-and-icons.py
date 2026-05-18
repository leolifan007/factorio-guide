"""Check all content for broken image references and shortcode paths."""
import os, re

CONTENT_DIR = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\content'
STATIC_IMG = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images'
LAYOUT_SRC = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\layouts\shortcodes'

# Check shortcodes
print("=== Shortcode image references ===")
for fname in sorted(os.listdir(LAYOUT_SRC)):
    with open(os.path.join(LAYOUT_SRC, fname), 'r', encoding='utf-8') as f:
        content = f.read()
    for m in re.finditer(r'(images/(?:icon|game-icons|diagrams)/[^"\')\s]+)', content):
        img_path = m.group(1)
        abs_path = os.path.join(STATIC_IMG, '..', img_path).replace('/', os.sep)
        exists = os.path.exists(abs_path)
        status = '✅' if exists else '❌ MISSING'
        print(f'  {status} {img_path}  (in {fname})')

# Also check for direct img references in shortcodes
for fname in sorted(os.listdir(LAYOUT_SRC)):
    with open(os.path.join(LAYOUT_SRC, fname), 'r', encoding='utf-8') as f:
        content = f.read()
    for m in re.finditer(r'(icon|image|src)="([^"]+\.(?:png|svg|jpg))"', content):
        val = m.group(2)
        abs_path = os.path.join(STATIC_IMG, '..', val).replace('/', os.sep)
        exists = os.path.exists(abs_path)
        status = '✅' if exists else '❌ MISSING'
        print(f'  {status} {val}  (in {fname})')

# Check content markdown files for image refs
print("\n=== Content image references ===")
for root, dirs, files in os.walk(CONTENT_DIR):
    for fname in sorted(files):
        if not fname.endswith('.md'): continue
        fpath = os.path.join(root, fname)
        rel = os.path.relpath(fpath, CONTENT_DIR)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        for m in re.finditer(r'!\[([^\]]*)\]\(([^\)]+)\)', content):
            url = m.group(2).strip()
            if url.startswith('http'): continue
            # Try to resolve relative to content dir
            base_dir = os.path.dirname(fpath)
            target = os.path.normpath(os.path.join(base_dir, url))
            exists = os.path.exists(target) or os.path.exists(target.replace('.md', '')) or os.path.exists(target + '.md')
            status = '✅' if exists else '❌ MISSING'
            if not exists:
                print(f'  {status} {rel}: ![]({url})')

# Check for external links that might 404
print("\n=== External URL references ===")
urls_seen = set()
for root, dirs, files in os.walk(CONTENT_DIR):
    for fname in sorted(files):
        if not fname.endswith('.md'): continue
        fpath = os.path.join(root, fname)
        rel = os.path.relpath(fpath, CONTENT_DIR)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        for m in re.finditer(r'\[([^\]]+)\]\((https?://[^\)]+)\)', content):
            url = m.group(2)
            if 'leolifan007' in url and url not in urls_seen:
                urls_seen.add(url)
                print(f'  {rel}: [{m.group(1)}]({url})')

print('\nDone')
