import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        full_text = ""
        for i in range(11, 15): # From page 12 to 15
            full_text += reader.pages[i].extract_text() + "\n"
        
        with open("extracto_cap3.txt", "w", encoding="utf-8") as f:
            f.write(full_text)
        print("Done writing to extracto_cap3.txt")
except Exception as e:
    print(f"Error: {e}")
    
