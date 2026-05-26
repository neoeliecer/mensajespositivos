import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def scan_pages():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(120, 160):
                page = reader.pages[i]
                text = page.extract_text()
                if text:
                    lines = text.strip().split('\n')
                    # Print first 2 non-empty lines
                    first_lines = [l.strip() for l in lines if l.strip()][:2]
                    print(f"Page {i+1}: {first_lines}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scan_pages()
