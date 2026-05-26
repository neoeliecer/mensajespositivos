
import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        start_index = 244 # Chapter 11 start
        end_scan_index = min(start_index + 20, len(reader.pages))

        print(f"Scanning pages {start_index} to {end_scan_index}...")

        for i in range(start_index, end_scan_index):
            page = reader.pages[i]
            text = page.extract_text()
            lines = text.split('\n')
            # Print first 5 lines of each page to identify headers
            print(f"\n--- Page {i + 1} (Index {i}) ---")
            for line in lines[:5]:
                print(line.strip())

except Exception as e:
    print(f"Error: {e}")
