import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_10.txt"

# Chapter 10: Found on Page 235 (index 234)
# Chapter 11: Found on Page 245 (index 244)
start_page_index = 234
end_page_index = 244

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        
        print(f"Extracting pages {start_page_index + 1} to {end_page_index}...")
        
        for i in range(start_page_index, end_page_index):
            text = reader.pages[i].extract_text()
            full_text += text + "\n"
            
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_text)
            
        print(f"Saved {len(full_text)} characters to {output_path}")

except Exception as e:
    print(f"Error: {e}")
