import moviepy.editor
video = moviepy.editor.VideoFileClip('deunavez.mp4')

audio = video.audio
audio.write_audiofile('deunavez.mp3')

#put the video name in (VideoFileClip)
#put the same name in the auidiofile as an mp3
