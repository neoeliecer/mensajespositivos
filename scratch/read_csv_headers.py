import csv

csv_path = r"c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"
output_path = r"c:\Users\neo\Documents\agente\mensajes positivos\scratch\calendar_headers.txt"

try:
    # Try reading with utf-8 first
    with open(csv_path, 'r', encoding='utf-8') as f:
        first_line = f.readline()
        
    with open(output_path, 'w', encoding='utf-8') as out_f:
        out_f.write(f"First line: {first_line}\n")
except Exception as e:
    with open(output_path, 'w', encoding='utf-8') as out_f:
        out_f.write(f"Error: {str(e)}\n")
