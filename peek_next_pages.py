import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total pages: {len(reader.pages)}")
        for i in range(213, min(230, len(reader.pages))):
            page_text = reader.pages[i].extract_text()
            print(f"\n--- PÁGINA {i} (Humana {i+1}) ---")
            if page_text:
                print(page_text[:500])
            else:
                print("[No text found]")
except Exception as e:
    print(f"Error: {e}")
