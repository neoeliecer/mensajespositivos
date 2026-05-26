/.
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Check pages 390 to 400 (indices)
        for i in range(390, min(400, len(reader.pages))):
            text = reader.pages[i].extract_text()
            lines = text.split('\n')
            print(f"--- Page {i + 1} (Index {i}) ---")
            for line in lines[:5]:
                print(line)
            print("")
            
except Exception as e:
    print(f"Error: {e}")
