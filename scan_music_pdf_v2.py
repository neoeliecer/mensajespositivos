import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def scan_chapters():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Scanning {num_pages} pages...")
            
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if text:
                    lines = text.split('\n')
                    for line in lines:
                        l_upper = line.upper().strip()
                        if "CAPÍTULO" in l_upper or "CAPITULO" in l_upper or (len(l_upper) < 30 and ("CAP." in l_upper)):
                             print(f"Page {i+1}: {line.strip()}")
                             break # Only one chapter per page usually

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scan_chapters()
