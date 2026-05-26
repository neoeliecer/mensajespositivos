import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_16():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(110, len(reader.pages)): # Start from after Chapter 15
                page_text = reader.pages[i].extract_text()
                if page_text and ("Capítulo 16" in page_text or "CAPÍTULO 16" in page_text or "Capitulo 16" in page_text):
                    print(f"Chapter 16 found on page {i+1}")
                    # Peek next page to see title
                    print(f"Page {i+1} text snippet: {page_text[:200]}")
                    return i
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_16()
