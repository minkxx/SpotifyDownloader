from pytube import YouTube, Search
import os
from moviepy.editor import *

# s = Search("Despacito")
# x = str(s.results[0]).split("=")
# y = x[-1].split(">")
# videoID = y[0]
# youtube_url = f'https://www.youtube.com/watch?v={videoID}'
# yt = YouTube(youtube_url)
# stream = yt.streams.filter(abr="128kbps")[0]
# stream.download(output_path="test/")

def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

def afterDl(file_path):
    for i  in os.listdir(file_path):
        if str(i).endswith(".mp4"):
            VIDEO_FILE_PATH = f"{file_path}{i}"
            AUDIO_FILE_PATH = f"{file_path}{i}.mp3"
            MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)

    for i  in os.listdir(file_path):
        x = str(i).split(".mp4")
        if str(i).endswith(".mp4.mp3"):
            os.rename(f"{file_path}{i}", f"{file_path}{x[0]}.mp3")

def removeMp4(file_path):
    for i in os.listdir(file_path):
        if str(i).endswith(".mp4"):
            os.remove(f"{file_path}{i}")
    

# afterDl("test/")
removeMp4("test/")