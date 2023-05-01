from tkinter import *
from database import *
from tkinter.messagebox import *
import os

root = Tk()
root.title("check your booking page")
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry(f"{w}x{h}")



def checkbooking():
    Label(root,text="                                            ",font = "Arial 10 bold").grid(row=4,column=0,padx = (w/3 ,0))
    Label(root,text="                                             ",font = "Arial 10 bold").grid(row=4,column=1)
    Label(root,text="                                              ",font = "Arial 10 bold").grid(row=5,column=0,padx = (w/3,0))
    Label(root,text="                                              ",font = "Arial 10 bold").grid(row=5,column=1)
    Label(root,text="                                             ",font = "Arial 10 bold").grid(row=6,column=0,padx = (w/3,0))
    Label(root,text="                                                  ",font = "Arial 10 bold").grid(row=6,column=1)
    Label(root,text="                                                      ",font = "Arial 10 bold").grid(row=7,column=0,padx = (w/3,0))
    Label(root,text="                                                   ",font = "Arial 10 bold").grid(row=7,column=1)
    Label(root,text="                                                 ",font = "Arial 10 bold").grid(row=8,column=0,padx = (w/3,0))
    Label(root,text="                                                  ",font = "Arial 10 bold").grid(row=9,column=0,padx = (w/3,0))
    Label(root,text="                                                    ",font = "Arial 10 bold").grid(row=9,column=1)
    Label(root,text="                                                                                                                                         ",font = "Arial 8").grid(row=10,column=0,padx = (w/3,0),columnspan=2)    
    if(entry1.get() == ""):
        showerror('field empty','one of the entries are missing please fill all the details!')
    else:

        if(len(entry1.get()) == 10  ):
            try:

                curser.execute('select * from bookinghistory where mobileno = ?',(int(entry1.get()),))
                res = curser.fetchall()
            except ValueError as e:
                res = []
                showerror('error','incorrect type input in entry')
            if(res == []):
                showinfo('ticket information','no ticket registered from this mobile no!')
            else:

                Label(root,text=f"Passengers : {res[0][1]}",font = "Arial 10 bold").grid(row=4,column=0,padx = (w/3 ,0))
                Label(root,text=f"Gender: {res[0][2]}",font = "Arial 10 bold").grid(row=4,column=1)
                Label(root,text=f"No of seats: {res[0][3]}",font = "Arial 10 bold").grid(row=5,column=0,padx = (w/3,0))
                Label(root,text=f"Phone: {res[0][0]}",font = "Arial 10 bold").grid(row=5,column=1)
                Label(root,text=f"Age: {res[0][4]}",font = "Arial 10 bold").grid(row=6,column=0,padx = (w/3,0))
                Label(root,text=f"Fare Rs: {res[0][9]}.00",font = "Arial 10 bold").grid(row=6,column=1)
                Label(root,text=f"Booking Ref:{res[0][10]}",font = "Arial 10 bold").grid(row=7,column=0,padx = (w/3,0))
                Label(root,text=f"Bus Details: {res[0][11]}",font = "Arial 10 bold").grid(row=7,column=1)
                Label(root,text=f"Travel on: {res[0][6]}",font = "Arial 10 bold").grid(row=8,column=0,padx = (w/3,0))
                Label(root,text=f"destination: {res[0][8]}",font = "Arial 10 bold").grid(row=9,column=0,padx = (w/3,0))
                Label(root,text=f"Boarding Point: {res[0][7]}",font = "Arial 10 bold").grid(row=9,column=1)
                Label(root,text=f"* Total amount Rs {res[0][9]}.00/- to be paid at the time of boarding the bus",font = "Arial 8").grid(row=10,column=0,padx = (w/3,0),columnspan=2)    
        else:
            showerror('mobileno error','please fill a valid mobile no!!')


    

bus = PhotoImage(file=".\\Bus_for_project.png")
homeimg = PhotoImage(file=".\\home.png")

Label(root,image=bus).grid(pady=10,row=0,column=0,columnspan=5,padx = (w/3,0))
Label(root,text="Online Bus Booking System",font = "Arial 22 bold",bg="light blue",fg = "red").grid(pady=12,row=1,column=0,columnspan=5,padx = (w/3,0))
Label(root,text="Bus Ticket",font = "Arial 18 bold",fg="green",bg="lightgreen").grid(pady=12,row=2,column=0,columnspan=5,padx = (w/3,0))


Label(root,text="Enter your mobile no: ",font = "Arial 11 bold").grid(row=3,column=0,padx = (w/3,0),pady=20)
entry1 = Entry(root,font = "Arial 11 bold")
entry1.grid(row=3,column=1,pady=20)
btn1 = Button(root,text="Check Booking ",font = "Arial 11 bold",command=checkbooking)
btn1.grid(row=3,column=2,pady=20)




def fun():
    if askyesno('Continue','Do you want to contine the app?'):
        root.destroy()
        os.startfile(".\\frontpage.py")
    else:
        showinfo('thanks','thanks for using python bus')
        root.destroy()

root.protocol('WM_DELETE_WINDOW',fun)


root.mainloop()
