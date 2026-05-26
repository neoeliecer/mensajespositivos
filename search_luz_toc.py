import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

def print_toc():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(2, 6): # Usually TOC is in the first few pages
            text = reader.pages[i].extract_text()
            print(f"--- Page {i+1} ---")
            print(text)

if __name__ == "__main__":
    print_toc()
