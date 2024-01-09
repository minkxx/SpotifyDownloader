from pySpotify import spotiSearch
from pyYtDl import songDl
from helperFunctions import MP4ToMP3, zip

import config

client = spotiSearch(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET)

url = input("Spotify Url : ")
if ("track" in (url.split("/"))) and (client.validUrl(url)):
    songName = client.getTrack(url)
    path = songDl(songName, "songs/")
    MP4ToMP3(path)
elif ("album" in (url.split("/"))) and (client.validUrl(url)):
    albumName, albumSongs = client.getAlbum(url)
    dir_path =  f"songs/{albumName}/"
    for i in albumSongs:
        path = songDl(i, dir_path)
        MP4ToMP3(path)
    albumSongs.clear()
    zip(albumName, dir_path)
elif ("playlist" in (url.split("/")))and (client.validUrl(url)):
    playlistName, playlistSongs = client.getPlaylist(url)
    dir_path =  f"songs/{playlistName}/"
    for j in playlistSongs:
        path = songDl(j, dir_path)
        MP4ToMP3(path)
    playlistSongs.clear()
    zip(playlistName, dir_path)
else:
    print("Not a spotify link!")