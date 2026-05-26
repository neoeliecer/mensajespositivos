import csv
import os

calendar_path = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

# Datos del Capítulo 21
new_row = [
    "manos",
    "21",
    "Preparación para la curación",
    "✨ El Secreto del Sanador: El arte de ser tu propio paciente primero. Descubre cómo proteger tu energía y elevar tu vibración según Barbara Brennan. #ManosQueCuran #SanacionEspiritual",
    "", # path_video
    "", # thumbnail
    "2026-04-15",
    "Draft"
]

try:
    # Intentamos abrir con utf-8 o latin-1 si falla
    try:
        with open(calendar_path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(new_row)
    except Exception:
        with open(calendar_path, 'a', newline='', encoding='latin-1') as f:
            writer = csv.writer(f)
            writer.writerow(new_row)
            
    print(f"Registro del Capítulo 21 añadido a {calendar_path}")

except Exception as e:
    print(f"Error al actualizar el calendario: {e}")
