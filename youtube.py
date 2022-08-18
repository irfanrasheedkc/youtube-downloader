from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

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
frame1= Frame(frame, relief= 'sunken',background='white')
frame1.pack(fill= BOTH, expand= True, padx= 10, pady=0)
label = Label(
    frame1,
    font = "Roboto 40 bold",
    foreground = "red",
    background = "white",
    text = "Welcome")
label.pack(pady=30)

#Paste download link
but_link = Button(frame, text="Browse file", command=browseFiles)
button1.pack(pady=1)

root.mainloop()
