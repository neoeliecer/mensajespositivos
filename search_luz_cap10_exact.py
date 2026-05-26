import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

def search_chapter():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(100, 150):
            text = reader.pages[i].extract_text()
            if text and ("Capítulo 10" in text or "CAPÍTULO 10" in text or "Capitulo 10" in text or "CAPITULO 10" in text):
                print(f"Found match on page {i+1}")
                print(text[:200])
                return

if __name__ == "__main__":
    search_chapter()
