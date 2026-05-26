import re

with open('luz_full_text.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Find start of chapter 10
start_match = re.search(r'Cap.tulo 10\s*\nSU CUERPO', content, re.IGNORECASE)
end_match = re.search(r'Cap.tulo 11\s*\nLA CURACI.N', content, re.IGNORECASE)

if start_match and end_match:
    chap_text = content[start_match.start():end_match.start()]
    with open('extracto_luz_cap10.txt', 'w', encoding='utf-8') as out:
        out.write(chap_text.strip())
    print("Chapter 10 extracted successfully.")
else:
    print("Could not find boundaries")
