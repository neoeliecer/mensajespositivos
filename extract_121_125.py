import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def extract_five_pages():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(120, 126):
                page = reader.pages[i]
                text = page.extract_text()
                print(f"--- PAGE {i+1} ---")
                if text:
                    print(text[:500]) # First 500 chars
                else:
                    print("[No text found]")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_five_pages()
