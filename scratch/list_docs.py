import os

def list_documents():
    docs_path = r"C:\Users\neo\Documents"
    output_file = r"c:\Users\neo\Documents\agente\mensajes positivos\scratch\docs_list.txt"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Listing directories under {docs_path}:\n")
        try:
            items = os.listdir(docs_path)
            for item in items:
                full_path = os.path.join(docs_path, item)
                is_dir = os.path.isdir(full_path)
                f.write(f"{'[DIR]' if is_dir else '[FILE]'} {item}\n")
                if is_dir and item.lower() in ["libros", "libro"]:
                    f.write(f"  Contents of {item}:\n")
                    try:
                        subitems = os.listdir(full_path)
                        for subitem in subitems:
                            f.write(f"    {subitem}\n")
                    except Exception as e:
                        f.write(f"    Error: {str(e)}\n")
        except Exception as e:
            f.write(f"Error listing base path: {str(e)}\n")
            
list_documents()
print("Done listing!")
