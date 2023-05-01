from tkinter import *
from tkinter.messagebox import *
# from seatbooking import mobileno
from database import *
import os

root = Tk()
root.title("bus ticket generated")
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry(f"{w}x{h}")


f1 = Frame(root)
f1.grid(row=0,column=0)
f2 = Frame(root,relief='groove',bd=3)
f2.grid(row=3,column=0,padx=(w/3,0))
    

bus = PhotoImage(file=".\\Bus_for_project.png")
homeimg = PhotoImage(file=".\\home.png")


Label(f1,image=bus).grid(pady=10,row=0,column=0,columnspan=2,padx = (w/3,0))
Label(f1,text="Online Bus Booking System",font = "Arial 22 bold",bg="light blue",fg = "red").grid(pady=12,row=1,column=0,columnspan=2,padx = (w/3,0))
Label(f1,text="Bus Ticket",font = "Arial 10 bold").grid(pady=12,row=2,column=0,columnspan=2,padx = (w/3,0))
curser.execute('select max(bookingref) from bookinghistory')
max = curser.fetchall()
max = max[0][0]
max = int(max)


curser.execute('select * from bookinghistory where bookingref = ? ',(max,))
ticket = curser.fetchall()

Label(f2,text=f"Passengers : {ticket[0][1]}",font = "Arial 10 bold").grid(row=3,column=0)
Label(f2,text=f"Gender: {ticket[0][2]}",font = "Arial 10 bold").grid(row=3,column=1)
Label(f2,text=f"No of seats: {ticket[0][3]}",font = "Arial 10 bold").grid(row=4,column=0)
Label(f2,text=f"Phone: {ticket[0][0]}",font = "Arial 10 bold").grid(row=4,column=1)
Label(f2,text=f"Age: {ticket[0][4]}",font = "Arial 10 bold").grid(row=5,column=0)
Label(f2,text=f"Fare Rs: {ticket[0][9]}",font = "Arial 10 bold").grid(row=5,column=1)
Label(f2,text=f"Booking Ref:{ticket[0][10]}",font = "Arial 10 bold").grid(row=6,column=0)
Label(f2,text=f"Bus Details: {ticket[0][11]}",font = "Arial 10 bold").grid(row=6,column=1)
Label(f2,text=f"Travel on: {ticket[0][6]}",font = "Arial 10 bold").grid(row=7,column=0)
Label(f2,text=f"destination: {ticket[0][8]}",font = "Arial 10 bold").grid(row=7,column=1)
Label(f2,text=f"Boarding Point: {ticket[0][7]}",font = "Arial 10 bold").grid(row=8,column=0)
Label(f2,text=f"* Total amount Rs {ticket[0][9]}.00/- to be paid at the time of boeding the bus",font = "Arial 8").grid(row=9,column=0,columnspan=2)

showinfo("success","seat booked!")

def fun():
    if askyesno('Continue','Do you want to contine the app?'):
        root.destroy()
        os.startfile(".\\frontpage.py")
    else:
        showinfo('thanks','thanks for using python bus')
        root.destroy()

root.protocol('WM_DELETE_WINDOW',fun)


root.mainloop()
