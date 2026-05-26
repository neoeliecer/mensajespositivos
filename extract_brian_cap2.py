import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\Brian-Tracy-El-poder-de-confiar-en-ti-mismo.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_brian_cap2.txt"
log_path = r"c:\Users\neo\Documents\agente\mensajes positivos\scratch\extract_brian_log.txt"

def log(msg):
    print(msg)
    with open(log_path, 'a', encoding='utf-8') as lf:
        lf.write(msg + "\n")

log("Starting extraction of Brian Tracy Book, Chapter 2...")

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)
        log(f"Total pages in book: {total_pages}")
        
        # Chapter 2 starts at Page 23 (index 22) and ends before Page 38 (index 37)
        start_page = 22
        end_page = 37
        
        log(f"Extraction range: Pages {start_page + 1} to {end_page}")
        
        chapter_text = []
        for i in range(start_page, end_page):
            if i < total_pages:
                text = reader.pages[i].extract_text()
                if text:
                    chapter_text.append(f"\n--- PÁGINA {i+1} ---\n")
                    chapter_text.append(text)
                    
        full_text = "\n".join(chapter_text)
        
        with open(output_path, "w", encoding="utf-8") as out_f:
            out_f.write(full_text)
            
        log(f"Extraction successful! Extracted {len(full_text)} characters and saved to {output_path}")
        
except Exception as e:
    log(f"Error occurred: {str(e)}")
