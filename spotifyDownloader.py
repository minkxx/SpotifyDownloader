from pySpotify import spotiSearch
from pyYtDl import songDl
from helperFunctions import MP4ToMP3, zip

import config

client = spotiSearch(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET)

url = input("Spotify Url : ")
if ("track" in (url.split("/"))) and (client.validUrl(url)):
    song = client.getTrack(url)
    path = songDl(song[0], "songs/")
    MP4ToMP3(path)
elif ("album" in (url.split("/"))) and (client.validUrl(url)):
    album = client.getAlbum(url)
    dir_path =  f"songs/{album[0]}/"
    for i in album[1]:
        path = songDl(i, dir_path)
        MP4ToMP3(path)
    zip(album[0], dir_path)
elif ("playlist" in (url.split("/")))and (client.validUrl(url)):
    playlist = client.getPlaylist(url)
    dir_path =  f"songs/{playlist[0]}/"
    for j in playlist[1]:
        path = songDl(j, dir_path)
        MP4ToMP3(path)
    zip(playlist[0], dir_path)
else:
    print("Not a spotify link!")