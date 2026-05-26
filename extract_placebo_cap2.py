import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\El placebo eres tú - Joe Dispenza.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    
    start_page = -1
    end_page = -1
    
    # Chapter 2 title: "2. Breve historia sobre el placebo" or "2  Breve historia"
    # Chapter 3 title: "3. El efecto placebo en el cerebro"
    for i in range(num_pages):
        text = reader.pages[i].extract_text()
        if start_page == -1 and ("Breve historia sobre el placebo" in text or "Breve historia" in text):
            # Make sure it's not the TOC (TOC is at the beginning)
            if i > 20: 
                start_page = i
        elif start_page != -1 and "El efecto placebo en el cerebro" in text:
            end_page = i
            break
            
    if start_page != -1:
        if end_page == -1: end_page = min(start_page + 20, num_pages)
        print(f"Extraction from page {start_page} to {end_page}")
        with open("extracto_placebo_cap2.txt", "w", encoding="utf-8") as out:
            for i in range(start_page, end_page):
                out.write(reader.pages[i].extract_text() + "\n")
        print("Extract saved to extracto_placebo_cap2.txt")
    else:
        print("Chapter 2 not found.")
