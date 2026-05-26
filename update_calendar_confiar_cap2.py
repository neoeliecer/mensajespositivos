import csv
import os
from datetime import datetime, timedelta

CSV_FILE = "content_calendar.csv"
POST_FILE = "post_facebook_confiar_cap2.md"
BOOK_NAME = "confiar"
CHAPTER_NUM = "2"
CHAPTER_TITLE = "Propósito y Poder Personal"

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
    
    # Let's find the next available date by scanning existing dates in CSV
    next_date = datetime.now()
    dates = []
    
    rows = []
    if file_exists:
        # Try reading with utf-8-sig, fall back to latin-1 if decode fails
        try:
            with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames if reader.fieldnames else headers
                for r in reader:
                    if not (r.get("Libro", "").lower() == BOOK_NAME.lower() and str(r.get("Capitulo", "")) == CHAPTER_NUM):
                        rows.append(r)
                        if r.get("Fecha_Publicacion"):
                            try:
                                dates.append(datetime.strptime(r["Fecha_Publicacion"], "%Y-%m-%d"))
                            except:
                                pass
        except UnicodeDecodeError:
            with open(CSV_FILE, "r", encoding="latin-1", newline="") as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames if reader.fieldnames else headers
                for r in reader:
                    if not (r.get("Libro", "").lower() == BOOK_NAME.lower() and str(r.get("Capitulo", "")) == CHAPTER_NUM):
                        rows.append(r)
                        if r.get("Fecha_Publicacion"):
                            try:
                                dates.append(datetime.strptime(r["Fecha_Publicacion"], "%Y-%m-%d"))
                            except:
                                pass

    if dates:
        next_date = max(dates) + timedelta(days=1)
    else:
        next_date = datetime.now() + timedelta(days=1)
        
    row = {
        "Libro": BOOK_NAME,
        "Capitulo": CHAPTER_NUM,
        "Titulo": CHAPTER_TITLE,
        "Texto_Post": post_content,
        "Ruta_Video": "",
        "Ruta_Portada": "",
        "Fecha_Publicacion": next_date.strftime("%Y-%m-%d"),
        "Estado": "Draft"
    }
    
    rows.append(row)
    
    # Sort rows if possible to keep them structured
    try:
        rows.sort(key=lambda x: (x.get("Libro", "").lower(), int(x["Capitulo"]) if x.get("Capitulo", "").isdigit() else 0))
    except Exception as e:
        print(f"Sorting error: {e}")
        pass

    with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Updated {CSV_FILE} with Book '{BOOK_NAME}' Chapter {CHAPTER_NUM} set for {next_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    update_csv()
