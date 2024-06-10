import socket
from tkinter import * 
from tkinter import ttk 
from tkinter import filedialog

window =  Tk() 
window.title('Music Window') 
window.geometry("300x300")
window.configure(bg = 'LightSkyBlue')

PORT = 8050 
IP_ADRESS = '127.0.0.1' 
SERVER = None 
BUFFER_SIZE = 4096



def musicWindow():
    
    selectlabel = Label(window, text= "Select Song", bg= 'LightSkyBlue', font = ("Calibri",10))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox',bg = 'LightSkyBlue', borderwidth=2, font = ("Calibri",10))
    listbox.place(x=10, y=18)
    
    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)
    
    PlayButton = Button(window,text="Play",width = 10,bd=1,bg="SkyBlue",font = ("Calibri",10))
    PlayButton.place(x=30,y=200)
    
    UploadButton = Button(window,text="Upload",bd=1,bg="SkyBlue", font = ("Calibri",10))
    UploadButton.place(x=30,y=250)
    
    DownloadButton = Button(window,text="Download",bd=1,bg="SkyBlue", font = ("Calibri",10))
    DownloadButton.place(x=30,y=250)
    
    StopButton=Button(window,text="Stop",bd=1, bg ="SkyBlue",font = ("Calibri",10))
    StopButton.place(x=30,y=200)
    
    infoLabel = Label(window,text = "", bg="blue",font =("Calibri",10)) 
    infoLabel.place(x = 4,y = 200) 

    window.mainloop() 


def setup():
    global SERVER
    global PORT
    global IP_ADRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADRESS, PORT))
    musicWindow()
setup()