import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

# Print page by page content to see the structure around chapters 11 and 12
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    
    # Print all pages briefly to find structure
    for i in range(num_pages):
        text = reader.pages[i].extract_text()
        if text and len(text.strip()) > 10:
            first_line = text.strip().split('\n')[0][:80]
            print(f"Page {i+1:3d}: {first_line}")
