
import PyPDF2
import os

def extract_chapter_1(pdf_path, output_path):
    print(f"Opening {pdf_path}...")
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            start_page = -1
            end_page = -1
            
            # Buscamos el inicio del capítulo 1
            # Basado en otros libros, el capítulo 1 suele estar después de la intro/prefacio
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text and ("CAPÍTULO 1" in text.upper() or "CAPITULO 1" in text.upper()):
                    print(f"Found Chapter 1 start on page {page_num + 1}")
                    start_page = page_num
                    break
            
            if start_page == -1:
                print("Could not find Chapter 1 start. Checking pages 10-30...")
                # Intento manual si el texto no es claro (a veces son imágenes con texto)
                start_page = 12 # Ajuste manual probable para este tipo de PDFs
            
            # Buscamos el inicio del capítulo 2 para saber dónde termina el 1
            for page_num in range(start_page + 1, num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text and ("CAPÍTULO 2" in text.upper() or "CAPITULO 2" in text.upper()):
                    print(f"Found Chapter 2 start on page {page_num + 1}")
                    end_page = page_num
                    break
            
            if end_page == -1:
                end_page = start_page + 15 # Valor por defecto si no se encuentra
            
            print(f"Extracting pages {start_page + 1} to {end_page}...")
            
            full_text = ""
            for page_num in range(start_page, end_page):
                page = reader.pages[page_num]
                full_text += page.extract_text() + "\n\n"
            
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write(full_text)
            
            print(f"Text saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"
    output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_musica_capitulo_1.txt"
    extract_chapter_1(pdf_path, output_path)
