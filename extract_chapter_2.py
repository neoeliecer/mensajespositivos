import PyPDF2
import sys

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        # Search for "Capítulo 2" in the first 100 pages
        start_page = -1
        for i in range(min(100, num_pages)):
            page = reader.pages[i]
            text = page.extract_text()
            if "Capítulo 2" in text or "CAPÍTULO 2" in text or "Chapter 2" in text:
                print(f"Found Chapter 2 on page {i+1}")
                start_page = i
                break
        
        if start_page != -1:
            # Extract text from start_page to start_page + 10 (approx chapter length)
            print("--- EXTRACTED TEXT ---")
            for i in range(start_page, min(start_page + 15, num_pages)):
                print(f"--- Page {i+1} ---")
                print(reader.pages[i].extract_text())
        else:
            print("Chapter 2 header not found in first 100 pages.")

except Exception as e:
    print(f"Error: {e}")
