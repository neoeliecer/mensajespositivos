import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def find_chapter_15():
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
                
                # Search for Chapter 14 title
                if "El Poder del Color y el Sonido" in text or "PODER DEL COLOR" in text.upper():
                    print(f"--- Found Chapter 14 on Page {i+1} ---")
                    # Peek at next 40 pages to find Chapter 15
                    for j in range(i+1, min(i+40, num_pages)):
                        next_text = reader.pages[j].extract_text()
                        if not next_text: continue
                        if "Capítulo" in next_text or "CAPÍTULO" in next_text or "Capitulo" in next_text:
                             print(f"--- Possible Chapter 15 found on Page {j+1} ---")
                             print(next_text[:1000])
                             return
                    break
            print("Chapter 14 not found in text.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_15()
