
"""
Created on Sun Jan 14 22:03:43 2018

@author: gabrieltenorio
"""

import os
from tkinter import *
from tkinter import filedialog,messagebox
import Reader


def selectDirectory():
    outPath = filedialog.askdirectory()
    try:
        OutputPath.set(outPath)
    except Exception as e:
        print(e)

def selectFile():
    file = filedialog.askopenfile()
    try:
        fPath = file.name
        InFile.set(fPath)
    except Exception as e:
        pass

def updateDB(path):
    if(path == ''):
        messagebox.showinfo("Errou", "the path is empty")
    else:
         outpath = selectDirectory()
#        Reader.readMainFile(path)
#        root.destroy()


root = Tk()

InFile = StringVar()
OutputPath = StringVar()
root.title("Awin")
root.geometry("550x120")
root.resizable(0, 0)
text = Entry(root,textvariable=InFile, width = 54, state=DISABLED).grid(row=0,column=0)
textOut = Entry(root,textvariable=OutputPath, width = 54).grid(row=1,column=0)
button = Button(root,text='Select', command=selectFile).grid(row=0,column=1)
button2 = Button(root,text='Create files', command=lambda: updateDB(InFile.get())).place(x=200,y=60)
button3 = Button(root,text='Close', command=root.destroy).place(x=300,y=60)



root.mainloop()