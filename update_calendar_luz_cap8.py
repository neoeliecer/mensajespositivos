import csv
import sys
import os
from datetime import date

sys.stdout.reconfigure(encoding='utf-8')

base = r"c:\Users\neo\Documents\agente\mensajes positivos"
calendar_path = os.path.join(base, "content_calendar.csv")

# Leer el post completo
post_path = os.path.join(base, "post_facebook_luz_cap8.md")
with open(post_path, "r", encoding="utf-8") as f:
    texto_post = f.read().strip()

# Leer el CSV
with open(calendar_path, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

# Actualizar la fila de luz cap 8
updated = False
for r in rows:
    if r.get("Libro") == "luz" and r.get("Capitulo") == "8":
        r["Titulo"] = "Hágase la Luz Cap 8: Los 7 Niveles de Tu Salud"
        r["Texto_Post"] = texto_post
        r["Ruta_Video"] = "luz_cap8.mp4"
        r["Ruta_Portada"] = os.path.join(base, "portada_luz_cap8.png")
        # Mantener fecha y estado actuales
        print(f"✅ Actualizado: Libro={r['Libro']}, Cap={r['Capitulo']}")
        print(f"   Título: {r['Titulo']}")
        print(f"   Fecha:  {r['Fecha_Publicacion']}")
        print(f"   Estado: {r['Estado']}")
        print(f"   Post preview: {r['Texto_Post'][:80]}...")
        updated = True
        break

if not updated:
    print("⚠️ No se encontró la entrada de luz cap 8. Agregando nueva...")
    rows.append({
        "Libro": "luz",
        "Capitulo": "8",
        "Titulo": "Hágase la Luz Cap 8: Los 7 Niveles de Tu Salud",
        "Texto_Post": texto_post,
        "Ruta_Video": "luz_cap8.mp4",
        "Ruta_Portada": os.path.join(base, "portada_luz_cap8.png"),
        "Fecha_Publicacion": "2026-04-30",
        "Estado": "Draft"
    })
    print("✅ Nueva fila agregada.")

# Guardar
with open(calendar_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("\n✅ Calendario actualizado correctamente.")
