import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

def print_page():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(reader.pages[110].extract_text())

if __name__ == "__main__":
    print_page()
