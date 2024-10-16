from getfm import *
from main import *
import pystray
from PIL import Image, ImageDraw
import threading


def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image



def on_clicked(icon, item):
    if str(item) == "Exit":
        icon.stop()

    elif str(item) == "Start":
        threading.Thread(target=show_rp, daemon=True).start()

    elif str(item) == "Stop":
        threading.Thread(target=stop_rp, daemon=True).start()

    elif str(item) == "Preferences":
        print("Not yet implemented.")


menu_i = pystray.Menu(
    pystray.MenuItem("Exit", on_clicked),
    pystray.MenuItem("Start", on_clicked),
    pystray.MenuItem("Stop", on_clicked),
    pystray.MenuItem("Preferences", on_clicked)



    
    
    
    
)


# In order for the icon to be displayed, you must provide an icon
icon = pystray.Icon('test name',icon=create_image(64, 64, 'black', 'white'),menu=menu_i)


# To finally show you icon, call run
icon.run()