from tkinter import*

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.get()
e.insert(0, "Enter your name")  # sets the default value of the box


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Enter your name",
                  padx=5, pady=5, command=myClick)
myButton.pack()


root.mainloop()
