import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        start_page = -1
        # Search for "Capítulo 7"
        for i in range(min(300, num_pages)):
            page = reader.pages[i]
            text = page.extract_text()
            if "CAPÍTULO 7" in text.upper() or "CAPÍTULO VII" in text.upper():
                # Avoid TOC matches if possible by checking if it's a short page or has typical header format, 
                # but broadly matching usually works if we check sequentially.
                # Assuming TOC is early, let's just pick the last one if duplicates, 
                # or better, let's just print all matches to be sure.
                print(f"Possible Chapter 7 on page {i+1}")
                # Usually the main chapter content is later than page 20
                if i > 10: 
                    start_page = i
                    print(f"CONFIRMED START: Chapter 7 on page {i+1}")
                    break
        
        if start_page != -1:
            end_page = num_pages
            # Search for Chapter 8 to find end
            for i in range(start_page + 1, min(start_page + 50, num_pages)):
                page = reader.pages[i]
                text = page.extract_text()
                if "CAPÍTULO 8" in text.upper() or "CAPÍTULO VIII" in text.upper():
                    print(f"Found Chapter 8 on page {i+1}")
                    end_page = i
                    break
            
            print(f"Extracting pages {start_page + 1} to {end_page}")
            print("--- START EXTRACTED TEXT ---")
            for i in range(start_page, end_page):
                # print(f"--- Page {i+1} ---")
                print(reader.pages[i].extract_text())
            print("--- END EXTRACTED TEXT ---")
        else:
            print("Chapter 7 header not found.")

except Exception as e:
    print(f"Error: {e}")
