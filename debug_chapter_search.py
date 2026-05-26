import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        print("--- Searching for variants of Chapter 7 ---")
        for i in range(len(reader.pages)):
            text = reader.pages[i].extract_text()
            # Check for various formats
            if "Capítulo 7" in text or "CAPÍTULO 7" in text or "Capítulo VII" in text or "CAPÍTULO VII" in text or "SÉPTIMO" in text.upper():
                print(f"Match on page {i+1}: {text[:50]}...")
            
            # Also check for Chapter 6 to see if we can deduce from there
            if "Capítulo 6" in text or "CAPÍTULO 6" in text:
                 print(f"Reference to Chapter 6 on page {i+1}")

except Exception as e:
    print(f"Error: {e}")
