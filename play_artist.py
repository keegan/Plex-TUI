import connect
import play_album

def play(key):
    item = connect.get("/library/metadata/" + key + "/children")
    print("Playing Artist " + item.attrib["parentTitle"])
    for child in item:
        play_album.play(child.attrib["ratingKey"])
