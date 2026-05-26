import PyPDF2
import sys

if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total pages: {len(reader.pages)}")
        # Check first 20 pages for TOC
        for i in range(min(20, len(reader.pages))):
            page_text = reader.pages[i].extract_text()
            if page_text:
                print(f"\n--- PÁGINA {i+1} ---")
                print(page_text)
except Exception as e:
    print(f"Error: {e}")
