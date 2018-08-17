import auth
import requests
import secret
import xml.etree.ElementTree as et
import urllib.parse

token = auth.auth()

def get_raw(location, args={}):
    query_string = urllib.parse.urlencode({"X-Plex-Token": token, **args})
    url = secret.root_url + location + "?" + query_string 
    return requests.get(url)

def get(location, args={}):
    data = get_raw(location, args)
    return et.fromstring(data.text)
