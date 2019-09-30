from tkinter import *


root = Tk() #Creates the root window
root.title("The Title") #Sets the title

text = Label(root, text="This is a label") #Creates a label
text.pack() #Lazy way to put it in the window

text2 = Label(root, text="This is below the other label")
text2.pack() #By default things get packed from top to bottom

root.mainloop() #Initiates the main loop so that the window doesnt close
