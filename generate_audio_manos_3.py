import asyncio
import edge_tts
import os
import re

VOICE = "es-CO-GonzaloNeural"
INPUT_FILE = "guion_manos_cap3.md"
OUTPUT_FILE = "guion_manos_cap3.mp3"

async def generate_audio():
    print(f"Reading {INPUT_FILE}...")
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.search(r"## 🎙️ Guión de Voz en Off\n\n(.*?)(?=\n\n---|\Z)", content, re.DOTALL)
    if match:
        text_to_read = match.group(1).strip()
        text_to_read = re.sub(r"\*\*\(Hook\)\*\*|\*\*\(Cuerpo\)\*\*|\*\*\(Cierre\)\*\*", "", text_to_read)
        text_to_read = re.sub(r"\(Hook\)|\(Cuerpo\)|\(Cierre\)", "", text_to_read)
        text_to_read = re.sub(r"\[Pausa.*?\]", "...", text_to_read)
        text_to_read = re.sub(r"\*\*.*?\*\*", lambda m: m.group(0).replace("**", ""), text_to_read)
    else:
        print("Could not find script section. Reading full content.")
        text_to_read = content

    print(f"Generating audio with voice {VOICE}...")
    communicate = edge_tts.Communicate(text_to_read, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Audio saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_audio())
