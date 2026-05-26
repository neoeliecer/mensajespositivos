import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print("Page 10:")
        print(reader.pages[9].extract_text())
        print("Page 11:")
        print(reader.pages[10].extract_text())
except Exception as e:
    print(f"Error: {e}")
    
