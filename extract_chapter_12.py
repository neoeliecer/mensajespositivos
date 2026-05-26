import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_file = "extracto_capitulo_12.txt"

# Page 272 is index 271. Let's extract 15 pages to be safe and check content.
start_page = 271
num_pages_to_extract = 20

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        with open(output_file, "w", encoding="utf-8") as out:
            for i in range(num_pages_to_extract):
                page_index = start_page + i
                if page_index < len(reader.pages):
                     text = reader.pages[page_index].extract_text()
                     out.write(f"--- Page {page_index + 1} ---\n")
                     out.write(text)
                     out.write("\n\n")
    
    print(f"Extracted {num_pages_to_extract} pages to {output_file}")

except Exception as e:
    print(f"Error: {e}")
