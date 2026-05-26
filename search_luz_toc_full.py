import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    with open('toc_full.txt', 'w', encoding='utf-8') as out:
        for i in range(2, 10):
            out.write(f"\n--- Page {i+1} ---\n")
            out.write(reader.pages[i].extract_text())
