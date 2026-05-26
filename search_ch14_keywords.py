import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def search_keywords():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(len(reader.pages)):
                text = reader.pages[i].extract_text()
                if text and ("Curación" in text or "color" in text.lower()):
                    if "Capítulo" in text or "CAPÍTULO" in text:
                        print(f"--- Possible Chapter Heading on Page {i+1} ---")
                        print(text[:500])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_keywords()
