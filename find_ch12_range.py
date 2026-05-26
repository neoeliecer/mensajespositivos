import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_ch12_range():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            ch12_start = -1
            ch13_start = -1
            
            # Start searching from page 74 (index 73)
            for i in range(73, min(160, num_pages)):
                text = reader.pages[i].extract_text()
                if text:
                    text_up = text.upper()
                    if "CAPÍTULO 12" in text_up or "CAPÍTULO XII" in text_up:
                        ch12_start = i + 1
                        print(f"Chapter 12 starts on page {ch12_start}")
                    if "CAPÍTULO 13" in text_up or "CAPÍTULO XIII" in text_up:
                        ch13_start = i + 1
                        print(f"Chapter 13 starts on page {ch13_start}")
                        break
            
            if ch12_start != -1:
                end_page = ch13_start - 1 if ch13_start != -1 else ch12_start + 10
                print(f"Chapter 12 range: {ch12_start} to {end_page}")
            else:
                print("Chapter 12 not found in the searched range.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_ch12_range()
