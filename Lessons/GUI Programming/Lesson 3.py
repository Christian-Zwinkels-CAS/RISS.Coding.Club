from tkinter import *


root = Tk()
root.title("Getting User Input")

def print_Details(): #You need to pass event as one of the arguments if using the bind method
	us = usr_e.get() #Gets the value of usr_e and assigns it to us
	pas = passwr_e.get()

	ussr = Label(root, text="Username: " + us)
	passw = Label(root, text="Password: " + pas)

	ussr.grid(row=3, column=0, sticky=W)
	passw.grid(row=4, column=0, sticky=W)

usr = Label(root, text="Username", anchor=W)
passwr = Label(root, text="Password", anchor=W)

but = Button(root, text="Show me my username and password", command=print_Details) #When the button is clicked call the function print_Details
#but.bind("<Button-1>", print_Details) You can use this if you want to bind the funtion to other button clicks

usr_e = Entry(root)
passwr_e = Entry(root)

usr.grid(row=0, column=0, sticky=W)
passwr.grid(row=1, column=0, sticky=W)

but.grid(row=2, column=0, columnspan=2)

usr_e.grid(row=0, column=1)
passwr_e.grid(row=1, column=1)

root.mainloop()
