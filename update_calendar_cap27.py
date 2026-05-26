import csv
import os

calendar_path = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

# Datos del Capítulo 27
new_row = [
    "manos",
    "27",
    "Cómo se desarrolla un Sanador: El Camino del Corazón",
    "¿Sientes el llamado a sanar? Convertirse en sanador no es algo que se aprenda en un libro de reglas rígidas. Es un proceso profundamente personal, una danza entre la verdad, el amor y la voluntad divina. #ManosQueCuran #SanacionEspiritual #BarbaraAnnBrennan",
    "", # Ruta_Video
    "", # Ruta_Portada
    "2026-04-21",
    "Draft"
]

try:
    with open(calendar_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
    print("Fila insertada correctamente en content_calendar.csv")
except Exception as e:
    print(f"Error al insertar fila: {e}")
