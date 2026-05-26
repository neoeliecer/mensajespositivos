import re

with open('luz_full_text.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Cap 15 empieza en posición 923211, Cap 16 en 1053565
start_pos = 923211
end_pos = 1053565

chapter_text = content[start_pos:end_pos]

output_path = r'c:\Users\neo\Documents\agente\mensajes positivos\extracto_luz_cap15.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(chapter_text.strip())

print(f"Capítulo 15 extraído: {len(chapter_text)} caracteres")
print("\nPrimeras 500 chars:")
print(chapter_text[:500])
print("\n...\nÚltimas 300 chars:")
print(chapter_text[-300:])
