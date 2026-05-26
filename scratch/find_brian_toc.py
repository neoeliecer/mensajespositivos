import pdfplumber

pdf_path = r'C:\Users\neo\Documents\libros\Brian-Tracy-El-poder-de-confiar-en-ti-mismo.pdf'

with pdfplumber.open(pdf_path) as pdf:
    print(f"Total pages: {len(pdf.pages)}")
    # Print text from first 15 pages to find the table of contents or Chapter 1
    for i in range(15):
        text = pdf.pages[i].extract_text()
        if text:
            print(f"--- PAGE {i+1} ---")
            lines = text.split('\n')
            for line in lines[:15]: # first 15 lines of each page
                print(line)
