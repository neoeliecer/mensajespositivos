import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
output_path = r"C:\Users\neo\Documents\agente\mensajes positivos\extracto_manos_cap9_raw.txt"

def extract_chapter():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            full_text = ""
            for i in range(52, 75):
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
    extract_chapter()
