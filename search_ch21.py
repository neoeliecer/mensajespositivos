import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def search_text(text_to_find, start=0, end=None):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        if end is None: end = len(reader.pages)
        for i in range(start, end):
            text = reader.pages[i].extract_text()
            if text and text_to_find.lower() in text.lower():
                print(f"FOUND '{text_to_find}' ON PAGE {i+1}")
                # print(text[:300])

search_text("Preparación para la curación")
search_text("Quinta Parte")
search_text("Capítulo 21")
