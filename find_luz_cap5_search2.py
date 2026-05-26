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
        
        for i in range(45, 59):
            text = reader.pages[i].extract_text()
            print(f"PÁGINA {i+1}:\n{text[:150]}")
            print("-" * 40)

except Exception as e:
    print(f"Error: {e}")
