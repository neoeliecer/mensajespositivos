import csv
import os

CSV_FILE = "content_calendar.csv"
POST_FILE = "post_facebook_capitulo_13.md"
SCRIPT_FILE = "guion_locucion_capitulo_13.md"
CHAPTER = "13"
TITLE = "La cara oculta de las redes"

def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

def update_csv():
    file_exists = os.path.isfile(CSV_FILE)
    
    headers = ["Chapter", "Title", "Facebook_Post_Text", "Script_Text", "Video_Path", "Status"]
    
    post_content = read_file(POST_FILE)
    script_content = read_file(SCRIPT_FILE)
    
    row = {
        "Chapter": CHAPTER,
        "Title": TITLE,
        "Facebook_Post_Text": post_content,
        "Script_Text": script_content,
        "Video_Path": "",  # To be filled by user
        "Status": "Ready for Video"
    }
    
    # Read existing rows to avoid duplicates or update existing
    rows = []
    if file_exists:
        with open(CSV_FILE, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                if r["Chapter"] != CHAPTER:
                    rows.append(r)
    
    rows.append(row)
    # Sort by chapter if possible (assuming integerable)
    try:
        rows.sort(key=lambda x: int(x["Chapter"]) if x["Chapter"].isdigit() else 0)
    except:
        pass

    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Updated {CSV_FILE} with Chapter {CHAPTER}")

if __name__ == "__main__":
    update_csv()
