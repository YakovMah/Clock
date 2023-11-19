from tkinter import *
from time import *

#this TK line make one other new window
#window = Tk()


def update():
    time_string = strftime("%H:%M:%S %p")
    time_lable.config(text=time_string)
  

    day_string = strftime("%A")
    day_label.config(text=day_string)


    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    name_string = ("Yakov Mahfoda")
    name_lable.config(text=name_string)

    window.after(1000,update)

window = Tk()
window.title("Clock")
icon_path = "icons\clock.ico"
window.iconbitmap(icon_path)

time_lable = Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_lable.pack()

day_label = Label(window,font=("ink Free",25))
day_label.pack()

date_label = Label(window,font=("ink Free",30))
date_label.pack()

name_lable = Label(window,font=("ink free",18))
name_lable.pack()

update()

window.mainloop()