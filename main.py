import threading
from pypresence import *
from getfm import *
from rp import *
from d import *

# Substitua pelo seu Client ID do aplicativo Discord
RPC = Presence(CLIENT_ID)  # Cria uma instância do Presence
RPC.connect()  # Conecta ao Discord


def main():
    while True:
        musica_atual, artista_atual, album_art = get_music()  # Pega a música atual
        update_discord_rpc(CLIENT_ID, musica_atual, artista_atual, album_art)  # Atualiza o Rich Presence
        time.sleep(3)

def show_rp():
    global rp_running
    rp_running = True
    while rp_running:
        musica_atual, artista_atual, album_art, album_name = get_music()  # Pega a música atual
        if musica_atual and artista_atual:
            # Atualiza o Rich Presence do Discord
            RPC.update(
                details=f"{musica_atual}",
                state=f"{artista_atual}",
                large_image=album_art if album_art else "default_image",  # Use uma imagem padrão se não houver capa
                large_text=f"{album_name}"  # Você pode mudar isso se quiser incluir mais informações
            )
            time.sleep(3)
        else:
            # Limpa o Rich Presence quando a música para de tocar
            RPC.clear()

def stop_rp():
    global rp_running
    rp_running = False
    RPC.clear()



if __name__ == "__main__":
    show_rp()