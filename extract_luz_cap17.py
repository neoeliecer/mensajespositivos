with open('luz_full_text.txt', 'r', encoding='utf-8') as f:
    content = f.read()

start_pos = 1171243
end_pos = 1238650

chapter_text = content[start_pos:end_pos]

output_path = r'c:\Users\neo\Documents\agente\mensajes positivos\extracto_luz_cap17.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(chapter_text.strip())

print(f"Capítulo 17 extraído: {len(chapter_text)} caracteres")
print("\nPrimeras 600 chars:")
print(chapter_text[:600])
print("\n...\nÚltimas 400 chars:")
print(chapter_text[-400:])
