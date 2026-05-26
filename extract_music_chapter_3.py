import PyPDF2
import os

def extract_music_chapter_3(pdf_path, output_path):
    print(f"Opening {pdf_path}...")
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            start_page = -1
            end_page = -1
            
            # Buscamos el inicio del capítulo 3
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    text_upper = text.upper()
                    if "CAPÍTULO 3" in text_upper or "CAPITULO 3" in text_upper or "CHAPTER 3" in text_upper:
                        print(f"Found Chapter 3 start on page {page_num + 1}")
                        print(f"Page content preview: {text[:200]}")
                        start_page = page_num
                        break
            
            if start_page == -1:
                print("Could not find Chapter 3 automatically. Dumping first 50 pages to check structure...")
                for i in range(min(50, num_pages)):
                    page = reader.pages[i]
                    text = page.extract_text()
                    if text and text.strip():
                        print(f"\n--- Page {i+1} ---")
                        print(text[:300])
                return
            
            # Buscamos el inicio del capítulo 4 para saber dónde termina el 3
            for page_num in range(start_page + 1, num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    text_upper = text.upper()
                    if "CAPÍTULO 4" in text_upper or "CAPITULO 4" in text_upper or "CHAPTER 4" in text_upper:
                        print(f"Found Chapter 4 start on page {page_num + 1}")
                        end_page = page_num
                        break
            
            if end_page == -1:
                end_page = start_page + 20  # Default range if chapter 4 not found
            
            print(f"Extracting pages {start_page + 1} to {end_page}...")
            
            full_text = ""
            for page_num in range(start_page, end_page):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    full_text += f"--- Page {page_num + 1} ---\n{text}\n\n"
            
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write(full_text)
            
            print(f"Text saved to {output_path}")
            print(f"Extracted {len(full_text)} characters")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_musica_capitulo_3.txt"
    extract_music_chapter_3(pdf_path, output_path)
