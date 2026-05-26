import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

def print_headers():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(95, 105):
            text = reader.pages[i].extract_text()
            lines = text.split('\n')
            for j in range(min(5, len(lines))):
                if 'cap' in lines[j].lower():
                    print(f"Page {i+1}: {lines[j]}")
            for line in lines[:5]:
                if '10' in line:
                    print(f"Page {i+1} has 10: {line}")

if __name__ == "__main__":
    print_headers()
