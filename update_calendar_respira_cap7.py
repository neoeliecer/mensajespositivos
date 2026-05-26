import csv
from datetime import datetime, timedelta

csv_path = r'c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv'

# New entry data
book = "respira"
chapter = "7"
title = "Respira Cap 7: Masticar para Respirar"
post_file = "post_facebook_respira_cap7.md"
video_file = "respira_cap7.mp4"
status = "Draft"

# Determine next date
try:
    with open(csv_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        last_line = lines[-1].strip()
        last_date_str = last_line.split(',')[-2]
        last_date = datetime.strptime(last_date_str, '%Y-%m-%d')
        next_date = last_date + timedelta(days=1)
except Exception:
    next_date = datetime.now() + timedelta(days=1)

next_date_str = next_date.strftime('%Y-%m-%d')

new_row = [book, chapter, title, post_file, video_file, "", next_date_str, status]

with open(csv_path, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(new_row)

print(f"Added Chapter 7 to calendar for {next_date_str}")
