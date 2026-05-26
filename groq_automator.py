import os
import re
import csv
import json
import requests
import PyPDF2
from datetime import datetime, timedelta

# ----------------------------------------------------
# CONFIGURATION & DIRECTORY PATHS
# ----------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "content_calendar.csv")
PDF_PATH = r"C:\Users\neo\Documents\libros\Brian-Tracy-El-poder-de-confiar-en-ti-mismo.pdf"
LOG_DIR = os.path.join(BASE_DIR, "scratch")
LOG_FILE = os.path.join(LOG_DIR, "automation_log.txt")

BOOK_NAME = "confiar"

# Make sure scratch dir exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_msg = f"[{timestamp}] {msg}"
    print(formatted_msg)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(formatted_msg + "\n")

# ----------------------------------------------------
# READ API KEYS (LOCAL .ENV OR DASHBOARD/.ENV.LOCAL)
# ----------------------------------------------------
def get_groq_key():
    # Try local root .env
    root_env = os.path.join(BASE_DIR, ".env")
    if os.path.exists(root_env):
        with open(root_env, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r"GROQ_API_KEY\s*=\s*(.*)", content)
            if match and match.group(1):
                return match.group(1).strip()

    # Try dashboard/.env.local
    dash_env = os.path.join(BASE_DIR, "dashboard", ".env.local")
    if os.path.exists(dash_env):
        with open(dash_env, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r"GROQ_API_KEY\s*=\s*(.*)", content)
            if match and match.group(1):
                return match.group(1).strip()
                
    return os.environ.get("GROQ_API_KEY")

# ----------------------------------------------------
# STEP 1: DETECT NEXT CHAPTER TO PROCESS
# ----------------------------------------------------
def get_next_chapter():
    last_cap = 0
    if os.path.exists(CSV_FILE):
        try:
            with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)
                for r in reader:
                    if r.get("Libro", "").lower() == BOOK_NAME.lower():
                        cap_val = r.get("Capitulo", "")
                        if cap_val.isdigit():
                            last_cap = max(last_cap, int(cap_val))
        except Exception as e:
            log(f"Error reading CSV for last chapter: {e}")
            
    # Fallback to scanning existing file names if CSV is empty or parsing fails
    files = os.listdir(BASE_DIR)
    for f in files:
        match = re.search(r"guion_confiar_cap(\d+)\.md", f)
        if match:
            last_cap = max(last_cap, int(match.group(1)))
            
    return last_cap + 1

# ----------------------------------------------------
# STEP 2: PDF PAGE EXTRACTION FOR A CHAPTER
# ----------------------------------------------------
def extract_chapter_text(chapter_num):
    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError(f"Brian Tracy book PDF not found at {PDF_PATH}")
        
    with open(PDF_PATH, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        total_pages = len(reader.pages)
        
        start_page = -1
        end_page = -1
        
        search_term = f"Capítulo {chapter_num}"
        next_search_term = f"Capítulo {chapter_num + 1}"
        
        # Búsqueda secuencial
        for i in range(total_pages):
            text = reader.pages[i].extract_text()
            if not text:
                continue
                
            # Regex lookups for start and end boundaries
            if start_page == -1 and (search_term in text or search_term.upper() in text or f"CAPÍTULO {chapter_num}" in text):
                start_page = i
                
            if start_page != -1 and i > start_page and (next_search_term in text or next_search_term.upper() in text or f"CAPÍTULO {chapter_num + 1}" in text):
                end_page = i
                break
                
        if start_page == -1:
            # Safe boundary fallbacks if chapter strings aren't found directly
            # E.g. index mapping approximations
            if chapter_num == 3:
                start_page = 37 # Page 38 approx
                end_page = 54   # Page 55 approx
            else:
                raise ValueError(f"Could not automatically detect boundaries for Chapter {chapter_num}")
                
        if end_page == -1:
            end_page = min(start_page + 16, total_pages) # Safe fallback size of 16 pages
            
        log(f"Chapter {chapter_num} page range: Pages {start_page + 1} to {end_page}")
        
        pages_content = []
        for i in range(start_page, end_page):
            text = reader.pages[i].extract_text()
            if text:
                pages_content.append(f"\n--- PÁGINA {i+1} ---\n")
                pages_content.append(text)
                
        return "\n".join(pages_content)

# ----------------------------------------------------
# STEP 3: API GENERATION WITH GROQ (LLAMA-3.3-70B)
# ----------------------------------------------------
def generate_content_with_groq(chapter_num, raw_text):
    api_key = get_groq_key()
    if not api_key:
        raise ValueError("GROQ_API_KEY missing from environment or .env configuration.")
        
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    system_instruction = (
        "Eres un guionista experto en crecimiento personal y redes sociales, con el tono inspirador de 'Matrix Producciones'. "
        "Tu misión es procesar el texto de un capítulo de libro y devolver un objeto JSON estructurado que contenga todos los materiales listos para usar.\n\n"
        "Debes responder ESTRICTAMENTE en formato JSON con la siguiente estructura (no agregues texto antes ni después, solo el objeto JSON):\n"
        "{\n"
        "  \"titulo_capitulo\": \"Título formal del capítulo\",\n"
        "  \"resumen\": \"Resumen ejecutivo del tema central (3 ideas principales y frase clave)\",\n"
        "  \"guion_voz_off\": \"Guion de locución fluido, inspirador y profundo de aproximadamente 300-400 palabras, estructurado con Gancho, Cuerpo y Reflexión final. Listo para leer.\",\n"
        "  \"guion_extendido\": \"Guion detallado y expandido con notas de producción y ejercicios prácticos.\",\n"
        "  \"post_facebook\": \"Un post de Facebook sumamente atractivo, utilizando emojis y hashtags relevantes.\",\n"
        "  \"post_instagram\": \"Un post de Instagram de alto impacto que contenga emojis y hashtags relevantes. Regla estricta: NO puede exceder los 2200 caracteres de longitud.\",\n"
        "  \"titulos_gancho\": [\"Título 1\", \"Título 2\", \"Título 3\", \"Título 4\", \"Título 5\"]\n"
        "}"
    )
    
    user_prompt = (
        f"Procesa el siguiente texto extraído del Capítulo {chapter_num} de Brian Tracy 'El poder de confiar en ti mismo':\n\n"
        f"{raw_text}\n\n"
        "Genera todos los campos solicitados en español."
    )
    
    payload = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_prompt}
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.65
    }
    
    log(f"Sending requests to Groq Cloud API for Chapter {chapter_num}...")
    response = requests.post(url, headers=headers, json=payload, timeout=60)
    
    if response.status_code != 200:
        raise RuntimeError(f"Groq API call failed: {response.status_code} - {response.text}")
        
    res_data = response.json()
    content_str = res_data["choices"][0]["message"]["content"]
    
    # Parse output
    return json.loads(content_str)

# ----------------------------------------------------
# STEP 4: SAVE OUTPUTS AND UPDATE THE CSV
# ----------------------------------------------------
def save_generated_files(chapter_num, data):
    # Save script files
    script_path = os.path.join(BASE_DIR, f"guion_confiar_cap{chapter_num}.md")
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(f"# Guion de Voz en Off: Capítulo {chapter_num} - {data['titulo_capitulo']}\n\n")
        f.write(data["guion_voz_off"])
        
    ext_path = os.path.join(BASE_DIR, f"guion_confiar_cap{chapter_num}_extendido.md")
    with open(ext_path, "w", encoding="utf-8") as f:
        f.write(f"# Guion Extendido: Capítulo {chapter_num} - {data['titulo_capitulo']}\n\n")
        f.write(data["guion_extendido"])
        
    fb_path = os.path.join(BASE_DIR, f"post_facebook_confiar_cap{chapter_num}.md")
    with open(fb_path, "w", encoding="utf-8") as f:
        f.write(data["post_facebook"])
        
    ig_path = os.path.join(BASE_DIR, f"post_instagram_confiar_cap{chapter_num}.md")
    with open(ig_path, "w", encoding="utf-8") as f:
        f.write(data["post_instagram"])
        
    titles_path = os.path.join(BASE_DIR, f"titulos_confiar_cap{chapter_num}.md")
    with open(titles_path, "w", encoding="utf-8") as f:
        f.write(f"# Títulos Gancho: Capítulo {chapter_num}\n\n")
        for i, t in enumerate(data["titulos_gancho"], 1):
            f.write(f"{i}. {t}\n")
            
    res_path = os.path.join(BASE_DIR, f"resumen_confiar_cap{chapter_num}.md")
    with open(res_path, "w", encoding="utf-8") as f:
        f.write(f"# Resumen de Enseñanzas: Capítulo {chapter_num}\n\n")
        f.write(data["resumen"])

    log(f"All markdown files saved successfully for Chapter {chapter_num}!")

def update_calendar_csv(chapter_num, data):
    headers = ["Libro", "Capitulo", "Titulo", "Texto_Post", "Ruta_Video", "Ruta_Portada", "Fecha_Publicacion", "Estado", "Texto_Post_Instagram"]
    
    rows = []
    dates = []
    file_exists = os.path.exists(CSV_FILE)
    
    if file_exists:
        try:
            with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames if reader.fieldnames else headers
                for r in reader:
                    # Ignore existing row of same book/chapter to avoid duplicates
                    if not (r.get("Libro", "").lower() == BOOK_NAME.lower() and str(r.get("Capitulo", "")) == str(chapter_num)):
                        rows.append(r)
                        if r.get("Fecha_Publicacion"):
                            try:
                                dates.append(datetime.strptime(r["Fecha_Publicacion"], "%Y-%m-%d"))
                            except:
                                pass
        except Exception as e:
            log(f"Warning reading CSV file: {e}")
            
    # Calculate next scheduled date
    if dates:
        next_date = max(dates) + timedelta(days=1)
    else:
        next_date = datetime.now() + timedelta(days=1)
        
    new_row = {
        "Libro": BOOK_NAME,
        "Capitulo": str(chapter_num),
        "Titulo": data["titulo_capitulo"],
        "Texto_Post": data["post_facebook"],
        "Ruta_Video": "",
        "Ruta_Portada": "",
        "Fecha_Publicacion": next_date.strftime("%Y-%m-%d"),
        "Estado": "Draft",
        "Texto_Post_Instagram": data["post_instagram"]
    }
    
    rows.append(new_row)
    
    # Sort
    try:
        rows.sort(key=lambda x: (x.get("Libro", "").lower(), int(x["Capitulo"]) if x.get("Capitulo", "").isdigit() else 0))
    except:
        pass
        
    with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
        
    log(f"Updated {CSV_FILE} with scheduled post for {next_date.strftime('%Y-%m-%d')}")

# ----------------------------------------------------
# MAIN EXECUTION PIPELINE
# ----------------------------------------------------
def main():
    log("====================================================")
    log("Starting Daily Content Automation Run...")
    log("====================================================")
    
    try:
        # Step 1: Detect Chapter
        chapter_num = get_next_chapter()
        log(f"Targeting Chapter: {chapter_num}")
        
        # Step 2: Extract PDF Text
        log("Extracting chapter text from PDF...")
        raw_text = extract_chapter_text(chapter_num)
        
        # Save raw text backup
        backup_path = os.path.join(BASE_DIR, f"extracto_brian_cap{chapter_num}.txt")
        with open(backup_path, "w", encoding="utf-8") as bf:
            bf.write(raw_text)
        log(f"Raw text backup saved to {backup_path}")
        
        # Step 3: Run Generation with Groq
        log("Generating copy assets using Groq Cloud API...")
        data = generate_content_with_groq(chapter_num, raw_text)
        
        # Step 4: Write Outputs and Update CSV
        log("Writing script and post markdown files...")
        save_generated_files(chapter_num, data)
        
        log("Updating calendar entries in CSV...")
        update_calendar_csv(chapter_num, data)
        
        log("====================================================")
        log("Daily Content Automation SUCCESS!")
        log("====================================================")
        
    except Exception as e:
        log("====================================================")
        log(f"Daily Content Automation FAILED: {str(e)}")
        log("====================================================")

if __name__ == "__main__":
    main()
