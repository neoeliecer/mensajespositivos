import os
import glob

def find_files():
    base_dir = r"C:\Users\neo\Documents"
    print(f"Searching in: {base_dir}")
    # Search for files with 'Brian' or 'confiar' in their name
    patterns = ["*Brian*", "*confiar*", "*Tracy*"]
    found = []
    
    # We will walk through the directory to find files
    for root, dirs, files in os.walk(base_dir):
        # Skip some system or agent dirs if needed, but let's look everywhere in Documents
        if ".agent" in root or ".git" in root or ".gemini" in root:
            continue
        for file in files:
            file_lower = file.lower()
            if any(p.strip("*").lower() in file_lower for p in patterns):
                full_path = os.path.join(root, file)
                found.append(full_path)
                print(f"Found: {full_path}")
                
    if not found:
        print("No matching files found via walk.")
        
find_files()
