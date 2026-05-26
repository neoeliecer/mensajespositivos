import asyncio
import edge_tts
import os
import re

VOICE = "es-CO-GonzaloNeural"
INPUT_FILE = r"C:\Users\neo\Documents\agente\mensajes positivos\guion_manos_cap7.md"
OUTPUT_FILE = r"C:\Users\neo\Documents\agente\mensajes positivos\guion_manos_cap7.mp3"

async def generate_audio():
    print(f"Reading {INPUT_FILE}...")
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Simple extraction for the locution part
    parts = re.findall(r"\*\*Locutor:\*\*\n(.*?)\n\n\*\*Cierre:\*\*", content, re.DOTALL)
    if parts:
        text_to_read = parts[0].strip()
        closing = re.search(r"\*\*Cierre:\*\*\n(.*?)\n\n---", content, re.DOTALL)
        if closing:
            text_to_read += " " + closing.group(1).strip()
    else:
        # Fallback if the regex fails
        text_to_read = content
        text_to_read = re.sub(r"# .*?\n", "", text_to_read)
        text_to_read = re.sub(r"\*\*Duration.*?\n", "", text_to_read)
        text_to_read = re.sub(r"\*\*Objective.*?\n", "", text_to_read)
        text_to_read = re.sub(r"---.*", "", text_to_read, flags=re.DOTALL)
        text_to_read = re.sub(r"\*\*Locutor:\*\*|\*\*Cierre:\*\*|\*\*Speaker:\*\*|\*\*Narrator:\*\*", "", text_to_read)
        text_to_read = re.sub(r"\*.*?\*", "", text_to_read)
        text_to_read = text_to_read.strip()

    print(f"Generating audio with voice {VOICE}...")
    communicate = edge_tts.Communicate(text_to_read, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Audio saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_audio())
