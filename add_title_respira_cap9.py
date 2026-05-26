from PIL import Image, ImageDraw, ImageFont
import os

def add_text_to_image(input_path, output_path, title_lines, chapter_text):
    # Load image
    img = Image.open(input_path)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Font selection
    font_paths = [
        r"C:\Windows\Fonts\georgiab.ttf",
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

    chapter_text = chapter_text.upper()

    def get_text_size(text, font):
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    # Calculate line widths and heights
    line_sizes = [get_text_size(line, title_font) for line in title_lines]
    chap_w, chap_h = get_text_size(chapter_text, chapter_font)

    # Ensure text doesn't exceed image width
    max_allowed_w = width * 0.9
    while any(w > max_allowed_w for w, h in line_sizes) and title_font.size > 20:
        new_size = title_font.size - 5
        title_font = ImageFont.truetype(title_font.path, new_size)
        line_sizes = [get_text_size(line, title_font) for line in title_lines]

    # Total height calculation
    spacing = 30
    total_text_h = chap_h + sum(h for w, h in line_sizes) + (spacing * len(title_lines))

    # Position: Center-bottom
    start_y = int(height * 0.75) - (total_text_h // 2)

    # Aesthetic
    gold_color = (255, 215, 0)
    white_color = (255, 255, 255)
    shadow_color = (0, 0, 0, 220)
    shadow_offset = 5

    def draw_with_shadow(draw, x, y, text, font, fill):
        draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=shadow_color)
        draw.text((x, y), text, font=font, fill=fill)

    # Draw chapter
    chap_x = (width - chap_w) // 2
    draw_with_shadow(draw, chap_x, start_y, chapter_text, chapter_font, white_color)

    # Draw title lines
    current_y = start_y + chap_h + spacing
    for i, line in enumerate(title_lines):
        w, h = line_sizes[i]
        x = (width - w) // 2
        draw_with_shadow(draw, x, current_y, line, title_font, gold_color)
        current_y += h + spacing

    img.save(output_path)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    input_img = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_respira_cap9.png"
    output_img = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_respira_cap9_con_titulo.png"
    add_text_to_image(input_img, output_img, ["EL ARTE DE", "AGUANTARLA"], "Capítulo 9")
