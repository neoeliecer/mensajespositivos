import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def extract_pages(start, end):
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            content = ""
            for i in range(start-1, min(end, num_pages)):
                text = reader.pages[i].extract_text()
                content += f"\n--- Page {i+1} ---\n"
                content += text if text else "[No text]"
            
            with open("music_toc_peek.txt", "w", encoding="utf-8") as out:
                out.write(content)
            print(f"Extracted pages {start} to {end} to music_toc_peek.txt")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_pages(1, 30)
