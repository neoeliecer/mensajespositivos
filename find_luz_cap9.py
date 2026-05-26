import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

start_page = -1
end_page = -1

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    total_pages = len(reader.pages)
    
    for i in range(70, total_pages):
        text = reader.pages[i].extract_text()
        if text:
            if re.search(r'(?i)Capítulo\s+9', text):
                print(f"Found Capítulo 9 on page {i}")
                if start_page == -1:
                    start_page = i
            if start_page != -1 and i > start_page + 1 and re.search(r'(?i)Capítulo\s+10', text):
                print(f"Found Capítulo 10 on page {i}")
                end_page = i
                break

print(f"Chapter 9 range: {start_page} to {end_page}")
