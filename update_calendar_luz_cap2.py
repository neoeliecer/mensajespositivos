import csv
import os
from datetime import datetime

CSV_FILE = "content_calendar.csv"
POST_FILE = "post_facebook_luz_cap2.md"

def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def update_csv():
    file_exists = os.path.isfile(CSV_FILE)
    
    headers = ["Libro", "Capitulo", "Titulo", "Texto_Post", "Ruta_Video", "Ruta_Portada", "Fecha_Publicacion", "Estado"]
    
    post_content = read_file(POST_FILE)
    
    row = {
        "Libro": "luz",
        "Capitulo": "2",
        "Titulo": "Hágase la Luz Cap 2: Las Cuatro Dimensiones",
        "Texto_Post": post_content,
        "Ruta_Video": "",
        "Ruta_Portada": "",
        "Fecha_Publicacion": "",
        "Estado": "Draft"
    }
    
    rows = []
    if file_exists:
        with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            # Use original headers
            headers = reader.fieldnames if reader.fieldnames else headers
            
            for r in reader:
                if not (r.get("Libro", "").lower() == "luz" and str(r.get("Capitulo", "")) == "2"):
                    rows.append(r)
    
    rows.append(row)

    with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Updated {CSV_FILE} con el Libro luz y Capitulo 2")

if __name__ == "__main__":
    update_csv()
