
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
search_terms = ["Capítulo 19", "Abrazar el dolor", "19. Abrazar el dolor"]

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total pages: {len(reader.pages)}")
        
        for i in range(len(reader.pages)):
            text = reader.pages[i].extract_text()
            for term in search_terms:
                if term.lower() in text.lower():
                    # Clean text for printing
                    clean_text = text[:200].replace('\n', ' ')
                    print(f"Found '{term}' on page {i + 1} (Index {i})")
                    print(f"Content snippet: {clean_text}...")
                    print("-" * 20)

except Exception as e:
    print(f"Error: {e}")
