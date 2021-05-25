from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry = ('300x300')

def commandTest():
    messagebox.showinfo(title = "Oba!!")
    buttonTest['image'] = buttonImage2


buttonImage1 = PhotoImage(file = 'TempBranco.png')
buttonImage2 = PhotoImage(file = 'TempAzul.png')

buttonTest = Button(root, image = buttonImage1, command = commandTest, borderwidth = 0)
buttonTest.place(x = 10, y = 10)


mainloop()