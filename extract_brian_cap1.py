import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\Brian-Tracy-El-poder-de-confiar-en-ti-mismo.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_brian_cap1.txt"
log_path = r"c:\Users\neo\Documents\agente\mensajes positivos\scratch\extract_brian_log.txt"

def log(msg):
    print(msg)
    with open(log_path, 'a', encoding='utf-8') as lf:
        lf.write(msg + "\n")

# Clear log
if os.path.exists(log_path):
    os.remove(log_path)

log("Starting extraction of Brian Tracy Book, Chapter 1...")

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)
        log(f"Total pages in book: {total_pages}")
        
        start_page = -1
        end_page = -1
        
        # Terms to search for Chapter 1
        ch1_terms = ["CAPÍTULO UNO", "CAPÍTULO 1", "LOS CIMENTOS DE LA CONFIANZA", "LOS FUNDAMENTOS DE LA AUTOCONFIANZA", "EL PRIMER CIMIENTO"]
        # Terms to search for Chapter 2
        ch2_terms = ["CAPÍTULO DOS", "CAPÍTULO 2", "PROPÓSITO Y PODER PERSONAL"]
        
        # Búsqueda secuencial
        for idx in range(total_pages):
            text = reader.pages[idx].extract_text()
            if not text:
                continue
                
            text_upper = text.upper()
            
            # Check for Chapter 1 start
            if start_page == -1:
                for term in ch1_terms:
                    if term in text_upper:
                        # Ensure it's not the Table of Contents (Índice)
                        if "ÍNDICE" not in text_upper and "CONTENIDO" not in text_upper:
                            start_page = idx
                            log(f"Found Chapter 1 start on page {idx + 1} with term '{term}'")
                            break
            
            # Check for Chapter 2 start
            if start_page != -1 and idx > start_page:
                for term in ch2_terms:
                    if term in text_upper:
                        if "ÍNDICE" not in text_upper and "CONTENIDO" not in text_upper:
                            end_page = idx
                            log(f"Found Chapter 2 start (Chapter 1 end) on page {idx + 1} with term '{term}'")
                            break
                if end_page != -1:
                    break
                    
        # Fallback if detection failed
        if start_page == -1:
            log("Warning: Could not detect Chapter 1 start automatically. Defaulting to page 15.")
            start_page = 14 # Index 14 (page 15)
        if end_page == -1:
            log("Warning: Could not detect Chapter 2 start automatically. Defaulting to start_page + 20.")
            end_page = start_page + 20
            
        log(f"Final extraction range: Pages {start_page + 1} to {end_page}")
        
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
