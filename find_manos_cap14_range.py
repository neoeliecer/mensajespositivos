import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_14():
    if not os.path.exists(pdf_path):
        print(f"Error: PDF not found at {pdf_path}")
        return

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        start_page = 96  # Index 95 was the last page of Chapter 13
        
        for i in range(start_page, start_page + 20): # Look ahead 20 pages
            if i < len(reader.pages):
                text = reader.pages[i].extract_text()
                if "CAPÍTULO 14" in text.upper() or "CAPITULO 14" in text.upper():
                    print(f"Found Chapter 14 start at page {i+1} (index {i})")
                    # Print a bit of text to confirm
                    print(text[:200])
                if "CAPÍTULO 15" in text.upper() or "CAPITULO 15" in text.upper():
                    print(f"Found Chapter 15 start at page {i+1} (index {i})")
                    break

if __name__ == "__main__":
    find_chapter_14()
