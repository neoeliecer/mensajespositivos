import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def read_p1_15():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(15):
                text = reader.pages[i].extract_text()
                print(f"--- Page {i+1} ---")
                print(text if text else "[No text found]")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_p1_15()
