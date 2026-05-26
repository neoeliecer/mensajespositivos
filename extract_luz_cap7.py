import PyPDF2
import sys

# Set encoding for Windows stdout
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_luz_cap7.txt"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        start_page = 69  # Page 70 (0-indexed)
        end_page = 76    # Page 77 (0-indexed)
        
        full_text = ""
        for i in range(start_page, end_page + 1):
            full_text += f"\n--- PÁGINA {i+1} ---\n" + reader.pages[i].extract_text()
        
        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(full_text)
        print(f"Extracted to {output_path}")

except Exception as e:
    print(f"Error: {e}")
