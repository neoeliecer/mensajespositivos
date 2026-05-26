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
                if "LOS SIETE NIVELES DEL PROCESO CURATIVO" in text.upper():
                    print("Page {}: found it!".format(i+1))
                    print(text[:200].encode('ascii', 'ignore').decode('ascii'))

except Exception as e:
    print("Error: {}".format(e))
