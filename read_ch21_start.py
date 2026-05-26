import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for i in [155, 156, 157, 158, 159, 160]:
        print(f"\n--- PAGE {i+1} ---\n")
        print(reader.pages[i].extract_text())
