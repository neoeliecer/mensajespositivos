import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def find_chapter_15():
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
                if "capítulo 15" in text.lower() or "capitulo 15" in text.lower() or "capítulo xv" in text.lower():
                    print(f"--- Found 'Capítulo 15' on Page {i+1} ---")
                    print(text[:800])
                
                if "capítulo 16" in text.lower() or "capitulo 16" in text.lower() or "capítulo xvi" in text.lower():
                    print(f"--- Found 'Capítulo 16' on Page {i+1} ---")
                    print(text[:800])

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_15()
