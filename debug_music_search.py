import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def find_chapter_14_and_15():
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
                if not text:
                    continue
                
                # Check for "Color y el Sonido" (Chapter 14)
                if "Color y el Sonido" in text:
                    print(f"--- Found mention of 'Color y el Sonido' on Page {i+1} ---")
                    print(text[:400])
                
                # Check for "Capítulo" followed by any number
                if "Capítulo" in text or "CAPÍTULO" in text:
                    print(f"--- Found 'Capítulo' on Page {i+1} ---")
                    print(text[:200])

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_14_and_15()
