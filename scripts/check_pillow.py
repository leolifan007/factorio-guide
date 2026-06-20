import sys, os
try:
    from PIL import Image, ImageDraw, ImageFont
    print("Pillow OK")
    sys.exit(0)
except ImportError:
    print("Pillow NOT available")
    sys.exit(1)
