import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def main():
    if not os.path.exists(pdf_path):
        print("PDF not found.")
        return
        
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            # Since Chapter 9 was "Palabras de Poder", and Chapter 11 is "Instrumentos",
            # Chapter 10 should be in between.
            # Let's search from page 50 to 180.
            for i in range(50, 180):
                text = reader.pages[i].extract_text()
                if not text:
                    continue
                text_upper = text.upper()
                if "CAPÍTULO 10" in text_upper or "CAPITULO 10" in text_upper:
                    print(f"--- Page {i+1} ---")
                    print(text[:1000])
                if "CAPÍTULO 11" in text_upper or "CAPITULO 11" in text_upper:
                    print(f"--- Page {i+1} (Chapter 11) ---")
                    print(text[:1000])
                if "INSTRUMENTO" in text_upper and ("CAPÍTULO" in text_upper or "CAPITULO" in text_upper):
                    print(f"--- Page {i+1} (Potential Instrument Chapter) ---")
                    print(text[:1000])

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
