
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
search_terms = ["Capítulo 22", "22. "] # To find the end of Chapter 21

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Search from page 375 (approx start of Ch 21)
        for i in range(375, min(410, len(reader.pages))):
            text = reader.pages[i].extract_text()
            for term in search_terms:
                if term in text:
                    lines = text.split('\n')
                    for line in lines[:10]: 
                        if term in line:
                            print(f"Potential start of Chapter 22 on page {i + 1} (Index {i})")
                            print(f"Line content: {line}")
                            print("-" * 20)
                            
except Exception as e:
    print(f"Error: {e}")
