import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print("TOC Dump (First 20 pages):")
        for i in range(20):
            text = reader.pages[i].extract_text()
            print(f"--- Page {i+1} ---")
            print(text)
            
except Exception as e:
    print(f"Error: {e}")
