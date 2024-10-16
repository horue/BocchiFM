from pypresence import Presence
import time

def update_discord_rpc(client_id, musica_atual, artista_atual, album_art):
    RPC = Presence(client_id)  # Cria uma instância do Presence
    RPC.connect()  # Conecta ao Discord

    while True:
        if musica_atual and artista_atual:
            # Atualiza o Rich Presence do Discord
            RPC.update(
                details=f"**{musica_atual}**",
                state=f"{artista_atual}",
                large_image=album_art if album_art else "default_image",  # Use uma imagem padrão se não houver capa
                large_text="Álbum"  # Você pode mudar isso se quiser incluir mais informações
            )
            time.sleep(3)
        else:
            # Limpa o Rich Presence quando a música para de tocar
            RPC.update(               
                state=f"by: {artista_atual}",
                details=f"{musica_atual}",
                large_image=album_art if album_art else "default_image",  # Use uma imagem padrão se não houver capa
                large_text="Álbum"  # Você pode mudar isso se quiser incluir mais informações
            )