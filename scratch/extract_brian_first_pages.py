import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Brian-Tracy-El-poder-de-confiar-en-ti-mismo.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\scratch\brian_pages_1_40.txt"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        total_pages = len(reader.pages)
        print(f"Total pages in book: {total_pages}")
        
        # Extract first 40 pages to find Chapter 1 and the Table of Contents
        end_page = min(40, total_pages)
        for i in range(end_page):
            text = reader.pages[i].extract_text()
            if text:
                full_text += f"\n--- PÁGINA {i+1} ---\n" + text + "\n"
                
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_text)
        print(f"Successfully wrote first {end_page} pages to {output_path}")
except Exception as e:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Error: {str(e)}")
    print(f"Error: {e}")
