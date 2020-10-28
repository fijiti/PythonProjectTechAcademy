
# Assignment Script Gui Challenge Step 261

from tkinter import *
import tkinter as tk

# Frame is Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.title("Check files")
       

        # Text boxes
        self.txt_box1 = tk.Entry(self.master,width=50,text='')
        self.txt_box1.grid(row=0, column=1, padx=(10, 25), pady=(46, 0),sticky=N+E+W)
        self.txt_box2 = tk.Entry(self.master,text='')
        self.txt_box2.grid(row=1, column=1, padx=(10, 25), pady=(10, 0),sticky=N+E+W)

        # Buttons
        self.btn_browse1 = tk.Button(self.master,width=12, height=1,text='Browse...')
        self.btn_browse1.grid(row=0, column = 0, padx=(15, 25), pady=(45, 10),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=12, height=1,text='Browse...')
        self.btn_browse2.grid(row=1, column = 0, padx=(15, 25), pady=(10, 10),sticky=W)
        self.btn_checkFiles = tk.Button(self.master,width=12, height=2,text='Check for files...')
        self.btn_checkFiles.grid(row=2, column = 0, padx=(15,25), pady=(5, 20),sticky=E)
        self.btn_close = tk.Button(self.master,width=12, height=2,text='Close Program')
        self.btn_close.grid(row=2, column = 1, padx=(0,25), pady=(5, 20),sticky=E)
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
                

        
