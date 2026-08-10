import requests
import time
import logging
from core.config import USERNAME, API_KEY

logging.basicConfig(filename='scrobbling_errors.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')


url = f"http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user={USERNAME}&api_key={API_KEY}&format=json"
track_duration_url = f"http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={API_KEY}&artist={{artist}}&track={{track}}&format=json"

ultima_musica = None

def get_music():
    try:
        global ultima_musica
        response = requests.get(url)
        data = response.json()

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
        except (requests.RequestException, ValueError) as e:
            logging.error(f"Falha ao obter música: {e}")
            return None, None, None, None

        if 'recenttracks' in data and 'track' in data['recenttracks']:
            tracks = data['recenttracks']['track']

            for track in tracks:
                if "@attr" in track and "nowplaying" in track["@attr"]:
                    musica_atual = track['name']
                    artista_atual = track['artist']['#text']
                    album_art = track['image'][2]['#text']  # Capa do álbum (tamanho médio)
                    album_name = track['album']['#text']
                    track_response = requests.get(track_duration_url.format(artist=artista_atual, track=musica_atual), timeout=5)
                    track_duration_data = track_response.json()     
                    track_duration = track_duration_data["track"]["duration"]
                    if album_name == None:
                        album_name = musica_atual

                    # Verifica se a música mudou
                    if musica_atual != ultima_musica:
                        print(f"Agora tocando: {musica_atual} - {artista_atual}")
                        ultima_musica = musica_atual  # Atualiza a última música
                    return musica_atual, artista_atual, album_art, album_name, track_duration
        return None, None, None, None, None  # Se não houver música tocando
    except ValueError as e:
        print(e)
        get_music()


def verify():
    while True:
        get_music()
        time.sleep(3)

if __name__ == "__main__":
    verify()