
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

# Start looking after Chapter 18 (which ended around page 363/364)
start_search_page = 360
end_search_page = 380

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        for i in range(start_search_page, end_search_page):
            if i < len(reader.pages):
                text = reader.pages[i].extract_text()
                # Print first 200 chars of each page to identify chapter start
                print(f"--- Page {i + 1} (Index {i}) ---")
                print(text[:200].replace('\n', ' '))
                print("\n")
            
except Exception as e:
    print(f"Error: {e}")
