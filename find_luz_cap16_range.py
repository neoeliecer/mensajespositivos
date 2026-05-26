import re

with open('luz_full_text.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscar TODAS las ocurrencias de Cap 16 y Cap 17
matches16 = list(re.finditer(r'Cap.tulo 16', content, re.IGNORECASE))
matches17 = list(re.finditer(r'Cap.tulo 17', content, re.IGNORECASE))

print(f"Ocurrencias de Cap 16: {len(matches16)}")
for m in matches16:
    print(f"  Posición {m.start()}: ...{repr(content[m.start():m.start()+150])}...")

print(f"\nOcurrencias de Cap 17: {len(matches17)}")
for m in matches17:
    print(f"  Posición {m.start()}: ...{repr(content[m.start():m.start()+150])}...")
