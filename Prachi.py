from pytube import YouTube
from tkinter import *

root = Tk()

root.geometry("300x400")
root.title("You tube video downloader")

def youtube():
    a = var.get() #https://www.youtube.com/watch?v=0NV1KdWRHck
    ytvideo=YouTube(a).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    ytvideo.download(r"D:\letsupgrade\praju")
    print("Entry box",a)

l1 = Label(root,text = "YouTube Video link ",fg="red",font=("bold",20))
l1.place(x=30,y=20)

var = StringVar()
el = Entry(root,textvariable=var,width=60)
el.place(x=40,y=80)

b1 = Button(root,text = "Download", command=youtube,bg="green",width=20,fg="white")
b1.place(x=80,y=120)






root.mainloop()