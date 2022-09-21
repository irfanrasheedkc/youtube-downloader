'''Download playlist....'''

from tkinter import *
from pytube import Playlist
from pytube import YouTube
import os
from tkinter import messagebox
from tkinter import ttk

def show():
    pb1.pack()
    pb1.start()
    root.update()
    global pl
    v.pack(side=RIGHT, fill='y')
    h.pack(side=BOTTOM, fill='x')
    vid_text = ""
    i = 1
    link = entry1.get()
    pl = Playlist(link)
    length=len(pl)
    for video in pl:
        root.update()
        pb1['value'] = (float(i)/length)*100
        yt = YouTube(video)
        vid_text = "\n" + str(i) + ".  " + yt.title+ "\n"
        text.insert(END, vid_text)
        text.pack()
        i = i+1
        print(yt.title)
        # label_vid.config(text=vid_text)
    but_download_video.grid(row=0, column=0)
    but_download_audio.grid(row=1, column=0)
    pb1.stop()
    pb1.forget()

'''Download all videos ....shows if a download is completed'''
def download_all_video():
    global root
    pb1.pack()
    pb1.start()
    root.update()
    global pl
    i = 1
    length = len(pl)
    for video in pl:
        root.update()
        pb1['value'] = (float(i) / length) * 100
        yt = YouTube(video)
        yt.streams.get_highest_resolution().download()
        print("completed file : "+str(i))
        i = i+1
    messagebox.showinfo("Succes", "Download completed succesfully")

def download_all_audio():
    global root
    pb1.pack()
    pb1.start()
    root.update()
    root.update()
    global entry_rename
    i = 1
    length = len(pl)
    for video in pl:
        root.update()
        pb1['value'] = (float(i) / length) * 100
        yt = YouTube(video)
        df= yt.streams.filter(only_audio=True)
        downloaded_file = df[0].download("./downloads")
        root , ext = os.path.splitext(downloaded_file)
        os.rename(downloaded_file, root + '.mp3')
        print("completed file : " + str(i))
        i = i + 1
    messagebox.showinfo("Succes", "Download completed succesfully")


#Tkinter window
root=Tk()
root.title('Playlist downloader')
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
    font = "Roboto 30 bold",
    foreground = "red",
    background = "white",
    text = "Yotube playlist downloader")
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
if 'www.youtube.com/playlist' in pyperclip.paste():
    link_text = pyperclip.paste()
entry1 = Entry(frame2,width=60)
entry1.insert(0,link_text)
entry1.grid(row=0,column=1)


#Show button
but_download = Button(frame, text="Show", command=show)
but_download.pack(pady=1)

#Progressbar for show button
pb1 = ttk.Progressbar(
    frame,
    orient='horizontal',
    mode='determinate',
    length=280
)

#Audio and video frame
frame4 = Frame(frame,background='white')
frame4.pack(fill= BOTH, padx= 240, pady=0)

#Video button
but_download_video = Button(frame4, text="Save All Video", command=download_all_video)

#Audio button
but_download_audio = Button(frame4, text="Save All Audio", command=download_all_audio)

#Frame for video names
# Add a frame to set the size of the window
frame5= Frame(root, relief= 'sunken')
frame5.pack(fill= BOTH, expand= True, padx= 10, pady=0)
frame5.configure(bg='white')

#Video names
frame3= Frame(frame5, background='white')
frame3.pack( padx= 10, pady=10)

#Add a vertical scrollbar
v=Scrollbar(frame3, orient='vertical')
h=Scrollbar(frame3, orient='horizontal')

# Add a text widget
text=Text(frame3, font=("Georgia, 12"), yscrollcommand=v.set , xscrollcommand=h.set)


root.mainloop()