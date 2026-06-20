"""Check which content files are being used and what image names they generate."""
from pathlib import Path
import re

content_dir = Path(r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\content')
featured_dir = Path(r'C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\featured')

# Get all content files
content_files = sorted(content_dir.rglob('*.md'))

# Get all image files
image_files = {f.stem for f in featured_dir.glob('*.jpg')}

print(f'Content files: {len(content_files)}')
print(f'Featured images: {len(image_files)}')
print()

for md in content_files:
    rel = md.relative_to(content_dir)
    # Get the section and base name
    parts = rel.parts
    # ContentBaseName logic
    stem = md.stem  # filename without .md
    # The template uses: $page.File.ContentBaseName | replaceRE "-guide$" ""
    img_name = re.sub(r'-guide$', '', stem)
    expected_img = f'{img_name}.jpg'
    
    exists = expected_img in image_files
    status = 'OK' if exists else 'MISSING'
    print(f'  {status}: sections={parts[0]}, file={stem:40s} -> image={expected_img}')