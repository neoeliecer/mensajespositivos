
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

def draw_pause_icon(draw, center_x, center_y, size, color):
    # Draw circle
    left = center_x - size
    top = center_y - size
    right = center_x + size
    bottom = center_y + size
    draw.ellipse([left, top, right, bottom], outline=color, width=10)
    
    # Draw bars
    bar_width = size * 0.2
    bar_height = size * 0.8
    bar_spacing = size * 0.2
    
    # Left bar
    draw.rectangle(
        [center_x - bar_spacing - bar_width, center_y - bar_height/2, 
         center_x - bar_spacing, center_y + bar_height/2], 
        fill=color
    )
    
    # Right bar
    draw.rectangle(
        [center_x + bar_spacing, center_y - bar_height/2, 
         center_x + bar_spacing + bar_width, center_y + bar_height/2], 
        fill=color
    )

def create_cover_image(text, output_path):
    width = 1080
    height = 1080
    
    # Calming Blue Gradient (Detox/Peace)
    start_color = (135, 206, 250) # Light Sky Blue
    end_color = (25, 25, 112)     # Midnight Blue
    
    img = create_gradient(width, height, start_color, end_color)
    draw = ImageDraw.Draw(img)
    
    # Draw Pause Icon (Symbolizing the Fast/Stop)
    draw_pause_icon(draw, width/2, height/2 - 100, 150, (255, 255, 255))
    
    # Fonts
    try:
        font_large = ImageFont.truetype("arialbd.ttf", 90)
        font_small = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Title: AYUNO DE DOPAMINA
    text_bbox = draw.textbbox((0, 0), text.upper(), font=font_large)
    text_w = text_bbox[2] - text_bbox[0]
    draw.text(((width - text_w) / 2, height/2 + 100), text.upper(), font=font_large, fill=(255, 255, 255))
    
    # Subtitle: Chapter 18
    sub_text = "Capítulo 18: Recupera tu mente"
    sub_bbox = draw.textbbox((0, 0), sub_text, font=font_small)
    sub_w = sub_bbox[2] - sub_bbox[0]
    draw.text(((width - sub_w) / 2, height/2 + 220), sub_text, font=font_small, fill=(200, 200, 200))

    img.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_18.png"
    create_cover_image("Ayuno de dopamina", output_path)
