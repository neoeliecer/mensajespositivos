
from PIL import Image, ImageDraw, ImageFont
import os

def add_title_to_image(input_path, output_path, text, subtitle):
    try:
        img = Image.open(input_path).convert("RGB")
        width, height = img.size
        draw = ImageDraw.Draw(img)
        
        # Load Fonts
        try:
            # Try to find a bold font
            font_path = "arialbd.ttf" 
            font_large = ImageFont.truetype(font_path, 100)
            font_small = ImageFont.truetype("arial.ttf", 50)
        except IOError:
            font_large = ImageFont.load_default()
            font_small = ImageFont.load_default()

        # Add Title with Shadow/Outline for visibility
        text = text.upper()
        
        # Calculate centering
        bbox = draw.textbbox((0, 0), text, font=font_large)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]
        x = (width - text_w) / 2
        y = (height - text_h) / 2
        
        # Draw Shadow/Outline (Thick black border for contrast against complex background)
        shadow_color = (0, 0, 0)
        outline_width = 4
        for adj_x in range(-outline_width, outline_width+1):
            for adj_y in range(-outline_width, outline_width+1):
                draw.text((x+adj_x, y+adj_y), text, font=font_large, fill=shadow_color)
        
        # Main Title (White)
        draw.text((x, y), text, font=font_large, fill=(255, 255, 255))
        
        # Subtitle
        sub_bbox = draw.textbbox((0, 0), subtitle, font=font_small)
        sub_w = sub_bbox[2] - sub_bbox[0]
        sub_x = (width - sub_w) / 2
        sub_y = y + text_h + 30
        
        # Subtitle Shadow
        for adj_x in range(-2, 3):
            for adj_y in range(-2, 3):
                 draw.text((sub_x+adj_x, sub_y+adj_y), subtitle, font=font_small, fill=shadow_color)
                 
        draw.text((sub_x, sub_y), subtitle, font=font_small, fill=(230, 230, 230))

        img.save(output_path)
        print(f"Title added. Saved to {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Input is the current 'portada_capitulo_18.png' (The neuron image)
    input_file = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_18.png"
    # We overwrite it or save as new. Let's overwrite to keep it simple for the user.
    output_file = r"c:\Users\neo\Documents\agente\mensajes positivos\portada_capitulo_18_titled.png"
    
    add_title_to_image(input_file, output_file, "Ayuno de Dopamina", "Marian Rojas Estapé | Cap. 18")
