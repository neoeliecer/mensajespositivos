import re

with open('luz_full_text.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Cap 17 comienza en 1171243
# Buscar Cap 18 para saber dónde termina el Cap 17
search_start = 1171243
search_area = content[search_start:search_start + 300000]

patterns = [
    r'Cap[íi]tulo\s+18',
    r'CAPÍTULO\s+18',
    r'CAPITULO\s+18',
]

print(f"Longitud total del texto: {len(content)}")
print()

for pat in patterns:
    matches = [(m.start() + search_start, m.group()) for m in re.finditer(pat, search_area, re.IGNORECASE)]
    if matches:
        print(f"Patrón '{pat}':")
        for pos, text in matches[:5]:
            print(f"  Pos {pos}: ...{repr(content[pos-100:pos+200])}...")
        print()
