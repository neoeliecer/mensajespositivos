import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def find_chapter_10():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Searching {num_pages} pages...")
            
            # Search for the table of contents first (usually near the beginning)
            print("\nChecking first 15 pages for TOC...")
            for i in range(15):
                text = reader.pages[i].extract_text()
                if "Índice" in text or "Contenido" in text or "Indice" in text:
                    print(f"Possible TOC on page {i+1}:")
                    print(text)
                    # No need to return yet, let's keep searching for Chap 10
            
            # Search for Chapter 10 specifically
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if "Capítulo 10" in text or "Capitulo 10" in text or "CAPÍTULO 10" in text:
                    print(f"\n--- Found Chapter 10 on Page {i+1} ---")
                    print(text[:2000])
                    return
                    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_10()
