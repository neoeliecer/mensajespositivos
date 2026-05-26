import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_3.txt"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        # Pages 92 to 127 (0-indexed: 91 to 126)
        for i in range(91, 127):
            text += f"--- Page {i+1} ---\n"
            text += reader.pages[i].extract_text() + "\n"
        
        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.write(text)
        print(f"Sucessfully extracted Chapter 3 to {output_path}")

except Exception as e:
    print(f"Error: {e}")
