import asyncio
import edge_tts
import os
import re

VOICE = "es-CO-GonzaloNeural"
INPUT_FILE = r"C:\Users\neo\Documents\agente\mensajes positivos\guion_manos_cap8.md"
OUTPUT_FILE = r"C:\Users\neo\Documents\agente\mensajes positivos\guion_manos_cap8.mp3"

async def generate_audio():
    print(f"Reading {INPUT_FILE}...")
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean text for reading
    text_to_read = content
    # Remove markdown headers and emphasis
    text_to_read = re.sub(r"# .*?\n", "", text_to_read)
    text_to_read = re.sub(r"\*\*Voz en Off:\*\*|\*\*Voz en Off:🎙️\*\*|🎙️", "", text_to_read)
    text_to_read = re.sub(r"\*\*.*?\*\*", "", text_to_read, flags=re.DOTALL) # Remove bold descriptors
    text_to_read = re.sub(r"\*.*?\*", "", text_to_read) # Remove italic descriptors
    text_to_read = re.sub(r"🌈|🧘‍♂️|✨", "", text_to_read) # Remove common emojis
    # Remove hashtags at the end
    text_to_read = re.sub(r"#\w+", "", text_to_read)
    
    text_to_read = text_to_read.strip()
    
    print(f"Text to read: {text_to_read[:100]}...")

    print(f"Generating audio with voice {VOICE}...")
    communicate = edge_tts.Communicate(text_to_read, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Audio saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_audio())
