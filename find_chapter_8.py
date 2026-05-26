import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_8():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Search from page 1 to 100 to be safe
            for i in range(len(reader.pages)):
                page_text = reader.pages[i].extract_text()
                if "Capítulo 8" in page_text or "CAPÍTULO 8" in page_text:
                    print(f"Found Chapter 8 on page {i+1} (index {i})")
                    print(f"Context: {page_text[:200]}")
                    # return # Don't return, might be in TOC first
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_8()
