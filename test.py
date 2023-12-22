from pytube import YouTube, Search
import os
from moviepy.editor import *

# s = Search("Despretion Talha Anjum")
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



for i  in os.listdir("test/"):
    if str(i).endswith(".mp4"):
        VIDEO_FILE_PATH = f"test/{i}"
        AUDIO_FILE_PATH = f"test/{i}.mp3"
        MP4ToMP3(VIDEO_FILE_PATH, AUDIO_FILE_PATH)
        
    
