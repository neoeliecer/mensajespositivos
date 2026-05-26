import PyPDF2

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"
output_file = "pdf_inspection.txt"

def inspect_pdf():
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            with open(output_file, 'w', encoding='utf-8') as out:
                out.write(f"Total pages: {num_pages}\n")
                for i in range(min(40, num_pages)):
                    page = reader.pages[i]
                    text = page.extract_text()
                    if text and text.strip():
                        out.write(f"\n--- Page {i+1} ---\n")
                        out.write(text)
            print(f"Inspection saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect_pdf()
