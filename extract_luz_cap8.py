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
        full_text = ""
        for i in range(76, 86): # Pages 77 to 86
            full_text += f"\n--- PÁGINA {i+1} ---\n" + reader.pages[i].extract_text()
        
        with open("extracto_luz_cap8.txt", "w", encoding="utf-8") as f:
            f.write(full_text)
        print("Extracted to extracto_luz_cap8.txt")

except Exception as e:
    print(f"Error: {e}")
