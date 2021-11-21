# we have to import all files (*) from the tkinter module
from tkinter import *

# to create window 
root = Tk() # root widget

# to print text using label widget
myLabel = Label(root, text="Hello World, yo this is George. waddup fellas !!")

# to put the label widget in the root window
myLabel.pack()

# to create event loop
root.mainloop()

