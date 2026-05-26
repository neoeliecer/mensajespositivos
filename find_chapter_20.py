
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
search_terms = ["20. ", "Capítulo 20", "20."]

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Search from page 365 (start of Ch 19) onwards
        for i in range(364, len(reader.pages)):
            text = reader.pages[i].extract_text()
            for term in search_terms:
                if term in text: # strict check
                    # Check if it looks like a title (e.g. at start of page or short line)
                    lines = text.split('\n')
                    for line in lines[:5]: # check first 5 lines
                        if term in line:
                            print(f"Potential start of Chapter 20 on page {i + 1} (Index {i})")
                            print(f"Line content: {line}")
                            print("-" * 20)

except Exception as e:
    print(f"Error: {e}")
