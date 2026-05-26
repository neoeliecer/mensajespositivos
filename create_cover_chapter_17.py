
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

def create_cover_image(text, output_path):
    width = 1080
    height = 1080
    
    # Create sunset gradient background (Orange to Blue/Purple)
    start_color = (255, 165, 0) # Orange
    end_color = (75, 0, 130)   # Indigo
    
    img = create_gradient(width, height, start_color, end_color)
    draw = ImageDraw.Draw(img)
    
    # Try to load a font, fallback to default if necessary
    try:
        font_path = "arialbd.ttf" # Bold arial
        font_size = 80
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        font = ImageFont.load_default()
        font_size = 40

    # Calculate text size and position
    # textbbox returns (left, top, right, bottom)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    # Draw shadow
    shadow_offset = 3
    draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=(50, 50, 50))
    
    # Draw main text
    draw.text((x, y), text, font=font, fill=(255, 255, 255))
    
    # Add Chapter number
    chapter_text = "CAPÍTULO 17"
    try:
        small_font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        small_font = ImageFont.load_default()
    
    bbox_chap = draw.textbbox((0, 0), chapter_text, font=small_font)
    chap_width = bbox_chap[2] - bbox_chap[0]
    
    draw.text(((width - chap_width) / 2, y - 80), chapter_text, font=small_font, fill=(240, 240, 240))
    
    # Add Author Name
    author_text = "Marian Rojas Estapé"
    bbox_auth = draw.textbbox((0, 0), author_text, font=small_font)
    auth_width = bbox_auth[2] - bbox_auth[0]
    
    draw.text(((width - auth_width) / 2, y + 100), author_text, font=small_font, fill=(240, 240, 240))

    img.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_17.png"
    create_cover_image("Reconquista tu vida", output_path)
