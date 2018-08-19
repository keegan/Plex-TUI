import play
import connect
import play_song
import random

def play(key):
    album = connect.get("/library/metadata/" + key + "/children")
    print("Playing Album " + ident(key))
    shuffle=input("Shuffle? Y/n: ")
    if shuffle !="n":
        random.shuffle(album)
    for track in album:
        play_song.play(track.attrib["ratingKey"])

def ident(key):
    album = connect.get("/library/metadata/" + key + "/children")
    return "\"" + album[0].attrib["parentTitle"] + "\" by \"" + album[0].attrib["grandparentTitle"] + "\""
