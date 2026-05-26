import sys
import csv
import os

# Configuración
CSV_PATH = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

def mark_published(libro, cap):
    if not os.path.exists(CSV_PATH):
        print("CSV no encontrado")
        return

    rows = []
    headers = []
    found = False
    
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        for r in reader:
            if r['Libro'].lower() == libro.lower() and int(r['Capitulo']) == int(cap):
                r['Estado'] = 'Published'
                found = True
            rows.append(r)
    
    if found:
        with open(CSV_PATH, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
        print(f"Capítulo {cap} de {libro} marcado como Publicado.")
    else:
        print("No se encontró la fila correspondiente.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python marcar_publicado.py [libro] [capitulo]")
    else:
        mark_published(sys.argv[1], sys.argv[2])
