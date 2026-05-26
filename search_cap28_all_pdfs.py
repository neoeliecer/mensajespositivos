import PyPDF2
import os

dirs = [r"C:\Users\neo\Documents\libros", r"C:\Users\neo\Documents\libros\cine"]

def search_in_dir(d):
    for f in os.listdir(d):
        if f.endswith(".pdf"):
            path = os.path.join(d, f)
            print(f"Checking {f}...")
            try:
                with open(path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    # Look for "Capítulo 28" in the first 50 pages and last 50 pages
                    pages_to_check = list(range(min(50, len(reader.pages)))) + list(range(max(0, len(reader.pages)-50), len(reader.pages)))
                    for i in set(pages_to_check):
                        page_text = reader.pages[i].extract_text()
                        if page_text and "capítulo 28" in page_text.lower():
                            print(f"MATCH in {f} on page {i+1}")
                            return
            except:
                pass

for d in dirs:
    search_in_dir(d)
