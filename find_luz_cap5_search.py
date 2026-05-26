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
        
        for i in range(35, 70):
            text = reader.pages[i].extract_text()
            if "Capítulo 5" in text or "Capitulo 5" in text or "CAPÍTULO 5" in text or "CAPITULO 5" in text or "5." in text.split('\n')[0]:
                print(f"PÁGINA {i+1}:\n{text[:500]}")
                print("-" * 40)
            if "Capítulo 4" in text or "Capitulo 4" in text or "CAPÍTULO 4" in text or "CAPITULO 4" in text:
                print(f"PÁGINA {i+1} (Ch4):\n{text[:500]}")
                print("-" * 40)
            if "Capítulo 6" in text or "Capitulo 6" in text or "CAPÍTULO 6" in text or "CAPITULO 6" in text:
                print(f"PÁGINA {i+1} (Ch6):\n{text[:500]}")
                print("-" * 40)

except Exception as e:
    print(f"Error: {e}")
