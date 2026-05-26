import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        start_page = -1
        for i in range(num_pages):
            page = reader.pages[i]
            text = page.extract_text()
            # The title of chapter 2 is "Breve historia sobre el placebo"
            if "Breve historia sobre el placebo" in text or "BREVE HISTORIA SOBRE EL PLACEBO" in text or "Breve historia" in text:
                print(f"Found match on page {i+1}")
                if start_page == -1 and i > 20: # skip TOC
                    start_page = i
        
        if start_page != -1:
            with open("texto_placebo_cap2.txt", "w", encoding="utf-8") as out:
                for i in range(start_page, min(start_page + 25, num_pages)):
                    out.write(f"--- Page {i+1} ---\n")
                    out.write(reader.pages[i].extract_text())
                    out.write("\n")
            print("Extracted to texto_placebo_cap2.txt")
        else:
            print("Chapter 2 not found.")

except Exception as e:
    print(f"Error: {e}")
