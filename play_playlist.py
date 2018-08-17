import connect
import play_song
import random

def play(key):
    plist = connect.get("/playlists/" + key + "/items")
    print("Playing Playlist \"" + plist.attrib["title"] + "\"")
    shuffle = input("Shuffle? Y/n: ")
    if shuffle != "n":
        random.shuffle(plist)
    for child in plist:
        play_song.play(child.attrib["ratingKey"])
