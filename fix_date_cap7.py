import sys

csv_path = r'c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv'

with open(csv_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

if lines:
    last_line = lines[-1]
    if "respira,7" in last_line:
        lines[-1] = last_line.replace("2026-05-15", "2026-05-16")
        with open(csv_path, 'w', encoding='utf-8', newline='') as f:
            f.writelines(lines)
        print("Updated Chapter 7 date to 2026-05-16")
    else:
        print("Chapter 7 not found in last line")
else:
    print("Empty file")
