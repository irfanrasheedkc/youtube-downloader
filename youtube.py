'''Issue on downloading 1080p video'''

from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
from urllib.request import urlopen
import os
from moviepy.editor import  *
import pyperclip

global yt

#Show function
def show():
    global link
    global entry_rename
    link = entry1.get()
    try:
        global yt
        yt = YouTube(link)
        print(yt.title)
        label2 = Label(
            frame3,
            font="Roboto 12 bold",
            foreground="black",
            background="white",
            text=yt.title)
        label2.pack()
        thumbnail(yt.thumbnail_url)
    except:
        messagebox.showinfo("Error", "Connection error!!!")
        exit()
    but_download_video.grid(row = 0 , column= 0)
    but_download_audio.grid(row = 0 , column= 1)

    #Rename file
    frame5.pack(fill=BOTH, padx=10, pady=0)
    label_rename = Label(
        frame5,
        font=("Arial", 12),
        background="white",
        text="Name of the file : ")
    label_rename.grid(row = 0 , column = 0)

    entry_rename = Entry(frame5 , width = 55 )
    entry_rename.insert(0, yt.title)
    entry_rename.grid(row = 0 , column = 1)

#Video function
def show_video():
    try:
        stream_list=yt.streams.filter(file_extension='mp4', progressive="True")
    except:
        print("Connection error!!")
    label_vid = Label(
        frame3,
        font="Roboto",
        background="white",
        text="Video : ")
    label_vid.pack()
    for st in stream_list:
        show_res(st)

#Creating button for 1080p
    but_1080 = Button(frame3, text="1080p", command=lambda: download_1080p())
    but_1080.pack()

#Audio function
def show_audio():
    try:
        stream_list=yt.streams.filter(only_audio=True , subtype='mp4')
    except:
        print("Connection error!!")

    label_aud = Label(
        frame3,
        font="Roboto",
        background="white",
        text="Audio only : ")
    label_aud.pack()

    for st in stream_list:
        show_abr(st)

#Showing thumbnail
def thumbnail(url):

    u = urlopen(url)
    raw_data = u.read()
    u.close()

    photo = ImageTk.PhotoImage(data=raw_data)
    label_thumbnail = Label(image=photo)
    label_thumbnail.image = photo
    label_thumbnail.pack()

#Show abr on button
def show_abr(stream):
    itag = stream.itag
    print(type(itag))
    if(itag==139):
        itag = "48kbps"
    if (itag == 140):
        itag = "128kbps"
    if (itag == 141):
        itag = "256kbps"
    but_abr = Button(frame3, text=itag, command=lambda:download(stream.itag,'.mp3'))
    but_abr.pack()

#Show resolution on button
def show_res(stream):
    but_res = Button(frame3, text=stream.resolution, command=lambda:download(stream.itag, '.mp4'))
    but_res.pack()

#Download video
def download(itag,ext):
    global entry_rename
    print("Downloading video with itag = ",itag)
    stream = yt.streams.get_by_itag(itag)
    downloaded_file = stream.download()
    base = entry_rename.get()
    new_file = base + ext
    os.rename(downloaded_file, new_file)
    messagebox.showinfo("Succes", "Download completed succesfully")

#Download 1080p
def download_1080p():
  global link
  # try:
  yt = YouTube(link)
  try:
    vid = yt.streams.filter(res="1080p").first().download()
  except:
    messagebox.showinfo("Not Available", "1080p not available for this video...")
  os.rename(vid , 'video_file.mp4')

  aud = yt.streams.filter(only_audio=True).first().download()
  os.rename(aud, 'audio_file.mp4')


  video_clip = VideoFileClip('video_file.mp4')
  audio_clip = AudioFileClip('audio_file.mp4')

  videoclip = video_clip.set_audio(audio_clip)

  videoclip.write_videofile(entry_rename.get()+'mp4' ,  fps=24, threads=1, codec="libx264")

  file_path = 'video_file.mp4'
  if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has been deleted")

  file_path = 'audio_file.mp4'
  if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has been deleted")

  # except Exception as e:
  #     print(e)
  #     print("Error")


#Tkinter window
root=Tk()
root.title('Video downloader')
root.geometry(f'600x600')
root.resizable(False,False)

#set window color
root.configure(bg='white')

#Title icon
photo = PhotoImage(file = "1.png")
root.iconphoto(False, photo)
# Add a frame to set the size of the window
frame= Frame(root, relief= 'sunken')
frame.pack(fill= BOTH, expand= True, padx= 10, pady=0)
frame.configure(bg='white')

#Heading
frame1= Frame(frame, background='white')
frame1.pack( padx= 10, pady=10)
label = Label(
    frame1,
    font = "Roboto 32 bold",
    foreground = "red",
    background = "white",
    text = "Yotube video downloader")
label.pack(padx=10,pady=0)


#Link paste
frame2= Frame(frame,background='white')
frame2.pack(fill= BOTH, padx= 10, pady=0)
label1 = Label(
    frame2,
    font = "Roboto",
    background = "white",
    text = "Paste link : ")
label1.grid(row=0,column=0)

link_text = ''
if 'www.youtube.com/watch' in pyperclip.paste():
    link_text = pyperclip.paste()
entry1 = Entry(frame2,width=60)
entry1.insert(0,link_text)
entry1.grid(row=0,column=1)


#Show button
but_download = Button(frame, text="Show", command=show)
but_download.pack(pady=1)

#Audio and video frame
frame4= Frame(frame,background='white')
frame4.pack(fill= BOTH, padx= 240, pady=0)

#Video button
but_download_video = Button(frame4, text="Video", command=show_video)

#Audio button
but_download_audio = Button(frame4, text="Audio", command=show_audio)

#Rename file
frame5= Frame(frame,background='white')


#Resolution and itag
frame3= Frame(frame,background='white')
frame3.pack(fill= BOTH, padx= 10, pady=0)

root.mainloop()