
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_20.txt"

# Chapter 20: Pages 372 to 376 (indices 371 to 375)
start_page_index = 371
end_page_index = 375

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        
        print(f"Extracting Chapter 20 (pages {start_page_index + 1}-{end_page_index + 1})...")
        
        for i in range(start_page_index, end_page_index + 1):
            if i < len(reader.pages):
                text = reader.pages[i].extract_text()
                full_text += text + "\n"
            else:
                print(f"Warning: Page index {i} is out of range.")
            
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_text)
            
        print(f"Saved {len(full_text)} characters to {output_path}")

except Exception as e:
    print(f"Error: {e}")
