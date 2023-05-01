from tkinter import *
from tkinter.messagebox import *
from database import *
import os

root = Tk()
root.title("Main seat booking")
h,w = root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry(f"{w}x{h}")


def showbus():

    to = str(entry1.get())
    fromm = str(entry2.get())
    date = str(entry3.get())
    if(entry1.get() == "" or entry2.get() == "" or entry3.get() == "" ):
        showerror('field empty','one of the entries are missing please fill all the details!')
    else:
        # print(len(val))
        curser.execute('select d.routeid from route as r ,route as d where r.routeid = d.routeid and r.sname = ? and d.sname = ? and r.sid < d.sid;',(fromm,to))
        ro = curser.fetchall()
        if(ro == []):
            showerror('Notice','sorry no bus travels from this route or date please try different route or date !')
            entry1.delete(0,20)
            entry2.delete(0,20)
            entry3.delete(0,20)
        else:
            # print(ro[0][0])
            ro = ro[0][0]
            ro = int(ro)
            curser.execute('select b.busid,o.op_name,b.bustype,r.availability,b.capacity,b.fare from bus as b,operator as o,runs as r where o.operatorid = b.opid and b.busid = r.busid and date = ? and b.rid = ? ',(date,ro))
            global val
            val = curser.fetchall()
            if(val == []):
                showinfo('bus info','sorry no bus available on this date')
                entry3.delete(0,20)
            else:

                Label(f3,text="Select Bus",font = "Arial 10 bold",fg="green").grid(row=4,column=0,padx = (w/4,0),pady = (20,0))
                Label(f3,text="Operator",font = "Arial 10 bold",fg="green").grid(row=4,column=1,pady = (20,0))
                Label(f3,text="Bus Type",font = "Arial 10 bold",fg="green").grid(row=4,column=2,pady = (20,0))
                Label(f3,text="Available/Capacity",font = "Arial 10 bold",fg="green").grid(row=4,column=3,pady = (20,0))
                Label(f3,text="Fare",font = "Arial 10 bold",fg="green").grid(row=4,column=4,pady = (20,0))
                global radiovalue
                radiovalue = IntVar()
                btn3 = Button(f3,text="Proceed to Book",font = "Arial 10 bold",bg="lightgreen",command=proceedtobook)
                btn3.grid(row=5 ,column=5,pady = (20,0),padx=(30,0))

                for i in range(len(val)):
                    # print(i)

                    btn = Radiobutton(f3,text=f"Bus {val[i][0]} ",indicator=0,variable=radiovalue,value=i+1,font = "Arial 9 bold",fg="black",bg="green")
                    btn.grid(padx = (w/4,0),row=5+ i,column=0,pady = (20,0))
                    Label(f3,text=f"{val[i][1]}",font = "Arial 9 bold",fg="blue").grid(row=5 + i,column=1,pady = (20,0))
                    Label(f3,text=f"{val[i][2]}",font = "Arial 10 bold",fg="green").grid(row=5 + i,column=2,pady = (20,0))
                    Label(f3,text=f"{val[i][3]}/{val[i][4]}",font = "Arial 10 bold",fg="green").grid(row=5 +i,column=3,pady = (20,0))
                    Label(f3,text=f"{val[i][5]}",font = "Arial 10 bold",fg="green").grid(row=5 +i,column=4,pady = (20,0))
                # print(radiovalue.get())
                # return radiovalue.get()
            
 
def home():
    root.destroy()
    os.startfile(".\\frontpage.py")
def proceedtobook():
    # print(radiovalue.get())
    if(val[radiovalue.get()-1][3] == "0"):
        showinfo('bus info','this bus is full please try other buses!')
    else:

        
        Label(f4,text="Fill Passenger Details to book the bus ticket",font = "Arial 19 bold",bg="light blue",fg = "red").grid(pady=50,row=21,column=0,columnspan=11,padx = (w/4,0))

    
        Label(f4,text="Name",font="Arial 10 bold").grid(row=22,column=0,padx = (w/6,0))
        global passentry1
        passentry1 = Entry(f4,font="Arial 10 bold")
        passentry1.grid(row=22,column=1)
        Label(f4,text="Gender",font="Arial 10 bold").grid(row=22,column=2,padx=(0,30))
        global passgender_type
        passgender_type = StringVar()
        passgender_type.set("Choose")
        option = ['Male','Female','Third Gender']
        menu = OptionMenu(f4,passgender_type,*option)
        menu.grid(row=22,column=3)
        Label(f4,text="No of seats",font="Arial 10 bold").grid(row=22,column=4,padx=(0,30))
        global passentry2
        passentry2 = Entry(f4,font="Arial 10 bold")
        passentry2.grid(row=22,column=5)
        Label(f4,text="Mobile No",font="Arial 10 bold").grid(row=22,column=6)
        global passentry3
        passentry3 = Entry(f4,font="Arial 10 bold")
        passentry3.grid(row=22,column=7)
        Label(f4,text="Age",font="Arial 10 bold").grid(row=22,column=8)
        global passentry4

        passentry4 = Entry(f4,font="Arial 10 bold")
        passentry4.grid(row=22,column=9)
        btn1 =Button(f4,text="Book Seat",font="Arial 10 bold",bg="green",command=bookseat)
        btn1.grid(row=22,column=10)
        # return [entry1.get(),gender_type.get(),entry2.get(),entry3.get(),entry4.get()]
  
def bookseat():
    global date
    date = str(entry3.get())
    global boarding
    boarding = str(entry2.get())
    global destination
    destination = str(entry1.get())
    global name

    name = str(passentry1.get())
    global gender
    gender = str(passgender_type.get())
    global seats
    seats = passentry2.get()
    global mobileno
    mobileno = passentry3.get()
    global age
    age = passentry4.get()
    # print(type(val[radiovalue.get()-1][5]))
    if(passentry1.get() == "" or passgender_type.get() == "" or passentry2.get() == "" or passentry3.get() =="" or passentry4.get() ==""):
        showerror('field empty','one of the entries are missing please fill all the details!')
    else:
        if(passentry4.get().isdigit() and passentry2.get().isdigit() and passentry3.get().isdigit()):

            if(len(passentry3.get()) == 10 ):

                if(int(passentry2.get()) > int(val[radiovalue.get()-1][3])):
                

                
                    showerror('error','sorry this many seats are not available try lower value!')
                    passentry2.delete(0,20)
                else:
                    if(int(passentry4.get()) >= 120):
                        showerror('age limit','age limit exceeds 120 !')
                        passentry4.delete(0,20)
                    else:

                        seats = int(passentry2.get())

                        toalfare = str(seats * int(val[radiovalue.get() - 1][5]))

                        choice = askyesno('Fare Confirm',f'Total Amount to be paid Rs {toalfare}.00 do you want to book seats?')
                        if (choice==True):
                            curser.execute('update runs set availability = ? where busid = ? and date = ?',(int(val[radiovalue.get()-1][3]) - seats,int(val[radiovalue.get()-1][0]),date))
                            curser.execute('insert into bookinghistory(mobileno,name,gender,seats,age,bid,datebook,boardingp,destination,farepaid,nameop) values (?,?,?,?,?,?,?,?,?,?,?)',(mobileno,name,gender,seats,age,int(val[radiovalue.get()-1][0]),date,boarding,destination,toalfare,str(val[radiovalue.get()-1][1])))
                            connect.commit()
                            root.destroy()
                            os.startfile(".\\busticket.py")
                        elif (choice == False):
                            showinfo('help','please share with us what went wrong?')
            else:
                showerror('mobileno error','please fill a valid mobile no!!')
                passentry3.delete(0,20)
        else:
            showerror('error','please fill the data with aprropriate datatype')


    
f1 = Frame(root)
f1.grid(row=0,column=0)
    
f2 = Frame(root)
f2.grid(row=1,column=0)
    
f3 = Frame(root)
f3.grid(row=4,column=0,columnspan=11)
    
f4 = Frame(root)
f4.grid(row=6,column=0,columnspan=11)
bus = PhotoImage(file=".\\Bus_for_project.png")
homeimg = PhotoImage(file=".\\home.png")

Label(f1,image=bus).grid(pady=10,row=0,column=0,columnspan=11,padx = (w/3,0))
Label(f2,text="Online Bus Booking System",font = "Arial 22 bold",bg="light blue",fg = "red").grid(pady=12,row=1,column=0,columnspan=11,padx = (w/3,0))
Label(f2,text="Enter Journey Details",font = "Arial 12 bold",bg="light green",fg = "green").grid(pady=12,row=2,column=0,columnspan=11,padx = (w/3,0))
Label(f2,text="To",font="Arial 10 bold").grid(row=3,column=0,padx = (w/4,0))
entry1 = Entry(f2,font="Arial 10 bold")
entry1.grid(row=3,column=1)
Label(f2,text="From",font="Arial 10 bold").grid(row=3,column=2,padx=(0,30))
entry2 = Entry(f2,font="Arial 10 bold")
entry2.grid(row=3,column=3)
Label(f2,text="Journey Date : (DD/MM/YYYY)",font="Arial 10 bold").grid(row=3,column=4)
entry3 = Entry(f2,font="Arial 10 bold")
entry3.grid(row=3,column=5)
btn1 =Button(f2,text="Show Bus",font="Arial 10 bold",bg="green",command=showbus)
btn1.grid(row=3,column=6,padx=(10,10))
btn2 = Button(f2,image=homeimg,font="Arial 10 bold",command=home,bg="lightgreen")
btn2.grid(row=3,column=7)
















root.mainloop()
