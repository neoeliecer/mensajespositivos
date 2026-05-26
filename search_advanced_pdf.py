import os
import re

try:
    import fitz # PyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False

try:
    import PyPDF2
    HAS_PYPDF2 = True
except ImportError:
    HAS_PYPDF2 = False

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def search_chapters():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    print(f"Searching in: {pdf_path}")
    
    if HAS_FITZ:
        print("Using PyMuPDF (fitz)...")
        doc = fitz.open(pdf_path)
        for i in range(len(doc)):
            page = doc[i]
            text = page.get_text()
            if "Capítulo 14" in text or "CAPÍTULO 14" in text or "Capitulo 14" in text:
                print(f"--- Found Chapter 14 on Page {i+1} ---")
                print(text[:1000])
            if "Capítulo 13" in text or "CAPÍTULO 13" in text:
                print(f"--- Found Chapter 13 on Page {i+1} ---")
        doc.close()
    elif HAS_PYPDF2:
        print("Using PyPDF2...")
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(len(reader.pages)):
                text = reader.pages[i].extract_text()
                if text and ("Capítulo 14" in text or "CAPÍTULO 14" in text or "Capitulo 14" in text):
                    print(f"--- Found Chapter 14 on Page {i+1} ---")
                    print(text[:1000])
    else:
        print("No PDF library found.")

if __name__ == "__main__":
    search_chapters()
