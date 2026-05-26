import os
import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

base = r'c:\Users\neo\Documents\agente\mensajes positivos'

archivos = {
    'Extracto (fuente)': 'extracto_luz_cap8.txt',
    'Resumen ejecutivo': 'resumen_luz_cap8.md',
    'Guion de voz':      'guion_luz_cap8.md',
    'Post de Facebook':  'post_facebook_luz_cap8.md',
    'Portada':           'portada_luz_cap8.png',
}

print('=' * 52)
print('  CAPITULO 8 - Hagase la Luz')
print('  Los siete niveles del proceso curativo')
print('=' * 52)

todos_ok = True
for nombre, archivo in archivos.items():
    ruta = os.path.join(base, archivo)
    existe = os.path.exists(ruta)
    if existe:
        tamano = os.path.getsize(ruta)
        print(f'  [OK] {nombre}: {tamano:,} bytes')
    else:
        print(f'  [FALTA] {nombre}')
        todos_ok = False

print()

# Verificar calendario
with open(os.path.join(base, 'content_calendar.csv'), 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        if r.get('Libro') == 'luz' and r.get('Capitulo') == '8':
            print(f'  [OK] Calendario registrado')
            print(f'       Titulo:  {r["Titulo"]}')
            print(f'       Fecha:   {r["Fecha_Publicacion"]}')
            print(f'       Estado:  {r["Estado"]}')
            print(f'       Video:   {r["Ruta_Video"]}')
            print(f'       Portada: {os.path.basename(r["Ruta_Portada"])}')
            break

print('=' * 52)
if todos_ok:
    print('  CAPITULO 8 COMPLETAMENTE LISTO!')
    print('  Recuerda nombrar tu video: luz_cap8.mp4')
else:
    print('  Algunos archivos faltan. Revisa arriba.')
print('=' * 52)
