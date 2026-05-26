
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

def draw_flowing_waves(draw, width, height, color, offset_y, amplitude, frequency, phase_shift):
    points = []
    for x in range(0, width, 5):
        # Multiple sine waves combined for organic flow
        y = (height / 2) + offset_y + \
            amplitude * math.sin(frequency * x + phase_shift) + \
            (amplitude / 2) * math.sin(frequency * 2 * x + phase_shift)
        points.append((x, y))
    
    if len(points) > 1:
        draw.line(points, fill=color, width=3)

def add_glow_particles(draw, width, height, count):
    for _ in range(count):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(2, 6)
        opacity = random.randint(50, 200)
        color = (255, 255, 255, opacity)
        
        # Simple glowing dot (circle)
        draw.ellipse([x, y, x+size, y+size], fill=color)

def create_creative_cover(output_path):
    width = 1080
    height = 1080
    
    # 1. Deep Oceanic/Space Background (Focus/Depth)
    # Center: Cyan/Bright Blue, Edge: Deep Indigo/Black
    bg = create_gradient_radial(width, height, (0, 150, 200), (10, 10, 40))
    img = bg.convert("RGBA")
    
    # 2. Flowing Lines (The "Stream" of consciousness)
    overlay = Image.new("RGBA", (width, height), (0,0,0,0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    # Draw many intertwining waves
    colors = [
        (0, 255, 255, 100),   # Cyan
        (255, 0, 255, 80),    # Magenta
        (100, 255, 100, 80),  # Green
        (255, 255, 255, 120)  # White
    ]
    
    for i in range(20):
        color = random.choice(colors)
        offset = random.randint(-400, 400)
        amplitude = random.randint(20, 100)
        freq = random.uniform(0.005, 0.02)
        phase = random.uniform(0, math.pi * 2)
        draw_flowing_waves(draw_overlay, width, height, color, offset, amplitude, freq, phase)
        
    # Apply blur to waves for "glowing" effect
    overlay = overlay.filter(ImageFilter.GaussianBlur(2))
    img = Image.alpha_composite(img, overlay)
    
    # 3. Add sharper waves on top
    overlay_sharp = Image.new("RGBA", (width, height), (0,0,0,0))
    draw_sharp = ImageDraw.Draw(overlay_sharp)
    for i in range(5):
         draw_flowing_waves(draw_sharp, width, height, (255, 255, 255, 200), random.randint(-100, 100), 50, 0.01, 0)
    img = Image.alpha_composite(img, overlay_sharp)

    # 4. Particles (Focus/Ideas)
    draw = ImageDraw.Draw(img)
    add_glow_particles(draw, width, height, 150)
    
    # 5. Typography
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 200)
        font_sub = ImageFont.truetype("arial.ttf", 60)
        font_small = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    # Main Title: FLOW
    text = "FLOW"
    bbox = draw.textbbox((0, 0), text, font=font_title)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    # Center text
    x = (width - w) / 2
    y = (height - h) / 2
    
    # Text Glo/Shadow
    shadow_offset = 8
    draw.text((x+shadow_offset, y+shadow_offset), text, font=font_title, fill=(0, 0, 50))
    
    # Main Text (White/Bright)
    draw.text((x, y), text, font=font_title, fill=(255, 255, 255))
    
    # Subtitle: El estado de flujo
    sub_text = "EL ESTADO DE FLUJO"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_sub)
    w_sub = bbox_sub[2] - bbox_sub[0]
    draw.text(((width - w_sub) / 2, y + h + 40), sub_text, font=font_sub, fill=(200, 240, 255))

    # Top Label: Capítulo 20
    top_text = "CAPÍTULO 20"
    bbox_top = draw.textbbox((0, 0), top_text, font=font_small)
    w_top = bbox_top[2] - bbox_top[0]
    draw.text(((width - w_top) / 2, 100), top_text, font=font_small, fill=(255, 255, 255))

    img = img.convert("RGB")
    img.save(output_path)
    print(f"Creative image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_20_creative.png"
    create_creative_cover(output_path)
