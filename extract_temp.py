import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def extract_chunk():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            full_text = ""
            for i in range(51, 65):
                page_text = reader.pages[i].extract_text()
                full_text += f"\n--- Page {i+1} ---\n"
                full_text += page_text + "\n"
            
            with open("temp_extract.txt", "w", encoding="utf-8") as f:
                f.write(full_text)
            print("Extracted to temp_extract.txt")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_chunk()
