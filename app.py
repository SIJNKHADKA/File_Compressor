
#   Main python file to run

import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter
import tkinter.font as font

#   Import compressor file
from compressor import *

width = 600
height= 400
lightThemeBg = "#26242f"
darkThemeBg = "#dee4e7"

win = Tk()
win.title("File Compressor")

if 'posix' == os.name:
    img = PhotoImage(file="imgs/app_icon.gif")
    win.iconphoto(True,img)
else:
    win.iconbitmap("imgs/app_icon.ico")


#   Set window size

win.geometry("{}x{}".format(width, height)) # same as win.geometry("600x400")
win.config(bg = darkThemeBg)

#   Load images
lightState = PhotoImage(file="imgs/light.png")
darkState = PhotoImage(file="imgs/dark.png")



lightMode = True

#   Canvas that displays home image
canvas = Canvas(win, width=300,bd=0, highlightthickness=0, relief='ridge', height=300, bg = darkThemeBg)
canvas.place(x = 50,y =  100)
homeImg = PhotoImage(file="imgs/home_img.png").subsample(2, 2)


# Create the image on the canvas without a box-like background
canvas.create_image(0, 0, anchor="nw", image=homeImg)

#   Display success message 
def displayMessageBox(title, description):
    messagebox.showinfo(title, description)    #   Show success message box

#   Switch mode on pressing light or dark button
def switchMode():
    global lightMode
    if lightMode:
        button.config(image = darkState, bg = lightThemeBg, activebackground=lightThemeBg)
        canvas.config(bg = lightThemeBg)

        win.config(bg = lightThemeBg)
        lightMode = False
    else:
        button.config(image = lightState, bg = darkThemeBg, activebackground=darkThemeBg)
        canvas.config(bg = darkThemeBg)

        win.config(bg = darkThemeBg)
        lightMode = True
    
def compressFile():
    #  openFileDialog for file compression
    win.filename = filedialog.askopenfilename(initialdir=os.path.normpath("C://"), title = "Select A Text File", filetypes=(("text files", "*.txt"),)) # may use this for all files, ("all files", "*.*")
    file_path =win.filename # This prints out selected file name
    # NOw proceed to apply algorithm from this filename
    # Better pass this filename as parameter to function from another file to do operation
    compressFile=compress()
    compressFile.compressor(file_path)
    
    #   Bin file saved to same location as txt file
    
    displayMessageBox("Compression Success", "You have succesfully compressed file to same directory.")
    
    pass

def extractFile():
    #    open file dialog for file extraction
    win.filename = filedialog.askopenfilename(initialdir=os.path.normpath("C://"), title = "Select A Binary File", filetypes=(("binary files", "*.bin"),))
    file_path =win.filename 
    print(win.filename) # This prints out selected file name
    # NOw proceed to apply algorithm from this filename
    decompressFile = compress()
    decompressFile.decompressor(file_path)
    displayMessageBox("Extraction Success", "You have succesfully extracted file to same directory.")
    

#   Place theme button with light theme default
button = Button(win, image=lightState, bd = 0, bg = darkThemeBg, activebackground=darkThemeBg, command = switchMode)
button.pack(padx=50, pady = 50)
button.place(x = width - 150, y = 10)


# Use CTkButton instead of tkinter Button for compress and extract button
compressButton = customtkinter.CTkButton(master=win, text_color=("black", "black"), text="Compress file",hover=True, hover_color="#0b6eca", width=170,height=50,border_width=0,corner_radius=0,text_font=("Courier", 12), command=compressFile)
compressButton.place(x = 3*width/4 , y =height/2 - 30, anchor=CENTER)

# extractButton = Button(win, text = "Extract File", command = openFileDialogForExtraction)
# extractButton.place(x = 3*width/4 , y =height/2 + 50)


# Use CTkButton instead of tkinter Button
extractButton = customtkinter.CTkButton(master=win, text="Extract file",text_color=("black", "black"),hover=True, hover_color="#0b6eca", width=170,height=50,border_width=0,corner_radius=0,text_font=("Courier", 12), command=extractFile)
extractButton.place(x = 3*width/4 , y =height/2 + 50, anchor=CENTER)

win.mainloop()
