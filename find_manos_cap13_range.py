import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_13():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for i in range(73, 150): # Start searching after Chapter 12
                text = reader.pages[i].extract_text()
                if "Capítulo 13" in text or "CAPÍTULO 13" in text:
                    print(f"Found Chapter 13 on page {i+1}")
                    # Find end of chapter by looking for Chapter 14
                    for j in range(i+1, 200):
                        next_text = reader.pages[j].extract_text()
                        if "Capítulo 14" in next_text or "CAPÍTULO 14" in next_text:
                            print(f"Found Chapter 14 on page {j+1}")
                            return i+1, j # i+1 is the start page, j is the end page (index of Chapter 14 page)
                    break
    except Exception as e:
        print(f"Error: {e}")
    return None, None

if __name__ == "__main__":
    start, end = find_chapter_13()
    if start and end:
        print(f"Chapter 13 Page Range: {start} to {end}")
