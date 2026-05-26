import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    # Check pages around 174 (which is index 173)
    # Let's check 173 to 185
    start_idx = 173
    end_idx = 185
    
    for i in range(start_idx, end_idx):
        print(f"\n--- PAGE {i+1} ---\n")
        print(reader.pages[i].extract_text())
