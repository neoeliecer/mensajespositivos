import PyPDF2

pdf_path = r"C:\Users\neo\Documents\libros\cine\Manos-que-curan-Barbara-Ann-Brennan.pdf"

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # Often TOC is at the end or at the beginning.
        # Let's check first 10 pages and last 10 pages.
        print("--- FIRST 10 PAGES ---")
        for i in range(10):
            print(f"\nPage {i+1}:")
            print(reader.pages[i].extract_text()[:1000])
        
        print("\n--- LAST 10 PAGES ---")
        for i in range(len(reader.pages)-10, len(reader.pages)):
            print(f"\nPage {i+1}:")
            print(reader.pages[i].extract_text()[:1000])
except Exception as e:
    print(f"Error: {e}")
