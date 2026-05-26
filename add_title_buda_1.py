from PIL import Image, ImageDraw, ImageFont
import os

def add_text_to_image(input_path, output_path, line1, line2, chapter_text):
    # Load image
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    img = Image.open(input_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Font selection
    font_paths = [
        r"C:\Windows\Fonts\georgiab.ttf", # Serif, elegant
        r"C:\Windows\Fonts\timesbd.ttf",
        r"C:\Windows\Fonts\arialbd.ttf"
    ]
    
    title_font_path = None
    for path in font_paths:
        if os.path.exists(path):
            title_font_path = path
            break
    
    if title_font_path:
        title_font = ImageFont.truetype(title_font_path, 70)
        chapter_font = ImageFont.truetype(title_font_path, 35)
    else:
        title_font = ImageFont.load_default()
        chapter_font = ImageFont.load_default()

    line1 = line1.upper()
    line2 = line2.upper()
    chapter_text = chapter_text.upper()

    def get_text_size(text, font):
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    chap_w, chap_h = get_text_size(chapter_text, chapter_font)
    l1_w, l1_h = get_text_size(line1, title_font)
    l2_w, l2_h = get_text_size(line2, title_font)

    # Scale font if too wide
    max_allowed_w = width * 0.9
    while (l1_w > max_allowed_w or l2_w > max_allowed_w) and title_font.size > 20:
        new_size = title_font.size - 5
        title_font = ImageFont.truetype(title_font_path, new_size)
        l1_w, l1_h = get_text_size(line1, title_font)
        l2_w, l2_h = get_text_size(line2, title_font)

    # Spacing and layout
    spacing = 25
    total_text_h = chap_h + l1_h + l2_h + (spacing * 2)
    center_y = int(height * 0.70) - (total_text_h // 2)

    chap_y = center_y
    l1_y = chap_y + chap_h + spacing
    l2_y = l1_y + l1_h + spacing

    chap_x = (width - chap_w) // 2
    l1_x = (width - l1_w) // 2
    l2_x = (width - l2_w) // 2

    # Colors
    gold_color = (255, 215, 0) # Gold
    white_color = (255, 255, 255)
    shadow_color = (0, 0, 0, 200)
    shadow_offset = 4

    def draw_with_shadow(draw, x, y, text, font, fill):
        draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=shadow_color)
        draw.text((x, y), text, font=font, fill=fill)

    draw_with_shadow(draw, chap_x, chap_y, chapter_text, chapter_font, white_color)
    draw_with_shadow(draw, l1_x, l1_y, line1, title_font, gold_color)
    draw_with_shadow(draw, l2_x, l2_y, line2, title_font, gold_color)

    img.save(output_path)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    import glob
    # Use glob to find the most recent generated image if multiple exist
    search_pattern = r"C:\Users\neo\.gemini\antigravity\brain\c7469211-3b59-42bf-b039-81ee95bec3fd\portada_buda_capitulo_1_*.png"
    files = glob.glob(search_pattern)
    if not files:
        print("No input image found.")
    else:
        input_img = max(files, key=os.path.getctime)
        output_img = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_buda_capitulo_1_con_titulo.png"
        add_text_to_image(input_img, output_img, "El Cerebro", "Autotransformador", "Buda, el cerebro - Capítulo 1")
