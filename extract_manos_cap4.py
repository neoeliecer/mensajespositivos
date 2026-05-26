import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
output_path = r"C:\Users\neo\Documents\agente\mensajes positivos\extracto_manos_cap4.txt"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        for i in range(15, 23): # pages 16 to 23
            full_text += reader.pages[i].extract_text() + "\n"
        
        # Only keep from "Capítulo 4" to "Revisión del capítulo" or early Chapter 5
        start_idx = full_text.find("Capítulo 4")
        end_idx1 = full_text.find("Revisión del capítulo 4", start_idx)
        end_idx2 = full_text.find("Capítulo 5", start_idx)
        
        end_idx = end_idx1 if end_idx1 != -1 else end_idx2
        
        if start_idx != -1 and end_idx != -1:
            chapter_text = full_text[start_idx:end_idx].strip()
        elif start_idx != -1:
            chapter_text = full_text[start_idx:].strip()
        else:
            chapter_text = full_text.strip()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(chapter_text)
        print(f"Extraction saved to {output_path}")

except Exception as e:
    print(f"Error: {e}")
