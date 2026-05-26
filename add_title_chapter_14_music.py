from PIL import Image, ImageDraw, ImageFont
import os

# Paths
input_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_musica_capitulo_14.png"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_musica_capitulo_14_con_titulo.png"

# Text configurations
text = "EL PODER DEL COLOR\nY EL SONIDO"
font_path = r"C:\Windows\Fonts\impact.ttf"

def add_title():
    if not os.path.exists(input_path):
        print(f"Error: Image not found at {input_path}")
        return

    try:
        img = Image.open(input_path)
        draw = ImageDraw.Draw(img)
        w, h = img.size

        # Font size adjustment
        fontsize = int(w / 12) # Dynamic font size
        try:
            font = ImageFont.truetype(font_path, fontsize)
        except OSError:
            font = ImageFont.load_default()
            print("Warning: Could not load requested font, using default.")

        # Calculate text position
        try:
           left, top, right, bottom = draw.textbbox((0, 0), text, font=font, align="center")
           text_w = right - left
           text_h = bottom - top
        except AttributeError:
           text_w, text_h = draw.textsize(text, font=font)

        x = (w - text_w) / 2
        y = (h - text_h) / 2

        # Add outline for readability
        outline_color = "black"
        text_color = "white"
        thickness = 5
        
        for adj_x in range(-thickness, thickness+1):
            for adj_y in range(-thickness, thickness+1):
                draw.text((x+adj_x, y+adj_y), text, font=font, fill=outline_color, align="center")

        # Draw main text
        draw.text((x, y), text, font=font, fill=text_color, align="center")

        img.save(output_path)
        print(f"Image saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    add_title()
