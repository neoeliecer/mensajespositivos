import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_7.txt"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        start_page = 174  # Based on previous finding (Page 175)
        end_page = num_pages
        
        # Look for end of chapter
        for i in range(start_page + 1, min(start_page + 50, num_pages)):
            page = reader.pages[i]
            text = page.extract_text()
            if "8." in text[:50] or "tema 8" in text.lower() or "capítulo 8" in text.lower():
                print(f"Found next chapter on page {i+1}")
                end_page = i
                break
        
        print(f"Extracting pages {start_page + 1} to {end_page}")
        
        full_text = ""
        for i in range(start_page, end_page):
            text = reader.pages[i].extract_text()
            full_text += text + "\n"
            
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(full_text)
            
        print(f"Saved to {output_path}")

except Exception as e:
    print(f"Error: {e}")
