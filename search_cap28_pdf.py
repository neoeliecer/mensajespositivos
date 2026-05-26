import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total pages: {len(reader.pages)}")
        # Look for "Capítulo 28" in the entire document text (it's small enough to check quickly)
        for i in range(len(reader.pages)):
            page_text = reader.pages[i].extract_text()
            if page_text and "capítulo 28" in page_text.lower():
                print(f"Found 'Capítulo 28' on page {i+1}")
                print(page_text[:500])
except Exception as e:
    print(f"Error: {e}")
