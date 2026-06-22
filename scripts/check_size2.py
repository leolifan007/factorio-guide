import os, sys

d = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\featured"
for f in sorted(os.listdir(d)):
    if not f.endswith(".jpg"):
        continue
    p = os.path.join(d, f)
    sz = os.path.getsize(p)
    print(f"{f}: {sz} bytes")
