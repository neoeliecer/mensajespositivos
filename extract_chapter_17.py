
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_17.txt"

# Chapter 17: Pages 339 to 357 (indices 338 to 356)
start_page_index = 338
end_page_index = 356

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        
        print(f"Extracting Chapter 17 (pages {start_page_index + 1}-{end_page_index + 1})...")
        
        for i in range(start_page_index, end_page_index + 1):
            text = reader.pages[i].extract_text()
            full_text += text + "\n"
            
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_text)
            
        print(f"Saved {len(full_text)} characters to {output_path}")

except Exception as e:
    print(f"Error: {e}")
