import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\El placebo eres tú - Joe Dispenza.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for i in range(5, 15):
        print(f"--- Page {i} ---")
        text = reader.pages[i].extract_text()
        print(text)
