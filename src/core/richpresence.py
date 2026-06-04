import threading
from pypresence import *
from core.lastfm import *
from core.config import CLIENT_ID
from pypresence.types import ActivityType, StatusDisplayType
import time


RPC = Presence(CLIENT_ID) 
RPC.connect() 


class RichPresence():
    globalSound = ""
    globalArtist = ""
    lastMusic = ""
    rp_running = False
    agora = int(time.time())



    def updateMusicInfo():
        musicInfoString = f"Now playing {RichPresence.globalSound} by {RichPresence.globalArtist}."


    @staticmethod
    def run():
        if RichPresence.rp_running:
            return
        RichPresence.rp_running = True
        try:
            while RichPresence.rp_running:
                musica_atual, artista_atual, album_art, album_name, music_duration = get_music()  # Gets music
                if musica_atual != RichPresence.lastMusic:
                    RichPresence.agora = int(time.time())
                if musica_atual and artista_atual:
                    # Atualiza o Rich Presence do Discord
                    RPC.update(
                        activity_type=ActivityType.LISTENING,
                        details=f"{musica_atual}",
                        state=f"{artista_atual}",
                        large_image=album_art if album_art else "default_image",  # Use a default image if no cover is provided
                        large_text=album_name if album_name else "No album found for this music.",
                        start=RichPresence.agora if music_duration else None,
                        end=RichPresence.agora + (int(music_duration)/1000) if music_duration else None,
                    )
                    RichPresence.globalSound = musica_atual
                    RichPresence.globalArtist = artista_atual
                    RichPresence.lastMusic = musica_atual
                    time.sleep(3)
                else:
                    RPC.clear()
                    time.sleep(10)
        except Exception as e:
            print(e)
        finally:
            RichPresence.rp_running = False

    @staticmethod
    def stop():
        global rp_running
        rp_running = False
        RPC.clear()



if __name__ == "__main__":
    RichPresence.run()