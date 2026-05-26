import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
output_path = r"C:\Users\neo\Documents\agente\mensajes positivos\extracto_manos_cap5.txt"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        # The chapter starts at index 22 and ends before Capítulo 6 at index 27
        for i in range(22, 27):
            page_text = reader.pages[i].extract_text()
            if page_text:
                full_text += page_text + "\n"
        
        # Clean up text if needed (e.g., specific boundaries)
        # We know it starts with "HISTORIA DE LA INVESTIGACIÓN..."
        # And ends when Capítulo 6 starts.
        
        start_marker = "HISTORIA DE LA INVESTIGACIÓN"
        end_marker = "Capítulo 6"
        
        start_idx = full_text.find(start_marker)
        end_idx = full_text.find(end_marker, start_idx)
        
        if start_idx != -1:
            if end_idx != -1:
                chapter_text = full_text[start_idx:end_idx].strip()
            else:
                chapter_text = full_text[start_idx:].strip()
        else:
            chapter_text = full_text.strip()

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(chapter_text)
        print(f"Extraction saved to {output_path}")

except Exception as e:
    print(f"Error: {e}")
