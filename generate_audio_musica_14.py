import asyncio
import edge_tts
import os

VOICE = "es-CO-GonzaloNeural"
INPUT_FILE = "guion_musica_capitulo_14.md"
OUTPUT_FILE = "guion_musica_capitulo_14.mp3"

async def generate_audio():
    if not os.path.exists(INPUT_FILE):
        print(f"File not found: {INPUT_FILE}")
        # Try full path if relative fails
        INPUT_FILE_FULL = r"c:\Users\neo\Documents\agente\mensajes positivos\guion_musica_capitulo_14.md"
        if os.path.exists(INPUT_FILE_FULL):
            with open(INPUT_FILE_FULL, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            return
    else:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            text = f.read()

    # Clean text: remove markdown headers/separators for better voiceover
    import re
    clean_text = re.sub(r'#.*?\n', '', text)
    clean_text = re.sub(r'---.*?\n', '', clean_text)
    clean_text = re.sub(r'\*\*.*?\*\*', '', clean_text)
    clean_text = re.sub(r'##.*?\n', '', clean_text)
    
    # Only keep the "Guión de Voz en Off" section if possible
    match = re.search(r'🎙️ Guión de Voz en Off(.*?)(##|$)', clean_text, re.DOTALL)
    if match:
        voiceover_text = match.group(1).strip()
    else:
        voiceover_text = clean_text

    print(f"Generating audio with voice {VOICE}...")
    communicate = edge_tts.Communicate(voiceover_text, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Audio saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(generate_audio())
