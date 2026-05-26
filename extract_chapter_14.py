import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

def extract_chapter_14():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        start_page = -1
        end_page = -1
        
        # Find Chapter 14
        # Start searching from page 170 to avoid TOC
        for i in range(170, len(reader.pages)):
            text = reader.pages[i].extract_text()
            if "14. Cómo nos manipulan" in text or "CÓMO NOS MANIPULAN" in text:
                 # Check if it's the chapter title page (usually has less text or specific formatting, but simple check first)
                 if start_page == -1:
                     start_page = i
                     print(f"Found Chapter 14 start at page {i+1}")
            
            if start_page != -1 and i > start_page and ("15." in text or "Capítulo 15" in text or "CAPÍTULO 15" in text):
                end_page = i
                print(f"Found Chapter 15 start at page {i+1}, stopping.")
                break
        
        if end_page == -1:
            end_page = start_page + 10 # Fallback if next chapter not found, read 10 pages

        if start_page != -1:
            full_text = ""
            for i in range(start_page, end_page):
                full_text += reader.pages[i].extract_text() + "\n"
            
            with open("texto_capitulo_14.txt", "w", encoding="utf-8") as f:
                f.write(full_text)
            print("Successfully extracted Chapter 14 text to texto_capitulo_14.txt")
        else:
            print("Chapter 14 not found.")

if __name__ == "__main__":
    extract_chapter_14()
