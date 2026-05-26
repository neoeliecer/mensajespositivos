from PIL import Image, ImageDraw, ImageFont
import os

def add_text_to_image(input_path, output_path, title_text, chapter_text):
    # Load image
    img = Image.open(input_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Font selection - trying common Windows fonts for a "magic" feel
    font_paths = [
        r"C:\Windows\Fonts\georgiab.ttf", # Serif, more elegant
        r"C:\Windows\Fonts\timesbd.ttf",
        r"C:\Windows\Fonts\arialbd.ttf"
    ]
    
    title_font = None
    chapter_font = None
    
    for path in font_paths:
        if os.path.exists(path):
            try:
                # Reduced sizes to ensure it fits (90 -> 70, 45 -> 35)
                title_font = ImageFont.truetype(path, 70)
                chapter_font = ImageFont.truetype(path, 35)
                break
            except:
                continue
    
    if not title_font:
        title_font = ImageFont.load_default()
        chapter_font = ImageFont.load_default()

    # Split title into two lines for better visual balance
    line1 = "EL ARTE DE LA"
    line2 = "NARRACIÓN MÁGICA"
    chapter_text = chapter_text.upper()

    def get_text_size(text, font):
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    chap_w, chap_h = get_text_size(chapter_text, chapter_font)
    l1_w, l1_h = get_text_size(line1, title_font)
    l2_w, l2_h = get_text_size(line2, title_font)

    # Ensure text doesn't exceed image width with a safety margin
    max_allowed_w = width * 0.9 # 90% of image width
    while (l1_w > max_allowed_w or l2_w > max_allowed_w) and title_font.size > 20:
        new_size = title_font.size - 5
        title_font = ImageFont.truetype(title_font.path, new_size)
        l1_w, l1_h = get_text_size(line1, title_font)
        l2_w, l2_h = get_text_size(line2, title_font)

    # Total height of text block
    spacing = 25
    total_text_h = chap_h + l1_h + l2_h + (spacing * 2)

    # Position: Bottom-center area, but higher than before to avoid edge cut-offs
    center_y = int(height * 0.70) - (total_text_h // 2)

    # Coordinates
    chap_y = center_y
    l1_y = chap_y + chap_h + spacing
    l2_y = l1_y + l1_h + spacing

    # X Coordinates (centered)
    chap_x = (width - chap_w) // 2
    l1_x = (width - l1_w) // 2
    l2_x = (width - l2_w) // 2

    # Aesthetic: Gold-like color for title, white for chapter
    gold_color = (255, 215, 0) # Gold
    white_color = (255, 255, 255)
    shadow_color = (0, 0, 0, 200)
    shadow_offset = 4

    # Draw function with shadow
    def draw_with_shadow(draw, x, y, text, font, fill):
        # Draw shadow
        draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=shadow_color)
        # Draw text
        draw.text((x, y), text, font=font, fill=fill)

    # Draw everything
    draw_with_shadow(draw, chap_x, chap_y, chapter_text, chapter_font, white_color)
    draw_with_shadow(draw, l1_x, l1_y, line1, title_font, gold_color)
    draw_with_shadow(draw, l2_x, l2_y, line2, title_font, gold_color)

    img.save(output_path)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    input_img = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_musica_capitulo_10.png"
    output_img = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_musica_capitulo_10_con_titulo.png"
    add_text_to_image(input_img, output_img, "El Arte de la Narración Mágica", "Capítulo 10")
