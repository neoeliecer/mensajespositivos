import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapters():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Searching {num_pages} pages...")
            
            for i in range(120, num_pages):
                text = reader.pages[i].extract_text()
                if not text: continue
                # Search for Chapter 17
                if "CAPÍTULO 17" in text.upper() or "CAPITULO 17" in text.upper():
                    print(f"FOUND Capítulo 17 on page {i+1}")
                if "CAPÍTULO 18" in text.upper() or "CAPITULO 18" in text.upper():
                    print(f"FOUND Capítulo 18 on page {i+1}")
                    # If we found 18, we can probably stop soon
                    # But if we were looking for 17, and found 18, we might have passed it
                    # although we are searching sequentially.
                if i % 20 == 0:
                    print(f"Searched up to page {i+1}...")
                
                # Stop if we found both and page 18 is after 17
                # Or just search a range.
                if i > 160: break

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapters()
