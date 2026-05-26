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
        for i in range(70, 90): # Search around the suspected area
            text = reader.pages[i].extract_text()
            if text:
                if "niveles del proceso curativo" in text.lower():
                    print("Page {}: found it!".format(i+1))
                    print(text[:200])

except Exception as e:
    print("Error: {}".format(e))
