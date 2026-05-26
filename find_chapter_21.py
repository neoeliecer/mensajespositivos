
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
search_terms = ["21. ", "Capítulo 21", "El deporte"]

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Search from page 370 (approx end of Ch 20)
        for i in range(370, min(400, len(reader.pages))):
            text = reader.pages[i].extract_text()
            # print(f"Checking page {i+1}...") # Debug
            for term in search_terms:
                if term in text:
                    lines = text.split('\n')
                    # check first 10 lines to be safe
                    for line in lines[:10]: 
                        if term in line:
                            print(f"Potential start of Chapter 21 on page {i + 1} (Index {i})")
                            print(f"Line content: {line}")
                            print("-" * 20)

except Exception as e:
    print(f"Error: {e}")
