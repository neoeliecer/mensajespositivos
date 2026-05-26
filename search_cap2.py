import PyPDF2

pdf_path = r"c:\Users\neo\Documents\agente\mensajes positivos\recupera tu mente.pdf"
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    with open("texto_placebo_cap2_search.txt", "w", encoding="utf-8") as out:
        for i in range(60, 70):
            out.write(f"--- Page {i+1} ---\n")
            out.write(reader.pages[i].extract_text() + "\n")
