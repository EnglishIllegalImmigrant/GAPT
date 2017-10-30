# Import necessary modules
import subprocess
from tkinter import *

# Define function to update system
def update():
    subprocess.call(['apt', 'update'])

# Define function to upgrade system
def upgrade():
    subprocess.call(['apt', 'dist-upgrade'])

# Create the GUI
window=Tk()
window.title('GUI Advanced Package Tool (GAPT)')
window.geometry('350x100')
b1=Button(window,text='Update',command=update)
b2=Button(window,text='Upgrade',command=upgrade)
b1.pack(side=LEFT,padx=50)
b2.pack(side=RIGHT,padx=50)
window.configure(background='white')
window.mainloop()