import PyPDF2
import os
import re

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def find_all_chapters():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Searching {num_pages} pages...")
            
            chapters = []
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if not text:
                    continue
                
                # Search for Chapter patterns
                # Example: "Capítulo 15", "CAPÍTULO XV", "15. Título"
                matches = re.finditer(r'(Cap[ií]tulo\s+(\d+|[IVXLCDM]+))', text, re.IGNORECASE)
                for match in matches:
                    chapters.append((i+1, match.group(0), text[match.start():match.start()+100].replace('\n', ' ')))
            
            if not chapters:
                print("No chapters found using standard patterns. Listing first few lines of each page with text...")
                for i in range(num_pages):
                    text = reader.pages[i].extract_text()
                    if text and text.strip():
                        print(f"Page {i+1}: {text.strip()[:100]}")
                        if i > 20: break # Only first 20 pages with text
            else:
                for page, title, preview in chapters:
                    print(f"Page {page}: {title} - {preview}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_all_chapters()
