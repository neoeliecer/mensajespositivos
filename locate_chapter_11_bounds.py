import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"Total pages: {num_pages}")

        # Search range based on previous chapter findings (around 240)
        start_search = 230
        end_search = min(280, num_pages)

        print(f"Searching for Chapter 11 and 12 between pages {start_search} and {end_search}...")

        found_11 = False
        found_12 = False

        for i in range(start_search, end_search):
            page = reader.pages[i]
            text = page.extract_text()
            lines = text.split('\n')
            
            # Check first few lines for Chapter 11
            for line in lines[:10]:
                 if "CAPÍTULO 11" in line.upper() or "CAPÍTULO XI" in line.upper() or "CHAPTER 11" in line.upper():
                     print(f"FOUND Chapter 11 on page {i+1} (index {i}): {line.strip()}")
                     found_11 = True
            
            # Check for Chapter 12 to find end of 11
            for line in lines[:10]:
                 if "CAPÍTULO 12" in line.upper() or "CAPÍTULO XII" in line.upper() or "CHAPTER 12" in line.upper() or "CONCLUSIÓN" in line.upper(): # Maybe Conclusion?
                     print(f"FOUND Chapter 12/Next Section on page {i+1} (index {i}): {line.strip()}")
                     found_12 = True

except Exception as e:
    print(f"Error: {e}")
