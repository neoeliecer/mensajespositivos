import PyPDF2
pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"
try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and ("VOCAL" in text.upper() or "MANTRAS" in text.upper()):
                snippet = text[:100].replace('\n', ' ')
                print(f"Page {i+1}: {snippet}")
except Exception as e:
    print(f"Error: {e}")
