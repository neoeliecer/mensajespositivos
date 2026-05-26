import PyPDF2
import os
import re

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def search_cap_9():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(50, 100): # Search around where we expect it
                page_text = reader.pages[i].extract_text()
                if re.search(r"Cap[íi]tulo\s+9", page_text, re.IGNORECASE):
                    print(f"Match found on page {i+1} (index {i})")
                    print(f"Context: {page_text[:400]}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_cap_9()
