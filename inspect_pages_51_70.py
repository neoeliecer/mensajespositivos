import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def inspect_pages():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(51, 70):
                page_text = reader.pages[i].extract_text()
                print(f"--- Page {i+1} (index {i}) ---")
                print(page_text[:150].replace("\n", " "))
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_pages()
