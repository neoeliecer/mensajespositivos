import requests
import os
import sys

# Cargar el token
TOKEN_FILE = r"C:\Users\neo\Documents\agente\mensajes positivos\fb_access_token.txt"
VIDEO_PATH = r"C:\Users\neo\Documents\agente\mensajes positivos\manos_cap18.mp4"
PAGE_ID = "me" # "me" funciona si el token es de página

def get_token():
    with open(TOKEN_FILE, 'r') as f:
        return f.read().strip()

def verify_token(token):
    url = f"https://graph.facebook.com/v19.0/me?access_token={token}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        print(f"Token valido. Conectado como: {data.get('name', 'Usuario desconocido')}")
        return True
    else:
        print(f"Error de Token: {r.text}")
        return False

def publish_video(token, video_path, title, description):
    print(f"Iniciando subida de video: {title}...")

    url = f"https://graph-video.facebook.com/v19.0/{PAGE_ID}/videos"
    
    files = {
        'source': open(video_path, 'rb')
    }
    
    data = {
        'access_token': token,
        'title': title,
        'description': description,
        'crosspost_to_instagram': 'true'
    }
    
    r = requests.post(url, data=data, files=files)
    
    if r.status_code == 200:
        res = r.json()
        print(f"Exito! Video publicado. ID: {res.get('id')}")
        return True
    else:
        print(f"Error al publicar: {r.text}")
        return False

if __name__ == "__main__":
    token = get_token()
    if verify_token(token):
        title = "Visión Interna"
        description = "¿Rayos X Humanos? Descubre el poder de la Visión Interna 🧬 En el Capítulo 18 de 'Manos que curan' exploramos la anatomía del tercer ojo. #Sanacion #VisionInterna"
        
        if os.path.exists(VIDEO_PATH):
            publish_video(token, VIDEO_PATH, title, description)
        else:
            print(f"No se encontro el video en: {VIDEO_PATH}")

