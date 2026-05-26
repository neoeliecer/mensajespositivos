import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total pages: {len(reader.pages)}")
        # Peek at the first 5 pages
        for i in range(min(5, len(reader.pages))):
            page_text = reader.pages[i].extract_text()
            print(f"\n--- PÁGINA {i+1} ---")
            print(page_text[:500])
except Exception as e:
    print(f"Error: {e}")
