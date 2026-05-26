import csv
import os

calendar_path = r"C:\Users\neo\Documents\agente\mensajes positivos\content_calendar.csv"
post_path = r"C:\Users\neo\Documents\agente\mensajes positivos\post_facebook_manos_cap15.md"
script_path = r"C:\Users\neo\Documents\agente\mensajes positivos\guion_manos_cap15.md"
audio_path = r"c:/Users/neo/Documents/agente/mensajes positivos/guion_manos_cap15.mp3"

def update_calendar():
    try:
        if not os.path.exists(post_path) or not os.path.exists(script_path):
            print("Error: Post or Script file missing.")
            return

        with open(post_path, 'r', encoding='utf-8') as f:
            post_text = f.read()
        
        with open(script_path, 'r', encoding='utf-8') as f:
            script_text = f.read()

        new_row = [
            "15 (Manos)", 
            "Del bloque energético a la enfermedad física", 
            post_text, 
            script_text, 
            audio_path, 
            "Ready"
        ]

        with open(calendar_path, 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(new_row)
        
        print(f"Updated {calendar_path} with Chapter 15 (Manos)")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_calendar()
