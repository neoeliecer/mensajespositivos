import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_8.txt"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        # Previous chapter ended around 191. Search around there.
        start_page = -1
        for i in range(190, min(210, num_pages)):
            text = reader.pages[i].extract_text()
            if "8. " in text and "soledad" in text.lower():
                start_page = i
                print(f"Found Chapter 8 start on page {i+1}")
                break
        
        if start_page == -1:
            print("Could not find start of Chapter 8")
            # Fallback based on previous run finding "Found next chapter on page 192"
            start_page = 191
            print(f"Using fallback start page {start_page+1}")

        end_page = num_pages
        # Look for end of chapter (Chapter 9)
        for i in range(start_page + 1, min(start_page + 50, num_pages)):
            page = reader.pages[i]
            text = page.extract_text()
            if "9." in text[:50] or "tema 9" in text.lower() or "capítulo 9" in text.lower():
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
