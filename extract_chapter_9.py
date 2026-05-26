import PyPDF2
import re

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\extracto_capitulo_9.txt"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        # Chapter 8 started around 190, so Chapter 9 should be after that.
        start_page = -1
        # Search range based on previous chapters.
        for i in range(210, min(250, num_pages)):
            text = reader.pages[i].extract_text()
            # Look for Chapter 9 title patterns
            # Note: Title might be "9. Que no te roben el sueño" or similar
            if "9. " in text and "sueño" in text.lower():
                start_page = i
                print(f"Found Chapter 9 start on page {i+1}")
                break
        
        if start_page == -1:
            print("Could not find start of Chapter 9 in expected range. Widening search.")
            for i in range(150, num_pages):
                 text = reader.pages[i].extract_text()
                 if "9. " in text and "sueño" in text.lower():
                    start_page = i
                    print(f"Found Chapter 9 start on page {i+1}")
                    break

        if start_page == -1:
             print("Still could not find Chapter 9. Checking for just '9.'")
             for i in range(210, num_pages):
                 text = reader.pages[i].extract_text()
                 lines = text.split('\n')
                 if any(line.strip().startswith("9.") for line in lines):
                    start_page = i
                    print(f"Found potential Chapter 9 start on page {i+1}")
                    break

        if start_page != -1:
            end_page = num_pages
            # Look for end of chapter (Chapter 10)
            # Chapter 10 title might contain "10."
            for i in range(start_page + 1, min(start_page + 50, num_pages)):
                page = reader.pages[i]
                text = page.extract_text()
                if "10." in text[:50] or "capítulo 10" in text.lower():
                    print(f"Found next chapter on page {i+1}")
                    end_page = i
                    break
            
            print(f"Extracting pages {start_page + 1} to {end_page}")
            
            full_text = ""
            for i in range(start_page, end_page):
                text = reader.pages[i].extract_text()
                full_text += text + "\n"
                
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(full_text)
                
            print(f"Saved to {output_path}")
            
            # Print first few lines for verification
            print("--- Preview ---")
            print(full_text[:500])
        else:
            print("Failed to find Chapter 9 start.")

except Exception as e:
    print(f"Error: {e}")
