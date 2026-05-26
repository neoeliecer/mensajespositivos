import csv
import os

calendar_path = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

new_row = [
    "manos",
    "24",
    "El Secreto Oculto de tus Vidas Pasadas ⏳✨",
    "⏳✨ ¿El tiempo es una ilusión? Descubre la sanación transtemporal. A veces, el origen de un dolor constante, una fobia o una pauta destructiva en nuestra vida, no pertenece a este espacio ni a este tiempo. Descubre el Capítulo 24 de 'Manos que curan'. #ManosQueCuran #VidasPasadas #SanacionEnergetica",
    "",
    "",
    "2026-04-18",
    "Draft"
]

try:
    with open(calendar_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
    print(f"Capítulo 24 registrado en el calendario para el 2026-04-18.")
except Exception as e:
    print(f"Error al actualizar el calendario: {e}")
