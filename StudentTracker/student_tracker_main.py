#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python Ver:   3.9.0
#
# Author:       Frank Inberg 
#
# Tested OS:    This code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk
from tkinter import messagebox


# Be sure to import out other modules
import student_tracker_gui
import student_tracker_func

# Frame is the Tkinter frame class that our own class wll inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(400,325) #(Width, Height)
        self.master.maxsize(400,325)
        # Call function to center window.
        student_tracker_func.center_window(self,400,325)
        self.master.title("The Student Tracker")
        self.master.configure(bg="#F0F0F0")
        # User clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracker_func.ask_quit(self))
        arg = self.master


        # Load in the GUI
        student_tracker_gui.load_gui(self)

if __name__ == "__main__":  
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
