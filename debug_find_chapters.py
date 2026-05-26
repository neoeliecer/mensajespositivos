import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Brian-Tracy-El-poder-de-confiar-en-ti-mismo.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")
    
    for idx in range(total_pages):
        text = reader.pages[idx].extract_text()
        if not text:
            continue
        
        text_upper = text.upper()
        if "CAPÍTULO" in text_upper or "CAPITULO" in text_upper:
            lines = text.split("\n")
            for line in lines:
                if "CAPÍTULO" in line.upper() or "CAPITULO" in line.upper():
                    print(f"Page {idx + 1}: {line.strip()}")
