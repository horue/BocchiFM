import configparser
from tkinter import messagebox

class Preferences:
    config = configparser.ConfigParser()
    config.read('pref.bcc')
    user_r = config.get('user', 'u')
    apikey = config.get('user', 'k')

    @classmethod
    def save_preferences(cls, user, key) -> None:
        if user == '':
            user = cls.user_r
        else:
            cls.config.set('user', 'u', str(user))
        if key == '':
            key = cls.apikey
        else:
            cls.config.set('user', 'k', str(key))

        # save to a file
        with open('pref.bcc', 'w') as configfile:
            cls.config.write(configfile)

        messagebox.showinfo("Success", "Preferences saved.")