import requests
import time
import logging
from core.config import USERNAME, API_KEY

logging.basicConfig(filename='scrobbling_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={USERNAME}&api_key={API_KEY}&format=json"

ultima_musica = None

def get_music():
    try:
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
                    album_name = track['album']['#text']                
                    if album_name == None:
                        album_name = musica_atual

                    # Verifica se a música mudou
                    if musica_atual != ultima_musica:
                        print(f"Agora tocando: {musica_atual} - {artista_atual}")
                        ultima_musica = musica_atual  # Atualiza a última música
                    return musica_atual, artista_atual, album_art, album_name
        return None, None, None, None  # Se não houver música tocando
    except ValueError as e:
        print(e)
        get_music()


def verify():
    while True:
        get_music()
        time.sleep(3)

if __name__ == "__main__":
    verify()