
import PyPDF2

def debug_full_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            print(f"Total pages: {len(reader.pages)}")
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text and text.strip():
                    print(f"Page {i+1}: {repr(text[:150])}")
                else:
                    # Check if there's any content at all (images etc)
                    if page.images:
                        print(f"Page {i+1}: No text, but has images.")
                    else:
                        print(f"Page {i+1}: Empty.")
                
                if i > 50: # Only check first 50 to avoid too much output
                    break
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"
    debug_full_pdf(pdf_path)
