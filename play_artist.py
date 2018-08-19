import connect
import play_album
import random

def play(key):
    item = connect.get("/library/metadata/" + key + "/children")
    print("Playing Artist \"" + item.attrib["parentTitle"] + "\"")
    shuffle = input("Shuffle? Y/n: ")
    if shuffle != "n":
        random.shuffle(item)
    for child in item:
        play_album.play(child.attrib["ratingKey"])

def ident(key):
    item = connect.get("/library/metadata/" + key + "/children")
    return item.attrib["parentTitle"]
