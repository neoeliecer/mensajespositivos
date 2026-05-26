import PyPDF2
import sys

# Set encoding for Windows stdout
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total pages: {len(reader.pages)}")
        # Check first 20 pages for TOC or Index
        for i in range(15):
            page_text = reader.pages[i].extract_text()
            if page_text:
                print(f"\n--- PAGE {i+1} ---")
                print(page_text)
except Exception as e:
    print(f"Error: {e}")
