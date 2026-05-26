import PyPDF2

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_musica_capitulo_7.txt"

def extract_music_chapter_7(pdf_path, output_path):
    print(f"Opening {pdf_path}...")
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            start_page = -1
            end_page = -1
            
            # Find Chapter 7
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    text_upper = text.upper()
                    if "CAPÍTULO 7" in text_upper or "CAPITULO 7" in text_upper or "CHAPTER 7" in text_upper:
                        # Check if it's not the TOC (usually TOC is early)
                        if page_num > 10:
                            print(f"Found Chapter 7 start on page {page_num + 1}")
                            start_page = page_num
                            break
            
            if start_page == -1:
                print("Could not find Chapter 7. Checking for Chapter 6 end...")
                # Fallback: search for Chapter 8 if Chapter 7 is hard to find by title
                # But let's look for Chapter 7 first.
                return
            
            # Find Chapter 8 to determine end
            for page_num in range(start_page + 1, num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    text_upper = text.upper()
                    if "CAPÍTULO 8" in text_upper or "CAPITULO 8" in text_upper or "CHAPTER 8" in text_upper:
                        print(f"Found Chapter 8 start on page {page_num + 1}")
                        end_page = page_num
                        break
            
            if end_page == -1:
                end_page = min(start_page + 30, num_pages)
            
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

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_music_chapter_7(pdf_path, output_path)
