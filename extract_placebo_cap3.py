import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\El placebo eres tú - Joe Dispenza.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    
    start_page = -1
    end_page = -1
    
    for i in range(num_pages):
        text = reader.pages[i].extract_text()
        if start_page == -1 and "El efecto placebo en el cerebro" in text:
            if i > 20: 
                start_page = i
        elif start_page != -1 and "El efecto placebo en el cuerpo" in text:
            # Check if this is truly the start of chapter 4 or just a mention inside chapter 3
            # We can just look for "4.  e l efecto placebo en el cuerpo" or similar.
            # actually let's just use a hardcoded distance of 30 pages since it's around page 121.
            if i > start_page + 10:
                end_page = i
                break
            
    if start_page != -1:
        if end_page == -1: end_page = min(start_page + 20, num_pages)
        print(f"Extraction from page {start_page} to {end_page}")
        with open("extracto_placebo_cap3.txt", "w", encoding="utf-8") as out:
            for i in range(start_page, end_page):
                out.write(reader.pages[i].extract_text() + "\n")
        print("Extract saved to extracto_placebo_cap3.txt")
    else:
        print("Chapter 3 not found.")
