import PyPDF2
import os
import re

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_musica_capitulo_12.txt"

def extract_chapter_12():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            start_page = -1
            end_page = -1
            
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if not text:
                    continue
                # Look for chapter 12 markers
                if re.search(r'(Cap[ií]tulo\s+12|CAPÍTULO\s+12|Cap\.\s*12)', text):
                    if start_page == -1:
                        start_page = i
                        print(f"Found Chapter 12 start on page {i+1}")
                        print(f"  Preview: {text[:200]}")
                
                # Look for chapter 13 to know where 12 ends
                if start_page != -1 and end_page == -1:
                    if re.search(r'(Cap[ií]tulo\s+13|CAPÍTULO\s+13|Cap\.\s*13)', text):
                        end_page = i
                        print(f"Found Chapter 13 start on page {i+1}")
                        break
            
            if start_page == -1:
                print("Could not find Chapter 12. Trying broader search...")
                # Try to find by scanning nearby pages after chapter 11
                for i in range(num_pages):
                    text = reader.pages[i].extract_text()
                    if text:
                        print(f"Page {i+1}: {text[:100]}")
                return
            
            if end_page == -1:
                end_page = min(start_page + 20, num_pages)
                print(f"No Chapter 13 found, using pages {start_page+1} to {end_page}")
            
            content = ""
            for i in range(start_page, end_page):
                content += reader.pages[i].extract_text() + "\n"
            
            with open(output_path, 'w', encoding='utf-8') as out:
                out.write(content)
            
            print(f"Extracted Chapter 12 ({end_page - start_page} pages) to {output_path}")
                    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    extract_chapter_12()
