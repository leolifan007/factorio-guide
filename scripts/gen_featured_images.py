"""Generate featured card images for new articles."""
from PIL import Image, ImageDraw, ImageFont
import os, math

SIZE = (1200, 509)
OUT = r"C:\Users\ROG\.qclaw\workspace-54nuktoh8cd83kjj\factorio-guide\static\images\featured"

def draw_gradient(draw, w, h, c1, c2):
    """Vertical gradient from c1 to c2."""
    for y in range(h):
        r = int(c1[0] + (c2[0]-c1[0]) * y / h)
        g = int(c1[1] + (c2[1]-c1[1]) * y / h)
        b = int(c1[2] + (c2[2]-c1[2]) * y / h)
        draw.line([(0,y),(w,y)], fill=(r,g,b))

def draw_grid(draw, w, h, color, step=60, alpha=40):
    """Subtle grid overlay."""
    for x in range(0, w, step):
        draw.line([(x,0),(x,h)], fill=(color[0],color[1],color[2],alpha))
    for y in range(0, h, step):
        draw.line([(0,y),(w,y)], fill=(color[0],color[1],color[2],alpha))

def draw_circle(draw, cx, cy, r, color):
    """Translucent circle."""
    for dr in range(r, 0, -int(r/20)+1):
        a = int(80 * (1 - dr/r))
        draw.ellipse([cx-dr, cy-dr, cx+dr, cy+dr], outline=(*color, a), width=1)

def make_image(name, grad_top, grad_bot, accent, label, sublabel):
    img = Image.new("RGBA", SIZE, (0,0,0,0))
    draw = ImageDraw.Draw(img, "RGBA")

    # gradient background
    draw_gradient(draw, SIZE[0], SIZE[1], grad_top, grad_bot)

    # grid overlay
    draw_grid(draw, SIZE[0], SIZE[1], (255,255,255), 60, 20)

    # decorative elements
    draw_circle(draw, 200, 150, 180, accent)
    draw_circle(draw, 950, 400, 120, accent)
    draw_circle(draw, 600, 50, 80, accent)

    # horizontal division line
    draw.rectangle([40, 170, 400, 174], fill=(255,255,255,40))

    # try to load a font
    font_large = None
    font_small = None
    for fp in [r"C:\Windows\Fonts\segoeuib.ttf", r"C:\Windows\Fonts\segoeui.ttf",
               r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\arial.ttf",
               r"C:\Windows\Fonts\consolab.ttf"]:
        if os.path.exists(fp):
            if font_large is None:
                font_large = ImageFont.truetype(fp, 38)
            if font_small is None:
                font_small = ImageFont.truetype(fp, 18)
        if font_large and font_small:
            break
    if font_large is None:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # label
    draw.text((40, 40), label, fill=(255,255,255,200), font=font_small)

    # title
    draw.text((40, 200), name, fill=(255,255,255,255), font=font_large)

    # subtitle
    draw.text((40, 260), sublabel, fill=(255,255,255,120), font=font_small)

    # bottom bar
    draw.rectangle([0, SIZE[1]-4, SIZE[0], SIZE[1]], fill=accent)

    return img.convert("RGB")

imgs = [
    ("purple-science-guide.jpg",
     (30,10,40), (60,20,70), (160, 50, 200),
     "PURPLE SCIENCE PACK", "Production Science Setup",
     "Electric furnaces · Modules · Ratios"),

    ("turret-defense-guide.jpg",
     (50,15,10), (80,20,10), (220, 80, 30),
     "DEFENSE", "Turret & Wall Defense",
     "Gun · Laser · Flamethrower"),

    ("gleba-spoilage-guide.jpg",
     (40,40,15), (50,30,10), (180, 160, 50),
     "GLEBA - SPACE AGE", "Spoilage Management Guide",
     "Bioflux · Nutrients · Circuit control"),
]

for fname, gt, gb, acc, label, name, sub in imgs:
    img = make_image(name, gt, gb, acc, label, sub)
    path = os.path.join(OUT, fname)
    img.save(path, "JPEG", quality=88)
    print(f"Created {path} ({os.path.getsize(path)//1024}KB)")
