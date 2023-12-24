from pytube import YouTube, Search
import os
from moviepy.editor import *
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import config

import urllib.request
import eyed3
from eyed3.id3.frames import ImageFrame

# s = Search("No Cap krsna")
# x = str(s.results[0]).split("=")
# y = x[-1].split(">")
# videoID = y[0]
# youtube_url = f'https://www.youtube.com/watch?v={videoID}'
# yt = YouTube(youtube_url)
# stream = yt.streams.filter(abr="128kbps")[0]
# x = stream.download(output_path="test/")

# def MP4ToMP3(mp4, mp3):
#     FILETOCONVERT = AudioFileClip(mp4)
#     FILETOCONVERT.write_audiofile(mp3)
#     FILETOCONVERT.close()

# def afterDl(file_path):
#     for i  in os.listdir(file_path):
#         if str(i).endswith(".mp4"):
#             VIDEO_FILE_PATH = f"{file_path}{i}"
#             AUDIO_FILE_PATH = f"{file_path}{i}.mp3"
#             MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)

#     for i  in os.listdir(file_path):
#         x = str(i).split(".mp4")
#         if str(i).endswith(".mp4.mp3"):
#             os.rename(f"{file_path}{i}", f"{file_path}{x[0]}.mp3")

# def removeMp4(file_path):
#     for i in os.listdir(file_path):
#         if str(i).endswith(".mp4"):
#             os.remove(f"{file_path}{i}")


client_id = config.SPOTIFY_CLIENT_ID
client_secret = config.SPOTIFY_CLIENT_SECRET
if config.SPOTIFY_CLIENT_ID and config.SPOTIFY_CLIENT_SECRET:
    client_credentials_manager = (
        SpotifyClientCredentials(
            client_id, client_secret
                )
            )
spotify = spotipy.Spotify(
    client_credentials_manager=client_credentials_manager
)

album = spotify.album("https://open.spotify.com/album/4013u1RNEHieH8NwnN0vNh?si=vBeC-Z3iTgaRYfTklulWTQ")
albumName = album["name"]
results = []
songName = []
# imgUrl = album["album"]["images"][0]["url"]
print(album["images"][1]["url"])
# for item in album["tracks"]["items"]:
#     print(item["images"])
    # info = item["name"]
    # songName.append(info)
    # for artist in item["artists"]:
    #     fetched = f' {artist["name"]}'
    #     if "Various Artists" not in fetched:
    #         info += fetched
    # results.append(info)
# trackImg = x["album"]["images"][0]["url"]
# trackName = x["name"]

# f = open(f"imgs/{trackName}.jpg",'wb')
# f.write(urllib.request.urlopen(trackImg).read())
# f.close()

# audiofile = eyed3.load("test/Despacito.mp3")
# if (audiofile.tag == None):
#     audiofile.initTag()

# audiofile.tag.images.set(ImageFrame.FRONT_COVER, open("imgs/No Cap.jpg",'rb').read(), 'image/jpeg')

# audiofile.tag.save()

# def setTrackCover(img_path, mp3_path, trackName):
#     f = open(f"imgs/{trackName}.jpg",'wb')
#     f.write(urllib.request.urlopen(img_path).read())
#     f.close()
#     audiofile = eyed3.load("test/Despacito.mp3")
#     if (audiofile.tag == None):
#         audiofile.initTag()
#     audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(mp3_path,'rb').read(), 'image/jpeg')
#     audiofile.tag.save()
