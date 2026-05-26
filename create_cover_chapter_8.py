
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random

def create_gradient(width, height, color1, color2):
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    
    # Linear gradient top to bottom
    for y in range(height):
        for x in range(width):
            mask_data.append(int(255 * (y / height)))
            
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def draw_vowel_waves(draw, width, height, color):
    # Draw intersecting, resonant sound waves to represent the vowels
    cx = width // 2
    cy = height // 2
    
    # Vowel bubbles / resonant centers
    centers = [(cx, cy-150), (cx-120, cy+50), (cx+120, cy+50), (cx-70, cy-50), (cx+70, cy-50)]
    
    for x, y in centers:
        # Draw sound ripples around each center
        for i in range(1, 5):
            radius = i * 60
            opacity = int(180 * (1 - i/5))
            circle_color = (color[0], color[1], color[2], opacity)
            draw.ellipse([x-radius, y-radius, x+radius, y+radius], outline=circle_color, width=3)
        
        # Inner glow core
        draw.ellipse([x-20, y-20, x+20, y+20], fill=(255, 255, 255, 100))

def create_mantra_cover(output_path):
    width = 1080
    height = 1080
    
    # Background: Warm Violet to Magenta (spiritual power and vocal energy)
    bg = create_gradient(width, height, (90, 20, 100), (200, 50, 100))
    img = bg.convert("RGBA")
    
    overlay = Image.new("RGBA", (width, height), (0,0,0,0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    # Draw resonant fields (vowels overlapping)
    draw_vowel_waves(draw_overlay, width, height, (255, 200, 230))
    
    # Soften the intersecting waves
    overlay = overlay.filter(ImageFilter.GaussianBlur(3))
    img = Image.alpha_composite(img, overlay)
    
    draw = ImageDraw.Draw(img)
    
    # Typography
    try:
        font_path_bold = "arialbd.ttf"
        font_path_reg = "arial.ttf"
        font_title = ImageFont.truetype(font_path_bold, 85)
        font_sub = ImageFont.truetype(font_path_reg, 50)
        font_small = ImageFont.truetype(font_path_bold, 35)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    # Main Title
    text_line1 = "LAS VOCALES"
    text_line2 = "COMO MANTRAS"
    
    bbox1 = draw.textbbox((0, 0), text_line1, font=font_title)
    w1 = bbox1[2] - bbox1[0]
    bbox2 = draw.textbbox((0, 0), text_line2, font=font_title)
    w2 = bbox2[2] - bbox2[0]
    h1 = bbox1[3] - bbox1[1]
    
    y = 650
    
    # Draw text with subtle shadow
    for offset in range(1, 4):
        draw.text(((width - w1) / 2 - offset, y - offset), text_line1, font=font_title, fill=(50, 0, 50, 100))
        draw.text(((width - w2) / 2 - offset, y + h1 + 10 - offset), text_line2, font=font_title, fill=(50, 0, 50, 100))
        
    draw.text(((width - w1) / 2, y), text_line1, font=font_title, fill=(255, 240, 255))
    draw.text(((width - w2) / 2, y + h1 + 10), text_line2, font=font_title, fill=(255, 220, 240))
    
    # Subtitle
    sub_text = "TU FARMACIA INTERNA"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_sub)
    w_sub = bbox_sub[2] - bbox_sub[0]
    draw.text(((width - w_sub) / 2, y + h1 * 2 + 50), sub_text, font=font_sub, fill=(255, 200, 220))

    # Top Label
    top_text = "CAPÍTULO 8"
    bbox_top = draw.textbbox((0, 0), top_text, font=font_small)
    w_top = bbox_top[2] - bbox_top[0]
    
    draw.line([(width//2 - 100, 150), (width//2 + 100, 150)], fill=(255, 200, 220, 150), width=2)
    draw.text(((width - w_top) / 2, 100), top_text, font=font_small, fill=(255, 255, 255))

    img = img.convert("RGB")
    img.save(output_path)
    print(f"Cover image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_musica_capitulo_8.png"
    create_mantra_cover(output_path)
