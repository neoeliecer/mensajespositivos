import PyPDF2
import sys

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_6.txt"

print(f"Opening PDF: {pdf_path}")
try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Chapter 6 is on pages 156 to 174 (0-indexed: 155 to 173)
        start_page = 155
        end_page = 174
        
        print(f"Extracting pages {start_page + 1} to {end_page}")
        extracted_text = ""
        for i in range(start_page, end_page):
            extracted_text += f"\n--- Page {i+1} ---\n"
            extracted_text += reader.pages[i].extract_text()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(extracted_text)
        print(f"Text saved to {output_path}")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
