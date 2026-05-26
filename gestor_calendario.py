import os
import re
import csv
from datetime import datetime, timedelta

# Configuración
BASE_DIR = r"c:\Users\neo\Documents\agente\mensajes positivos"
CSV_PATH = os.path.join(BASE_DIR, "content_calendar.csv")

def scan_files():
    """Busca videos y portadas en la carpeta siguiendo la nomenclatura libro_capX."""
    files = os.listdir(BASE_DIR)
    found_videos = {}
    found_covers = {}
    
    for f in files:
        vid_match = re.match(r'([a-zA-Z]+)_cap(\d+)\.(mp4|mov|avi|mkv)', f, re.I)
        if vid_match:
            libro, cap = vid_match.groups()[:2]
            key = (libro.lower(), int(cap))
            found_videos[key] = os.path.join(BASE_DIR, f)
            
        img_match = re.match(r'([a-zA-Z]+)_cap(\d+)\.(png|jpg|jpeg)', f, re.I)
        if img_match:
            libro, cap = img_match.groups()[:2]
            key = (libro.lower(), int(cap))
            found_covers[key] = os.path.join(BASE_DIR, f)
            
    return found_videos, found_covers

def update_calendar():
    if not os.path.exists(CSV_PATH):
        print(f"Error: No se encontró el archivo {CSV_PATH}")
        return

    rows = []
    headers = []
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)

    vids, covers = scan_files()
    
    last_date_str = ""
    for r in rows:
        if r.get('Fecha_Publicacion'):
            last_date_str = r['Fecha_Publicacion']

    if last_date_str:
        try:
            last_date = datetime.strptime(last_date_str, '%Y-%m-%d')
        except:
            last_date = datetime.now()
    else:
        last_date = datetime.now()

    updates_made = 0
    processed_keys = set()
    
    for r in rows:
        libro = r['Libro'].lower()
        cap = int(r['Capitulo'])
        key = (libro, cap)
        processed_keys.add(key)
        
        if key in vids:
            if r['Estado'] != 'Published':
                r['Ruta_Video'] = vids[key]
                if key in covers:
                    r['Ruta_Portada'] = covers[key]
                
                if not r.get('Fecha_Publicacion'):
                    last_date += timedelta(days=1)
                    r['Fecha_Publicacion'] = last_date.strftime('%Y-%m-%d')
                
                r['Estado'] = 'Ready'
                updates_made += 1

    # Agregar nuevos videos que no estaban en el CSV
    for (libro, cap), path in vids.items():
        if (libro, cap) not in processed_keys:
            last_date += timedelta(days=1)
            new_row = {
                'Libro': libro,
                'Capitulo': str(cap),
                'Titulo': f"Capítulo {cap} de {libro}",
                'Texto_Post': f"¡Nuevo contenido de {libro}! Capítulo {cap} disponible.",
                'Ruta_Video': path,
                'Ruta_Portada': covers.get((libro, cap), ""),
                'Fecha_Publicacion': last_date.strftime('%Y-%m-%d'),
                'Estado': 'Ready'
            }
            rows.append(new_row)
            updates_made += 1

    if updates_made > 0:
        with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Calendario actualizado: {updates_made} cambios realizados.")
    else:
        print("No se encontraron archivos nuevos para sincronizar.")

if __name__ == "__main__":
    update_calendar()
