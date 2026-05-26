import PyPDF2

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def inspect_pdf():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            for i in range(min(40, num_pages)):
                page = reader.pages[i]
                text = page.extract_text()
                if text and text.strip():
                    print(f"\n--- Page {i+1} ---")
                    print(text[:500])

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_pdf()
