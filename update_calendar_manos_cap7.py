import csv
import os
from datetime import datetime, timedelta

CSV_PATH = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"
POST_PATH = r"c:\Users\neo\Documents\agente\mensajes positivos\post_facebook_manos_cap7.md"

def get_last_date(rows):
    last_date = None
    for r in rows:
        if r.get('Fecha_Publicacion'):
            try:
                d = datetime.strptime(r['Fecha_Publicacion'], '%Y-%m-%d')
                if last_date is None or d > last_date:
                    last_date = d
            except:
                pass
    return last_date or datetime.now()

def append_to_calendar():
    # Read post content
    with open(POST_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove header if present
    content = content.replace("# Post de Facebook: Manos que curan - Capítulo 7", "").strip()
    
    # Read existing rows
    rows = []
    headers = []
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        rows = list(reader)
    
    # Check if already exists
    for r in rows:
        if r['Libro'].lower() == 'manos' and r['Capitulo'] == '7':
            print("Capítulo 7 ya existe en el calendario.")
            return

    last_date = get_last_date(rows)
    next_date = last_date + timedelta(days=1)
    
    new_row = {
        'Libro': 'manos',
        'Capitulo': '7',
        'Titulo': 'Manos que curan Cap 7: El Campo Energético Humano (Aura)',
        'Texto_Post': content,
        'Ruta_Video': '',
        'Ruta_Portada': r'c:\Users\neo\Documents\agente\mensajes positivos\portada_manos_capitulo_7_con_titulo.png',
        'Fecha_Publicacion': next_date.strftime('%Y-%m-%d'),
        'Estado': 'Draft'
    }
    
    rows.append(new_row)
    
    with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Capítulo 7 registrado para el {next_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    append_to_calendar()
