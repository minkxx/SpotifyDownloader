import tkinter as tk
from tkinter import ttk

from helperFunctions import MP4ToMP3, zip
from pySpotify import spotiSearch
from pyYtDl import songDl
import config

client = spotiSearch(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET)

global user_url

def download():
    url = user_url.get()
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
    elif ("playlist" in (url.split("/")))and (client.validUrl(url)):
        playlistName, playlistSongs = client.getPlaylist(url)
        dir_path =  f"songs/{playlistName}/"
        for j in playlistSongs:
            path = songDl(j, dir_path)
            MP4ToMP3(path)
        playlistSongs.clear()
    else:
        output.set("Not a Spotify Link")
        pass

root = tk.Tk()
root.title("Spotify Downloader")

user_url = tk.StringVar()
output = tk.StringVar()

frame = ttk.Frame(root)

frame.grid(column=0, row=0, ) #sticky=("N", "W", "E", "S")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

title = ttk.Label(frame, text="Spotify Downloader", font=("Microsoft JhengHei UI", 20), foreground="#32A852")
title.grid(column=3,row=1)

url_entry = ttk.Entry(frame, width=7, textvariable=user_url)
url_entry.grid(column=3, row=3, sticky=("W", "E"))

ttk.Button(frame, text="Download", command=download).grid(column=3, row=5, sticky="W")

output_label = ttk.Label(frame, text=output, font=("Microsoft JhengHei UI", 15)).grid(column=3, row=7)

root.mainloop()