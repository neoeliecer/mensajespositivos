import sys

csv_path = r'c:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv'

# Try different encodings
for enc in ['utf-8', 'latin-1', 'cp1252']:
    try:
        with open(csv_path, 'r', encoding=enc) as f:
            lines = f.readlines()
        
        if lines:
            last_line = lines[-1]
            if "respira,7" in last_line:
                lines[-1] = last_line.replace("2026-05-15", "2026-05-16")
                with open(csv_path, 'w', encoding=enc, newline='') as f:
                    f.writelines(lines)
                print(f"Updated Chapter 7 date to 2026-05-16 using {enc}")
                sys.exit(0)
    except Exception as e:
        print(f"Failed with {enc}: {e}")

print("Could not update Chapter 7 date")
