from module.pySpotify import spotiSearch
from module.pyYtDl import songDl
from module.helperFunctions import MP4ToMP3, setCoverArt, zip

import config

client = spotiSearch(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET)

url = input("Spotify Url : ")

if ("track" in (url.split("/"))) and (client.validUrl(url)):
    song = client.getTrack(url)
    path = songDl(song[0], "songs/")
    mp3_path = MP4ToMP3(path)
    setCoverArt(song[0], song[1], mp3_path)

elif ("album" in (url.split("/"))) and (client.validUrl(url)):
    album = client.getAlbum(url)
    dir_path = f"songs/{album[0]}/"
    for i in album[1]:
        path = songDl(i, dir_path)
        mp3_path = MP4ToMP3(path)
        setCoverArt(i, album[2], mp3_path)
    zip(album[0], dir_path)

elif ("playlist" in (url.split("/"))) and (client.validUrl(url)):
    playlist = client.getPlaylist(url)
    dir_path = f"songs/{playlist[0]}/"
    for j in playlist[1]:
        path = songDl(j[0], dir_path)
        mp3_path = MP4ToMP3(path)
        setCoverArt(j[0], j[1], mp3_path)
    zip(playlist[0], dir_path)
else:
    print("Not a spotify link!")
