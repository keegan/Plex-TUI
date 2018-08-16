import requests
from secret import *
import json

url='https://plex.tv/users/sign_in.json'

headers={
        'X-Plex-Client-Identifier': 'PlexTUI-V1.0-1',
        'X-Plex-Product': 'Plex TUI',
        'X-Plex-Version': 'V1.0'
        }

data={
        'user[login]': username,
        'user[password]': password
        }

def auth():
    r = requests.post(url, data=data, headers=headers)
    
    obj = json.loads(r.text)

    return obj['user']['authentication_token']


if __name__=='__main__':
    print(auth())
