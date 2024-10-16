import pylast
import requests
import time
import logging
from d import *

# Configuração do logging para registrar erros
logging.basicConfig(filename='scrobbling_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Credenciais do Last.fm (substitua pelos seus valores)

url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={USERNAME}&api_key={API_KEY}&format=json"

# Variável global para armazenar a última música
ultima_musica = None

def get_music():
    global ultima_musica
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code != 200:
        logging.error(f"Erro ao fazer requisição: {response.status_code}")
        return None, None, None

    data = response.json()

    if 'recenttracks' in data and 'track' in data['recenttracks']:
        tracks = data['recenttracks']['track']

        for track in tracks:
            if "@attr" in track and "nowplaying" in track["@attr"]:
                musica_atual = track['name']
                artista_atual = track['artist']['#text']
                album_art = track['image'][2]['#text']  # Capa do álbum (tamanho médio)

                # Verifica se a música mudou
                if musica_atual != ultima_musica:
                    print(f"Agora tocando: {musica_atual} - {artista_atual}")
                    ultima_musica = musica_atual  # Atualiza a última música
                return musica_atual, artista_atual, album_art
    return None, None, None  # Se não houver música tocando


def verify():
    while True:
        get_music()
        time.sleep(3)

if __name__ == "__main__":
    verify()