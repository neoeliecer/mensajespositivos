import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
output_path = r"C:\Users\neo\Documents\agente\mensajes positivos\temp_extract_ch16.txt"

def peek_ch16():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            full_text = ""
            # Range 118 to 130 (Indices 117 to 129)
            for i in range(117, 130): 
                if i < len(reader.pages):
                    page_text = reader.pages[i].extract_text()
                    if page_text:
                        full_text += f"\n--- Página {i+1} ---\n"
                        full_text += page_text + "\n"
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(full_text.strip())
            print(f"Extraction saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    peek_ch16()
