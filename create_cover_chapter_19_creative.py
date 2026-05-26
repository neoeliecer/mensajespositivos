
from PIL import Image, ImageDraw, ImageFont
import random
import math

def create_radial_gradient(width, height, center_color, edge_color):
    base = Image.new('RGB', (width, height), edge_color)
    top = Image.new('RGB', (width, height), center_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    
    center_x, center_y = width / 2, height / 2
    max_dist = math.sqrt((width/2)**2 + (height/2)**2)
    
    for y in range(height):
        for x in range(width):
            dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            ratio = dist / max_dist
            # Invert ratio: 1 at center, 0 at edge
            value = int(255 * (1 - ratio))
            mask_data.append(value)
            
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def draw_fire_ice_symbol(draw, center_x, center_y, size):
    # Draw "Ice" crystals (Blue shards)
    shard_color = (135, 206, 250, 150) # Light blue transparent
    
    # Random shards radiating out
    for _ in range(15):
        angle = random.uniform(0, 2 * math.pi)
        length = random.uniform(size * 0.8, size * 1.5)
        width = random.uniform(10, 30)
        
        x2 = center_x + math.cos(angle) * length
        y2 = center_y + math.sin(angle) * length
        
        # Triangle pointing out
        p1 = (center_x + math.cos(angle - 0.1) * 20, center_y + math.sin(angle - 0.1) * 20)
        p2 = (center_x + math.cos(angle + 0.1) * 20, center_y + math.sin(angle + 0.1) * 20)
        p3 = (x2, y2)
        
        draw.polygon([p1, p2, p3], fill=shard_color)

    # Draw "Fire" core (Red/Orange/Yellow circles)
    core_size = size * 0.6
    draw.ellipse([center_x - core_size, center_y - core_size, 
                  center_x + core_size, center_y + core_size], fill=(255, 69, 0)) # Red Orange
                  
    core_size = size * 0.4
    draw.ellipse([center_x - core_size, center_y - core_size, 
                  center_x + core_size, center_y + core_size], fill=(255, 165, 0)) # Orange
                  
    core_size = size * 0.2
    draw.ellipse([center_x - core_size, center_y - core_size, 
                  center_x + core_size, center_y + core_size], fill=(255, 255, 0)) # Yellow

def add_particles(draw, width, height, count, color):
    for _ in range(count):
        x = random.randint(0, width)
        y = random.randint(0, height)
        size = random.randint(1, 4)
        draw.ellipse([x, y, x+size, y+size], fill=color)

def draw_text_with_shadow(draw, text, position, font, text_color, shadow_color, shadow_offset=(5, 5)):
    x, y = position
    # Draw shadow
    draw.text((x + shadow_offset[0], y + shadow_offset[1]), text, font=font, fill=shadow_color)
    # Draw text
    draw.text((x, y), text, font=font, fill=text_color)

def create_creative_cover(output_path):
    width = 1080
    height = 1080
    
    # 1. Background: Radial Gradient (Deep Blue to Black)
    # Center: Deep Sky Blue, Edge: Very Dark Blue/Black
    bg = create_radial_gradient(width, height, (0, 50, 100), (0, 5, 20))
    
    # Enable RGBA for transparency
    img = bg.convert("RGBA")
    overlay = Image.new("RGBA", (width, height), (0,0,0,0))
    draw = ImageDraw.Draw(overlay)
    
    # 2. Symbol: Fire inside Ice
    draw_fire_ice_symbol(draw, width/2, height/2 - 50, 200)
    
    # 3. Particles (Snow/Sparks)
    add_particles(draw, width, height, 200, (200, 230, 255, 200)) # Blueish white
    add_particles(draw, width, height, 50, (255, 200, 100, 200))  # Yellowish sparks
    
    # Composite overlay
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img) # Draw on final image for text (no transparency needed for text usually)
    
    # 4. Impactful Typography
    try:
        font_large = ImageFont.truetype("arialbd.ttf", 90) # Standard bold
        font_med = ImageFont.truetype("arial.ttf", 50)
        # Try to load a thicker font if available, else standard bold
        font_title = ImageFont.truetype("impact.ttf", 140)
    except IOError:
        font_large = ImageFont.load_default()
        font_med = ImageFont.load_default()
        font_title = ImageFont.load_default()

    # Title: ABRAZAR EL DOLOR
    # Split into two lines for impact
    title_line1 = "ABRAZAR"
    title_line2 = "EL DOLOR"
    
    # Line 1
    bbox1 = draw.textbbox((0, 0), title_line1, font=font_title)
    w1 = bbox1[2] - bbox1[0]
    draw_text_with_shadow(draw, title_line1, ((width - w1)/2, height/2 + 150), font_title, (255, 255, 255), (0, 0, 0))
    
    # Line 2 (Red/Orange for emphasis?)
    bbox2 = draw.textbbox((0, 0), title_line2, font=font_title)
    w2 = bbox2[2] - bbox2[0]
    draw_text_with_shadow(draw, title_line2, ((width - w2)/2, height/2 + 300), font_title, (255, 100, 50), (0, 0, 0))
    
    # Subtitle
    sub_text = "CAPÍTULO 19: RECUPERA TU MENTE"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_med)
    w_sub = bbox_sub[2] - bbox_sub[0]
    draw.text(((width - w_sub)/2, 100), sub_text, font=font_med, fill=(200, 200, 200))

    img = img.convert("RGB")
    img.save(output_path)
    print(f"Creative image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_19_creative.png"
    create_creative_cover(output_path)
