import PyPDF2
import sys
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for i in range(4, 15):
        text = reader.pages[i].extract_text()
        print(f"--- Page {i} ---")
        if text:
            print("\n".join(text.split('\n')[:10]))
