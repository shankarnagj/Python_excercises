from tkinter import *

window = Tk()
window.geometry("200x100")
def km_to_miles():
    miles = float(e1_value.get()) * 1.609
    t1.delete("1.0",END)
    t1.insert(END,miles)

b_1 = Button(window, text = "Execute",command =km_to_miles)
b_1.grid(row = 1,column = 0)

e1_value = IntVar()
e1 = Entry(window,textvariable = e1_value)
e1.grid(row = 0,column = 0)

t1 = Text(window,height = 1,width = 10)
t1.grid(row = 2,column = 0)

window.mainloop()