import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
start_page = 8
end_page = 14  # exclusive

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    with open("extracto_manos_cap2.txt", "w", encoding="utf-8") as out:
        for i in range(start_page, end_page):
            text = reader.pages[i].extract_text()
            if text:
                out.write(text + "\n")
                
print(f"Extraction from page {start_page} to {end_page} completed.")
