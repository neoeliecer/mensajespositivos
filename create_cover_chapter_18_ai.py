
from PIL import Image, ImageDraw, ImageFont
import shutil
import os

# Source image from AI generation
src = r"C:\Users\neo\.gemini\antigravity\brain\00f5005a-256e-4590-8d1b-13224fd9f396\portada_capitulo_18_ai_1773112923793.png"
dest = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_18_final.png"

img = Image.open(src).convert("RGBA")
width, height = img.size

# Create overlay for text area
overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)

# Semi-transparent dark band at bottom
band_height = 220
draw.rectangle([(0, height - band_height), (width, height)], fill=(10, 10, 30, 180))

# Fonts
try:
    font_title = ImageFont.truetype("arialbd.ttf", 80)
    font_subtitle = ImageFont.truetype("arial.ttf", 44)
    font_cap = ImageFont.truetype("arial.ttf", 36)
except IOError:
    font_title = ImageFont.load_default()
    font_subtitle = ImageFont.load_default()
    font_cap = ImageFont.load_default()

# Merge overlay
img = Image.alpha_composite(img, overlay)
draw = ImageDraw.Draw(img)

# Title text
title = "AYUNO DE DOPAMINA"
tb = draw.textbbox((0, 0), title, font=font_title)
tw = tb[2] - tb[0]
draw.text(((width - tw) / 2, height - 195), title, font=font_title, fill=(255, 220, 80))

# Subtitle
subtitle = "Capítulo 18 · Recupera Tu Mente"
sb = draw.textbbox((0, 0), subtitle, font=font_subtitle)
sw = sb[2] - sb[0]
draw.text(((width - sw) / 2, height - 100), subtitle, font=font_subtitle, fill=(200, 220, 255))

# Author
author = "Marian Rojas Estapé"
ab = draw.textbbox((0, 0), author, font=font_cap)
aw = ab[2] - ab[0]
draw.text(((width - aw) / 2, height - 50), author, font=font_cap, fill=(160, 180, 220))

# Save as RGB
img.convert("RGB").save(dest, quality=95)
print(f"✅ Portada guardada en: {dest}")
