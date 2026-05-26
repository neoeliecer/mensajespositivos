import subprocess
import re
import os

script_path = r"C:\Users\neo\Documents\agente\mensajes positivos\guion_manos_cap15.md"
output_path = r"C:\Users\neo\Documents\agente\mensajes positivos\guion_manos_cap15.mp3"

def generate_audio():
    try:
        if not os.path.exists(script_path):
            print(f"Error: Script not found at {script_path}")
            return

        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract voiceover section
        match = re.search(r'## 🎙️ Guion de Voz en Off\n\n(.*?)\n\n---', content, re.DOTALL)
        if not match:
            print("Error: Voiceover section not found in script.")
            return

        voiceover_text = match.group(1)
        # Remove stage directions like (Hook), (Cuerpo), [Pausa], etc.
        voiceover_text = re.sub(r'\(.*?\)', '', voiceover_text)
        voiceover_text = re.sub(r'\[.*?\]', '', voiceover_text)
        voiceover_text = voiceover_text.strip()

        print(f"Generating audio for text: {voiceover_text[:100]}...")

        # Use a temporary text file to avoid command line length limits
        with open("tmp_voiceover.txt", "w", encoding="utf-8") as f:
            f.write(voiceover_text)
        
        # Try running via python module
        subprocess.run(['py', '-m', 'edge_tts', '--voice', 'es-MX-DaliaNeural', '--file', 'tmp_voiceover.txt', '--write-media', output_path], check=True)
        
        print(f"Audio generated successfully at {output_path}")
        os.remove("tmp_voiceover.txt")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_audio()
