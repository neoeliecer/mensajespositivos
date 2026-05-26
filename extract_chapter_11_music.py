import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_musica_capitulo_11.txt"

def extract_chapter_11():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            start_page = -1
            end_page = -1
            
            # First, find where Chapter 11 starts and where Chapter 12 starts
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if "Capítulo 11" in text or "Capitulo 11" in text or "CAPÍTULO 11" in text:
                    if start_page == -1:
                        start_page = i
                        print(f"Found Chapter 11 start on page {i+1}")
                
                if "Capítulo 12" in text or "Capitulo 12" in text or "CAPÍTULO 12" in text:
                    if start_page != -1 and end_page == -1:
                        end_page = i
                        print(f"Found Chapter 12 start on page {i+1}")
                        break
            
            if start_page == -1:
                print("Could not find Chapter 11")
                return
            
            if end_page == -1:
                end_page = num_pages
            
            content = ""
            for i in range(start_page, end_page):
                content += reader.pages[i].extract_text() + "\n"
            
            with open(output_path, 'w', encoding='utf-8') as out:
                out.write(content)
            
            print(f"Extracted Chapter 11 to {output_path}")
                    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_chapter_11()
