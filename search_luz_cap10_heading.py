import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

def search():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(80, 110):
            text = reader.pages[i].extract_text()
            lines = text.split('\n')
            for line in lines:
                if 'MANTENER' in line.upper() and 'SANO' in line.upper():
                    print(f"Page {i+1}: {line}")

if __name__ == "__main__":
    search()
