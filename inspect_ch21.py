import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    # Check pages around 155
    start_idx = 155
    end_idx = 175
    
    for i in range(start_idx, end_idx):
        if i >= len(reader.pages): break
        print(f"\n--- PAGE {i+1} ---\n")
        text = reader.pages[i].extract_text()
        if text:
            print(text[:500]) # Solo los primeros 500 caracteres para no saturar
        else:
            print("[No text found on this page]")
