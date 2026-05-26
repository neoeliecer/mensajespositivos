import PyPDF2
import re

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapters():
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        start_page = 57 # chapter 10 started on 58
        end_page = None
        
        for i in range(57, 70):
            if i < len(reader.pages):
                text = reader.pages[i].extract_text()
                if text:
                    if re.search(r'Cap.tulo 11', text, re.IGNORECASE) or re.search(r'Cap.tulo once', text, re.IGNORECASE):
                        end_page = i
                        print(f"Found Chapter 11 on page {i+1}")
                        break
        
        if end_page is None:
            print("Chapter 11 not found in range 57-70.")

if __name__ == "__main__":
    find_chapters()
