from PIL import Image, ImageDraw, ImageFont
import os

# Paths
source_dir = r"C:\Users\neo\.gemini\antigravity\brain\06820dab-1eb0-403f-ab17-713ef1eb075d"
image_filename = "cover_chapter_12_inner_voice_1770742646238.png"
input_path = os.path.join(source_dir, image_filename)
output_filename = "cover_chapter_12_with_title.png"
output_path = os.path.join(source_dir, output_filename)

# Text configurations
text = "EL PODER DE\nTU VOZ INTERIOR"
font_path = "arial.ttf" # Try default
try:
    font_path = r"C:\Windows\Fonts\impact.ttf" # Impact is usually good for titles
except:
    pass

def add_title():
    if not os.path.exists(input_path):
        print(f"Error: Image not found at {input_path}")
        return

    try:
        img = Image.open(input_path)
        draw = ImageDraw.Draw(img)
        w, h = img.size

        # Font size adjustment
        fontsize = 100 
        try:
            font = ImageFont.truetype(font_path, fontsize)
        except OSError:
            font = ImageFont.load_default()
            print("Warning: Could not load requested font, using default.")

        # Calculate text position (centered, slightly upper or middle)
        # Using textbbox if available (Pillow >= 9.2.0) or textsize
        try:
           left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
           text_w = right - left
           text_h = bottom - top
        except AttributeError:
           text_w, text_h = draw.textsize(text, font=font)

        x = (w - text_w) / 2
        y = (h - text_h) / 2

        # Add outline/shadow for readability
        outline_color = "black"
        text_color = "white"
        thickness = 5
        
        # Draw outline
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
