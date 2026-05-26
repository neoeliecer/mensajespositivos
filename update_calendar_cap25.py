import csv
import os

calendar_path = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

# Datos del Capítulo 25
new_row = [
    "manos",
    "25",
    "Médico, Cúrate a ti mismo: La Revolución de la Nueva Medicina",
    "¿Alguna vez has sentido que tu cuerpo te envía mensajes que no logras descifrar? En el capítulo 25 de 'Manos que curan', Barbara Ann Brennan nos revela una verdad poderosa: El paciente es el verdadero sanador. #ManosQueCuran #SanacionEspiritual #BarbaraAnnBrennan #CrecimientoPersonal",
    "", # Ruta_Video
    "", # Ruta_Portada
    "2026-04-19",
    "Draft"
]

try:
    with open(calendar_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(new_row)
    print("Fila insertada correctamente en content_calendar.csv")
except Exception as e:
    print(f"Error al insertar fila: {e}")
