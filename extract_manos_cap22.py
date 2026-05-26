import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_manos_cap22.txt"

# Buscamos desde el índice 155 (página 156) hasta el índice 184 (página 185)
start_page = 155
end_page = 184

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for i in range(start_page, end_page + 1):
            if i < len(reader.pages):
                page_text = reader.pages[i].extract_text()
                if page_text:
                    text += f"\n--- PÁGINA {i+1} ---\n"
                    text += page_text
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Texto extraído correctamente en {output_path}")

except Exception as e:
    print(f"Error: {e}")
