from PIL import Image, ImageDraw, ImageFont
import os

# Source and destination paths
src = r"C:\Users\neo\.gemini\antigravity\brain\fd086b92-e5b8-4dca-9471-5fa81284fd3c\portada_capitulo_10_base_1775054211088.png"
dest = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_10.png"

def create_final_cover():
    if not os.path.exists(src):
        print(f"Error: Source image not found at {src}")
        return

    img = Image.open(src).convert("RGBA")
    width, height = img.size

    # Create overlay for text area
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)

    # Semi-transparent dark band at bottom for readability
    band_height = 250
    draw_overlay.rectangle([(0, height - band_height), (width, height)], fill=(0, 0, 0, 160))

    # Fonts
    try:
        # Standard Windows font paths
        font_path_bold = "arialbd.ttf"
        font_path_reg = "arial.ttf"
        
        font_title = ImageFont.truetype(font_path_bold, 70)
        font_subtitle = ImageFont.truetype(font_path_reg, 40)
        font_cap = ImageFont.truetype(font_path_bold, 32)
    except IOError:
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
        font_cap = ImageFont.load_default()

    # Merge overlay to the image
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    # Title text
    title = "EL SECRETO DEL DIAGNÓSTICO ENERGÉTICO"
    tb = draw.textbbox((0, 0), title, font=font_title)
    tw = tb[2] - tb[0]
    draw.text(((width - tw) / 2, height - 210), title, font=font_title, fill=(255, 230, 100)) # Golden title

    # Subtitle
    subtitle = "Herramientas Ancestrales para tu Bienestar"
    sb = draw.textbbox((0, 0), subtitle, font=font_subtitle)
    sw = sb[2] - sb[0]
    draw.text(((width - sw) / 2, height - 120), subtitle, font=font_subtitle, fill=(240, 240, 240)) # Soft white

    # Chapter / Book Label
    label = "CAPÍTULO 10 · MANOS QUE CURÁN"
    lb = draw.textbbox((0, 0), label, font=font_cap)
    lw = lb[2] - lb[0]
    draw.text(((width - lw) / 2, height - 60), label, font=font_cap, fill=(200, 200, 200))

    # Optional: Decoration at top
    draw.line([(width//2 - 150, 100), (width//2 + 150, 100)], fill=(255, 230, 100, 180), width=3)

    # Save final image
    img.convert("RGB").save(dest, quality=95)
    print(f"Final cover image saved to {dest}")

if __name__ == "__main__":
    create_final_cover()
