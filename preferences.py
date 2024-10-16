import configparser
import tkinter
from tkinter import messagebox


config = configparser.ConfigParser()
config.read('pref.bcc')


def save_pref(user, key):
    if user == '':
        pass
    else:
        config.set('user', 'u', str(user))
    if key == '':
        pass
    else:
        config.set('user', 'k', str(key))

    # save to a file
    with open('pref.bcc', 'w') as configfile:
        config.write(configfile)

    messagebox.showinfo("Success", "Preferences saved.")