import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_17():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Search from page 121 (index 120) to 150
            for i in range(120, min(160, len(reader.pages))):
                text = reader.pages[i].extract_text()
                if not text: continue
                if "Capítulo 17" in text or "CAPÍTULO 17" in text or "Acceso directo a la información" in text:
                    print(f"Chapter 17 start: Page {i + 1}")
                if "Capítulo 18" in text or "CAPÍTULO 18" in text or "Visión interna" in text:
                    print(f"Chapter 18 start: Page {i + 1}")
                    break
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_17()
