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
        # Search between page 77 and 87
        for i in range(76, 88):
            text = reader.pages[i].extract_text()
            print(f"\n--- PÁGINA {i+1} ---")
            print(text[:200]) # First 200 chars

except Exception as e:
    print(f"Error: {e}")
