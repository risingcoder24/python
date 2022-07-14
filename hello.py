from tkinter import*

root = Tk()

# creating a lable widget

mylabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
mylabel2 = Label(root, text="My name is Khushi").grid(row=1,column=5)
mylabel3 = Label(root, text="           ").grid(row=1,column=1)

# showing it onto the screen

# mylable1.pack()
# mylabel1.grid(row=0, column=0)
# mylabel2.grid(row=1,column=5)
# mylabel3.grid(row=1,column=1)

root.mainloop()