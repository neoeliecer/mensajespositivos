import PyPDF2
import os

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

def find_chapter_11():
    try:
        if not os.path.exists(pdf_path):
            print(f"Error: PDF not found at {pdf_path}")
            return

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            start_page = -1
            end_page = -1
            
            # Start searching from where Chapter 10 ended (Page 66)
            for i in range(60, num_pages):
                page_text = reader.pages[i].extract_text()
                if page_text and "Capítulo 11" in page_text:
                    print(f"Found 'Capítulo 11' on page {i+1}")
                    start_page = i
                    break
            
            if start_page != -1:
                for i in range(start_page + 1, num_pages):
                    page_text = reader.pages[i].extract_text()
                    if page_text and "Capítulo 12" in page_text:
                        print(f"Found 'Capítulo 12' on page {i+1}")
                        end_page = i
                        break
            
            if start_page != -1:
                print(f"Chapter 11 range: {start_page+1} to {end_page if end_page != -1 else 'end'}")
            else:
                print("Could not find Chapter 11")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_chapter_11()
