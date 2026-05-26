import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_ch11_range():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Total pages: {num_pages}")
            
            ch11_start = -1
            ch12_start = -1
            
            # Search from page 65 (index 64) onwards
            for i in range(65, min(150, num_pages)):
                text = reader.pages[i].extract_text()
                if text:
                    text_up = text.upper()
                    if "CAPÍTULO 11" in text_up or "CAPÍTULO XI" in text_up:
                        ch11_start = i + 1
                        print(f"Chapter 11 starts on page {ch11_start}")
                    if "CAPÍTULO 12" in text_up or "CAPÍTULO XII" in text_up:
                        ch12_start = i + 1
                        print(f"Chapter 12 starts on page {ch12_start}")
                        break
            
            if ch11_start != -1:
                end_page = ch12_start - 1 if ch12_start != -1 else ch11_start + 10
                print(f"Chapter 11 range: {ch11_start} to {end_page}")
            else:
                print("Chapter 11 not found in the searched range.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_ch11_range()
