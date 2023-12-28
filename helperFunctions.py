import shutil
from moviepy.editor import *

def MP4ToMP3(mp4_path:str):
    mp3_path = mp4_path.split(".")[0] + ".mp3"
    file = AudioFileClip(mp4_path)
    file.write_audiofile(mp3_path)
    file.close()
    os.remove(mp4_path)

def zip(zip_name:str, dir_path:str):
    shutil.make_archive(zip_name, "zip", dir_path)