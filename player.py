#!/usr/bin/env python3
import play
import connect
import urllib.parse
import itertools
import play_album
import play_song
import play_artist
import play_playlist
import ident

def search():
    search = urllib.parse.quote_plus(input("Search Term: "))

    results = connect.get("/hubs/search", {"query" : search})

    results = [ r for r in results if int(r.attrib["size"]) > 0]
    # only can play tracks, artists, or albums
    results = [ r for r in results if r.attrib["type"] in ["track", "album", "artist", "playlist"]]

    i = 0
    flat_results = []
    for result in results:
        print("----" + result.attrib["title"] + "----")
        for item in result:
            flat_results.append(item)
            print(str(i) + ") " + ident.ident(item.attrib["ratingKey"], item.attrib["type"]))
            i = i + 1

    print("--------")
    print(str(i) + ") Search Again")
    i += 1
    print(str(i) + ") Quit")

    selection = int(input("Choice: "))
    if selection == i - 1:
        return
    if selection >= i:
        quit()

    chosen = flat_results[selection]
    play_chosen(chosen)

    print(  "--------\n" + \
            "0) Play Again\n" + \
            "1) Search Again\n" + \
            "2) Quit" )
    choice = int(input("Choice: "))
    if choice == 0:
        play_chosen(chosen)
    elif choice == 1:
        return
    else:
        quit()

def quit():
    print("Exiting...")
    exit()

def play_chosen(chosen):
    if chosen.attrib["type"] == "artist":
        play_artist.play(chosen.attrib["ratingKey"])
    elif chosen.attrib["type"] == "track":
        play_song.play(chosen.attrib["ratingKey"])
    elif chosen.attrib["type"] == "album":
        play_album.play(chosen.attrib["ratingKey"])
    elif chosen.attrib["type"] == "playlist":
        play_playlist.play(chosen.attrib["ratingKey"])
    else:
        print("Internal Error: Invalid Media Type")



if __name__ == "__main__":
    while True:
        search()
