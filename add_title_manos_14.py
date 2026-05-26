from PIL import Image, ImageDraw, ImageFont
import os

def add_text_to_image(input_path, output_path, title_line1, title_line2, chapter_text):
    # Load image
    if not os.path.exists(input_path):
        print(f"Error: Input image not found at {input_path}")
        return

    img = Image.open(input_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Font selection
    font_paths = [
        r"C:\Windows\Fonts\georgiab.ttf", # Serif Bold
        r"C:\Windows\Fonts\georgia.ttf",
        r"C:\Windows\Fonts\timesbd.ttf",
        r"C:\Windows\Fonts\arialbd.ttf"
    ]
    
    title_font = None
    chapter_font = None
    
    for path in font_paths:
        if os.path.exists(path):
            try:
                title_font = ImageFont.truetype(path, 80)
                chapter_font = ImageFont.truetype(path, 40)
                break
            except:
                continue
    
    if not title_font:
        title_font = ImageFont.load_default()
        chapter_font = ImageFont.load_default()

    def get_text_size(text, font):
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    chap_w, chap_h = get_text_size(chapter_text, chapter_font)
    l1_w, l1_h = get_text_size(title_line1, title_font)
    l2_w, l2_h = get_text_size(title_line2, title_font)

    # Adjust font size if too wide
    max_allowed_w = width * 0.9
    while (l1_w > max_allowed_w or l2_w > max_allowed_w) and title_font.size > 20:
        new_size = title_font.size - 5
        title_font = ImageFont.truetype(title_font.path, new_size)
        l1_w, l1_h = get_text_size(title_line1, title_font)
        l2_w, l2_h = get_text_size(title_line2, title_font)

    # Spacing and layout
    spacing = 30
    total_h = chap_h + l1_h + l2_h + (spacing * 2)
    
    # Position: Bottom area
    start_y = int(height * 0.75) - (total_h // 2)

    # Aesthetic colors
    gold_color = (255, 215, 0) # Gold
    white_color = (255, 255, 255)
    shadow_color = (0, 0, 0, 220)
    shadow_offset = 5

    def draw_with_shadow(x, y, text, font, fill):
        draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=shadow_color)
        draw.text((x, y), text, font=font, fill=fill)

    # Drawing
    draw_with_shadow((width - chap_w) // 2, start_y, chapter_text, chapter_font, white_color)
    draw_with_shadow((width - l1_w) // 2, start_y + chap_h + spacing, title_line1, title_font, gold_color)
    draw_with_shadow((width - l2_w) // 2, start_y + chap_h + l1_h + (spacing * 2), title_line2, title_font, gold_color)

    img.save(output_path)
    print(f"Final cover saved to {output_path}")

if __name__ == "__main__":
    input_img = "portada_manos_cap14_base.png"
    output_img = "portada_manos_capitulo_14_con_titulo.png"
    add_text_to_image(input_img, output_img, "LA SEPARACIÓN", "DE LA REALIDAD", "CAPÍTULO 14")
