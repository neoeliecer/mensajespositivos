import csv
import os

CSV_PATH = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

new_row = {
    'Libro': 'respira',
    'Capitulo': '9',
    'Titulo': 'Nueve: Aguantarla',
    'Texto_Post': '🧠 ¿Sabías que el miedo no está solo en tu mente, sino en tu sangre? James Nestor nos cuenta por qué aguantar la respiración es la clave para superar la ansiedad. #Respira #SaludMental #Capitulo9',
    'Ruta_Video': '',
    'Ruta_Portada': '',
    'Fecha_Publicacion': '2026-05-18',
    'Estado': 'Draft'
}

# Check if it already exists
already_exists = False
if os.path.exists(CSV_PATH):
    with open(CSV_PATH, 'r', encoding='latin-1') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Libro'] == 'respira' and row['Capitulo'] == '9':
                already_exists = True
                break

if not already_exists:
    with open(CSV_PATH, 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Libro', 'Capitulo', 'Titulo', 'Texto_Post', 'Ruta_Video', 'Ruta_Portada', 'Fecha_Publicacion', 'Estado'])
        writer.writerow(new_row)
    print("Capítulo 9 registrado en el calendario.")
else:
    print("El capítulo 9 ya está registrado.")
