import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"
output = []
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    for i in range(15, 60):
        text = reader.pages[i].extract_text()
        if "Capítulo 5" in text:
            output.append(f"Found Capítulo 5 on page index {i}")

print("\n".join(output))
