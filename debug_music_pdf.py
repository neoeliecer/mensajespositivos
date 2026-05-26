import PyPDF2

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    num_pages = len(reader.pages)
    print(f"Total pages: {num_pages}")
    
    # Check first few and last few pages for text
    for i in [0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 150, 200]:
        if i < num_pages:
            text = reader.pages[i].extract_text()
            print(f"\n=== Page {i+1} (len={len(text) if text else 0}) ===")
            if text:
                print(repr(text[:200]))
