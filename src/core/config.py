import configparser
from core.cid import c_id

config = configparser.ConfigParser()
config.read('pref.bcc')
user = config.get('user', 'u')
apikey = config.get('user', 'k')



CLIENT_ID = c_id
API_KEY = apikey
USERNAME = user


if __name__ == "__main__":
    print(user)
    print(apikey)