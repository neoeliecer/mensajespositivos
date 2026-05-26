import csv

row = [
    'manos',
    '18',
    'Visión Interna',
    '¿Rayos X Humanos? Descubre el poder de la Visión Interna 🧬 En el Capítulo 18 de "Manos que curan" exploramos la anatomía del tercer ojo. #Sanacion #VisionInterna',
    '',
    '',
    '2026-04-12',
    'Draft'
]

CSV_PATH = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

# Leer existentes para evitar duplicados si se corre de nuevo
rows = []
with open(CSV_PATH, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

# Verificar si ya existe el cap 18 de manos
exists = any(r[0] == 'manos' and r[1] == '18' for r in rows)

if not exists:
    with open(CSV_PATH, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row)
    print("Fila añadida correctamente.")
else:
    print("La fila ya existía.")
