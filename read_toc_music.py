import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def read_toc():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Read first 15 pages for TOC
            for i in range(15):
                text = reader.pages[i].extract_text()
                print(f"--- Page {i+1} ---")
                print(text)
                    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_toc()
