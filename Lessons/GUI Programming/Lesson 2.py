from tkinter import *

root = Tk()
root.title("Using the grid layout")

usr = Label(root, text="Username", anchor=W) #Anchor aligns the text in this case to the west (yeah I know its weird)
passwr = Label(root, text="Password", anchor=W)

but = Button(root, text="Show me my username and password") #Next lesson we can bind this to a function that shows the user what they typed in

usr_e = Entry(root) #Creates an entry box with allows string input from the user
passwr_e = Entry(root)

usr.grid(row=0, column=0, sticky=W) #Places it to row 1 and column 1 aligning  it to the west
passwr.grid(row=1, column=0, sticky=W)

but.grid(row=3, column=0, columnspan=2) #Columnspan lets the object span over 2 columns

usr_e.grid(row=0, column=1)
passwr_e.grid(row=1, column=1)

root.mainloop()
