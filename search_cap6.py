import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\El placebo eres tú - Joe Dispenza.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for i in range(160, 250):
        text = reader.pages[i].extract_text()
        if text:
            if "Capítulo 6" in text or "\n6\n" in text or "6 \n" in text or text.strip().startswith("6\n"):
                print(f"Page {i}:\n{text[:200]}\n...")
