import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        # Let's extract metadata/TOC if possible, or just search more broadly
        # Search for "Cap" and "3" in the same page
        start_page = -1
        for i in range(min(150, num_pages)):
            page = reader.pages[i]
            text = page.extract_text()
            if ("3" in text and "Cap" in text) or ("III" in text and "Cap" in text):
                print(f"Possible header on page {i+1}: {text[:100]}...")
                # If we find "Capítulo 3" with any variations
                if "CAPÍTULO 3" in text.upper() or "CAPÍTULO III" in text.upper():
                    print(f"Found Chapter 3 on page {i+1}")
                    start_page = i
                    break
        
        if start_page != -1:
            # Look for the start of Chapter 4 to find the end of Chapter 3
            end_page = num_pages
            for i in range(start_page + 1, min(start_page + 50, num_pages)):
                page = reader.pages[i]
                text = page.extract_text()
                if "CAPÍTULO 4" in text.upper() or "CAPÍTULO IV" in text.upper():
                    print(f"Found Chapter 4 on page {i+1}")
                    end_page = i
                    break
            
            print(f"Extracting pages {start_page + 1} to {end_page}")
            print("--- START EXTRACTED TEXT ---")
            for i in range(start_page, end_page):
                print(f"--- Page {i+1} ---")
                print(reader.pages[i].extract_text())
            print("--- END EXTRACTED TEXT ---")
        else:
            print("Chapter 3 header not found in first 150 pages.")
            # Let's dump the first 20 pages to see the TOC
            print("--- TABLE OF CONTENTS / FIRST 20 PAGES ---")
            for i in range(20):
                print(f"Page {i+1}: {reader.pages[i].extract_text()}")

except Exception as e:
    print(f"Error: {e}")
