import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

def find_chapter_22():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Searching {num_pages} pages...")
            
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if "Capítulo 22" in text or "Capitulo 22" in text:
                    print(f"--- Found Chapter 22 on Page {i+1} ---")
                    print(text[:500])
                    return
            
            print("Chapter 22 not found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_22()
