import auth
import requests
import xml.etree.ElementTree as et
from secret import root_url

token = auth.auth()
running = '/library/'

def req(loc):
    return requests.get(root_url + loc + '?X-Plex-Token=' + token)

root = et.fromstring(req(running).text)
for i,child in enumerate(root):
    print(str(i) + ": " + child.tag, child.attrib)

next = int(input('select next: '))

while next != -1:
    loc = root[next].attrib['key'] + '/'
    running += loc
    root = et.fromstring(req(running).text)
    for i, child in enumerate(root):
        print(str(i) + ': ' + child.tag, child.attrib)

    next = int(input('select next: '))
