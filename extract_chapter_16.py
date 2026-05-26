import PyPDF2
import re

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

def extract_chapter_16():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            start_page = -1
            end_page = -1
            
            # Find Chapter 16
            # Start searching from page 185 (approx, based on Ch 15 location which was around 314?? wait, Ch 15 was found at 314. So Ch 16 should be after that.)
            # Actually, let's just search a broader range or from 310 onwards.
            
            print("Searching for Chapter 16...")
            for i in range(310, len(reader.pages)):
                text = reader.pages[i].extract_text()
                
                # Loose matching for title
                if "16. El impacto de las redes" in text or "IMPACTO DE LAS REDES" in text:
                     if start_page == -1:
                         # Ensure it's not TOC
                         if i > 20:
                             start_page = i
                             print(f"Found Chapter 16 start at page {i+1}")
                
                if start_page != -1 and i > start_page:
                    if "17." in text or "Capítulo 17" in text or "CAPÍTULO 17" in text:
                        end_page = i
                        print(f"Found Chapter 17 start at page {i+1}, stopping.")
                        break
            
            if start_page != -1:
                if end_page == -1:
                    end_page = min(start_page + 12, len(reader.pages)) # Fallback
                    print(f"End page not found, reading 12 pages until {end_page}")

                full_text = ""
                for i in range(start_page, end_page):
                    full_text += reader.pages[i].extract_text() + "\n"
                
                output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\texto_capitulo_16.txt"
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(full_text)
                print(f"Successfully extracted Chapter 16 text to {output_path}")
                print(f"Extracted {len(full_text)} characters.")
            else:
                print("Chapter 16 start not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    extract_chapter_16()
