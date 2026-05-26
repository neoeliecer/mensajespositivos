import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    # Peek at pages around 58 to find Chapter 6
    for i in range(57, 75):
        text = reader.pages[i].extract_text()
        if "Capítulo" in text or "CAPÍTULO" in text:
            print(f"--- PAGE {i+1} ---")
            print(text[:200])
