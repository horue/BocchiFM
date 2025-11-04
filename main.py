import threading
from pypresence import *
from api.getfm import *
from rp import *
from d import *

# Substitua pelo seu Client ID do aplicativo Discord
RPC = Presence(CLIENT_ID)  # Cria uma instância do Presence
RPC.connect()  # Conecta ao Discord

def show_rp():
    global rp_running
    rp_running = True
    try:
        while rp_running:
            musica_atual, artista_atual, album_art, album_name = get_music()  # Gets music
            if musica_atual and artista_atual:
                # Atualiza o Rich Presence do Discord
                RPC.update(
                    details=f"{musica_atual}",
                    state=f"{artista_atual}",
                    large_image=album_art if album_art else "default_image",  # Use a default image if no cover is provided
                    large_text=album_name if album_name else "No album found for this music.",
                )
                time.sleep(3)
            else:
                RPC.clear()
                time.sleep(10)
                show_rp()
    except Exception as e:
        print(e)
        time.sleep(2)
        show_rp()

def stop_rp():
    global rp_running
    rp_running = False
    RPC.clear()



if __name__ == "__main__":
    show_rp()