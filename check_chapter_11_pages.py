import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Check suspected start of Chapter 11
        start_index = 244
        print(f"--- Page {start_index + 1} (Index {start_index}) ---")
        print(reader.pages[start_index].extract_text()[:500])
        print("--------------------------------------------------\n")

        # Search for Chapter 12 to determine end
        print("Searching for Chapter 12...")
        for i in range(start_index, start_index + 30): # Look ahead 30 pages
            text = reader.pages[i].extract_text()
            if "Capítulo 12" in text or "Capítulo XII" in text or "12. " in text:
                print(f"Found possible Chapter 12 on Page {i+1} (Index {i})")
                print(text[:200])
                break

except Exception as e:
    print(f"Error: {e}")
