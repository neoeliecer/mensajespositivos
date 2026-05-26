import asyncio
import edge_tts

# Texto de prueba (un fragmento del guion)
TEXTO_PRUEBA = "El cerebro recuerda lo que le calma. Si ante el estrés buscas dopamina fácil, tu mente te pedirá siempre esa vía de escape."

# Lista de voces a probar
VOCES = [
    {"id": "es-MX-JorgeNeural", "nombre": "Jorge (H - Mexico)", "archivo": "voz_jorge_mx.mp3"},
    {"id": "es-CO-GonzaloNeural", "nombre": "Gonzalo (H - Colombia)", "archivo": "voz_gonzalo_co.mp3"},
    {"id": "es-ES-AlvaroNeural", "nombre": "Alvaro (H - España)", "archivo": "voz_alvaro_es.mp3"},
    {"id": "es-MX-DaliaNeural", "nombre": "Dalia (M - Mexico)", "archivo": "voz_dalia_mx.mp3"},
    {"id": "es-ES-ElviraNeural", "nombre": "Elvira (M - España)", "archivo": "voz_elvira_es.mp3"}
]

async def generar_muestras():
    print("Generando muestras de voz...")
    for voz in VOCES:
        print(f"Generando: {voz['nombre']}...")
        comunicate = edge_tts.Communicate(TEXTO_PRUEBA, voz["id"])
        await comunicate.save(voz["archivo"])
        print(f" -> Guardado en: {voz['archivo']}")
    
    print("\n¡Listo! Escucha los archivos .mp3 generados y dime cuál prefieres.")

if __name__ == "__main__":
    asyncio.run(generar_muestras())
