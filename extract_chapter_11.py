import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_11.txt"

# Chapter 11: Pages 245 to 272 (indices 244 to 271)
start_page_index = 244
end_page_index = 271

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        
        print(f"Extracting Chapter 11 (pages {start_page_index + 1}-{end_page_index + 1})...")
        
        for i in range(start_page_index, end_page_index + 1):
            text = reader.pages[i].extract_text()
            full_text += text + "\n"
            
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_text)
            
        print(f"Saved {len(full_text)} characters to {output_path}")

except Exception as e:
    print(f"Error: {e}")
