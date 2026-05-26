
from PIL import Image, ImageDraw, ImageFont
import os

src = r"C:\Users\neo\.gemini\antigravity\brain\00f5005a-256e-4590-8d1b-13224fd9f396\portada_musica_capitulo_13_1773144008787.png"
dest = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_musica_capitulo_13.png"

img = Image.open(src).convert("RGBA")
width, height = img.size

overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

band_height = 240
draw.rectangle([(0, height - band_height), (width, height)], fill=(5, 0, 15, 195))

try:
    font_title1 = ImageFont.truetype("arialbd.ttf", 60)
    font_title2 = ImageFont.truetype("arialbd.ttf", 50)
    font_subtitle = ImageFont.truetype("arial.ttf", 34)
    font_author = ImageFont.truetype("arial.ttf", 28)
except IOError:
    font_title1 = ImageFont.load_default()
    font_title2 = font_title1
    font_subtitle = font_title1
    font_author = font_title1

img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Line 1
line1 = "EL SONIDO Y"
tb1 = draw.textbbox((0, 0), line1, font=font_title1)
tw1 = tb1[2] - tb1[0]
draw.text(((width - tw1) / 2, height - 235), line1, font=font_title1, fill=(255, 215, 80))

# Line 2
line2 = "LOS CHAKRAS"
tb2 = draw.textbbox((0, 0), line2, font=font_title2)
tw2 = tb2[2] - tb2[0]
draw.text(((width - tw2) / 2, height - 175), line2, font=font_title2, fill=(180, 120, 255))

# Subtitle
subtitle = "Cap. 13 - La Curacion por la Musica"
sb = draw.textbbox((0, 0), subtitle, font=font_subtitle)
sw = sb[2] - sb[0]
draw.text(((width - sw) / 2, height - 115), subtitle, font=font_subtitle, fill=(200, 200, 255))

# Author
author = "Ted Andrews"
ab = draw.textbbox((0, 0), author, font=font_author)
aw = ab[2] - ab[0]
draw.text(((width - aw) / 2, height - 55), author, font=font_author, fill=(170, 160, 220))

img.convert("RGB").save(dest, quality=95)
print("Portada guardada en:", dest)
