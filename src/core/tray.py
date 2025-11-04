from api.getfm import *
from main import *
import pystray
from PIL import Image, ImageDraw
import threading
from preferences.preferences_scr import *

class App:
    def icon(width, height, color1, color2) -> Image:
        image = Image.open(r'assets/bcc_2.png')
        return image

    def on_clicked(icon, item) -> None:
        if str(item) == "Exit":
            icon.stop()

        elif str(item) == "Start":
            threading.Thread(target=show_rp, daemon=True).start()

        elif str(item) == "Stop":
            threading.Thread(target=stop_rp, daemon=True).start()

        elif str(item) == "Preferences":
            threading.Thread(target=PreferencesScreen.edit_pref, daemon=True).start()

    @classmethod
    def create_menu(cls) -> pystray.Menu:
        menu: pystray.Menu = pystray.Menu(
            pystray.MenuItem(f"BocchiFM by horue.", None, enabled=False),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Start", cls.on_clicked),
            pystray.MenuItem("Stop", cls.on_clicked),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Preferences", cls.on_clicked),
            pystray.MenuItem("Exit", cls.on_clicked) 
        )
        return menu

    def run():
        icon = pystray.Icon('test name',icon=App.icon(64, 64, 'black', 'white'),menu=App.create_menu())
        icon.run()

App.run()