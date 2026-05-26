import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def find_chapter_14():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Searching {num_pages} pages...")
            
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if text and ("capítulo 14" in text.lower() or "capitulo 14" in text.lower()):
                    print(f"--- Found 'Capítulo 14' on Page {i+1} ---")
                    print(text[:500])
                    
                if text and ("capítulo 15" in text.lower() or "capitulo 15" in text.lower()):
                    print(f"--- Found 'Capítulo 15' on Page {i+1} ---")
                    print(text[:500])

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_14()
