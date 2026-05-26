import asyncio
import edge_tts
import os
import re

VOICE = "es-CO-GonzaloNeural"
INPUT_FILE = "guion_respira_cap1_extendido.md"
OUTPUT_FILE = "guion_respira_cap1_extendido.mp3"

async def generate_audio():
    print(f"Reading {INPUT_FILE}...")
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Eliminar títulos y separadores
    text_to_read = re.sub(r"#.*?\n", "", content)
    text_to_read = re.sub(r"---", "", text_to_read)
    
    # Eliminar las acotaciones entre corchetes **[INTRO...]**, **[BLOQUE...]**
    text_to_read = re.sub(r"\*\*\[.*?\]\*\*", "", text_to_read)
    
    # Eliminar notas de pie de página o texto en cursiva al final
    text_to_read = re.sub(r"\*Basado en.*?\*", "", text_to_read)
    
    text_to_read = text_to_read.strip()

    print(f"Generating audio with voice {VOICE}...")
    communicate = edge_tts.Communicate(text_to_read, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Audio saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_audio())
