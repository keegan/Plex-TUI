import play
import connect
import play_song

def play(key):
    album = connect.get("/library/metadata/" + key + "/children")
    print("Playing Album \"" + album.attrib["parentTitle"] + "\"")
    for track in album:
        play_song.play(track.attrib["ratingKey"])
