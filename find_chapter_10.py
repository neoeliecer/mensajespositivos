import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")
        
        # Search range based on Chapter 9 (approx 220+)
        for i in range(220, min(270, num_pages)):
            text = reader.pages[i].extract_text()
            # Loose match for Chapter 10 title
            if "10" in text and ("inflamado" in text.lower() or "cerebro" in text.lower()):
                print(f"--- Page {i+1} ---")
                print(text[:200].replace('\n', ' '))
                print("----------------")
            elif "Capítulo 10" in text or "CAPÍTULO 10" in text:
                 print(f"--- Page {i+1} (Explicit Chapter) ---")
                 print(text[:200].replace('\n', ' '))
                 print("----------------")

        # Also look for end (Chapter 11)
        for i in range(240, min(290, num_pages)):
             text = reader.pages[i].extract_text()
             if "11" in text and ("capítulo" in text.lower() or "dopamina" in text.lower() or "atención" in text.lower()): # hypothetical keywords
                  print(f"--- Page {i+1} (Potential Subseq Chapter) ---")
                  print(text[:200].replace('\n', ' '))
                  print("----------------")

except Exception as e:
    print(f"Error: {e}")
