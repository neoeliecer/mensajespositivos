with open('luz_full_text.txt', 'r', encoding='utf-8') as f:
    content = f.read()

cap18_start = 1238650

# Search for chapter 19 or Conclusion after cap18
import re

search_area = content[cap18_start + 500:]
patterns = [
    r'Cap[ií]tulo\s*19',
    r'CONCLUSI[OÓ]N',
    r'Conclusi[oó]n',
    r'AP[EÉ]NDICE',
    r'Ap[eé]ndice',
]

for pat in patterns:
    m = re.search(pat, search_area, re.IGNORECASE)
    if m:
        abs_pos = cap18_start + 500 + m.start()
        print(f"Pattern '{pat}' at pos {abs_pos}:")
        print(repr(content[abs_pos:abs_pos+200]))
        print()
