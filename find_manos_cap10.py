import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Man-que-curan-Barbara-Ann-Brennan.pdf"
# Error in path? Let's check the path from extract_manos_cap1.py again
pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_10():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            # Start from where Chapter 9 ended (approx page 58)
            for i in range(58, min(100, num_pages)):
                text = reader.pages[i].extract_text()
                if text:
                    lines = text.split('\n')
                    # Look for "CAPÍTULO 10" or "Diez" or similar
                    for line in lines[:10]:
                        if "CAPÍTULO" in line.upper() and ("10" in line or "X" in line or "DIEZ" in line):
                            print(f"MATCH on page {i+1} (index {i}): {line.strip()}")
                            # Peek next few pages to find where it ends (Chapter 11 start)
                            for j in range(i + 1, min(i + 20, num_pages)):
                                next_text = reader.pages[j].extract_text()
                                if next_text:
                                    for next_line in next_text.split('\n')[:10]:
                                        if "CAPÍTULO" in next_line.upper() and ("11" in next_line or "XI" in next_line or "ONCE" in next_line):
                                            print(f"End of chapter 10 probably at page {j} (index {j-1})")
                                            return i, j
                            return i, i + 10 # Default range if Chapter 11 not found
    except Exception as e:
        print(f"Error: {e}")
    return None

if __name__ == "__main__":
    find_chapter_10()
