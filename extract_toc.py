import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total pages: {len(reader.pages)}")
        # Check first 20 pages for TOC
        for i in range(min(20, len(reader.pages))):
            page_text = reader.pages[i].extract_text()
            if "índice" in page_text.lower() or "contenido" in page_text.lower() or "capítulo" in page_text.lower():
                print(f"\n--- PÁGINA {i+1} ---")
                print(page_text)
except Exception as e:
    print(f"Error: {e}")
