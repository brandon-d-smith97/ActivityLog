from tkinter import *

root = Tk()
root.geometry("400x400")

def submit():
    actTitle.delete(0, END)
    actMin0.delete(0, END)

actTitle = Entry(root, width=40)
actTitle.grid(row=0, column = 0)
actTitle.insert(0, "Enter title of Activity")

actMin0 = Entry(root, width = 40)
actMin0.grid(row=2, column = 0)
actMin0.insert(0, "Enter Number of Minutes to log")

submit_create = Button(root, text = "Submit Creation", command=submit)
submit_create.grid(row=3,column=0)

root.mainloop()