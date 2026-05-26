import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def find_chapter_titles():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if not text: continue
                
                if "El Sonido y los Chakras" in text:
                    print(f"--- Found Chapter 13 on Page {i+1} ---")
                    # Peek at next pages to find Chapter 14
                    for j in range(i+1, min(i+30, num_pages)):
                        next_text = reader.pages[j].extract_text()
                        if not next_text: continue
                        if "Capítulo" in next_text or "CAPÍTULO" in next_text:
                            print(f"--- Possible Chapter found on Page {j+1} ---")
                            print(next_text[:500])
                    break
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_titles()
