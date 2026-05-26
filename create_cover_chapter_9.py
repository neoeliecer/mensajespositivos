from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random

def create_mystic_bg(width, height):
    # Deep cosmos background
    bg = Image.new('RGB', (width, height), (5, 10, 30))
    draw = ImageDraw.Draw(bg)
    
    # Adding subtle "stars" or energy static
    for _ in range(300):
        x = random.randint(0, width)
        y = random.randint(0, height)
        c = random.randint(50, 200)
        draw.point((x, y), fill=(c, c, int(c*1.5)))
        
    return bg

def draw_power_sigil(draw, width, height):
    # Draw geometric/sound patterns representing "Words of Power"
    cx, cy = width//2, height//2 - 50
    
    # Outer glow rings
    for r in range(150, 350, 40):
        alpha = int(100 * (1 - (r-150)/200))
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(200, 150, 50, alpha), width=2)

    # Star or geometric center
    points = []
    outer_r = 180
    inner_r = 70
    sides = 8
    
    for i in range(sides*2):
        angle = i * math.pi / sides
        r = outer_r if i % 2 == 0 else inner_r
        x = cx + r * math.sin(angle)
        y = cy - r * math.cos(angle)
        points.append((x,y))
        
    draw.polygon(points, outline=(255, 200, 100, 200), width=4)
    # Inner energy ball
    for r in range(5, 40, 5):
        alpha = int(255 - r*5)
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(255, 255, 200, alpha))
        
def create_chapter_9_cover(output_path):
    width = 1080
    height = 1080
    
    img = create_mystic_bg(width, height).convert("RGBA")
    
    overlay = Image.new("RGBA", (width, height), (0,0,0,0))
    draw_overlay = ImageDraw.Draw(overlay)
    
    # Glowing geometry representing directed intent and power words
    draw_power_sigil(draw_overlay, width, height)
    
    # Blur for ethereal light effect
    overlay_blurred = overlay.filter(ImageFilter.GaussianBlur(8))
    
    # Combine sharp and soft layers
    img = Image.alpha_composite(img, overlay_blurred)
    img = Image.alpha_composite(img, overlay)
    
    draw = ImageDraw.Draw(img)
    
    # Typography
    try:
        font_path_bold = "arialbd.ttf"
        font_path_reg = "arial.ttf"
        font_title = ImageFont.truetype(font_path_bold, 110)
        font_sub = ImageFont.truetype(font_path_reg, 45)
        font_small = ImageFont.truetype(font_path_bold, 35)
    except IOError:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_small = ImageFont.load_default()
        
    # Main Title
    text = "PALABRAS DE PODER"
    bbox = draw.textbbox((0, 0), text, font=font_title)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    
    x = (width - w) / 2
    y = 680
    
    # Text Glow (Golden)
    for offset in range(1, 5):
        draw.text((x-offset, y-offset), text, font=font_title, fill=(200, 150, 0, 70))
        draw.text((x+offset, y+offset), text, font=font_title, fill=(200, 150, 0, 70))
        
    draw.text((x, y), text, font=font_title, fill=(255, 240, 200)) # Warm golden-white
    
    # Subtitle
    sub_text = "ENTONACIÓN Y SONIDO DIRIGIDO"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_sub)
    w_sub = bbox_sub[2] - bbox_sub[0]
    draw.text(((width - w_sub) / 2, y + h + 30), sub_text, font=font_sub, fill=(200, 180, 100))

    # Top Label
    top_text = "CAPÍTULO 9"
    bbox_top = draw.textbbox((0, 0), top_text, font=font_small)
    w_top = bbox_top[2] - bbox_top[0]
    
    draw.line([(width//2 - 100, 100), (width//2 + 100, 100)], fill=(255, 200, 100, 150), width=2)
    draw.text(((width - w_top) / 2, 50), top_text, font=font_small, fill=(255, 220, 150))

    img = img.convert("RGB")
    img.save(output_path)
    print(f"Cover image saved to {output_path}")

if __name__ == "__main__":
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_musica_capitulo_9.png"
    create_chapter_9_cover(output_path)
