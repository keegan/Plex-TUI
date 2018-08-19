import play_song
import play_album
import play_artist

def ident(key, typ):
    if typ == "track":
        return play_song.ident(key)
    elif typ == "album":
        return play_album.ident(key)
    elif typ == "artist":
        return play_artist.ident(key)
