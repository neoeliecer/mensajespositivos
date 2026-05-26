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
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            # Extract first 20 pages to look for TOC
            with open("music_book_head_pages.txt", "w", encoding="utf-8") as out:
                for i in range(min(20, num_pages)):
                    text = reader.pages[i].extract_text()
                    out.write(f"\n--- PAGE {i+1} ---\n")
                    out.write(text if text else "[No text found on this page]")
            
            print("Extracted first 20 pages to music_book_head_pages.txt")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_toc()
