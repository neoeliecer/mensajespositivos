import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

def print_pages():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print("Page 110:")
        print(reader.pages[109].extract_text())
        print("Page 111:")
        print(reader.pages[110].extract_text()[:300])

if __name__ == "__main__":
    print_pages()
