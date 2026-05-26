
import PyPDF2
pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(f"Total pages: {len(reader.pages)}")
except Exception as e:
    print(f"Error: {e}")
