try:
  import Tkinter              # Python 2
  import ttk
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk



def load():

  root = Tkinter.Tk()

  ft = ttk.Frame()
  

  ft.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)

  pb_hd = ttk.Progressbar(ft, orient='horizontal', mode='determinate')
  

  pb_hd.pack(expand=True, fill=Tkinter.BOTH, side=Tkinter.TOP)
  
  pb_hd.start(10)
  

  root.mainloop()


load();