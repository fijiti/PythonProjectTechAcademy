
# FILE TRANSFER ASSIGNMENT PART THREE

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import time
import shutil
import os

# Frame is Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.title("Check files")
        # Confirm user wants to quit when clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
       

        # Text boxes
        self.txt_box1 = tk.Entry(self.master,width=50,text='')
        self.txt_box1.grid(row=0, column=1, padx=(10, 25), pady=(46, 0),sticky=N+E+W)
        self.txt_box2 = tk.Entry(self.master,text='')
        self.txt_box2.grid(row=1, column=1, padx=(10, 25), pady=(10, 0),sticky=N+E+W)

        # Buttons
        self.btn_browse1 = tk.Button(self.master,width=12, height=1,text='Browse...',command=lambda: getSourcePath(self))
        self.btn_browse1.grid(row=0, column = 0, padx=(15, 25), pady=(45, 10),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=12, height=1,text='Browse...',command=lambda: getDestinationPath(self))
        self.btn_browse2.grid(row=1, column = 0, padx=(15, 25), pady=(10, 10),sticky=W)
        self.btn_checkFiles = tk.Button(self.master,width=12, height=2,text='Check for files...',command=lambda: checkFilesToMove(self))
        self.btn_checkFiles.grid(row=2, column = 0, padx=(15,25), pady=(5, 20),sticky=E)
        self.btn_close = tk.Button(self.master,width=12, height=2,text='Close Program',command=lambda: ask_quit(self))
        self.btn_close.grid(row=2, column = 1, padx=(0,25), pady=(5, 20),sticky=E)

# Get source directy of files want checked for transfer
def getSourcePath(self):
    dirname = filedialog.askdirectory()
    self.txt_box1.insert(0,dirname)
    

# Get destination path for files that need to be transfered
def getDestinationPath(self):
    dirname = filedialog.askdirectory()
    self.txt_box2.insert(0,dirname)
   
    

# Variable for reference to seconds in a day
SECONDS_IN_DAY = 24 * 60 * 60


def checkFilesToMove(self):
    source = self.txt_box1.get()
    print(source)
    destination = self.txt_box2.get()
    print(destination)
    files = os.listdir(source)

    # Time now in seconds 
    now = time.time()
    before = now - SECONDS_IN_DAY

    # Get last mod time of file
    def last_mod_time(fname):
        return os.path.getmtime(fname)

    # Iterate through source files and see if less than todays date - 24 hours.
    for fname in files:
        src_fname = os.path.join(source, fname)
        # If last mod date less than before 24 hours before today then move file to destination.
        if last_mod_time(src_fname) < before:
            dst_fname = os.path.join(destination, fname)
            shutil.move(src_fname, dst_fname)

# Catch if the user clicks on the windows upper-right 'X' to ensure they want to close app
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
                

        
