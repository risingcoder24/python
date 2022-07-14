from faulthandler import disable
from tkinter import*

root = Tk()


def myClick():
    myLabel = Label(root, text="Look I clicked a Button!")
    myLabel.pack()



myButton = Button(root, text = "Click me!", padx=5, pady= 5, command=myClick, fg="blue", bg="red") #state = DISABLED)
myButton.pack()
#myButton.grid()
root.mainloop()