import spotipy
import asyncio
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import Search
from pytube import YouTube

import config

class songAPI:
    def __init__(self):    
        client_id = config.SPOTIFY_CLIENT_ID
        client_secret = config.SPOTIFY_CLIENT_SECRET
        if config.SPOTIFY_CLIENT_ID and config.SPOTIFY_CLIENT_SECRET:
            client_credentials_manager = (
                SpotifyClientCredentials(
                    client_id, client_secret
                        )
                    )
        self.spotify = spotipy.Spotify(
            client_credentials_manager=client_credentials_manager
        )

    def checkUrl(self,url):
        x = url.split("/")
        if "track" in x:
            return "track"
        elif "album" in x:
            return "album"
        elif "playlist" in x:
            return "playlist"
        
    def downloadTrack(self, url):
        if self.checkUrl(url) != "track":
            print("Not a track")
        else:
            track = self.spotify.track(url)
            info = track["name"]
            for artist in track["artists"]:
                fetched = f' {artist["name"]}'
                if "Various Artists" not in fetched:
                    info += fetched
            songInfo = Search(info)
            x = str(songInfo.results[0]).split("=")
            y = x[-1].split(">")
            videoID = y[0]
            youtube_url = f'https://www.youtube.com/watch?v={videoID}'
            yt = YouTube(youtube_url)
            stream =  yt.streams.filter(abr="128kbps")[0]
            stream.download(output_path="songs/")

    def downloadAlbum(self, url):
        if self.checkUrl(url) != "album":
            print("Not an album")
        else:
            album = self.spotify.album(url)
            albumName = album["name"]
            results = []
        for item in album["tracks"]["items"]:
            info = item["name"]
            for artist in item["artists"]:
                fetched = f' {artist["name"]}'
                if "Various Artists" not in fetched:
                    info += fetched
            results.append(info)
            for i in results:
                songInfo = Search(i)
                x = str(songInfo.results[0]).split("=")
                y = x[-1].split(">")
                videoID = y[0]
                youtube_url = f'https://www.youtube.com/watch?v={videoID}'
                yt = YouTube(youtube_url)
                stream =  yt.streams.filter(abr="128kbps")[0]
                stream.download(output_path=f"songs/{albumName}/")

    def downloadPlaylist(self, url):
        if self.checkUrl(url) != "playlist":
            print("Not a playlist")
        else:
            playlist = self.spotify.playlist(url)
            playlistName = playlist["name"]
            results = []
        for item in playlist["tracks"]["items"]:
            info = item["name"]
            for artist in item["artists"]:
                fetched = f' {artist["name"]}'
                if "Various Artists" not in fetched:
                    info += fetched
            results.append(info)
            for i in results:
                songInfo = Search(i)
                x = str(songInfo.results[0]).split("=")
                y = x[-1].split(">")
                videoID = y[0]
                youtube_url = f'https://www.youtube.com/watch?v={videoID}'
                yt = YouTube(youtube_url)
                stream =  yt.streams.filter(abr="128kbps")[0]
                stream.download(output_path=f"songs/{playlistName}/")

if __name__ == "__main__":   
    client = songAPI()
    userUrl = input(": ")
    isValid = client.checkUrl(userUrl)
    if isValid == "track":
        client.downloadTrack(str(userUrl))
    elif isValid == "album":
        client.downloadAlbum(str(userUrl))
    elif isValid == "playlist":
        client.downloadPlaylist(str(userUrl))
    else:
        print("Invalid url")