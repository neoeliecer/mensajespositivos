import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

def search_chapter():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(100, 115):
            text = reader.pages[i].extract_text()
            lines = text.split('\n')
            for line in lines:
                if '10' in line and 'cap' in line.lower():
                    print(f"Found on page {i+1}: {line}")
                elif 'Cap' in line:
                    print(f"Page {i+1}: {line}")

if __name__ == "__main__":
    search_chapter()
