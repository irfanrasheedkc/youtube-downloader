from pytube import YouTube
from moviepy.editor import *
import os
def download_1080p:
  yt = YouTube('https://www.youtube.com/watch?v=pcqsKpLLtUw')
  vid = yt.streams.filter(res="1080p").first().download()
  os.rename(vid, 'video_file.mp4')

  aud = yt.streams.filter(only_audio=True).first().download()
  os.rename(aud, 'audio_file.mp4')


  video_clip = VideoFileClip('video_file.mp4')
  audio_clip = AudioFileClip('audio_file.mp4')
  videoclip = video_clip.set_audio(audio_clip)
  videoclip.write_videofile("final.mp4")
  file_path = 'video_file.mp4'
  if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has been deleted")
  file_path = 'audio_file.mp4'
  if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has been deleted")