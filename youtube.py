'''Need to add showing thumbnail of youtube video..........'''
from tkinter import *
from pytube import YouTube
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
from urllib.request import urlopen

#Download function
def show():
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
        stream_list=yt.streams.filter(file_extension='mp4', progressive="True")
    except:
        print("Connection error...")

    for st in stream_list:
        new_line(st)
        print(st.resolution)
        print(st.itag)

    save()

#Showing thumbnail
def thumbnail(url):
    u = urlopen(url)
    raw_data = u.read()
    u.close()

    photo = ImageTk.PhotoImage(data=raw_data)
    label_thumbnail = Label(image=photo)
    label_thumbnail.image = photo
    label_thumbnail.pack()

#Show resolution on button
def new_line(stream):
    but_res = Button(frame3, text=stream.resolution, command=lambda:download(stream.itag))
    but_res.pack()


#Save button function
def save():
    pass
#Download video
def download(itag):
    print("Downloading video with itag = ",itag)
    stream = yt.streams.get_by_itag(itag)
    stream.download()
#Tkinter window
root=Tk()
root.title('Youtube downloader')
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
    font = "Roboto 35 bold",
    foreground = "red",
    background = "white",
    text = "Yotube downloader")
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

entry1 = Entry(frame2,width=60)
entry1.grid(row=0,column=1)


#Download button
but_download = Button(frame, text="Show", command=show)
but_download.pack(pady=1)

#Resolution and itag
frame3= Frame(frame,background='white')
frame3.pack(fill= BOTH, padx= 10, pady=0)

root.mainloop()