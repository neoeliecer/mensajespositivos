import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
output_path = r"C:\Users\neo\Documents\agente\mensajes positivos\extracto_manos_cap3.txt"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        for i in range(10, 14): # pages 11 to 14
            full_text += reader.pages[i].extract_text() + "\n"
        
        # Only keep from "Capítulo 3" to "Revisión del capítulo 3"
        start_idx = full_text.find("Capítulo 3")
        end_idx = full_text.find("Revisión del capítulo 3", start_idx)
        if start_idx != -1 and end_idx != -1:
            chapter_text = full_text[start_idx:end_idx].strip()
        else:
            chapter_text = full_text.strip()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(chapter_text)
        print(f"Extraction saved to {output_path}")

except Exception as e:
    print(f"Error: {e}")
