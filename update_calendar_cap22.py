import csv
import os

calendar_path = 'content_calendar.csv'
chapter_num = '22'
book = 'manos'
title = 'Curación del Espectro Total'
post_content = '✨ Curación del Espectro Total: Más allá de lo físico ✨. Barbara Ann Brennan nos enseña la técnica de la Quelación para limpiar y cargar nuestro campo energético. #ManosQueCuran #Sanación #BarbaraBrennan'
date = '2026-04-16'
status = 'Draft'

new_row = [book, chapter_num, title, post_content, '', '', date, status]

with open(calendar_path, mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(new_row)

print(f"Capítulo {chapter_num} agregado al calendario.")
