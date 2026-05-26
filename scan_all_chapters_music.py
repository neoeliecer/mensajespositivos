import PyPDF2
import os
import re

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def scan_all_chapters():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if not text:
                    continue
                
                # Search for "Capítulo X" patterns
                match = re.search(r'(Cap[ií]tulo\s+(\d+)|CAPÍTULO\s+(\d+))', text)
                if match:
                    chap_num = match.group(2) or match.group(3)
                    clean_text = text[:100].replace('\n', ' ')
                    print(f"Page {i+1}: Chapter {chap_num}")
                    print(f"  Snippet: {clean_text}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    scan_all_chapters()
