import csv
from datetime import datetime, timedelta

calendar_file = 'content_calendar.csv'

def get_next_available_date():
    last_date = None
    with open(calendar_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Fecha_Publicacion']:
                last_date = row['Fecha_Publicacion']
                
    if last_date:
        # Assuming format YYYY-MM-DD
        date_obj = datetime.strptime(last_date, "%Y-%m-%d")
        next_date = date_obj + timedelta(days=1)
        return next_date.strftime("%Y-%m-%d")
    else:
        return datetime.now().strftime("%Y-%m-%d")

next_date = get_next_available_date()

# Append to CSV
with open(calendar_file, mode='a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Libro,Capitulo,Titulo,Texto_Post,Ruta_Video,Ruta_Portada,Fecha_Publicacion,Estado
    writer.writerow(['luz', '9', 'Hágase la Luz Cap 9: Las energías terrestres como fundamento de la vida', 'post_facebook_luz_cap9.md', 'luz_cap9.mp4', '', next_date, 'Draft'])

print(f"Added Capítulo 9 to calendar for date: {next_date}")
