import os
from PIL import Image

base = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide"
d = os.path.join(base, "static", "images", "featured")

for f in sorted(os.listdir(d)):
    if not f.endswith(".jpg"):
        continue
    p = os.path.join(d, f)
    sz = os.path.getsize(p)
    im = Image.open(p)
    print(f"{f:40s} {sz:>8,} bytes  {im.size[0]}x{im.size[1]}  mode={im.mode}")
