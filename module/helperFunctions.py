import shutil
import requests
from moviepy.editor import *
import eyed3
from eyed3.id3.frames import ImageFrame
import os


def MP4ToMP3(mp4_path: str):
    mp3_path = mp4_path.split(".")[0] + ".mp3"
    file = AudioFileClip(mp4_path)
    file.write_audiofile(mp3_path)
    file.close()
    os.remove(mp4_path)
    return mp3_path


def zip(zip_name: str, dir_path: str):
    if not os.path.exists("zips/"):
        os.mkdir("zips/")
    x = shutil.make_archive(zip_name, "zip", dir_path)
    y = r"" + x.split("\\")[-1]
    os.rename(y, f"zips/{y}")
    zip_path = f"zips/{y}"
    return zip_path


def setCoverArt(image_name: str, img_url: str, mp3_path: str):
    if not os.path.exists("songs/imgs/"):
        os.mkdir("songs/imgs/")
    img_data = requests.get(img_url).content
    with open(f"songs/imgs/{image_name}.png", "wb") as f:
        f.write(img_data)

    img_path = f"songs/imgs/{image_name}.png"

    audiofile = eyed3.load(mp3_path)
    if audiofile.tag == None:
        audiofile.initTag()
    audiofile.tag.images.set(
        ImageFrame.FRONT_COVER, open(img_path, "rb").read(), "image/png"
    )
    audiofile.tag.save()
    os.remove(img_path)
