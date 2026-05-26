import os
import re
import PyPDF2

# Configuración
BASE_DIR = r"c:\Users\neo\Documents\agente\mensajes positivos"
BOOK_MAP = {
    'luz': r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf",
    'manos': r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
}

def get_current_series_and_chapter():
    files = os.listdir(BASE_DIR)
    
    # Prioritizamos 'luz' ya que es la serie actual
    luz_chapters = []
    manos_chapters = []
    
    for f in files:
        m_luz = re.search(r'extracto_luz_cap(\d+)\.txt', f)
        if m_luz:
            luz_chapters.append(int(m_luz.group(1)))
            
        m_manos = re.search(r'extracto_manos_cap(\d+)\.txt', f)
        if m_manos:
            manos_chapters.append(int(m_manos.group(1)))
            
    if luz_chapters:
        return 'luz', max(luz_chapters)
    elif manos_chapters:
        return 'manos', max(manos_chapters)
    return 'luz', 0 # Por defecto empezamos con luz 0 si no hay nada

def find_chapter_range(series, chapter_num):
    pdf_path = BOOK_MAP.get(series)
    if not pdf_path or not os.path.exists(pdf_path):
        return -1, -1
        
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        start_page = -1
        end_page = -1
        
        search_term = f"Capítulo {chapter_num}"
        next_search_term = f"Capítulo {chapter_num + 1}"
        
        # Búsqueda secuencial para mayor precisión
        for i in range(len(reader.pages)):
            text = reader.pages[i].extract_text()
            if not text: continue
            
            if start_page == -1 and (search_term in text or search_term.upper() in text):
                start_page = i
            
            if start_page != -1 and (next_search_term in text or next_search_term.upper() in text):
                end_page = i
                break
                
        return start_page, end_page

def main():
    series, last_cap = get_current_series_and_chapter()
    next_cap = last_cap + 1
    print(f"Serie actual: {series}")
    print(f"Último capítulo procesado: {last_cap}")
    print(f"Próximo capítulo a procesar: {next_cap}")
    
    start, end = find_chapter_range(series, next_cap)
    if start != -1:
        print(f"Rango detectado: Página {start + 1} hasta {end if end != -1 else 'final'}")
        print(f"NEXT_SERIES={series}")
        print(f"NEXT_CHAPTER={next_cap}")
        print(f"START_PAGE={start}")
        print(f"END_PAGE={end if end != -1 else start + 10}") # Fallback safe range
    else:
        print("No se pudo detectar el rango automáticamente para el próximo capítulo.")

if __name__ == "__main__":
    main()
