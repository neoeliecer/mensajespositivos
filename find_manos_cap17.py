import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_17():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Start searching from page 120 (index 119) onwards
            for i in range(120, min(150, len(reader.pages))):
                text = reader.pages[i].extract_text()
                if "CAPÍTULO 17" in text.upper() or "CAPITULO 17" in text.upper():
                    print(f"Chapter 17 found on page {i+1}")
                if "CAPÍTULO 18" in text.upper() or "CAPITULO 18" in text.upper():
                    print(f"Chapter 18 found on page {i+1}")
                    break

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_17()
