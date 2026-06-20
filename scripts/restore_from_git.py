import subprocess, os

base = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide"
outdir = os.path.join(base, "static", "images", "featured")

files = [
    ("main-bus-design.jpg", f"{base}\\tmp_restore\\main-bus-design.jpg"),
    ("red-science-pack.jpg", f"{base}\\tmp_restore\\red-science-pack.jpg"),
    ("quality-modules.jpg", f"{base}\\tmp_restore\\quality-modules.jpg"),
]

for name, tmppath in files:
    # Extract from git using cat-file (binary safe)
    blob_hash = subprocess.run(
        ["git", "-C", base, "rev-parse", f"5680bc3^:static/images/featured/{name}"],
        capture_output=True, text=True, check=True
    ).stdout.strip()

    with open(tmppath, "wb") as f:
        subprocess.run(
            ["git", "-C", base, "cat-file", "-p", blob_hash],
            stdout=f, check=True
        )

    # Read back to verify
    with open(tmppath, "rb") as f:
        header = f.read(2)
    sig = "0x" + "".join(f"{b:02X}" for b in header)
    size = os.path.getsize(tmppath)
    print(f"{name} -> {sig} ({size} bytes)")

    # Copy to static
    dest = os.path.join(base, "static", "images", "featured", name)
    with open(tmppath, "rb") as src, open(dest, "wb") as dst:
        dst.write(src.read())

    # Verify static copy
    with open(dest, "rb") as f:
        header2 = f.read(2)
    sig2 = "0x" + "".join(f"{b:02X}" for b in header2)
    size2 = os.path.getsize(dest)
    print(f"  -> copied to static: {sig2} ({size2} bytes)")
