import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def list_chapters():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Searching {num_pages} pages for chapters...")
            
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if not text:
                    continue
                
                lines = text.split('\n')
                for line in lines:
                    low_line = line.lower()
                    if "capítulo" in low_line or "capitulo" in low_line:
                        print(f"Page {i+1}: {line.strip()}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_chapters()
