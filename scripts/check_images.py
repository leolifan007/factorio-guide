import re
html = open(r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\docs\index.html', encoding='utf-8').read()
all_refs = [(m.start(), m.group()) for m in re.finditer(r'images/featured/[^\s">]+', html)]
print(f'Featured image refs: {len(all_refs)}')
for i, (start, ref) in enumerate(all_refs[:5]):
    ctx_start = max(0, start-30)
    ctx_end = min(len(html), start+len(ref)+30)
    ctx = html[ctx_start:ctx_end].replace('\n', ' ')
    print(f'  {i}: ...{ctx}...')
if len(all_refs) > 5:
    print(f'  ... ({len(all_refs)-5} more)')
    # Show last 3
    for i, (start, ref) in enumerate(all_refs[-3:], len(all_refs)-3):
        ctx_start = max(0, start-30)
        ctx_end = min(len(html), start+len(ref)+30)
        ctx = html[ctx_start:ctx_end].replace('\n', ' ')
        print(f'  {i}: ...{ctx}...')
