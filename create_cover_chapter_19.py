
from PIL import Image, ImageDraw, ImageFont
import os

def create_gradient(width, height, start_color, end_color):
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def draw_mountain_icon(draw, center_x, center_y, size, color):
    # Draw a triangle (Mountain)
    # Points: (top_center, bottom_left, bottom_right)
    half_size = size
    
    p1 = (center_x, center_y - half_size) # Top
    p2 = (center_x - half_size, center_y + half_size/2) # Bottom Left
    p3 = (center_x + half_size, center_y + half_size/2) # Bottom Right
    
    draw.polygon([p1, p2, p3], outline=color, width=15)
    
    # Draw a "snow cap" line
    cap_y = center_y - half_size * 0.3
    cap_left_x = center_x - half_size * 0.35
    cap_right_x = center_x + half_size * 0.35
    
    draw.line([cap_left_x, cap_y, center_x, center_y - half_size * 0.1, cap_right_x, cap_y], fill=color, width=8)

def create_cover_image(text, output_path):
    width = 1080
    height = 1080
    
    # Gradient: Dark Gray (Challenge) to Light Blue (Clarity/Ice)
    start_color = (50, 50, 60)   # Dark Gray
    end_color = (135, 206, 235)  # Sky Blue
    
    img = create_gradient(width, height, start_color, end_color)
    draw = ImageDraw.Draw(img)
    
    # Draw Mountain Icon
    draw_mountain_icon(draw, width/2, height/2 - 120, 180, (255, 255, 255))
    
    # Fonts
    try:
        # Try to find a bold font, fallback to default
        font_large = ImageFont.truetype("arialbd.ttf", 90)
        font_small = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Title: ABRAZAR EL DOLOR
    text_upper = text.upper()
    
    # Simple centering logic
    try:
        text_bbox = draw.textbbox((0, 0), text_upper, font=font_large)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]
    except AttributeError:
        # Fallback for older PIL versions
        text_w, text_h = draw.textsize(text_upper, font=font_large)
        
    draw.text(((width - text_w) / 2, height/2 + 80), text_upper, font=font_large, fill=(255, 255, 255))
    
    # Subtitle: Capítulo 19
    sub_text = "Capítulo 19: Recupera tu mente"
    try:
        sub_bbox = draw.textbbox((0, 0), sub_text, font=font_small)
        sub_w = sub_bbox[2] - sub_bbox[0]
    except AttributeError:
        sub_w, sub_h = draw.textsize(sub_text, font=font_small)
        
    draw.text(((width - sub_w) / 2, height/2 + 200), sub_text, font=font_small, fill=(230, 230, 230))

    img.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_19.png"
    create_cover_image("Abrazar el dolor", output_path)
