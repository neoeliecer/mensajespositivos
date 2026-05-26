import PyPDF2

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def find_chapter_4_range():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            start_page = -1
            end_page = -1
            
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    text_upper = text.upper()
                    if start_page == -1 and ("CAPÍTULO 4" in text_upper or "CAPITULO 4" in text_upper):
                        print(f"DEBUG: Found Chapter 4 start on page {page_num + 1}")
                        start_page = page_num
                    
                    if start_page != -1 and ("CAPÍTULO 5" in text_upper or "CAPITULO 5" in text_upper):
                        print(f"DEBUG: Found Chapter 5 start on page {page_num + 1}")
                        end_page = page_num
                        break
            
            if start_page != -1:
                if end_page == -1:
                    end_page = num_pages
                print(f"RESULT: Chapter 4 is from page {start_page + 1} to {end_page}")
            else:
                print("RESULT: Could not find Chapter 4")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_4_range()
