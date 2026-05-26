import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

def search_chapter(chapter_num):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total pages: {len(reader.pages)}")
        
        for i in range(70, min(150, len(reader.pages))): # Start searching around page 70
            text = reader.pages[i].extract_text()
            if text and (f"Capítulo {chapter_num}" in text or f"CAPÍTULO {chapter_num}" in text or f"Capitulo {chapter_num}" in text or f"CAPITULO {chapter_num}" in text):
                print(f"Found match on page {i+1}")
                print(text[:200])
                print("-" * 40)

if __name__ == "__main__":
    search_chapter(10)
