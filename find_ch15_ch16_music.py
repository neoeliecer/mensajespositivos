import PyPDF2
import os
import re

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def find_chapter_15_and_16():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Searching {num_pages} pages...")
            
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if not text:
                    continue
                
                # Check for Chapter 14, 15, 16
                if re.search(r'CAP[IÍ]TULO\s+14', text, re.IGNORECASE):
                    print(f"--- Found Chapter 14 on Page {i+1} ---")
                    print(text[:300])
                
                if re.search(r'CAP[IÍ]TULO\s+15', text, re.IGNORECASE):
                    print(f"--- Found Chapter 15 on Page {i+1} ---")
                    print(text[:300])
                
                if re.search(r'CAP[IÍ]TULO\s+16', text, re.IGNORECASE):
                    print(f"--- Found Chapter 16 on Page {i+1} ---")
                    print(text[:300])

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_15_and_16()
