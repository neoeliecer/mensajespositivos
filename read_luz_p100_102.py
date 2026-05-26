import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

def print_pages():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(99, 102):
            print(f"--- Page {i+1} ---")
            print(reader.pages[i].extract_text())

if __name__ == "__main__":
    print_pages()
