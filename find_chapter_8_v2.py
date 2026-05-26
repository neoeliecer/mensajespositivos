import PyPDF2
import os
import sys

# Set encoding to utf-8 for console output
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_8_v2():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Chapter 7 was index 30-50.
            # Let's search from index 45 to 60
            for i in range(45, 60):
                if i >= len(reader.pages): break
                page_text = reader.pages[i].extract_text()
                if "Capítulo 8" in page_text or "CAPÍTULO 8" in page_text:
                    print(f"Found Chapter 8 on page {i+1} (index {i})")
                    print(f"Context: {page_text[:200]}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_8_v2()
