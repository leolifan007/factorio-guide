"""Check existing icon quality."""
import struct, os

d = r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\Factorio_Site\static\images\icon'
sizes = set()
for f in sorted(os.listdir(d)):
    p = os.path.join(d, f)
    with open(p, 'rb') as fh:
        h = fh.read(40)
    if h[:8] == b'\x89PNG\r\n\x1a\n':
        w = struct.unpack('>I', h[16:20])[0]
        hgt = struct.unpack('>I', h[20:24])[0]
    else:
        w = hgt = 0
    sizes.add((w, hgt))
    print(f'{f:30s} {w}x{hgt} {os.path.getsize(p):>6}B')

print(f'\nTotal icons: {len(os.listdir(d))}')
print(f'Unique sizes: {sizes}')
