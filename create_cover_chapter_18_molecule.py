
from PIL import Image, ImageDraw, ImageFont
import math

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

def draw_hexagon(draw, center_x, center_y, size, color, width=5):
    points = []
    for i in range(6):
        angle_deg = 60 * i - 30 
        angle_rad = math.radians(angle_deg)
        x = center_x + size * math.cos(angle_rad)
        y = center_y + size * math.sin(angle_rad)
        points.append((x, y))
    
    draw.polygon(points, outline=color, width=width)
    return points

def create_cover_image(text, output_path):
    width = 1080
    height = 1080
    
    # Deep Blue/Purple Gradient for "neuroscience" feel
    start_color = (10, 10, 50)    # Very Dark Blue
    end_color = (72, 61, 139)     # Dark Slate Blue
    
    img = create_gradient(width, height, start_color, end_color)
    draw = ImageDraw.Draw(img)
    
    # Draw Molecule Structure (Stylized Dopamine)
    center_x = width // 2
    center_y = height // 2 - 100
    size = 120
    molecule_color = (0, 255, 255) # Cyan/Neon Blue
    
    # Main ring (Benzene)
    hex_points = draw_hexagon(draw, center_x - 60, center_y, size, molecule_color, width=8)
    
    # Side chain (simplified)
    start_point = hex_points[1] # Top right check
    end_point = (start_point[0] + 100, start_point[1] - 80)
    draw.line([start_point, end_point], fill=molecule_color, width=8)
    
    # Atom nodes (circles)
    node_radius = 15
    for p in hex_points:
        draw.ellipse([p[0]-node_radius, p[1]-node_radius, p[0]+node_radius, p[1]+node_radius], fill=molecule_color)
    
    draw.ellipse([end_point[0]-node_radius, end_point[1]-node_radius, end_point[0]+node_radius, end_point[1]+node_radius], fill=molecule_color)

    # Fonts
    try:
        font_large = ImageFont.truetype("arialbd.ttf", 90)
        font_small = ImageFont.truetype("arial.ttf", 50)
    except IOError:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Title
    text_bbox = draw.textbbox((0, 0), text.upper(), font=font_large)
    text_w = text_bbox[2] - text_bbox[0]
    draw.text(((width - text_w) / 2, height/2 + 150), text.upper(), font=font_large, fill=(255, 255, 255))
    
    # Subtitle
    sub_text = "Capítulo 18: Recupera tu mente"
    sub_bbox = draw.textbbox((0, 0), sub_text, font=font_small)
    sub_w = sub_bbox[2] - sub_bbox[0]
    draw.text(((width - sub_w) / 2, height/2 + 260), sub_text, font=font_small, fill=(200, 200, 200))

    img.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_18.png"
    create_cover_image("Ayuno de dopamina", output_path)
