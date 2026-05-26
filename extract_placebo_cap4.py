import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\El placebo eres tú - Joe Dispenza.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    
    start_page = -1
    end_page = -1
    
    for i in range(120, 200):
        text = reader.pages[i].extract_text()
        
        # Chapter 4 starts around 130
        if start_page == -1 and "El efecto placebo en el cuerpo" in text:
            start_page = i
        
        # Look for Chapter 5 "Cómo los pensamientos cambian" or just "5\n" or "Capítulo 5"
        if start_page != -1 and i > start_page + 10:
            if re.search(r'\b5\b', text) and "actitud" in text.lower(): # Just a guess, let's just grab 35 pages
                pass

    if start_page != -1:
        end_page = min(start_page + 28, num_pages) # Typically a chapter is ~25 pages
        print(f"Extraction from page {start_page} to {end_page}")
        with open("extracto_placebo_cap4.txt", "w", encoding="utf-8") as out:
            for i in range(start_page, end_page):
                out.write(reader.pages[i].extract_text() + "\n")
        print("Extract saved to extracto_placebo_cap4.txt")
    else:
        print("Chapter 4 not found.")
