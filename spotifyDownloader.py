from pySpotify import spotiSearch
from pyYtDl import songDl, MP4ToMP3

import config

client = spotiSearch(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET)

url = input("Spotify Url : ")
if ("track" in (url.split("/"))) and (client.validUrl(url)):
    songName = client.getTrack(url)
    path = songDl(songName, "songs/")
    MP4ToMP3(path)
elif ("album" in (url.split("/"))) and (client.validUrl(url)):
    albumName, albumSongs = client.getAlbum(url)
    for i in albumSongs:
        apath = songDl(i, f"songs/{albumName}/")
        MP4ToMP3(apath)
    albumSongs.clear()
elif ("playlist" in (url.split("/")))and (client.validUrl(url)):
    playlistName, playlistSongs = client.getPlaylist(url)
    for j in playlistSongs:
        spath = songDl(j, f"songs/{playlistName}/")
        MP4ToMP3(spath)
    playlistSongs.clear()
else:
    print("Not a spotify link!")