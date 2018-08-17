import os
import time as t

def play_track(time):
    elapsed = 0
    while elapsed < time:
        rows, cols = size()
        interval = time // int(cols)
        seconds = (elapsed // 1000) % 60
        minutes = (elapsed // 60000) % 60
        to_print = "\r%02d:%02d " % (minutes,seconds)
        to_print = to_print + ("/" * (elapsed * (int(cols) // time)))
        print(to_print, end="")
        t.sleep(interval / 1000)
        elapsed += interval


def size():
    return os.popen('stty size', 'r').read().split()
