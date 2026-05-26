import asyncio
import edge_tts

VOICE = "es-CO-GonzaloNeural"
INPUT_FILE = "voz_post_facebook_capitulo_11.md"
OUTPUT_FILE = "voz_post_facebook_capitulo_11.mp3"

async def generate_audio():
    print(f"Reading {INPUT_FILE}...")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()

    print(f"Generating audio with voice {VOICE}...")
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Audio saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_audio())
