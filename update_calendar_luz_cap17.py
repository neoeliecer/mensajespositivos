import csv
import os

csv_path = r'c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv'

new_row = [
    'luz',
    '17',
    'Hagase la Luz Cap 17: Nuestra Intencionalidad y la Dimension del Hara',
    'post_facebook_luz_cap17.md',
    'luz_cap17.mp4',
    '',
    '2026-05-10',
    'Draft'
]

with open(csv_path, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(new_row)

print("OK: Capitulo 17 registrado en content_calendar.csv")
print(f"Fila: {new_row}")
