'''Download subtitles of youtube video'''

from tkinter import *
from pytube import YouTube
from tkinter import messagebox

#Show function
def show():
    # global link
    # global entry_rename
    link = entry1.get()
    # try:
    global yt
    yt = YouTube(link)
    print(yt.title)
    print(yt.captions)
    for c in yt.captions:
        if "en" in c.code:
            print(c)
            break
    caption = c
    print(caption.generate_srt_captions())
    #
    # except:
    #         messagebox.showinfo("Error", "Connection error!!!")
    #         exit()


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
    font = "Roboto 29 bold",
    foreground = "red",
    background = "white",
    text = "Yotube subtitle downloader")
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

#Show button
but_download = Button(frame, text="Show", command=show)
but_download.pack(pady=1)

root.mainloop()
