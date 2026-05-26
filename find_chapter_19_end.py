
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

start_index = 364  # Page 365
end_check_index = 375

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        for i in range(start_index, end_check_index):
            if i < len(reader.pages):
                text = reader.pages[i].extract_text()
                # Print first 200 chars of each page
                print(f"--- Page {i + 1} (Index {i}) ---")
                print(text[:200].replace('\n', ' '))
                print("-" * 20)
            
except Exception as e:
    print(f"Error: {e}")
