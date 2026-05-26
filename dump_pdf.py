import PyPDF2
pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\todo_libro_musica.txt"
try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = []
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                full_text.append(f"--- PAGE {i+1} ---\n{text}")
        with open(output_path, 'w', encoding='utf-8') as out:
            out.write('\n'.join(full_text))
    print(f"Dumped to {output_path}")
except Exception as e:
    print(f"Error: {e}")
