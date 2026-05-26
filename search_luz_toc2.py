import PyPDF2
import sys

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    with open('toc_utf8.txt', 'w', encoding='utf-8') as out:
        for i in range(2, 6):
            text = reader.pages[i].extract_text()
            out.write(text)
