import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\El placebo eres tú - Joe Dispenza.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    
    start_page = 164
    
    # Let's find end_page by looking for chapter 7
    end_page = start_page + 25
    for i in range(start_page + 1, num_pages):
        text = reader.pages[i].extract_text()
        if "7" in text and "Capítulo" in text or "\n7\n" in text or "7 \n" in text or text.strip().startswith("7\n"):
            end_page = i
            break
            
    print(f"Extraction from page {start_page} to {end_page}")
    with open("extracto_placebo_cap6.txt", "w", encoding="utf-8") as out:
        for i in range(start_page, end_page):
            out.write(reader.pages[i].extract_text() + "\n")
    print("Extract saved to extracto_placebo_cap6.txt")
