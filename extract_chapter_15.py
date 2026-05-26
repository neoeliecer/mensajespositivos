import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

def extract_chapter_15():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            start_page = -1
            end_page = -1
            
            # Find Chapter 15
            # Start searching from page 180 (approx, based on Ch 14 location)
            for i in range(180, len(reader.pages)):
                text = reader.pages[i].extract_text()
                # Debug print for pages around where we expect it
                # if i > 200 and i < 220:
                #    print(f"Page {i}: {text[:100]}...")

                if "15. Tecnología en las aulas" in text or "TECNOLOGÍA EN LAS AULAS" in text:
                     if start_page == -1:
                        # Double check it's not the TOC (usually early pages)
                        if i > 20: 
                             start_page = i
                             print(f"Found Chapter 15 start at page {i+1}")
                
                if start_page != -1 and i > start_page and ("16." in text or "Capítulo 16" in text or "CAPÍTULO 16" in text):
                    end_page = i
                    print(f"Found Chapter 16 start at page {i+1}, stopping.")
                    break
            
            if start_page != -1:
                if end_page == -1:
                    end_page = min(start_page + 10, len(reader.pages)) # Fallback
                    print(f"End page not found, reading 10 pages until {end_page}")

                full_text = ""
                for i in range(start_page, end_page):
                    full_text += reader.pages[i].extract_text() + "\n"
                
                output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\texto_capitulo_15.txt"
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(full_text)
                print(f"Successfully extracted Chapter 15 text to {output_path}")
                print(f"Extracted {len(full_text)} characters.")
            else:
                print("Chapter 15 start not found.")
                # Fallback search entire document if not found in range
                if start_page == -1:
                    print("Searching entire document...")
                    for i in range(len(reader.pages)):
                        text = reader.pages[i].extract_text()
                        if "15. Tecnología en las aulas" in text:
                            print(f"Found at page {i+1}")
                            start_page = i
                            break

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    extract_chapter_15()
