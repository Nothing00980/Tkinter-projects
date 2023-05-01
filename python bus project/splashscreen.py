from tkinter import *
import os

root = Tk()
root.title("Online bus booking app")
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry(f"{w}x{h}")
f1 = Frame(root)
f1.grid(row=0,column=0,pady = (h/7,0))
bus = PhotoImage(file=".\\Bus_for_project.png")

Label(f1,image=bus).grid(padx=w/3,pady=10,row=0,column=0)
Label(f1,text="Online Bus Booking System",font = "Arial 22 bold",bg="light blue",fg = "red").grid(padx=w/3,pady=12,row=1,column=0)
Label(f1,text="Name:Yuvraj Bhati",font = "Arial 14 bold",fg = "blue").grid(padx=w/3,pady=(20,0),row=2,column=0)
Label(f1,text="Er: 211B362",font = "Arial 14 bold",fg = "blue").grid(padx=w/3, pady=(10,10),row=3,column=0)
Label(f1,text="Mobile: 455454545",font = "Arial 14 bold",fg = "blue").grid(padx=w/3,pady=(0,20),row=4,column=0)
Label(f1,text="Submitted to : Dr mahesh kumar",font = "Arial 18 bold",bg="light blue",fg = "red").grid(padx=w/3,pady=(37,5),row=5,column=0)
Label(f1,text="Project Based Learning",font = "Arial 13 bold",fg = "red").grid(padx=w/3,row=6,column=0)


def fun(e=0):
    root.destroy()
    os.startfile(".\\frontpage.py")
root.bind('<KeyPress>',fun)

root.mainloop()
