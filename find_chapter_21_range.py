import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_21_range():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            start_page = -1
            end_page = -1
            
            # Buscamos desde la página 155 (donde terminó el 20)
            for i in range(150, 180): # Buscamos en un rango amplio alrededor del final del anterior
                if i >= len(reader.pages):
                    break
                    
                text = reader.pages[i].extract_text()
                if not text: continue
                
                # Buscamos Capítulo 21
                if start_page == -1 and ("Capítulo 21" in text or "Capítulo veintiuno" in text or "CAPÍTULO 21" in text):
                    start_page = i
                    print(f"Capítulo 21 encontrado en la página {i+1}")
                
                # Buscamos Capítulo 22
                if start_page != -1 and i > start_page:
                    if ("Capítulo 22" in text or "Capítulo veintidós" in text or "CAPÍTULO 22" in text):
                        end_page = i - 1
                        print(f"Capítulo 22 encontrado en la página {i+1}")
                        break
            
            return start_page, end_page

    except Exception as e:
        print(f"Error: {e}")
        return -1, -1

start, end = find_chapter_21_range()
print(f"RESULT: START={start}, END={end}")
