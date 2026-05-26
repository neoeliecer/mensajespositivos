import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

# Find where chapters 11 and 12 are based on what we know about chapter 11
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    
    # Scan pages looking for chapter markers - print any page that mentions chapter numbers
    for i in range(num_pages):
        text = reader.pages[i].extract_text()
        if not text:
            continue
        # Look for any chapter-like content
        lower = text.lower()
        if any(x in lower for x in ['capítulo', 'capitulo', 'chapter', 'parte']):
            print(f"=== Page {i+1} ===")
            print(text[:300])
            print()
