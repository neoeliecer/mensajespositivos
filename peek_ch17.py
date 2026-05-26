import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def peek_pages():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Check 30 pages starting from page 121 (index 120)
            for i in range(120, 150):
                text = reader.pages[i].extract_text()
                if not text: continue
                lines = text.split('\n')
                # Check first 5 lines for chapter headings
                for line in lines[:5]:
                    if "CAPÍTULO 17" in line.upper() or "CAPITULO 17" in line.upper():
                        print(f"--- CHAPTER 17 START FOUND ON PAGE {i+1} ---")
                        print(line)
                    if "CAPÍTULO 18" in line.upper() or "CAPITULO 18" in line.upper():
                        print(f"--- CHAPTER 18 START FOUND ON PAGE {i+1} ---")
                        print(line)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    peek_pages()
