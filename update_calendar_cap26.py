import csv
import os

calendar_path = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

# Datos del Capítulo 26
new_row = [
    "manos",
    "26",
    "La Salud: Un Reto para Ser Uno Mismo",
    "¿Sabías que la salud es mucho más que la ausencia de dolor? Es el reto diario de ser quien realmente eres. En el Capítulo 26 de 'Manos que curan', aprendemos claves para cuidar tu templo sagrado. #ManosQueCuran #SaludHolistica #BarbaraAnnBrennan #SanacionEspiritual",
    "", # Ruta_Video
    "", # Ruta_Portada
    "2026-04-20",
    "Draft"
]

try:
    with open(calendar_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
    print("Fila insertada correctamente en content_calendar.csv")
except Exception as e:
    print(f"Error al insertar fila: {e}")
