import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_9():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Chapter 8 starts at index 51. Let's look from index 55 onwards.
            for i in range(51, len(reader.pages)):
                page_text = reader.pages[i].extract_text()
                if "Capítulo 9" in page_text or "CAPÍTULO 9" in page_text:
                    print(f"Found Chapter 9 on page {i+1} (index {i})")
                    # Sneak peek at the text around it
                    print(f"Context: {page_text[:100]}")
                    return
            print("Chapter 9 not found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_9()
