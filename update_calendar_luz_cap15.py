import csv
import os

calendar_path = r'c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv'

new_row = {
    'series': 'luz',
    'chapter': '15',
    'title': 'Hágase la Luz Cap 15: Observaciones de las interacciones aurales durante las relaciones',
    'post_file': 'post_facebook_luz_cap15.md',
    'video_file': 'luz_cap15.mp4',
    'cover_image': '',
    'publish_date': '2026-05-08',
    'status': 'Draft'
}

# Read existing
with open(calendar_path, 'r', encoding='utf-8') as f:
    content = f.read()

print("Últimas 3 líneas actuales:")
lines = content.strip().split('\n')
for l in lines[-3:]:
    print(repr(l))

# Append new row
with open(calendar_path, 'a', encoding='utf-8', newline='') as f:
    f.write(f"\nluz,15,Hágase la Luz Cap 15: Observaciones de las interacciones aurales durante las relaciones,post_facebook_luz_cap15.md,luz_cap15.mp4,,2026-05-08,Draft")

print("\n✅ Capítulo 15 registrado en el calendario.")
