# Import necessary modules
import subprocess
from tkinter import *


def update():
    subprocess.call(['apt', 'update'])

def upgrade():
    subprocess.call(['apt', 'dist-upgrade'])

# Create the GUI
window=Tk()
window.title('GUI Advanced Package Tool (GAPT)')
window.geometry('350x100')
l1=Label(window,text='WARNING: Do not press each button more than once as it interrupts the command that is currently running.')
b1=Button(window,text='Update',command=update)
b2=Button(window,text='Upgrade',command=upgrade)
b1.pack(side=LEFT,padx=50)
b2.pack(side=RIGHT,padx=50)
window.configure(background='white')
window.mainloop()