import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Check pages around 174 (where Ch6 ended)
        start_check = 174
        end_check = 190
        
        for i in range(start_check, end_check):
            print(f"\n--- Page {i+1} ---")
            text = reader.pages[i].extract_text()
            print(text[:500]) # Print first 500 chars

except Exception as e:
    print(f"Error: {e}")
