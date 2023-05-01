from tkinter import *
import os
from tkinter.messagebox import *

root = Tk()
root.title("Admin page")
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry(f"{w}x{h}")

def newoperator():
    root.destroy()
    import operatordetails
def newbus():
    root.destroy()
    os.startfile(".\\addbusdetails.py")
def newroute():
    root.destroy()
    os.startfile(".\\busrouteaadd.py")
def newrun():
    root.destroy()
    os.startfile(".\\busrunningdetails.py")


bus = PhotoImage(file=".\\Bus_for_project.png")
homeimg = PhotoImage(file=".\\home.png")

Label(root,image=bus).grid(pady=10,row=0,column=0,columnspan=4,padx = (w/3,0))
Label(root,text="Online Bus Booking System",font = "Arial 22 bold",bg="light blue",fg = "red").grid(pady=12,row=1,column=0,columnspan=4,padx = (w/3,0))
Label(root,text="Add New Details to DataBase",font = "Arial 18 bold",fg="green").grid(pady=12,row=2,column=0,columnspan=4,padx = (w/3,0))



btn1 = Button(root,text="New Operator ",font = "Arial 14 bold",bg = "lightgreen",command=newoperator)
btn1.grid(padx=(w/3,0),row=3,column=0,pady=20)
btn2 = Button(root,text="New Bus ",font = "Arial 14 bold",bg="orange",command=newbus)
btn2.grid(row=3,column=1,pady=20,padx=20)
btn3 = Button(root,text="New Route ",font = "Arial 14 bold",bg="lightblue",command=newroute)
btn3.grid(row=3,column=2,pady=20,padx=20)
btn4 = Button(root,text="New Run ",font = "Arial 14 bold",bg="lightpink",command=newrun)
btn4.grid(row=3,column=3,pady=20,padx=20)

def fun():
    if askyesno('Continue','Do you want to contine the app?'):
        root.destroy()
        os.startfile(".\\frontpage.py")
    else:
        showinfo('thanks','thanks for using python bus')
        root.destroy()

root.protocol('WM_DELETE_WINDOW',fun)


root.mainloop()
