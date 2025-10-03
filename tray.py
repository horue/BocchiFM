from getfm import *
from main import *
import pystray
from PIL import Image, ImageDraw
import threading
from preferences_scr import *


def icon(width, height, color1, color2):
    image = Image.open(r'Visual_Assets/bcc_2.png')
    return image



def on_clicked(icon, item):
    if str(item) == "Exit":
        icon.stop()

    elif str(item) == "Start":
        threading.Thread(target=show_rp, daemon=True).start()

    elif str(item) == "Stop":
        threading.Thread(target=stop_rp, daemon=True).start()

    elif str(item) == "Preferences":
        threading.Thread(target=edit_pref, daemon=True).start()


menu_i = pystray.Menu(
    pystray.MenuItem(f"BocchiFM by horue.", None, enabled=False),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Start", on_clicked),
    pystray.MenuItem("Stop", on_clicked),
    pystray.Menu.SEPARATOR,
    pystray.MenuItem("Preferences", on_clicked),
    pystray.MenuItem("Exit", on_clicked) 
)


# In order for the icon to be displayed, you must provide an icon
icon = pystray.Icon('test name',icon=icon(64, 64, 'black', 'white'),menu=menu_i)


# To finally show you icon, call run
icon.run()