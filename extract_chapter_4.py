import PyPDF2
import sys

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_4.txt"

print(f"Opening PDF: {pdf_path}")
try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        start_page = -1
        # Search for Chapter 4
        for i in range(50, num_pages):
            if i % 10 == 0:
                print(f"Searching page {i}...")
                sys.stdout.flush()
            
            page = reader.pages[i]
            text = page.extract_text()
            if "CAPÍTULO 4" in text.upper() or "CAPÍTULO IV" in text.upper():
                print(f"Found Chapter 4 on page {i+1}")
                start_page = i
                break
        
        if start_page != -1:
            end_page = num_pages
            for i in range(start_page + 1, min(start_page + 60, num_pages)):
                page = reader.pages[i]
                text = page.extract_text()
                if "CAPÍTULO 5" in text.upper() or "CAPÍTULO V" in text.upper():
                    print(f"Found Chapter 5 on page {i+1}")
                    end_page = i
                    break
            
            print(f"Extracting pages {start_page + 1} to {end_page}")
            extracted_text = ""
            for i in range(start_page, end_page):
                print(f"Processing page {i+1}...")
                sys.stdout.flush()
                extracted_text += f"\n--- Page {i+1} ---\n"
                extracted_text += reader.pages[i].extract_text()
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(extracted_text)
            print(f"Text saved to {output_path}")
        else:
            print("Chapter 4 header not found.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
