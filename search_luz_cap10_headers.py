import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

def print_headers():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(104, 110):
            text = reader.pages[i].extract_text()
            lines = text.split('\n')
            for j in range(min(10, len(lines))):
                print(f"Page {i+1}, line {j}: {lines[j]}")
            print("-" * 20)

if __name__ == "__main__":
    print_headers()
