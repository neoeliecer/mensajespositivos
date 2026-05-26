from PIL import Image, ImageDraw, ImageFont
import os
import glob

def add_text_to_image(input_path, output_path, line1, line2, chapter_text):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    img = Image.open(input_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    font_paths = [
        r"C:\Windows\Fonts\georgiab.ttf",
        r"C:\Windows\Fonts\timesbd.ttf",
        r"C:\Windows\Fonts\arialbd.ttf"
    ]
    
    title_font_path = next((p for p in font_paths if os.path.exists(p)), None)
    
    if title_font_path:
        title_font = ImageFont.truetype(title_font_path, 80)
        chapter_font = ImageFont.truetype(title_font_path, 40)
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

    max_allowed_w = width * 0.9
    while (l1_w > max_allowed_w or l2_w > max_allowed_w) and title_font.size > 20:
        new_size = title_font.size - 5
        title_font = ImageFont.truetype(title_font_path, new_size)
        l1_w, l1_h = get_text_size(line1, title_font)
        l2_w, l2_h = get_text_size(line2, title_font)

    spacing = 30
    total_text_h = chap_h + l1_h + l2_h + (spacing * 2)
    center_y = int(height * 0.75) - (total_text_h // 2)

    chap_y = center_y
    l1_y = chap_y + chap_h + spacing
    l2_y = l1_y + l1_h + spacing

    chap_x = (width - chap_w) // 2
    l1_x = (width - l1_w) // 2
    l2_x = (width - l2_w) // 2

    gold_color = (255, 215, 0)
    white_color = (255, 255, 255)
    shadow_color = (0, 0, 0, 200)
    shadow_offset = 5

    def draw_with_shadow(draw, x, y, text, font, fill):
        draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=shadow_color)
        draw.text((x, y), text, font=font, fill=fill)

    draw_with_shadow(draw, chap_x, chap_y, chapter_text, chapter_font, white_color)
    draw_with_shadow(draw, l1_x, l1_y, line1, title_font, gold_color)
    draw_with_shadow(draw, l2_x, l2_y, line2, title_font, gold_color)

    img.save(output_path)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    # Path to the raw image generated in previous step
    input_img = r"C:\Users\neo\.gemini\antigravity\brain\50bb3afb-e729-43ba-ae88-b4b957359d63\portada_manos_cap6_raw_1774724776411.png"
    output_img = r"C:\Users\neo\Documents\agente\mensajes positivos\portada_manos_capitulo_6_con_titulo.png"
    add_text_to_image(input_img, output_img, "El Campo", "Energético Universal", "Manos que curan - Capítulo 6")
