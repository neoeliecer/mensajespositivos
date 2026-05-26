import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\El placebo eres tú - Joe Dispenza.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    
    start_page = -1
    
    for i in range(140, 200):
        text = reader.pages[i].extract_text()
        
        # Chapter 5 starts around 147 - "Cómo los pensamientos cambian el cerebro y el cuerpo"
        if start_page == -1 and "5\n" in text and "cambian" in text.lower() and "cuerpo" in text.lower():
            start_page = i
            break

    if start_page != -1:
        end_page = min(start_page + 25, num_pages)
        print(f"Extraction from page {start_page} to {end_page}")
        with open("extracto_placebo_cap5.txt", "w", encoding="utf-8") as out:
            for i in range(start_page, end_page):
                out.write(reader.pages[i].extract_text() + "\n")
        print("Extract saved to extracto_placebo_cap5.txt")
    else:
        print("Chapter 5 not found.")
