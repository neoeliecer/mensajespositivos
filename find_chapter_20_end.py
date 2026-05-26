
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

start_index = 371  # Start of Ch 20
end_check_index = 385 # Check a decent range

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        for i in range(start_index, min(end_check_index, len(reader.pages))):
            text = reader.pages[i].extract_text()
            # Print first 200 chars of each page to see headers
            print(f"--- Page {i + 1} (Index {i}) ---")
            print(text[:200].replace('\n', ' '))
            print("-" * 20)
            
except Exception as e:
    print(f"Error: {e}")
