
#WEB PAGE GENERATOR ASSIGNMENT Step 265

import webbrowser
from tkinter import *
import tkinter as tk

# Frame is Tkinter Frame class that our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define master frame configuration
        self.master = master
        self.master.title("The Web Page Generator")

        # Label
        self.lbl_description = Label(self.master,text='Input content for body of your website')
        self.lbl_description.grid(row=0, column=0, padx=(25,15), pady=(10,0), sticky=W)

        # Text box
        self.txt_box1 = tk.Entry(self.master,width=70,text='')
        self.txt_box1.grid(row=1, column=0, padx=(25,15), pady=(10,0), sticky=W)

        # Button
        self.btn_create = Button(self.master,width=12,height=1,text='Create Website',command=lambda: createWebsite(self))
        self.btn_create.grid(row=2, column=0, padx=(25,20), pady=(10,20), sticky=W)
        

# Function that is called after you enter data in text box and creates web site page in new tab.
def createWebsite(self):
    html_top ="""
    <html>
        <body>
            <h1>
                Stay tuned for our amazing summer sale!
            </h1>
    """
    html_middle = self.txt_box1.get()
    html_bottom="""
        </body>
    </html>
    """

    with open("index.html", "w") as file:
        file.write(html_top + html_middle + html_bottom)

    url = 'index.html'
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
