import PyPDF2
import os

pdf_path = r"c:\Users\neo\Documents\libros\La Curacion Por La Musica - Ted Andrews.pdf"

def extract_images():
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            # Try to extract the first image from page 1 (TOC usually near start)
            # and maybe page 180 (where Chapter 15 might be)
            pages_to_check = [1, 2, 3, 4, 180, 181, 182]
            
            for page_num in pages_to_check:
                if page_num > len(reader.pages):
                    continue
                
                page = reader.pages[page_num-1]
                if "/XObject" in page["/Resources"]:
                    xObject = page["/Resources"]["/XObject"].get_object()
                    for obj in xObject:
                        if xObject[obj]["/Subtype"] == "/Image":
                            size = (xObject[obj]["/Width"], xObject[obj]["/Height"])
                            data = xObject[obj].get_data()
                            if xObject[obj]["/Filter"] == "/FlateDecode":
                                img = Image.frombytes("RGB", size, data)
                                img.save(f"page_{page_num}_img_{obj[1:]}.png")
                                print(f"Saved page_{page_num}_img_{obj[1:]}.png")
                            elif xObject[obj]["/Filter"] == "/DCTDecode":
                                with open(f"page_{page_num}_img_{obj[1:]}.jpg", "wb") as f:
                                    f.write(data)
                                print(f"Saved page_{page_num}_img_{obj[1:]}.jpg")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    from PIL import Image
    extract_images()
