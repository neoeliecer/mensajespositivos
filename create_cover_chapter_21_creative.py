
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

def draw_dynamic_lines(draw, width, height, color):
    # Simulate movement/speed lines
    points = []
    start_y = random.randint(0, height)
    for x in range(0, width, 10):
        # Sine wave with increasing frequency/amplitude to simulate energy
        y = start_y + math.sin(x * 0.02) * 50 + (x/width) * 100
        points.append((x, y))
    
    if len(points) > 1:
        draw.line(points, fill=color, width=random.randint(2, 5))

def draw_neural_connections(draw, width, height, count):
    # Simulate neural connections/synapses
    for _ in range(count):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = x1 + random.randint(-100, 100)
        y2 = y1 + random.randint(-100, 100)
        
        color = (255, 255, 255, random.randint(50, 150))
        draw.line([(x1, y1), (x2, y2)], fill=color, width=1)
        # nodes
        draw.ellipse([x1-2, y1-2, x1+2, y1+2], fill=color)
        draw.ellipse([x2-2, y2-2, x2+2, y2+2], fill=color)

def create_creative_cover(output_path):
    width = 1080
    height = 1080
    
    # 1. Background: Energetic Orange/Red to Deep Purple (Action -> Wisdom)
    bg = create_gradient_radial(width, height, (255, 100, 50), (40, 0, 60))
    img = bg.convert("RGBA")
    
    # 2. Dynamic Movement Lines (The Sport/Action)
    overlay = Image.new("RGBA", (width, height), (0,0,0,0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    for i in range(15):
        color = (255, 255, 255, random.randint(30, 80))
        draw_dynamic_lines(draw_overlay, width, height, color)
        
    # Apply motion blur
    overlay = overlay.filter(ImageFilter.GaussianBlur(1))
    img = Image.alpha_composite(img, overlay)
    
    # 3. Neural Network Overlay (The Brain Benefit)
    overlay_neural = Image.new("RGBA", (width, height), (0,0,0,0))
    draw_neural = ImageDraw.Draw(overlay_neural)
    draw_neural_connections(draw_neural, width, height, 50)
    img = Image.alpha_composite(img, overlay_neural)

    draw = ImageDraw.Draw(img)
    
    # 4. Typography
    try:
        # Try to find a bold font
        font_path = "arialbd.ttf"
        font_title = ImageFont.truetype(font_path, 140)
        font_sub = ImageFont.truetype("arial.ttf", 60)
        font_small = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    # Main Title: EL DEPORTE
    text = "EL DEPORTE"
    bbox = draw.textbbox((0, 0), text, font=font_title)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    # Center text
    x = (width - w) / 2
    y = (height - h) / 2 - 50
    
    # Shadow
    draw.text((x+5, y+5), text, font=font_title, fill=(0, 0, 0, 150))
    # Main Text
    draw.text((x, y), text, font=font_title, fill=(255, 255, 255))
    
    # Subtitle: UN GRAN ALIADO
    sub_text = "UN GRAN ALIADO"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_sub)
    w_sub = bbox_sub[2] - bbox_sub[0]
    draw.text(((width - w_sub) / 2, y + h + 20), sub_text, font=font_sub, fill=(255, 200, 100))

    # Top Label: Capítulo 21
    top_text = "CAPÍTULO 21"
    
    # Draw a small box for the label
    bbox_top = draw.textbbox((0, 0), top_text, font=font_small)
    w_top = bbox_top[2] - bbox_top[0]
    h_top = bbox_top[3] - bbox_top[1]
    
    # label_bg_rect = [(width - w_top)/2 - 20, 90, (width + w_top)/2 + 20, 100 + h_top + 10]
    # draw.rectangle(label_bg_rect, fill=(0, 0, 0, 100))
    
    draw.text(((width - w_top) / 2, 100), top_text, font=font_small, fill=(255, 255, 255))

    img = img.convert("RGB")
    img.save(output_path)
    print(f"Creative image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_21_creative.png"
    create_creative_cover(output_path)
