import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
output = []
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for i in range(20, 80): # check pages 20 to 80
        text = reader.pages[i].extract_text()
        if text and "Capítulo 5" in text:
            output.append(f"Found Capítulo 5 on page index {i}")
        if text and "Capítulo 6" in text:
            output.append(f"Found Capítulo 6 on page index {i}")

print("\n".join(output))
