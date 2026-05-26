import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"
out_path = r"c:\Users\neo\Documents\agente\mensajes positivos\luz_chapters.txt"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        with open(out_path, 'w', encoding='utf-8') as out:
            for i in range(min(50, len(reader.pages))):
                page_text = reader.pages[i].extract_text()
                if page_text:
                    lines = page_text.split('\n')
                    for line in lines:
                        if re.search(r'(?i)cap[ií]tulo\s+\d+', line):
                            out.write(f"Page {i+1}: {line.strip()}\n")
    print(f"Done, check {out_path}")
except Exception as e:
    print(f"Error: {e}")
