import csv
import os

calendar_path = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"

new_row = [
    "luz",
    "7",
    "Hágase la Luz Cap 7: Las Siete Fases de la Curación",
    "¡LA SANACIÓN NO ES UNA LÍNEA RECTA! 🌀✨ ¿Sientes que das un paso adelante y dos atrás? Esto es para ti. 👇\n\nEn el Capítulo 7 de Hágase la Luz, Barbara Ann Brennan nos revela un secreto liberador: Sanar es un viaje en espiral, no una curva ascendente. 🐚\n\nA menudo, cuando empezamos a mejorar, sentimos más dolor o irritación. ¡No es que estés peor! Es que tu nivel de conciencia ha subido y ya no toleras los desequilibrios que antes dabas por 'normales'. 📈\n\n#HagaseLaLuz #BarbaraAnnBrennan #SanacionHolistica #Espiritualidad #CrecimientoPersonal #SaludIntegral #SanacionEmocional #LuzInterior #Bienestar",
    "guion_luz_cap7.md",
    "post_facebook_luz_cap7.md",
    "2026-04-27",
    "Draft"
]

with open(calendar_path, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(new_row)

print(f"Added Chapter 7 (Luz) to {calendar_path}")
