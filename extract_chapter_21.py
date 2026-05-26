
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_21.txt"

# Chapter 21: Pages 381 to 391 (indices 380 to 390)
start_page_index = 380
end_page_index = 390

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        
        print(f"Extracting Chapter 21 (pages {start_page_index + 1}-{end_page_index + 1})...")
        
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
