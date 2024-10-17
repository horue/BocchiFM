import configparser
import tkinter
from tkinter import messagebox


config = configparser.ConfigParser()
config.read('pref.bcc')
user_r = config.get('user', 'u')
apikey = config.get('user', 'k')

def save_pref(user, key):
    if user == '':
        user = user_r
    else:
        config.set('user', 'u', str(user))
    if key == '':
        key = apikey
    else:
        config.set('user', 'k', str(key))

    # save to a file
    with open('pref.bcc', 'w') as configfile:
        config.write(configfile)

    messagebox.showinfo("Success", "Preferences saved.")