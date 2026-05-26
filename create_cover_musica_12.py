
from PIL import Image, ImageDraw, ImageFont
import os

src = r"C:\Users\neo\.gemini\antigravity\brain\00f5005a-256e-4590-8d1b-13224fd9f396\portada_musica_capitulo_12_1773113272998.png"
dest = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_musica_capitulo_12.png"

img = Image.open(src).convert("RGBA")
width, height = img.size

overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Taller dark band to fit all text
band_height = 270
draw.rectangle([(0, height - band_height), (width, height)], fill=(5, 0, 20, 195))

try:
    font_title = ImageFont.truetype("arialbd.ttf", 50)
    font_subtitle = ImageFont.truetype("arial.ttf", 34)
    font_cap = ImageFont.truetype("arial.ttf", 28)
except IOError:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_cap = ImageFont.load_default()

img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Two-line title to avoid overflow
line1 = "MANTRAS Y CANTICOS"
line2 = "SAGRADOS"
tb1 = draw.textbbox((0, 0), line1, font=font_title)
tw1 = tb1[2] - tb1[0]
draw.text(((width - tw1) / 2, height - 245), line1, font=font_title, fill=(255, 215, 80))

tb2 = draw.textbbox((0, 0), line2, font=font_title)
tw2 = tb2[2] - tb2[0]
draw.text(((width - tw2) / 2, height - 190), line2, font=font_title, fill=(255, 215, 80))

# Subtitle
subtitle = "Cap. 12 - La Curacion por la Musica"
sb = draw.textbbox((0, 0), subtitle, font=font_subtitle)
sw = sb[2] - sb[0]
draw.text(((width - sw) / 2, height - 128), subtitle, font=font_subtitle, fill=(200, 190, 255))

# Author
author = "Ted Andrews"
ab = draw.textbbox((0, 0), author, font=font_cap)
aw = ab[2] - ab[0]
draw.text(((width - aw) / 2, height - 55), author, font=font_cap, fill=(170, 160, 220))

img.convert("RGB").save(dest, quality=95)
print("Portada guardada en:", dest)
