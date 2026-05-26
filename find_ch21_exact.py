import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_text_in_range(start, end, text_to_find):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(start, end):
            if i >= len(reader.pages): break
            text = reader.pages[i].extract_text()
            if text and text_to_find.lower() in text.lower():
                print(f"FOUND '{text_to_find}' ON PAGE {i+1}")
                # print(text[:200])

find_text_in_range(150, 180, "Capítulo 21")
find_text_in_range(150, 180, "Quinta Parte")
find_text_in_range(150, 180, "Capítulo 22")
