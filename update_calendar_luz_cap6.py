import csv
import os

calendar_path = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

new_row = [
    "luz",
    "6",
    "Hágase la Luz Cap 6: El Tándem Sanador-Médico",
    "✨ ¿CIENCIA O ESPIRITUALIDAD? ¿POR QUÉ NO AMBAS? ✨\n\nEn el Capítulo 6 de Hágase la Luz, Barbara Ann Brennan nos revela el poder del Tándem Sanador-Médico. 🩺✨\n\nImagina un equipo de salud donde el médico cuida tu cuerpo físico y el sanador cuida tu campo energético, acelerando tu recuperación al doble. 🚀\n\n¿Alguna vez has complementado un tratamiento médico con terapias energéticas? ¡Te leemos! 👇\n\n#HagaseLaLuz #BarbaraAnnBrennan #SanacionIntegral #MedicinaYEspiritualidad #EnergiaVital #DespertarEspiritual",
    "",
    "",
    "2026-04-26",
    "Draft"
]

with open(calendar_path, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(new_row)

print(f"Added Chapter 6 to {calendar_path}")
