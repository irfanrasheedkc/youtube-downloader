'''Welcome window....'''

from tkinter import *
import os

def run_video():
    window.destroy()
    os.system('python youtube.py')

def run_playlist():
    window.destroy()
    os.system('python playlist.py')


#Creating tkinter window
window=Tk()
window.title('Youtube downloader')
window.geometry(f'600x600')
window.resizable(False,False)

#Title icon
photo = PhotoImage(file = "1.png")
window.iconphoto(False, photo)


#Create video button
button_vid = Button(window, text = "Video" ,  bg="#eb4034" , fg="white", activebackground="white" ,activeforeground="red", bd=10 , height = 18 , width=82 , command=run_video )
button_vid.grid(row=0 , column=0)

#Creating playlist button
button_play = Button(window, text = "Playlist", bg="#eb4034" ,fg="white", activebackground="white" ,activeforeground="red", bd=10 , height = 18 , width=82 , command=run_playlist)
button_play.grid(row = 1 , column = 0)


window.mainloop()