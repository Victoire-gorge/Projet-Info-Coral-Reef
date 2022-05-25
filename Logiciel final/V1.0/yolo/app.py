from concurrent.futures import process
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from turtle import right, update
from PIL import Image, ImageTk
import subprocess
from subprocess import PIPE
import os
from time import process_time

root = Tk()
#root.geometry("500x300")
root.resizable(False,False)

in_dir = []
out_dir = []
folder_pos = 0
elapsed_time = 0

def update_image(path):
    image = Image.open(path)
    image = image.resize((300,300),Image.ANTIALIAS)
    display_image = ImageTk.PhotoImage(image)

    label = tkinter.Label(image=display_image)
    label.image = display_image

    image_holder.create_image(25,25, anchor=NW, image=display_image)

def get_first_file(input_dir,length):
    output = input_dir
    for i in range(length):
        output += '/' + os.listdir(output)[-1]
    return output 

def movein_folder(shift):
    try:
        folder_pos += shift
        print(folder_pos)
    except:
        print("Success")

def select_file():
    filetypes = (
        ('Pictures', '*.jpg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    in_dir.append(filename)
    update_image(in_dir[-1])

def select_folder():
    filename = fd.askdirectory(
        title='Open a folder',
        initialdir='/'
    )
    
    if len(os.listdir(filename)) > 0:
        in_dir.append(filename)
        #movein_folder(0)
        

def display_in_dir():
    cmd='python yolo/detect.py --source ' + in_dir[-1]
    p = subprocess.Popen(cmd, shell=True, stdout=PIPE)
    out,err = p.communicate()
    output_dir = get_first_file('./yolo/runs/detect',2)
    out_dir.append(output_dir)
    update_image(out_dir[-1])


detect_button = Button(
    root, 
    text="Detect", 
    width=20,
    command=display_in_dir
    )

open_button = Button(
    root,
    text='Open a File',
    width=20,
    command=select_file
)

"""
open_folder_button = Button(
    root,
    text='Open a Folder',
    width=20,
    command=select_folder
)
"""

left_arrow_button = Button(
    root,
    width=3,
    text="<",
    command=movein_folder(-1),
    state=DISABLED
)

right_arrow_button = Button(
    root,
    width=3,
    text=">",
    command=movein_folder(1),
    state=DISABLED
)

image_holder = Canvas(
    root,
    width=350,
    height=350,
    bg='gray'
)

time_display = Label(
    root,
    width=20,
    text="Elapsed time: 0.00s"
)

open_button.grid(column=2,row=0)
#open_folder_button.grid(column=2,row=1)
left_arrow_button.grid(column=0,row=11)
right_arrow_button.grid(column=1,row=11)
detect_button.grid(column=2,row=2)
time_display.grid(column=2,row=3)
image_holder.grid(row=0,column=0,rowspan=10,columnspan=2)

root.mainloop()