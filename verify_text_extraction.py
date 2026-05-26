import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def search_text(query):
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Searching for '{query}' in {num_pages} pages...")
            
            for i in range(num_pages):
                text = reader.pages[i].extract_text()
                if query.lower() in text.lower():
                    print(f"--- Found '{query}' on Page {i+1} ---")
                    print(text[:1000])
                    return i+1
            
            print(f"'{query}' not found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Title of chapter 9
    search_text("Entonación")
    # Title of chapter 10
    search_text("Narración Mágica")
