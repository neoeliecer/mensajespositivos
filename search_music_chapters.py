import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def find_chapters():
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
                # Case insensitive search
                if "capítulo 11" in text.lower() or "capitulo 11" in text.lower():
                    print(f"--- Found 'Capítulo 11' on Page {i+1} ---")
                    print(text[:500])
                    # Keep searching to see if it appears again (e.g. in TOC and header)
                
                if "capítulo 12" in text.lower() or "capitulo 12" in text.lower():
                    print(f"--- Found 'Capítulo 12' on Page {i+1} ---")
                    print(text[:500])

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapters()
