
"""
Created on Sun Jan 14 22:03:43 2018

@author: gabrieltenorio
"""

from timeit import default_timer as timer
from tkinter import *
from tkinter import filedialog,messagebox
import Reader


def idNotFound(error):
        aws = messagebox.askyesno(title=error, message=error+'\n'+'Do you want to add it?')
        if (aws == 1):
            error = error.split(':')
            error = error[1][1:]
            teste.load()
        else:
            pass

def main():
    
    def selectDirectory():
        try:
            diretory = filedialog.askdirectory()
        except Exception as e:
            print(e)
        OutputPath.set(diretory)
        
    def selectDirectory():
        try:
            diretory = filedialog.askdirectory()
        except Exception as e:
            print(e)
        updatePath.set(diretory)
    

    def selectFile():
        file = filedialog.askopenfile()
        try:
            fPath = file.name
            InFile.set(fPath)
        except Exception as e:
            pass
    
    def createFiles(path, outPath):
        if(path == ''):
            messagebox.showinfo("Errou", "the path is empty")
        elif(outPath ==''):
            messagebox.showinfo("Errou", "the Output path is empty")
        else:
             start = timer()
             Reader.readMainFile(path,outPath)
             end = timer()
             print('Tempo de execução: ', start-end)
             root.destroy()
             
    def updateDB():
        root2 = Tk()   
        updatePath = StringVar()
        OutputPath = StringVar()
        root2.title("Selecione os arquivos para atualizar")
        root2.resizable(0, 0)
        
        DBlabel1 = Label(root2, text="Input").grid(row=0,column=0,columnspan=2,)
        DBtext = Entry(root2,textvariable=updatePath, width = 54, state=DISABLED).grid(row=1,column=0)
        DBbutton = Button(root2,text='Select', command=selectDirectory).grid(row=1,column=1)
        
        DBbutton2 = Button(root2,text='Create files', command=lambda: createFiles(updatePath.get()), width = 55).grid(row=4,column=0,columnspan=2,)
             
    
    
    root = Tk()   
    root.iconbitmap('marcos.ico')
    InFile = StringVar()
    OutputPath = StringVar()
    root.title("Negócio do Marcos")
    root.resizable(0, 0)
    
    myMenu = Menu()
    listone = Menu()
    myMenu.add_cascade(label="Update DataBase", command = updateDB)
    root.config(menu=myMenu)
    
    label1 = Label(root, text="Input").grid(row=0,column=0,columnspan=2,)
    text = Entry(root,textvariable=InFile, width = 54, state=DISABLED).grid(row=1,column=0)
    button = Button(root,text='Select', command=selectFile).grid(row=1,column=1)
    
    
    label2 = Label(root, text="Output").grid(row=2,column=0,columnspan=2,)
    textOut = Entry(root,textvariable=OutputPath, width = 54, state=DISABLED).grid(row=3,column=0)
    buttonOut = Button(root,text='Select', command=selectDirectory).grid(row=3,column=1)
   
    
    button2 = Button(root,text='Create files', command=lambda: createFiles(InFile.get(),OutputPath.get()), width = 55).grid(row=4,column=0,columnspan=2,)
   
    root.mainloop()

if __name__ == "__main__":
    main()