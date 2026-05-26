import re

with open('luz_full_text.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscar TODAS las ocurrencias de Cap 15
matches15 = list(re.finditer(r'Cap.tulo 15', content, re.IGNORECASE))
matches16 = list(re.finditer(r'Cap.tulo 16', content, re.IGNORECASE))

print(f"Ocurrencias de Cap 15: {len(matches15)}")
for m in matches15:
    print(f"  Posición {m.start()}: ...{repr(content[m.start():m.start()+150])}...")

print(f"\nOcurrencias de Cap 16: {len(matches16)}")
for m in matches16:
    print(f"  Posición {m.start()}: ...{repr(content[m.start():m.start()+150])}...")
