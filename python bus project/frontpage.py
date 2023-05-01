from tkinter import *
import os
from tkinter.messagebox import *

root = Tk()
root.title("MEnu")
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry(f"{w}x{h}")

def seatbooking():
    root.destroy()
    os.startfile(".\\seatbooking.py")

def checkbookedseat():
    root.destroy()
    os.startfile(".\\checkyourbooking.py")
def addbusdetails():
    root.destroy()
    os.startfile(".\\adddetails.py")



bus = PhotoImage(file=".\\Bus_for_project.png")

Label(root,image=bus).grid(padx=w/3,pady=10,row=0,column=0,columnspan=3)
Label(root,text="Online Bus Booking System",font = "Arial 22 bold",bg="light blue",fg = "red").grid(padx=w/3,pady=12,row=1,column=0,columnspan=3)

btn1 = Button(root,text="Seat Booking",font = "Arial 12 bold",command=seatbooking,bg="lightgreen")
btn1.grid(row=2,column=0,pady=40)
btn2 = Button(root,text="Check Booked Seat",font = "Arial 12 bold",command=checkbookedseat,bg="lightgreen")
btn2.grid(row=2,column=1,pady=40)
btn3 = Button(root,text="Add Bus Details",font = "Arial 12 bold",command=addbusdetails,bg="green")
btn3.grid(row=2,column=2,pady=40)
Label(root,text="For Admin Only",fg = "red",font="Arial 10 bold ").grid(row=3,column=2,pady=1)








def fun():
    if askyesno('Quit','Do you wish to close the app?'):
        showinfo('thanks','thanks for using python bus')
        root.destroy()
    else:
        pass

root.protocol('WM_DELETE_WINDOW',fun)






root.mainloop()