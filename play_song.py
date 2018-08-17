import play as ply
import connect
import time
import os


def play(key):
    track = connect.get("/library/metadata/" + key)
    ply.play(track[0][0][0].attrib["key"])
    dur = int(track[0][0][0].attrib["duration"])
    print("Playing: \"" + track[0].attrib["title"] + "\"")
    seconds = (dur // 1000) % 60
    minutes = (dur // 60000) % 60
    elapsed = 0
    while elapsed < dur:
        elapsed_min = (elapsed // 60000) % 60
        elapsed_sec = (elapsed // 1000) % 60
        print("\r%02d:%02d / %02d:%02d" % (elapsed_min, elapsed_sec, minutes, seconds), end="")
        time.sleep(0.5)
        elapsed += 500
        if not "ffplay" in os.popen("ps aux").read():
            print()
            return
    print()
