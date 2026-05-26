import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        # Start searching from where Chapter 6 ended (approx page 170)
        for i in range(170, min(300, num_pages)):
            page = reader.pages[i]
            text = page.extract_text()
            # Normalize text for search
            lower_text = text.lower()
            
            # Check for possible titles
            if "miedo bloquea" in lower_text or "tema 7" in lower_text or "capítulo 7" in lower_text or "capítulo vii" in lower_text:
                print(f"Possible Match on Page {i+1}:")
                print(text[:200]) # Print first 200 chars
                print("-" * 20)

except Exception as e:
    print(f"Error: {e}")
