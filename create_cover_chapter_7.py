
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random

def create_gradient_radial(width, height, inner_color, outer_color):
    image = Image.new('RGB', (width, height), outer_color)
    inner = Image.new('RGB', (width, height), inner_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    center_x, center_y = width / 2, height / 2
    max_radius = math.sqrt((width/2)**2 + (height/2)**2)
    
    for y in range(height):
        for x in range(width):
            dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            ratio = dist / max_radius
            mask_data.append(int(255 * (1 - ratio)))
            
    mask.putdata(mask_data)
    image.paste(inner, (0, 0), mask)
    return image

def draw_harmonics_visual(draw, center, width, height, color_base):
    # Draw concentric, pulsating waves to represent harmonics
    cx, cy = center
    for i in range(1, 12):
        radius = i * 45
        opacity = int(255 * (1 - i/12) * 0.5)
        color = (color_base[0], color_base[1], color_base[2], opacity)
        
        # Draw dotted or dashed ellipses to represent "subtle" energy
        draw.ellipse([cx-radius, cy-radius, cx+radius, cy+radius], outline=color, width=2)
        
        # Particle/sparkle effects along the waves
        for _ in range(8):
            angle = random.uniform(0, 2 * math.pi)
            px = cx + radius * math.cos(angle)
            py = cy + radius * math.sin(angle)
            dot_color = (255, 255, 255, random.randint(100, 200))
            draw.ellipse([px-2, py-2, px+2, py+2], fill=dot_color)

def create_harmonic_cover_v2(output_path):
    width = 1080
    height = 1080
    
    # 1. Background: Radiant Cyan to Deep Indigo (Clarity and Regeneration)
    bg = create_gradient_radial(width, height, (50, 200, 220), (10, 20, 60))
    img = bg.convert("RGBA")
    
    # 2. Harmonic Waves Overlay
    overlay = Image.new("RGBA", (width, height), (0,0,0,0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    draw_harmonics_visual(draw_overlay, (width//2, height//2 - 100), width, height, (180, 240, 255))
    
    # Apply soft blur for ethereal feel
    overlay = overlay.filter(ImageFilter.GaussianBlur(1))
    img = Image.alpha_composite(img, overlay)
    
    draw = ImageDraw.Draw(img)
    
    # 3. Typography
    try:
        font_path_bold = "arialbd.ttf"
        font_path_reg = "arial.ttf"
        font_title = ImageFont.truetype(font_path_bold, 110)
        font_sub = ImageFont.truetype(font_path_reg, 50)
        font_small = ImageFont.truetype(font_path_bold, 40)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    # Main Title: ARMÓNICOS
    text = "ARMÓNICOS"
    bbox = draw.textbbox((0, 0), text, font=font_title)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    x = (width - w) / 2
    y = 680
    
    # Text Shadow/Glow
    for offset in range(1, 5):
        draw.text((x-offset, y-offset), text, font=font_title, fill=(50, 255, 255, 60))
        draw.text((x+offset, y+offset), text, font=font_title, fill=(50, 255, 255, 60))
        
    draw.text((x, y), text, font=font_title, fill=(255, 255, 255))
    
    # Subtitle: LA MEDICINA DEL FUTURO
    sub_text = "LA MEDICINA DEL FUTURO"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_sub)
    w_sub = bbox_sub[2] - bbox_sub[0]
    draw.text(((width - w_sub) / 2, y + h + 30), sub_text, font=font_sub, fill=(150, 240, 255))

    # Top Label: CAPÍTULO 7
    top_text = "CAPÍTULO 7"
    bbox_top = draw.textbbox((0, 0), top_text, font=font_small)
    w_top = bbox_top[2] - bbox_top[0]
    
    # Top decorative line
    draw.line([(width//2 - 120, 150), (width//2 + 120, 150)], fill=(255, 255, 255, 120), width=2)
    draw.text(((width - w_top) / 2, 90), top_text, font=font_small, fill=(255, 255, 255))

    # Final conversion and save
    img = img.convert("RGB")
    img.save(output_path)
    print(f"Cover image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_musica_capitulo_7.png"
    create_harmonic_cover_v2(output_path)
