import play as ply
import connect
import time
import os


def play(key):
    track = connect.get("/library/metadata/" + key)
    ply.play(track[0][0][0].attrib["key"])
    dur = int(track[0][0][0].attrib["duration"])
    print("Playing: " + ident(key))
    seconds = (dur // 1000) % 60
    minutes = (dur // 60000) % 60
    elapsed = 0
    while "ffplay" in os.popen("ps aux").read():
        time.sleep(3)
    print()

def ident(key):
    track = connect.get("/library/metadata/" + key)
    return "\"" + track[0].attrib["title"] + "\" from \"" + track[0].attrib["parentTitle"] + "\" by \"" + track[0].attrib["grandparentTitle"] + "\""
