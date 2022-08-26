import os

from pytube.cli import on_progress
from pytube import YouTube

video_url = input("paste ur video link:  ")


try:
    yt = YouTube(video_url, on_progress_callback = on_progress)
    yt.streams\
        .filter(file_extension='mp4')\
        .get_highest_resolution()\
        .download(os.path.curdir+"/videos")

except EOFError as err:
    print(err)

else:
    print("Successfully Downloaded!")
