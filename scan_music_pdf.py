import PyPDF2

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def scan_chapters(pdf_path):
    print(f"Scanning {pdf_path}...")
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    text_upper = text.upper()
                    if "CAPÍTULO" in text_upper or "CAPITULO" in text_upper:
                        lines = text.strip().split('\n')
                        first_line = lines[0] if lines else ""
                        print(f"Page {i+1}: {first_line[:100]}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scan_chapters(pdf_path)
