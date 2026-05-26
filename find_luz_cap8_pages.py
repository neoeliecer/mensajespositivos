import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        for i in range(num_pages):
            page_text = reader.pages[i].extract_text()
            if page_text:
                # Look for "Capítulo 8" or "Capítulo VIII"
                if re.search(r'(?i)Cap[ií]tulo\s+8', page_text) or re.search(r'(?i)Cap[ií]tulo\s+VIII', page_text):
                    lines = page_text.split('\n')
                    for line in lines[:5]:
                        if re.search(r'(?i)Cap[ií]tulo\s+8', line) or re.search(r'(?i)Cap[ií]tulo\s+VIII', line):
                            print(f"FOUND Chapter 8 header on page {i+1}")
                            print(f"Line: {line}")
            
                # Look for "Capítulo 9" or "Capítulo IX"
                if re.search(r'(?i)Cap[ií]tulo\s+9', page_text) or re.search(r'(?i)Cap[ií]tulo\s+IX', page_text):
                    lines = page_text.split('\n')
                    for line in lines[:5]:
                        if re.search(r'(?i)Cap[ií]tulo\s+9', line) or re.search(r'(?i)Cap[ií]tulo\s+IX', line):
                            print(f"FOUND Chapter 9 header on page {i+1}")
                            print(f"Line: {line}")

except Exception as e:
    print(f"Error: {e}")
