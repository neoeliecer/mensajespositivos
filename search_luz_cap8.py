import PyPDF2
import re
import sys
import codecs

if sys.platform == "win32":
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

pdf_path = r"C:\Users\neo\Documents\libros\Hágase-la-Luz-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i in range(len(reader.pages)):
            text = reader.pages[i].extract_text()
            if text:
                if re.search(r'(?i)Cap[ií]tulo\s+8', text):
                    header = text[:100].replace('\n', ' ')
                    # Sanitize for print
                    print("Page {}: {}".format(i+1, header.encode('ascii', 'ignore').decode('ascii')))

except Exception as e:
    print("Error: {}".format(e))
