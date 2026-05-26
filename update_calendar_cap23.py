import csv
import os

calendar_path = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

new_row = [
    "manos",
    "23",
    "El Secreto para Sanar con Color y Sonido 🎨🎶",
    "🌈 ¿Sabías que cada color en tu aura tiene un propósito sagrado? En el capítulo 23 de 'Manos que curan' exploramos la vibración profunda de los colores y el sonido como herramientas de sanación. #ManosQueCuran #SanacionEnergetica #Cromoterapia",
    "",
    "",
    "2026-04-17",
    "Draft"
]

try:
    with open(calendar_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
    print(f"Capítulo 23 registrado en el calendario para el 2026-04-17.")
except Exception as e:
    print(f"Error al actualizar el calendario: {e}")
