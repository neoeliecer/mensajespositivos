
from PIL import Image, ImageDraw, ImageFont
import math

def create_gradient(width, height, start_color, end_color):
    base = Image.new('RGB', (width, height), start_color)
    top = Image.new('RGB', (width, height), end_color)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        # Linear gradient vertical
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def draw_flow_wave(draw, width, height, color):
    # Draw a sine-wave like stream
    points = []
    
    # Wave parameters
    amplitude = 40
    frequency = 0.015
    phase = 0
    center_y = height / 2 - 100
    
    # We'll draw multiple lines to create a "stream" effect
    for offset_y in [-40, 0, 40]:
        points = []
        for x in range(200, width - 200, 5):
            # Sine wave formula: y = A * sin(B * x + C) + D
            y = amplitude * math.sin(frequency * x + phase) + center_y + offset_y
            points.append((x, y))
        
        if len(points) > 1:
            draw.line(points, fill=color, width=12)

def create_cover_image(text, output_path):
    width = 1080
    height = 1080
    
    # Gradient: Deep Blue to Bright Cyan/Teal
    start_color = (0, 30, 80)     # Deep Blue
    end_color = (0, 200, 200)     # Bright Teal
    
    img = create_gradient(width, height, start_color, end_color)
    draw = ImageDraw.Draw(img)
    
    # Draw Flow Icon (Waves)
    draw_flow_wave(draw, width, height, (255, 255, 255))
    
    # Fonts
    try:
        font_large = ImageFont.truetype("arialbd.ttf", 100)
        font_small = ImageFont.truetype("arial.ttf", 40)
        font_med = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_med = ImageFont.load_default()

    # Title: FLOW
    text_upper = text.upper()
    
    try:
        text_bbox = draw.textbbox((0, 0), text_upper, font=font_large)
        text_w = text_bbox[2] - text_bbox[0]
    except AttributeError:
         text_w, text_h = draw.textsize(text_upper, font=font_large)
        
    draw.text(((width - text_w) / 2, height/2 + 20), text_upper, font=font_large, fill=(255, 255, 255))
    
    # Subtitle 2: El estado de flujo
    sub2_text = "El estado de flujo"
    try:
        sub2_bbox = draw.textbbox((0, 0), sub2_text, font=font_med)
        sub2_w = sub2_bbox[2] - sub2_bbox[0]
    except AttributeError:
        sub2_w, sub2_h = draw.textsize(sub2_text, font=font_med)
        
    draw.text(((width - sub2_w) / 2, height/2 + 130), sub2_text, font=font_med, fill=(240, 240, 240))

    # Chapter Number
    sub_text = "Capítulo 20: Recupera tu mente"
    try:
        sub_bbox = draw.textbbox((0, 0), sub_text, font=font_small)
        sub_w = sub_bbox[2] - sub_bbox[0]
    except AttributeError:
        sub_w, sub_h = draw.textsize(sub_text, font=font_small)
        
    draw.text(((width - sub_w) / 2, height/2 + 220), sub_text, font=font_small, fill=(200, 200, 220))

    img.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_20.png"
    create_cover_image("FLOW", output_path)
