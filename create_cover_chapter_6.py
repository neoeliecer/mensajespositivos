
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

def draw_harmonic_waves(draw, width, height, color, frequency, amplitude, offset_y):
    # Simulate harmonic sound waves
    points = []
    for x in range(0, width, 5):
        y = offset_y + math.sin(x * frequency) * amplitude 
        points.append((x, y))
    
    if len(points) > 1:
        draw.line(points, fill=color, width=3)

def draw_sacred_geometry(draw, center, radius, color):
    # Draw simple circles to represent harmony/vibration
    x, y = center
    for r in range(radius // 4, radius + 1, radius // 4):
        draw.ellipse([x-r, y-r, x+r, y+r], outline=color, width=1)
    
    # Lines connecting points (flower of life hint)
    num_points = 12
    points = []
    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        px = x + radius * math.cos(angle)
        py = y + radius * math.sin(angle)
        points.append((px, py))
    
    for i in range(num_points):
        for j in range(i + 1, num_points):
            # Only connect close points to keep it clean
            if (j - i) in [1, 2, num_points-1, num_points-2]:
                draw.line([points[i], points[j]], fill=color, width=1)

def create_harmonic_cover(output_path):
    width = 1080
    height = 1080
    
    # 1. Background: Violet to Deep Blue (Spirituality and Depth)
    bg = create_gradient_radial(width, height, (100, 50, 150), (10, 5, 40))
    img = bg.convert("RGBA")
    
    # 2. Harmonies / Waves
    overlay = Image.new("RGBA", (width, height), (0,0,0,0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    # Multiple harmonic waves
    colors = [
        (255, 255, 255, 100),
        (200, 150, 255, 80),
        (150, 200, 255, 60)
    ]
    
    for i in range(6):
        color = random.choice(colors)
        freq = 0.005 + (i * 0.002)
        amp = 30 + (i * 10)
        off_y = height // 2 + (i - 2.5) * 40
        draw_harmonic_waves(draw_overlay, width, height, color, freq, amp, off_y)
        
    img = Image.alpha_composite(img, overlay)
    
    # 3. Sacred Geometry Element
    overlay_geo = Image.new("RGBA", (width, height), (0,0,0,0))
    draw_geo = ImageDraw.Draw(overlay_geo)
    draw_sacred_geometry(draw_geo, (width//2, height//2 - 150), 300, (255, 255, 255, 40))
    img = Image.alpha_composite(img, overlay_geo)

    draw = ImageDraw.Draw(img)
    
    # 4. Typography
    try:
        # Use standard windows fonts
        font_path_bold = "arialbd.ttf"
        font_path_reg = "arial.ttf"
        font_title = ImageFont.truetype(font_path_bold, 120)
        font_sub = ImageFont.truetype(font_path_reg, 50)
        font_small = ImageFont.truetype(font_path_bold, 40)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    # Main Title: LA ARMONÍA
    text = "LA ARMONÍA"
    bbox = draw.textbbox((0, 0), text, font=font_title)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    # Position title in lower middle
    x = (width - w) / 2
    y = 650
    
    # Glow effect for text
    for offset in range(1, 4):
        draw.text((x-offset, y-offset), text, font=font_title, fill=(180, 100, 255, 100))
        draw.text((x+offset, y+offset), text, font=font_title, fill=(180, 100, 255, 100))
        
    draw.text((x, y), text, font=font_title, fill=(255, 255, 255))
    
    # Subtitle: EL ECO DEL ESPÍRITU
    sub_text = "EL ECO DEL ESPÍRITU"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_sub)
    w_sub = bbox_sub[2] - bbox_sub[0]
    draw.text(((width - w_sub) / 2, y + h + 40), sub_text, font=font_sub, fill=(200, 180, 255))

    # Top Label: CAPÍTULO 6
    top_text = "CAPÍTULO 6"
    bbox_top = draw.textbbox((0, 0), top_text, font=font_small)
    w_top = bbox_top[2] - bbox_top[0]
    
    # Decorative line for top label
    line_y = 100 + 50
    draw.line([(width//2 - 100, line_y), (width//2 + 100, line_y)], fill=(255, 255, 255, 150), width=2)
    
    draw.text(((width - w_top) / 2, 100), top_text, font=font_small, fill=(255, 255, 255))

    # Final touch: subtle blur on the background elements
    img = img.filter(ImageFilter.GaussianBlur(0.5))

    img = img.convert("RGB")
    img.save(output_path)
    print(f"Cover image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_musica_capitulo_6.png"
    create_harmonic_cover(output_path)
