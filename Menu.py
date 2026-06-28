# import only these functions
# which are needed
from tkinter import *
from tkinter.ttk import *
from time import strftime

#creating tkinterwindow
root = Tk()
root.title('Menu Demonstration')

#creating menubar
menubar = Menu(root)

#adding file menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade (label='File', menu=file)
file.add_command (label='New File', command = None)
file.add_command (label='Open', command = None)
file.add_command (label='Save', command = None)
file.add_separator()
file.add_command (label='Exit', command = root.destroy)

#adding edit menu and commansds
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu='Edit')
edit.add_command(label='Cut', command= None)
edit.add_command(label='Copy ', command=None)
edit.add_command(label='Paste ', command=None)
edit.add_command(label='Select all', command=None)
edit.add_separator()
edit.add_command(label='Find', command=None)
edit.add_command(label='Find again', command=None)

#adding help menu
help_ = Menu(menubar, tearoff= 0)
menubar.add_cascade (label= 'Help', menu=help_)
help_.add_command (label='Tk Help', command=None)
help_.add_command (label='demo', command=None)
help_.add_separator()
help_.add_command (label='About Tk', command=None)

#display menu
root.config (menu=menubar)
mainloop()